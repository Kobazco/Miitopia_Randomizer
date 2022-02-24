import os
import sys

Enemy = {'-Enemy', '-enemy'}
Jobs = {'-Jobs', '-jobs'}
Treasure = {'-Treasure', '-treasure'}
Exit = {'-Exit', '-exit'}

print('Type one of the following Randomization options:\n')

print('-Enemy\n\n'
      'Randomizes enemies in every stage after the first 2 based on their strength.\n'
      'As an example, Rock Moths can be replaced with similarly weak enemies such as a Pom or Mouthy Tomato.\n'
      'Also randomizes battle background and music.\n')

print('-Jobs\n\n'
      'Randomizes the world in which Jobs are unlocked. Also randomizes the look of what weapon a Job uses.\n')

print('-Treasure\n\n'
      'Randomizes the contents of all Treasure Chests.\n')


def main():
    print('Enter desired randomization: (-Enemy, -Jobs, -Treasure or -Exit to exit)\n')

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
    else:
        sys.stdout.write("Please use one of the options listed below\n")
        main()


main()
