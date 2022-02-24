import csv
import random

# Possible Treasure Outcomes
treasureOutcomes = ['Money', 'Dish', 'GameTicket', 'Weapon', 'Armor', 'Candy', 'Banana', 'Enemy']
moneyAmount = [50, 300, 900, 1000, 1500, 2500, 3000]
snackAmount = [1, 3]

# Define Food Types

with open('Input/Dish/Dish.csv') as csv_file:
    csv_reader = csv.reader(csv_file, delimiter=',')
    line_count = 0
    foodlist = []
    for row in csv_reader:
        Food = row[0]
        foodlist.append(Food)
        # print(Food)
        line_count += 1

# Randomize Treasure Chests
with open('Input/Treasure/TreasureBox.csv') as csv_file:
    treasure_reader = csv.reader(csv_file, delimiter=',')
    line_count = 0
    with open('Output/Treasure/TreasureBox.csv', mode="w", newline="") as out_file:
        for row in treasure_reader:
            if row[1] != "KeyItem":                             # Exclude Key Items
                row[1] = random.choice(treasureOutcomes)
                if row[1] == "Money":
                    row[2] = random.choice(moneyAmount)
                if row[1] == "GameTicket":
                    row[2] = random.randrange(1, 5)
                if row[1] == "Weapon" or row[1] == "Armor":
                    row[2] = 12
                if row[1] == "Candy" or row[1] == "Banana":
                    row[2] = random.choice(snackAmount)
                if row[1] == "Enemy":
                    row[2] = ''
                if row[1] == "Dish":
                    row[2] = random.choice(foodlist)
            treasure_writer = csv.writer(out_file, delimiter=',')
            treasure_writer.writerow(row)

