import sys
from os.path import join

max_seed_value = 2147483647

# The original stageEnemy.py didn't randomize world 7 and 8, so we won't either
world_limit = 6

# Limit of enemies to randomize
# Note that this is the limit, it does not set the amount of enemies
enemy_limit_switch = 8
enemy_limit_3ds = 4

# It still isn't nice to just put a big list into here, but it's better than having the actual files IMO
# Note that this is 0-indexed, so world_files_to_randomize[0] gives you the data for world 1
battle_files_to_randomize: list[list[str]] = [
    # World 1
    [
        'W1_0_04_enemy', 'W1_0_11_enemy', 'W1_0_18_enemy', 'W1_1_03_enemy', 'W1_2_04_enemy', 'W1_2_09_enemy',
        'W1_2_14_enemy', 'W1_0_06_enemy', 'W1_0_12_enemy', 'W1_0_19_enemy', 'W1_1_04_enemy', 'W1_2_05_enemy',
        'W1_2_10_enemy', 'W1_2_15_enemy', 'W1_0_08_enemy', 'W1_0_13_enemy', 'W1_0_20_Horse_enemy', 'W1_2_01_enemy',
        'W1_2_06_enemy', 'W1_2_11_enemy', 'W1_0_09_enemy', 'W1_0_15_enemy', 'W1_1_01_enemy', 'W1_2_02_enemy',
        'W1_2_07_enemy', 'W1_2_12_enemy', 'W1_0_10_enemy', 'W1_0_17_enemy', 'W1_1_02_enemy', 'W1_2_03_enemy',
        'W1_2_08_enemy', 'W1_2_13_enemy'
    ],
    # World 2
    [
        'W2_1_02_enemy', 'W2_1_04_enemy', 'W2_1_06_enemy', 'W2_1_08_enemy', 'W2_2_01_enemy', 'W2_2_02_enemy',
        'W2_2_03_enemy', 'W2_2_04_enemy', 'W2_2_05_enemy', 'W2_2_06_enemy', 'W2_2_07_enemy', 'W2_2_11_enemy',
        'W2_2_12_enemy', 'W2_3_01_enemy', 'W2_3_02_enemy', 'W2_3_03_enemy', 'W2_3_04_enemy', 'W2_3_05_enemy',
        'W2_3_06_enemy', 'W2_3_07_enemy', 'W2_3_08_enemy', 'W2_3_10_enemy', 'W2_3_11_enemy', 'W2_3_12_enemy',
        'W2_3_13_enemy', 'W2_3_15_enemy', 'W2_3_16_enemy', 'W2_3_20_enemy', 'W2_3_21_enemy', 'W2_3_24_enemy',
        'W2_3_25_enemy'
    ],
    # World 3
    [
        'W3_1_01_enemy', 'W3_1_02_enemy', 'W3_1_03_enemy', 'W3_1_05_enemy', 'W3_1_06_enemy', 'W3_1_07_enemy',
        'W3_1_08_enemy', 'W3_1_09_enemy', 'W3_1_10_enemy', 'W3_1_11_enemy', 'W3_1_12_enemy', 'W3_1_13_enemy',
        'W3_1_14_enemy', 'W3_1_15_enemy', 'W3_1_16_enemy', 'W3_1_17_enemy', 'W3_1_18_enemy', 'W3_1_19_enemy',
        'W3_1_20_enemy', 'W3_1_21_enemy', 'W3_1_22_enemy', 'W3_1_23_enemy', 'W3_1_24_enemy', 'W3_1_26_enemy',
        'W3_2_02_enemy', 'W3_2_03_enemy', 'W3_2_04_enemy', 'W3_2_05_enemy', 'W3_2_06_enemy', 'W3_2_07_enemy',
        'W3_2_08_enemy', 'W3_2_09_enemy', 'W3_2_10_enemy', 'W3_2_11_enemy', 'W3_2_12_enemy', 'W3_2_13_enemy',
        'W3_2_14_enemy', 'W3_2_15_enemy', 'W3_2_16_enemy', 'W3_2_18_enemy', 'W3_3_02_enemy', 'W3_3_04_enemy',
        'W3_3_06_enemy'
    ],
    # World 4
    [
        'W4_1_01_enemy', 'W4_1_02_enemy', 'W4_1_04_enemy', 'W4_1_05_enemy', 'W4_1_06_enemy', 'W4_1_07_enemy',
        'W4_1_08_enemy', 'W4_1_09_enemy', 'W4_1_11_enemy', 'W4_1_13_enemy', 'W4_2_01_enemy', 'W4_2_02_enemy',
        'W4_2_03_enemy', 'W4_2_05_enemy', 'W4_2_06_enemy', 'W4_2_07_enemy', 'W4_2_08_enemy', 'W4_2_10_enemy',
        'W4_3_01_enemy', 'W4_3_02_enemy', 'W4_3_03_enemy', 'W4_3_05_enemy', 'W4_3_06_enemy', 'W4_3_08_enemy',
        'W4_3_10_enemy', 'W4_3_11_enemy', 'W4_3_12_enemy', 'W4_3_13_enemy', 'W4_3_14_enemy', 'W4_3_15_enemy',
        'W4_3_16_enemy', 'W4_3_17_enemy', 'W4_3_18_enemy', 'W4_3_19_enemy', 'W4_3_20_enemy', 'W4_3_22_enemy',
        'W4_3_24_enemy', 'W4_3_25_enemy', 'W4_3_26_enemy', 'W4_3_27_enemy'
    ],
    # World 5
    [
        'W5_1_01_enemy', 'W5_1_02_enemy', 'W5_1_03_enemy', 'W5_1_04_enemy', 'W5_1_05_enemy', 'W5_1_06_enemy',
        'W5_1_07_enemy', 'W5_1_08_enemy', 'W5_1_09_enemy', 'W5_1_10_enemy', 'W5_1_11_enemy', 'W5_3_01_enemy',
        'W5_3_02_enemy', 'W5_3_03_enemy', 'W5_3_04_enemy', 'W5_3_05_enemy', 'W5_3_07_enemy', 'W5_3_08_enemy',
        'W5_3_09_enemy', 'W5_3_10_enemy', 'W5_3_11_enemy', 'W5_3_12_enemy', 'W5_3_13_enemy', 'W5_3_14_enemy',
        'W5_3_15_enemy', 'W5_3_16_enemy', 'W5_3_18_enemy', 'W5_3_19_enemy', 'W5_3_20_enemy', 'W5_5_01_enemy',
        'W5_5_02_enemy', 'W5_5_03_enemy', 'W5_5_04_enemy', 'W5_5_05_enemy', 'W5_5_06_enemy', 'W5_5_07_enemy',
        'W5_5_08_enemy', 'W5_5_09_enemy', 'W5_5_10_enemy', 'W5_5_11_enemy', 'W5_5_12_enemy', 'W5_5_13_enemy',
        'W5_5_14_enemy', 'W5_5_15_enemy', 'W5_5_16_enemy', 'W5_5_17_enemy', 'W5_5_18_enemy'
    ],
    # World 6
    [
        'W6_1_01_enemy', 'W6_1_02_enemy', 'W6_1_03_enemy', 'W6_2_02_enemy', 'W6_2_03_enemy', 'W6_2_04_enemy',
        'W6_2_05_enemy', 'W6_2_06_enemy', 'W6_3_01_enemy', 'W6_3_02_enemy', 'W6_3_03_enemy', 'W6_3_04_enemy',
        'W6_4_01_enemy', 'W6_4_02_enemy', 'W6_4_03_enemy', 'W6_4_04_enemy', 'W6_4_05_enemy', 'W6_4_07_enemy',
        'W6_4_08_enemy', 'W6_5_01_enemy', 'W6_5_02_enemy', 'W6_6_01_enemy', 'W6_6_02_enemy', 'W6_6_03_enemy',
        'W6_6_05_enemy', 'W6_6_07_enemy',
    ],
    # World 7
    [
        'W7_1_02_enemy', 'W7_1_03_enemy', 'W7_1_04_enemy', 'W7_1_06_enemy', 'W7_1_07_enemy', 'W7_1_08_enemy',
        'W7_1_09_enemy', 'W7_1_11_enemy', 'W7_1_12_enemy', 'W7_1_14_enemy', 'W7_1_15_enemy', 'W7_1_17_enemy',
        'W7_1_19_enemy', 'W7_1_20_enemy', 'W7_1_21_enemy', 'W7_1_22_enemy',
    ],
    # World 8
    [
        'W8_1_04_enemy', 'W8_2_05_enemy', 'W8_3_05_enemy', 'W8_4_04_enemy', 'W8_5_06_enemy', 'W8_6_04_enemy',
        'W8_7_05_enemy', 'W8_8_05_enemy', 'W8_Tower2_enemy', 'W8_Tower_enemy',
    ]
]

base_romfs_dir = join('romfs', 'cmn', 'param')
base_input_dir = join('Input', base_romfs_dir)
base_output_dir = join('Output', base_romfs_dir)

if getattr(sys, 'frozen', False) and hasattr(sys, '_MEIPASS'):
    data_path = join(sys._MEIPASS, 'Data')
else:
    data_path = 'Data'

required_files: dict[str, list[str]] = {
    'battles': [
        'bg.sarc', 'enemy.sarc', 'sound.sarc', 'book.sarc',
        *[join('stage', f'World{i:02}.sarc') for i in range(1, world_limit+1)]
    ],
    'jobs': ['job.sarc'],
    'treasure': ['dish.sarc', join('stage', 'Treasure.sarc')],
    'npcs': ['npc.sarc'],
    'dark_lord': ['enemy.sarc'],
    'grub': ['dish.sarc']
}
