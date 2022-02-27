import csv
import random
import os
import sys
import subprocess
import sarc


# Get Enemy names and levels

dsyes = {'Y', 'y'}
dsno = {'N', 'n'}
ds = 0

print('Are you using the 3DS version? (Y/N)\n')


def dsmode():
    global ds
    choice = input()
    if choice in dsyes:
        ds = 1
    elif choice in dsno:
        ds = 0
        # Switch custom face info file
        subprocess.run(["sarc", "update", "Input/Enemy/enemyFaceConfig.csv", "Output/romfs/cmn/param/enemy.sarc",
                        "--base-path", "Input/Enemy"])
    else:
        sys.stdout.write("Please type Y or N in order to indicate you are using the 3DS version or not\n")
        dsmode()


dsmode()


class Enemy:
    instances = []

    def __init__(self, name, level):
        self.name = row[0]
        self.level = int(row[7])
        __class__.instances.append(self)

    def __repr__(self):
        return "% s % s" % (self.name, self.level)

    def __str__(self):
        return "% s is level" " % s" % (self.name, self.level)


# Get Enemy data
with open('enemyStatus.csv') as csv_file:
    csv_reader = csv.reader(csv_file, delimiter=',')
    line_count = 0

    enemies = []
    for row in csv_reader:
        enemy = Enemy(row[0], row[7])
        enemies.append(enemy)
    line_count += 1


# Get Background data
with open('BGData.csv') as csv_file:
    bg_reader = csv.reader(csv_file, delimiter=',')
    BGdata = []
    for row in bg_reader:
        bg = row[0]
        BGdata.append(bg)


# Get BGM data
with open('BgmList.csv') as csv_file:
    bgm_reader = csv.reader(csv_file, delimiter=',')
    BGMList = []
    for row in bgm_reader:
        bgm = row[0]
        BGMList.append(bgm)

enemiesByName = {}
for enemy in Enemy.instances:
    if enemy.name not in enemiesByName:
        enemiesByName[enemy.name] = enemy.level

# print(enemiesByName)

enemiesByLevel = {}
for enemy in Enemy.instances:
    if enemy.level not in enemiesByLevel:
        enemiesByLevel[enemy.level] = []
    enemiesByLevel[enemy.level].append(enemy.name)

# print(enemiesByLevel)


# Randomize Enemies in stages

def randomize_col(row, col, currlevel):
    if ',' in row[col]:
        return

    # print("Original Level:", currlevel)
    randLevel = random.randrange(currlevel - 2, currlevel + 2)
    if randLevel <= 0:
        randLevel += 2
    # print(filename, 'Level:', randLevel)
    randEnemies = enemiesByLevel[randLevel]
    randIndex = random.randrange(len(randEnemies))
    randEnemy = randEnemies[randIndex]
    # print(filename, randEnemy)
    row[col] = randEnemy


def randomize_row(row, currlevel):
    rowrando = random.randint(2, 6)
    for i in range(2, rowrando + 1):
        randomize_col(row, i, currlevel)


# World 1
for filename in os.listdir("Input/World01"):
    with open(os.path.join("Input/World01", filename)) as csv_file:
        with open(os.path.join("Output/World01", filename), mode='w', newline="") as out_file:
            enemy_reader = csv.reader(csv_file, delimiter=",")
            enemy_writer = csv.writer(out_file, delimiter=",")
            for row in enemy_reader:
                if ',' not in row[2]:
                    currlevel = enemiesByName[row[2]]
                    if ds == 0:
                        row[13] = random.choice(BGdata)
                    row[14] = random.choice(BGMList)
                randomize_row(row, currlevel)
                enemy_writer.writerow(row)

print('World 1 Randomized')

# World 2
for filename in os.listdir("Input/World02"):
    with open(os.path.join("Input/World02", filename)) as csv_file:
        with open(os.path.join("Output/World02", filename), mode='w', newline="") as out_file:
            enemy_reader = csv.reader(csv_file, delimiter=",")
            enemy_writer = csv.writer(out_file, delimiter=",")
            for row in enemy_reader:
                if "," not in row[2]:
                    currlevel = enemiesByName[row[2]]
                    if ds == 0:
                        row[13] = random.choice(BGdata)
                    row[14] = random.choice(BGMList)
                randomize_row(row, currlevel)
                enemy_writer.writerow(row)

