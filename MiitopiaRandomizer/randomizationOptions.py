import csv
import logging
import os.path
import random
from io import StringIO

import sarc

from MiitopiaRandomizer.const import battle_files_to_randomize, world_limit, base_output_dir, required_files
from MiitopiaRandomizer.util import verify_input_files, copy_input_to_output, read_input_sarc, \
    get_csv_rows_from_input_sarc, randomize_csv_rows, get_writer_from_output_sarc, write_sarc_to_output, \
    get_data_file_path


def randomize_battles(is_switch: bool, randomize_music=True, randomize_backgrounds=True):
    verify_input_files(required_files['battles'])

    logger = logging.getLogger('BattleRandomizer')
    logger.info('Randomizing battles...')

    if is_switch:
        copy_input_to_output('enemy.sarc')
        # FIXME: Why do we do this?
        with open(os.path.join(base_output_dir, 'enemy.sarc'), 'rb') as dst:
            writer = sarc.read_sarc_and_make_writer(dst)
            face_config_file_path = get_data_file_path('enemyFaceConfig.csv')
            with open(face_config_file_path, 'rb') as src:
                writer.add_file('enemyFaceConfig.csv', src.read())

    enemies: list[tuple[str, int]] = []
    for enemy_data in get_csv_rows_from_input_sarc('enemy.sarc', 'enemyStatus.csv'):
        enemies.append((enemy_data[0], int(enemy_data[7])))

    backgrounds: list[str] = []
    for bg_data in get_csv_rows_from_input_sarc('bg.sarc', 'BGData.csv'):
        if bg_data[1]:
            backgrounds.append(bg_data[0])

    backgroundmusic: list[str] = []
    for bgm_data in get_csv_rows_from_input_sarc('sound.sarc', 'BgmList.csv'):
        # Don't add Jingles (starting with JGL)
        if bgm_data[0].startswith('BGM'):
            backgroundmusic.append(bgm_data[0])

    world_files_to_randomize = [os.path.join('stage', f'World{i:02}.sarc') for i in range(1, world_limit+1)]

    for i, world_filename in enumerate(world_files_to_randomize):
        copy_input_to_output(world_filename)

        logger.debug(f'Randomizing {world_filename}')
        src_archive = read_input_sarc(world_filename)
        files_in_archive = src_archive.list_files()
        dst_archive = sarc.make_writer_from_sarc(src_archive)

        # Go through each file that we want to randomize
        for file_name in battle_files_to_randomize[i]:
            file_name = file_name + '.csv'

            # Skip the file if it doesn't exist in the sarc
            # This might happen on the 3DS version since we also try to randomize Switch-only files
            if file_name not in files_in_archive:
                logger.info(f'File {file_name} not found in archive {world_filename}')
                continue

            # If the file exists, read out its contents and prepare a csv_writer
            file_data = StringIO(
                src_archive.get_file_data(file_name).tobytes().decode(),
                newline=''
            )
            csv_reader = csv.reader(file_data)
            randomized_data = StringIO()
            csv_writer = csv.writer(randomized_data)

            # Randomize all the rows in the file
            for row in csv_reader:
                randomized_row = row.copy()

                # The 3DS supports random backgrounds, but it doesn't load them properly
                # TODO: Find out how to make random backgrounds work on 3DS
                if is_switch and randomize_backgrounds:
                    randomized_row[13] = random.choice(backgrounds)

                if randomize_music:
                    randomized_row[14] = random.choice(backgroundmusic)

                for enemy_index in range(2, 7):
                    enemy_name = row[enemy_index]
                    # If we have no enemies anymore, we're done
                    # NOTE: This could be used to add/remove a random amount of enemies in the future
                    if not enemy_name:
                        break

                    # If the enemy name has a comma, the 2nd part is used to specify the enemy's face(s)?
                    # Currently, we skip these enemies since AFAIK there are some enemies that can hold multiple
                    # faces and I don't think every enemy supports that so we'd end up with a mess if we randomized
                    # them
                    # TODO: Make enemies with specified faces randomized too
                    if ',' in enemy_name:
                        randomized_row[enemy_index] = row[enemy_index]
                        continue

                    # Pick a random enemy out of all of them that has a similar level
                    curr_level = next(enemy[1] for enemy in enemies if enemy[0] == enemy_name)
                    random_level_offset = random.randint(-2, 2)
                    # Make sure the level doesn't go below 1
                    random_level = max([curr_level + random_level_offset, 1])
                    # Get all enemies with this new level
                    new_enemies = [enemy[0] for enemy in enemies if enemy[1] == random_level]
                    new_enemy = random.choice(new_enemies)
                    # Store this new random enemy
                    randomized_row[enemy_index] = new_enemy
                # Once all the enemies are randomized, we can write the row
                csv_writer.writerow(randomized_row)
            # Since we wrote to the StringIO and now want to read it back out,
            # we have to go to the start first
            randomized_data.seek(0)
            dst_archive.add_file(file_name, randomized_data.read().encode())
        # Finally, write the new randomized sarc data into the file
        with open(os.path.join(base_output_dir, world_filename), 'wb') as dst_file:
            dst_archive.write(dst_file)
        logger.debug(f'Randomized {world_filename}')
    logger.info('Battles randomized')


