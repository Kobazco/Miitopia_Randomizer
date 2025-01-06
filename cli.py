import argparse
import logging
import os.path
import random
import subprocess
import sys

from MiitopiaRandomizer import randomizationOptions
from MiitopiaRandomizer.util import clear_output_dir, get_file_version


# TODO: List of planned features:
#  - Enemy Skills
#  - Grub Bonuses - basic done
#  - Randomly Create New Enemies
#  - Enemy Faces
#  - NPC Clothes Colors
#  - Include Job outfits in NPC Model Randomization
#  - Clothes Colors
#  - Job Skills
#  - Apply Random Dark Lord to Battles


def main():
    logger = logging.getLogger('Main')

    # Parse arguments with argparse
    parser = argparse.ArgumentParser(description='Miitopia Randomizer', formatter_class=argparse.RawTextHelpFormatter)
    parser.add_argument(
        '--battles', '-B',
        action='store_true',
        help='Randomizes every battle in every stage (except for the first 2).\n' +
             'Music, background (if possible) and enemies are randomized.\n' +
             'Enemies are randomized based on their strength: \n' +
             'As an example, Rock Moths can be replaced with similarly weak enemies such as a Pom or Mouthy Tomato.'
    )
    parser.add_argument(
        '--jobs', '-J',
        action='store_true',
        help='Randomizes the world in which Jobs are unlocked. Also randomizes the look of what weapon a Job uses.'
    )
    parser.add_argument(
        '--treasure', '-T',
        action='store_true',
        help='Randomizes the contents of all Treasure Chests.'
    )
    parser.add_argument(
        '--npcs', '-N',
        action='store_true',
        help='Randomizes the NPCs models, as well as what enemy the Dark Lord is.'
    )
    parser.add_argument(
        '--seed', '-S',
        action='store',
        help='Specifies a seed to use for the randomization.\n' +
             'Useful if you want to play the same game with/against someone else'
    )
    parser.add_argument(
        '--grub', '-G',
        action='store_true',
        help='Randomizes the stats that Grub give on consumption,\n' +
             'as well as its sound effect and tastiness'
    )
    parser.add_argument(
        '--color', '-C',
        action='store_true',
        help='Randomizes the colors that armor/clothes have.'
    )
    args = parser.parse_args()

    # If the user double-clicked the program, print the help and start a cmd session
    if len(sys.argv) < 2:
        parser.print_help()
        if getattr(sys, 'frozen', False) and hasattr(sys, '_MEIPASS'):
            if sys.platform == 'win32':
                subprocess.run(['cmd', '/K', 'echo>nul'])
            # On Mac/Linux there's no easy way to start a GUI terminal,
            # so those people will have to open it themselves (or just use the actual GUI)
        sys.exit()

    clear_output_dir()

    # Set and print out the seed
    if args.seed:
        seed = int(args.seed)
        logger.info(f'Using seed {seed}')
    else:
        seed = random.randrange(sys.maxsize)
        logger.info(f'The seed for this randomization is {seed}')
    random.seed(seed)

    # Write the seed to the output folder
    with open(os.path.join('Output', 'seed.txt'), 'w') as f:
        f.write(str(seed))

    # Do the actual work
    is_switch = get_file_version() == 'Switch'
    if args.battles:
        randomizationOptions.randomize_battles(is_switch)
    if args.jobs:
        randomizationOptions.randomize_jobs()
    if args.treasure:
        randomizationOptions.randomize_treasure()
    if args.npcs:
        randomizationOptions.randomize_npcs(is_switch)
        randomizationOptions.randomize_dl()
    if args.grub:
        randomizationOptions.randomize_grub()
    if args.color:
        randomizationOptions.randomize_colors()


if __name__ == '__main__':
    logging.basicConfig(
        level=logging.INFO,
        format='[%(asctime)s] [%(name)s/%(levelname)s] %(message)s',
        datefmt='%H:%M:%S'
    )
    main()
