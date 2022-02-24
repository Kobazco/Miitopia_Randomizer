Miitopia Randomizer Beta

Run main.py and choose as many of the randomization options as you'd like. Details
on what option does what are listed when you run main.py

Requirements:
- Switch-Toolbox https://github.com/KillzXGaming/Switch-Toolbox/releases
- Download experimental latest
- A modded switch or switch emulator (Ryujinx is suggested due to Mii Maker support)
- A Miitopia romfs dump (We cannot legally provide this)
- Knowledge of how to install mods to atmosphere cfw or your emulator of choice

The fight against the Mini Slime as well as the first area afterwards are not
randomized in order to avoid softlocking. Randomization of enemies/stages begins
in the first area unlocked after getting Inn access.

Instructions are made with Switch-Toolbox in mind for .sarc editing

Enemy Randomization Instructions:
1. Extract ALL of the contents of the following .sarc files to their own unique
folders based on world# romfs\cmn\param\stage\World0X
2. So you should have a bunch of folders named World 01, World02, etc. with all
of their respective .csv files in said folders
3. Run stageEnemy.py
4. Navigate to the Output folder
5. Take all of the "World" folders and drag them to the folder containing your
extracted World csvs. Click "yes" to replace
6. In Switch-Toolbox, open World01.sarc. Click "repack" and select your modified
World01 folder. Save the file. Repeat for every "World" folder
7. Place the modified .sarc files in your romfs\cmn\param\stage\ folder for your
modded switch or emulator. Wherever you place your mods

Jobs Instructions:
1. Run jobOrder.py
2. Navigate to romfs\cmn\param\
3. Open job.sarc in Switch-Toolbox
4. Right click "JobInfo.csv" and click "replace raw data"
5. Replace with "JobInfo.csv" from the Output folder.
6. Save
7. Place modified job.sarc file in romfs\cmn\param\ or wherever your mods are located

Treasure Instructions:
*TRAP CHESTS CURRENTLY DO NOT WORK*
1. Run treasure.py
2. Navigate to romfs\cmn\param\stage\
3. Open Treasure.sarc in Switch-Toolbox
4. Right click on "TreasureBox.csv" and click "replace raw data"
5. Replace with "TreasureBox.csv" from Output\Treasure
6. Save
7. Place modified Treasure.sarc file in romfs\cmn\param\stage\ or wherever your mods are located

If crashing on battle starts:
    Use the custom "enemy.sarc" if you are playing on Console/Ryujinx to ensure faceless boss enemies
    won't spawn (which cause crashes).

    Might still cause crashes later on with certain boss cutscenes. If so, delete the enemy.sarc to get past those
    cutscenes and then re add it after.