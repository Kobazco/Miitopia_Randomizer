Miitopia Randomizer Beta (Switch & 3DS)

# Requirements:
- A modded switch/3DS or emulator (Ryujinx is suggested due to Mii Maker support, Citra for 3DS)
- A Miitopia romfs dump (We cannot legally provide this)
- Knowledge of how to install mods on cfw or your emulator of choice
- Python 3.6+ (**64 bit version**)
- sarc.py `pip install sarc`

# Options:
###### -Enemy
    Randomizes the enemies that appear in areas, based on their internal "level" in order to ensure
    you fight enemies of similar strength.
    Randomizes Battle Backgrounds (Switch only)
    Randomizes Battle Music

###### -Jobs
    Randomizes the world in which Jobs are unlocked. Also randomizes the look of what weapon 
    a Job uses

###### -Treasure
    Randomizes the contents of all Treasure Chests. Enemy (trap chests) currently spawn an 
    empty battle.

###### -NPCs
    Randomizes the models and sizes of all NPCs. Also randomizes which enemy the Dark & Darker Lord 
    are in cutscenes.

The fight against the Mini Slime as well as the first area afterwards are not
randomized in order to avoid softlocking. Randomization of enemies/stages begins
in the first area unlocked after getting Inn access.

# Instructions
1. Create the following folders in this order if it does not already exist: `Output/romfs/cmn/param/stage`
2. Place the following files from your Miitopia romfs dump into `Output/romfs/cmn/param`: `enemy.sarc, job.sarc, npc.sarc`
3. Place the following files from your Miitopia romfs dump into `Output/romfs/cmn/param/stage`: `Treasure.sarc, World01 - World06.sarc files`
4. Run `main.py`
5. Enter your desired Randomization options
6. Move the `romfs` folder from Output to the location of your mods and say "yes" to replace all if prompted

### No Such File or Directory error
1. Open command prompt
2. `cd file path for where you extracted the randomizer`
3. Example would be `cd C:/Users/Username/Downloads/Miitopia_Randomizer`
4. `python main.py`
5. Go to step 5 of Instructions.

### Mod Location/Folder
- For Atmosphere cfw users, this is `atmosphere/contents/01003DA010E8A000/` Place the romfs folder here
- For emulator users, both Ryujinx and Yuzu you can just right click the game and select "view mod location" and place the romfs folder there.
