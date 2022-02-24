Miitopia Randomizer Beta (Switch & 3DS)

Run main.py and choose as many of the randomization options as you'd like. Details
on what option does what are listed when you run main.py

# Options:
###### -Enemy
    Randomizes the enemies that appear in areas, based on their internal "level" in order to ensure
    you fight enemies of similar strength.
    Randomizes Battle Backgrounds (Switch only)
    Randomizes Battle Music

###### -Jobs
    Randomizes the world in which Jobs are unlocked. Also randomizes the look of what weapon a Job uses

###### -Treasure
    Randomizes the contents of all Treasure Chests. Enemy (trap chests) currently spawn an empty battle.

# Requirements:
- Switch-Toolbox https://github.com/KillzXGaming/Switch-Toolbox/releases
- Download experimental latest
- A modded switch or switch emulator (Ryujinx is suggested due to Mii Maker support)
- Or the above but for a 3DS if you are playing that version.
- A Miitopia romfs dump (We cannot legally provide this)
- Knowledge of how to install mods to atmosphere cfw or your emulator of choice

The fight against the Mini Slime as well as the first area afterwards are not
randomized in order to avoid softlocking. Randomization of enemies/stages begins
in the first area unlocked after getting Inn access.

# Instructions
Instructions are made with Switch-Toolbox in mind for .sarc editing

Follow these instructions based on what you ran with main.py

## Enemy Randomization Instructions:
1. Extract ALL of the contents of the following .sarc files to their own unique
folders based on world# romfs\cmn\param\stage\World0X
2. So you should have a bunch of folders named World 01, World02, etc. with all
of their respective .csv files in said folders
3. Navigate to the Output folder
4. Take all of the "World" folders and drag them to the folder containing your
extracted World csvs. Click "yes" to replace
5. In Switch-Toolbox, open World01.sarc. Click "repack" and select your modified
World01 folder. Save the file. Repeat for every "World" folder
6. Place the modified .sarc files in your romfs\cmn\param\stage\ folder for your
modded switch or emulator. Wherever you place your mods

## Jobs Instructions:
1. Navigate to romfs\cmn\param\
2. Open job.sarc in Switch-Toolbox
3. Right click "JobInfo.csv" and click "replace raw data"
4. Replace with "JobInfo.csv" from the Output folder.
5. Save
6. Place modified job.sarc file in romfs\cmn\param\ or wherever your mods are located

## Treasure Instructions:
*TRAP CHESTS CURRENTLY DO NOT WORK*
1. Navigate to romfs\cmn\param\stage\
2. Open Treasure.sarc in Switch-Toolbox
3. Right click on "TreasureBox.csv" and click "replace raw data"
4. Replace with "TreasureBox.csv" from Output\Treasure
5. Save
6. Place modified Treasure.sarc file in romfs\cmn\param\stage\ or wherever your mods are located

If crashing on battle starts:
    Use the custom "enemy.sarc" if you are playing on Console/Ryujinx to ensure faceless boss enemies
    won't spawn (which cause crashes).
    Might still cause crashes later on with certain boss cutscenes. If so, delete the enemy.sarc to get past those
    cutscenes and then re add it after.