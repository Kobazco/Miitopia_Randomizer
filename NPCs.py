import csv
import random

miiEffects = ['Normal', 'Angry', 'Laugh', 'Terror', 'Cry', 'Excite', 'Spite', 'Anxious', 'Vacancy', 'Gleeful',
              'Cranky', 'Sleep', 'Nightmare', 'Dance', 'Puppet', 'Aging', 'Burn', 'Eat', 'Faceless', 'Pharaoh',
              'Spider', 'Stone', 'Ice']

# Define NPC Parameters

with open('Input/NPC/NPCList.csv') as csv_file:
    csv_reader = csv.reader(csv_file, delimiter=',')
    line_count = 0
    npcmodels = []
    for row in csv_reader:
        NPC = row[7]
        if NPC != '':
            npcmodels.append(NPC)
        # print(npcmodels)
        line_count += 1

# Randomize NPC Models
with open('Input/NPC/NPCList.csv') as csv_file:
    npc_reader = csv.reader(csv_file, delimiter=',')
    line_count = 0
    with open('Output/NPC/NPCList.csv', mode="w", newline="") as out_file:
        for row in npc_reader:
            row[7] = random.choice(npcmodels)
            # print(row[7])
            row[10] = random.randint(10, 130)
            row[11] = random.randint(10, 130)
            # row[28] = random.choice(miiEffects)
            npc_reader = csv.writer(out_file, delimiter=',')
            npc_reader.writerow(row)
