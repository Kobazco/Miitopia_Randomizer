import os
import sys

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
                   'Equipment', 'Job', 'NPC', 'Treasure']
    for Directories in Directories:
        output = 'Output/{}'.format(Directories)
        if not os.path.exists(output):
            os.makedirs(output)

    print('Enter desired randomization: (-Enemy, -Jobs, -Treasure, -NPCs or -Exit to exit)\n')

    choice = input()
    if choice in Enemy:
        import stageEnemy
        print('Enemies randomized\n')
        main()
    elif choice in Jobs:
        import jobOrder
        print('Job Order & Weapon look randomized\n')
        main()
    elif choice in Treasure:
        import treasure
        print('Treasure chests randomized\n')
        main()
    elif choice in Exit:
        exit()
    elif choice in NPC:
        import NPCs
        print('NPCs randomized\n')
        main()
    else:
        sys.stdout.write("Please use one of the options listed below\n")
        main()


main()
