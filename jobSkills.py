import csv
import random
import os

# Skill "tiers", decided by me. Man thief's skills really suck, don't they? Elf is so OP as well.

tier1 = ['FighterDouble', 'WizardFire', 'PriestCure', 'ThiefTrap', 'IdolEncore', 'CookCooking', 'TankHumanCannon',
         'DevilJokeFork', 'RoyaltyWave', 'RoyaltyDance', 'FlowerFlower', 'ScientistBugCrush', 'SharpenClaws',
         'CatStealDish']

tier2 = ['FighterGuard', 'FighterSlap', 'WizardLightning', 'WizardSleep', 'WizardBigWeapon', 'PriestCalm',
         'PriestResurrect', 'ThiefDagger', 'ThiefTrap', 'ThiefHighJump', 'ThiefPilfer', 'IdolHowling',
         'IdolLoveCall', 'IdolConcert', 'VampireCurse', 'CookHeating', 'CookBakedBanana', 'CookSpicy', 'TankWildShot',
         'TankDefense', 'DevilWhisper', 'DevilPickHip', 'RoyaltyTeatime', 'RoyaltyEscort', 'FlowerLifeDew', 'FlowerFan',
         'FlowerWhistle', 'FlowerFlower2', 'ScientistJetFlask', 'ScientistIgnition', 'CatFrisk', 'CatPunch',
         'ElfDanceArrow']

tier3 = ['FighterSpin', 'WizardExplosion', 'PriestKarma', 'IdolFunService', 'VampireEat', 'CookBanquet', 'TankBeam',
         'DevilMagicDrain', 'DevilEnergyDrain', 'RoyaltyBlind', 'ScientistGuardMask', 'CatDoubleScratch']

tier4 = ['FighterTwice', 'WizardFire2', 'WizardLightning2', 'PriestCure2', 'PriestCureAll', 'ThiefCreep', 'IdolDance',
         'VampireRevive', 'VampireBreath', 'CookCooking2', 'TankRepair', 'DevilSeduce', 'DevilPunishFork',
         'RoyaltyDoubleWave', 'FlowerFlowerPark', 'ScientistCureCode', 'ScientistAbsorbent', 'CatGroom', 'ElfCureMelody']

tier5 = ['FighterEyeSlash', 'WizardExplosion2', 'PriestCure3', 'ThiefDagger2', 'IdolHowling2', 'VampireBreath2',
         'CookSpicyAll', 'CookCookMonster', 'TankHeatShot', 'DevilDeathWhisper', 'RoyaltyCologne', 'FlowerEarthAnger',
         'CatLick', 'ElfMagicArrow']

tier6 = ['FighterReviveSlap', 'WizardBarrier', 'WizardLightning3', 'PriestResurrect2', 'ThiefRock', 'ThiefLargeTrap',
         'IdolAngelSong', 'VampireZombify', 'CookCooking3', 'TankBeam2', 'FlowerFlowerPark2', 'ScientistJetFlask2',
         'ElfGuardArrow']

tier7 = ['WizardExplosion3', 'PriestHoly', 'VampireBreath3', 'DevilGrindFork', 'RoyaltyWaveAll', 'FlowerFanAll',
         'ScientistBlackHole', 'CatScratchAll', 'ElfGuardArrow']

tier8 = ['FighterSpin2', 'WizardFire3', 'PriestCureAll2', 'VampireBatRose', 'ElfForestGrace', 'ElfPrayer',
         'ElfArrowRain']

# Open all the Job Status sheets and clear existing skills
for filename in os.listdir("Input/Job"):
    with open(os.path.join("Input/Job", filename)) as csv_file:
        with open(os.path.join("Output/Job", filename), mode='w', newline="") as out_file:
            jstatus_reader = csv.reader(csv_file, delimiter=',')
            jstatus_writer = csv.writer(out_file, delimiter=',')
            for row in jstatus_reader:
                level = int(row[0])
                # print(filename, level)
                row[7] = ''                                     # Clear Skill Column
                if level == 2:                                  # 100% Tier 1 Skill
                    row[7] = random.choice(tier1)
                    randchance = random.randint(1,10)
                if level == 4 and randchance <= 6:               # 60% Tier 1 Skill
                    row[7] = random.choice(tier1)
                if level == 5:                                  # 100% Tier 2 Skill
                    row[7] = random.choice(tier2)
                    randchance = random.randint(1,10)
                if level == 7 and randchance <= 5:               # 50% Tier 2 Skill
                    row[7] = random.choice(tier2)
                    randchance = random.randint(1, 10)
                if level == 9 and randchance <= 3:              # 30% Tier 2 Skill
                    row[7] = random.choice(tier2)
                if level == 10:                                 # 100% Tier 3 Skill
                    row[7] = random.choice(tier3)
                    randchance = random.randint(1, 10)
                if level == 13 and randchance <= 5:              # 50% Tier 3 Skill
                    row[7] = random.choice(tier3)
                if level == 15:                                 # 100% Tier 4 Skill
                    row[7] = random.choice(tier4)
                    randchance = random.randint(1, 10)
                if level == 18 and randchance <= 4:              # 40% Tier 4 Skill
                    row[7] = random.choice(tier4)
                    randchance = random.randint(1, 10)
                if level == 19 and randchance <= 2:              # 20% Tier 4 Skill
                    row[7] = random.choice(tier4)
                if level == 20:                                 # 100% Tier 5 Skill
                    row[7] = random.choice(tier5)
                    randchance = random.randint(1, 10)
                if level == 23 and randchance <= 3:              # 30% Tier 5 Skill
                    row[7] = random.choice(tier5)
                if level == 25:                                 # 100% Tier 6 Skill
                    row[7] = random.choice(tier6)
                    randchance = random.randint(1, 10)
                if level == 28 and randchance <= 3:              # 30% Tier 6 Skill
                    row[7] = random.choice(tier6)
                if level == 30:                                 # 100% Tier 7 Skill
                    row[7] = random.choice(tier7)
                    randchance = random.randint(1, 10)
                if level == 33 and randchance <= 2:              # 20% Tier 7 Skill
                    row[7] = random.choice(tier7)
                if level == 35:                                 # 100% Tier 8 Skill
                    row[7] = random.choice(tier8)
                    randchance = random.randint(1, 10)
                if level == 38 and randchance <= 1:             # 10% Tier 8 Skill
                    row[7] = random.choice(tier8)
                jstatus_writer.writerow(row)