def randomize_jobs(hidden_job_logic=True, randomize_worlds=True, randomize_weapons=True):
    verify_input_files(required_files['jobs'])

    logger = logging.getLogger('JobRandomizer')
    logger.info('Randomizing jobs...')

    # Get all rows from JobInfo.csv
    source_rows = get_csv_rows_from_input_sarc('job.sarc', 'JobInfo.csv')
    if hidden_job_logic:
        # Make the hidden jobs unlock in World 2 and 3 and make them non-hidden
        # This is basically an early form of logic, so no job is "left out" once we randomize
        worlds_hidden_jobs_unlock_in = [2, 3]
        for row in source_rows:
            if row[1] == '0':
                row[1] = str(worlds_hidden_jobs_unlock_in.pop())
            row[2] = ''

    # 1 -> World the job unlocks in
    # 4 -> Job weapon
    columns_to_randomize: list[int] = []
    if randomize_worlds:
        columns_to_randomize.append(1)
    if randomize_weapons:
        columns_to_randomize.append(4)

    randomized_data = randomize_csv_rows(
        source_rows,
        columns_to_randomize
    )

    # Write our randomized data into the output file
    copy_input_to_output('job.sarc')
    sarc_writer = get_writer_from_output_sarc('job.sarc')
    sarc_writer.add_file('JobInfo.csv', randomized_data)
    write_sarc_to_output(sarc_writer, 'job.sarc')

    logger.info('Jobs randomized')


def randomize_treasure():
    verify_input_files(required_files['treasure'])

    logger = logging.getLogger('TreasureRandomizer')
    logger.info('Randomizing treasure...')

    possible_chest_contents = [
        'Money', 'Dish', 'GameTicket', 'Weapon', 'Armor', 'Candy', 'Banana', 'Enemy'
    ]
    money_amounts = [
        50, 300, 900, 1000, 1500, 2500, 3000
    ]

    # Treasure chests can hold food, so we have to get all possible food names first
    dishes: list[str] = []
    for row in get_csv_rows_from_input_sarc('dish.sarc', 'Dish.csv'):
        dishes.append(row[0])

    randomized_data = StringIO()
    csv_writer = csv.writer(randomized_data)

    treasure_sarc_path = os.path.join('stage', 'Treasure.sarc')
    for row in get_csv_rows_from_input_sarc(treasure_sarc_path, 'TreasureBox.csv'):
        # Do not randomize key items
        if row == 'KeyItem':
            continue
        content = row[1] = random.choice(possible_chest_contents)
        if content == 'Money':
            row[2] = random.choice(money_amounts)
        elif content == 'Dish':
            row[2] = random.choice(dishes)
        elif content == 'GameTicket':
            row[2] = random.randint(1, 5)
        elif content in ['Weapon', 'Armor']:
            row[2] = 12
        elif content in ['Candy', 'Banana']:
            row[2] = random.randrange(1, 3)
        elif content == 'Enemy':
            row[2] = ''
        csv_writer.writerow(row)

    copy_input_to_output(treasure_sarc_path)
    sarc_writer = get_writer_from_output_sarc(treasure_sarc_path)
    randomized_data.seek(0)
    sarc_writer.add_file('TreasureBox.csv', randomized_data.read().encode())
    write_sarc_to_output(sarc_writer, treasure_sarc_path)

    logger.info('Treasures randomized')


def randomize_npcs():
    verify_input_files(required_files['npcs'])

    logger = logging.getLogger('NpcRandomizer')
    logger.info('Randomizing NPCs...')

    npc_data = get_csv_rows_from_input_sarc('npc.sarc', 'NPCList.csv')

    all_npc_models: list[str] = []
    for row in npc_data:
        if row[7]:
            all_npc_models.append(row[7])

    randomized_data = StringIO()
    csv_writer = csv.writer(randomized_data)
    for row in npc_data:
        randomized_row = row.copy()
        randomized_row[7] = random.choice(all_npc_models)
        # These were originally 10 and 11, but looking at the file,
        # that seems to have been a mistake (lists start at 0 :)
        randomized_row[9] = random.randint(10, 130)
        randomized_row[10] = random.randint(10, 130)
        csv_writer.writerow(randomized_row)
    copy_input_to_output('npc.sarc')
    sarc_writer = get_writer_from_output_sarc('npc.sarc')
    randomized_data.seek(0)
    sarc_writer.add_file('NPCList.csv', randomized_data.read().encode())
    write_sarc_to_output(sarc_writer, 'npc.sarc')

    logger.info('NPCs randomized')


def randomize_dl():
    verify_input_files(required_files['dark_lord'])

    logger = logging.getLogger('DarkLordRandomizer')
    logger.info('Randomizing Dark Lord Enemy Model...')

    enemy_data = get_csv_rows_from_input_sarc('enemy.sarc', 'enemyInfo.csv')

    all_enemy_models: list[str] = []
    for row in enemy_data:
        all_enemy_models.append(row[1])

    randomized_data = StringIO()
    csv_writer = csv.writer(randomized_data)
    for row in enemy_data:
        if row[0] in ('SatanDemo0', 'SuperSatanDemo0'):
            randomized_row = row.copy()
            randomized_row[1] = random.choice(all_enemy_models)
            csv_writer.writerow(randomized_row)
        else:
            csv_writer.writerow(row)

    copy_input_to_output('enemy.sarc')
    sarc_writer = get_writer_from_output_sarc('enemy.sarc')
    randomized_data.seek(0)
    sarc_writer.add_file('enemyInfo.csv', randomized_data.read().encode())
    write_sarc_to_output(sarc_writer, 'npc.sarc')

    logger.info('Randomized Dark Lord Enemy Model')
