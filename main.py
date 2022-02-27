import os
import sys
import sarc
import subprocess

Enemy = {'-Enemy', '-enemy'}
Jobs = {'-Jobs', '-jobs'}
Treasure = {'-Treasure', '-treasure'}
Exit = {'-Exit', '-exit'}
NPC = {'-NPCs', '-npcs'}

print('Type one of the following Randomization options:\n')

print('-Enemy\n\n'
      'Randomizes enemies in every stage after the first 2 based on their strength.\n'
      'As an example, Rock Moths can be replaced with similarly weak enemies such as a Pom or Mouthy Tomato.\n'
      'Also randomizes battle background and music.\n')

print('-Jobs\n\n'
      'Randomizes the world in which Jobs are unlocked. Also randomizes the look of what weapon a Job uses.\n')

print('-Treasure\n\n'
      'Randomizes the contents of all Treasure Chests.\n')

print ('NPCs\n\n'
       'Randomizes the NPCs models, as well as what enemy the Dark Lord is.\n')


def main():
    Directories = ['World01', 'World02', 'World03', 'World04', 'World05', 'World06', 'World07', 'World08', 'Dish',
                   'Equipment', 'Job', 'NPC', 'Treasure', 'Enemy', 'romfs/cmn/param/stage']
    for Directories in Directories:
        output = 'Output/{}'.format(Directories)
        if not os.path.exists(output):
            os.makedirs(output)

    print('Enter desired randomization: (-Enemy, -Jobs, -Treasure, -NPCs or -Exit to exit)\n')

    choice = input()
    if choice in Enemy:
        import stageEnemy
        print('Enemies randomized\n')

        # Modify relevant .sarc files
        print('Building .sarc archives...\n')
        subprocess.run(["sarc", "update", "Output/World01", "Output/romfs/cmn/param/stage/World01.sarc"])
        subprocess.run(["sarc", "update", "Output/World02", "Output/romfs/cmn/param/stage/World02.sarc"])
        subprocess.run(["sarc", "update", "Output/World03", "Output/romfs/cmn/param/stage/World03.sarc"])
        subprocess.run(["sarc", "update", "Output/World04", "Output/romfs/cmn/param/stage/World04.sarc"])
        subprocess.run(["sarc", "update", "Output/World05", "Output/romfs/cmn/param/stage/World05.sarc"])
        subprocess.run(["sarc", "update", "Output/World06", "Output/romfs/cmn/param/stage/World06.sarc"])
        main()
    elif choice in Jobs:
        import jobOrder
        print('Job Order & Weapon look randomized\n')

        # Modify relevant .sarc files
        print('Building .sarc archives...\n')
        subprocess.run(["sarc", "update", "Output/Job", "Output/romfs/cmn/param/job.sarc"])
        main()
    elif choice in Treasure:
        import treasure
        print('Treasure chests randomized\n')

        # Modify relevant .sarc files
        print('Building .sarc archives...\n')
        subprocess.run(["sarc", "update", "Output/Treasure", "Output/romfs/cmn/param/stage/Treasure.sarc"])
        main()
    elif choice in Exit:
        exit()
    elif choice in NPC:
        import NPCs
        import enemies
        print('NPCs randomized\n')

        # Modify relevant .sarc files
        print('Building .sarc archives...\n')
        subprocess.run(["sarc", "update", "Output/NPC", "Output/romfs/cmn/param/npc.sarc"])
        subprocess.run(["sarc", "update", "Output/Enemy", "Output/romfs/cmn/param/enemy.sarc"])
        main()
    else:
        sys.stdout.write("Please use one of the options listed below\n")
        main()


main()

# TODO: List of planned features
#   Auto creation of .sarc files
#   Enemy Skills
#   Grub Bonuses
#   New Enemies for greater variety
#   Enemy Faces
#   NPC Clothes Colors
#   Include Job outfits in NPC Model Randomization
