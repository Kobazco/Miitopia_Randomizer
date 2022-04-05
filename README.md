## Miitopia Randomizer (Switch & 3DS)


### Requirements
- A modded switch/3DS or emulator (Ryujinx is suggested due to Mii Maker support, Citra for 3DS)
- A Miitopia romfs dump (We cannot legally provide this)
- Knowledge of how to install mods on cfw or your emulator of choice


### Options

#### GUI
When hovering over an option in the GUI, a tooltip will appear explaining the option

#### CLI
```
usage: MiitopiaRandomizer_cli [-h] [--battles] [--jobs] [--treasure] [--npcs] [--seed SEED]

Miitopia Randomizer

options:
  -h, --help            show this help message and exit
  --battles, -B         Randomizes every battle in every stage (except for the first 2).
                        Music, background (if possible) and enemies are randomized.
                        Enemies are randomized based on their strength: 
                        As an example, Rock Moths can be replaced with similarly weak enemies such as a Pom or Mouthy Tomato.
  --jobs, -J            Randomizes the world in which Jobs are unlocked. Also randomizes the look of what weapon a Job uses.
  --treasure, -T        Randomizes the contents of all Treasure Chests.
  --npcs, -N            Randomizes the NPCs models, as well as what enemy the Dark Lord is.
  --seed SEED, -S SEED  Specifies a seed to use for the randomization.
                        Useful if you want to play the same game with/against someone else
```


### Note
The fight against the Mini Slime as well as the first area afterwards are notrandomized in order to avoid softlocking.  
Randomization of enemies/stages begins in the first area unlocked after getting Inn access.


### Instructions
1. Copy your 'cmn' folder from your romfs into Input/romfs/
2. As a temporary bug fix, please use [this](https://drive.google.com/file/d/1RqisLxdneC9mJZLLoWS9gk9-Zi41ZRpu/view?usp=sharing) pre-edited enemy.sarc and place it in Input/romfs/cmn/param and select "yes" to replace when prompted.
3. Run package_release.bat or package_release.sh
4. Run the GUI or the CLI in the newly created Release folder
5. Select the options you want
6. Copy the 'romfs' folder from the output directory into your mod location and overwrite all files if prompted


### Mod Location/Folder
- For Atmosphere cfw users, this is `atmosphere/contents/01003DA010E8A000/` Place the romfs folder here
- For emulator users, both Ryujinx and Yuzu you can just right click the game and select "view mod location" and place the romfs folder there.


### Credits
- @Connicpu for an incredible amount of assistance and teaching me how to use python. Definitely would not have been in a usable state like this without her.
- Sarc python reader and writer by @leoetlino and @BravelyPeculiar https://github.com/zeldamods/sarc
- @CommandMC for refactoring the entire project.