print('World 2 Randomized')

# World 3
for filename in os.listdir("Input/World03"):
    with open(os.path.join("Input/World03", filename)) as csv_file:
        with open(os.path.join("Output/World03", filename), mode='w', newline="") as out_file:
            enemy_reader = csv.reader(csv_file, delimiter=",")
            enemy_writer = csv.writer(out_file, delimiter=",")
            for row in enemy_reader:
                if "," not in row[2]:
                    currlevel = enemiesByName[row[2]]
                    if ds == 0:
                        row[13] = random.choice(BGdata)
                    row[14] = random.choice(BGMList)
                randomize_row(row, currlevel)
                enemy_writer.writerow(row)

print('World 3 Randomized')

# World 4
for filename in os.listdir("Input/World04"):
    with open(os.path.join("Input/World04", filename)) as csv_file:
        with open(os.path.join("Output/World04", filename), mode='w', newline="") as out_file:
            enemy_reader = csv.reader(csv_file, delimiter=",")
            enemy_writer = csv.writer(out_file, delimiter=",")
            for row in enemy_reader:
                if "," not in row[2]:
                    currlevel = enemiesByName[row[2]]
                    if ds == 0:
                        row[13] = random.choice(BGdata)
                    row[14] = random.choice(BGMList)
                randomize_row(row, currlevel)
                enemy_writer.writerow(row)

print('World 4 Randomized')

# World 5
for filename in os.listdir("Input/World05"):
    with open(os.path.join("Input/World05", filename)) as csv_file:
        with open(os.path.join("Output/World05", filename), mode='w', newline="") as out_file:
            enemy_reader = csv.reader(csv_file, delimiter=",")
            enemy_writer = csv.writer(out_file, delimiter=",")
            for row in enemy_reader:
                if "," not in row[2]:
                    currlevel = enemiesByName[row[2]]
                    if ds == 0:
                        row[13] = random.choice(BGdata)
                    row[14] = random.choice(BGMList)
                randomize_row(row, currlevel)
                enemy_writer.writerow(row)

print('World 5 Randomized')

# World 6
for filename in os.listdir("Input/World06"):
    with open(os.path.join("Input/World06", filename)) as csv_file:
        with open(os.path.join("Output/World06", filename), mode='w', newline="") as out_file:
            enemy_reader = csv.reader(csv_file, delimiter=",")
            enemy_writer = csv.writer(out_file, delimiter=",")
            for row in enemy_reader:
                if "," not in row[2]:
                    currlevel = enemiesByName[row[2]]
                    if ds == 0:
                        row[13] = random.choice(BGdata)
                    row[14] = random.choice(BGMList)
                randomize_row(row, currlevel)
                enemy_writer.writerow(row)

print('World 6 Randomized')

# World 7
# for filename in os.listdir("Input/World07"):
#     with open(os.path.join("Input/World07", filename)) as csv_file:
#         with open(os.path.join("Output/World07", filename), mode='w', newline="") as out_file:
#             enemy_reader = csv.reader(csv_file, delimiter=",")
#            enemy_writer = csv.writer(out_file, delimiter=",")
#            for row in enemy_reader:
#                randomize_row(row)
#                enemy_writer.writerow(row)

# print('World 7 Randomized')

# World 8
# for filename in os.listdir("Input/World08"):
#    with open(os.path.join("Input/World08", filename)) as csv_file:
#        with open(os.path.join("Output/World08", filename), mode='w', newline="") as out_file:
#            enemy_reader = csv.reader(csv_file, delimiter=",")
#            enemy_writer = csv.writer(out_file, delimiter=",")
#            for row in enemy_reader:
#                randomize_row(row)
#                enemy_writer.writerow(row)
#
# print('World 8 Randomized')
