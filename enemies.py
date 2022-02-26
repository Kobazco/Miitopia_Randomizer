import csv
import random

# Define Enemy Models

with open('Input/Enemy/enemyInfo.csv') as csv_file:
    csv_reader = csv.reader(csv_file, delimiter=',')
    line_count = 0
    enemyModels = []
    for row in csv_reader:
        EnemyModel = row[1]
        enemyModels.append(EnemyModel)
        # print(enemyModels)
        line_count += 1

# Randomize NPC Models
with open('Input/Enemy/enemyInfo.csv') as csv_file:
    enemy_reader = csv.reader(csv_file, delimiter=',')
    line_count = 0
    with open('Output/Enemy/enemyInfo.csv', mode="w", newline="") as out_file:
        for row in enemy_reader:
            if row[0] == 'SatanDemo0' or row[0] == 'SuperSatanDemo0':
                row[1] = random.choice(enemyModels)
            enemy_reader = csv.writer(out_file, delimiter=',')
            enemy_reader.writerow(row)
