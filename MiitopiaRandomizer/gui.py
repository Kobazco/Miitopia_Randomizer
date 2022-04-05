import logging
import os.path
import random
import sys
from typing import Callable

from PyQt6.QtGui import QIntValidator
from PyQt6.QtWidgets import QMainWindow, QWidget, QVBoxLayout, QLabel, QFrame, QCheckBox, QPushButton, QHBoxLayout, \
    QLineEdit, QMessageBox

from MiitopiaRandomizer import randomizationOptions, version
from MiitopiaRandomizer.const import required_files, base_input_dir, max_seed_value
from MiitopiaRandomizer.util import get_file_version, verify_input_files, show_folder, clear_output_dir


class HorizontalLine(QFrame):
    def __init__(self, *args, **kwargs):
        super(HorizontalLine, self).__init__(*args, **kwargs)
        self.setFrameShape(QFrame.Shape.HLine)
        self.setFrameShadow(QFrame.Shadow.Sunken)


class MainWindow(QMainWindow):
    def __init__(self, *args, **kwargs):
        super(MainWindow, self).__init__(*args, **kwargs)
        self.logger = logging.getLogger('Main')
        self.logger.info('Starting MiitopiaRandomizer...')

        main_widget = QWidget(self)
        self.setCentralWidget(main_widget)
        layout = QVBoxLayout(main_widget)

        title_label = QLabel('Miitopia Randomizer v' + version)
        default_font = title_label.font()
        default_font.setPointSize(14)
        title_label.setFont(default_font)
        layout.addWidget(title_label)

        layout.addWidget(HorizontalLine(main_widget))

        # Battle randomization

        randomize_battles = QCheckBox('Randomize battles', main_widget)
        randomize_battles.setToolTip(
            'Randomizes the enemies that appear in battle.\n'
            'Some logic is applied: Randomized enemies will have a similar level\n'
            'and important enemies won\'t be randomized.'
        )
        layout.addWidget(randomize_battles)

        randomize_battle_music = QCheckBox('Randomize battle background music', main_widget)
        randomize_battle_music.setEnabled(False)
        layout.addWidget(randomize_battle_music)
        randomize_battles.stateChanged.connect(randomize_battle_music.setEnabled)
        randomize_battles.stateChanged.connect(randomize_battle_music.setChecked)

        randomize_battle_backgrounds = QCheckBox('Randomize battle backgrounds')
        randomize_battle_backgrounds.setEnabled(False)
        # This option only works on Switch, so only show the checkbox if we are on Switch
        if get_file_version() != '3DS':
            layout.addWidget(randomize_battle_backgrounds)
            randomize_battles.stateChanged.connect(randomize_battle_backgrounds.setEnabled)
            randomize_battles.stateChanged.connect(randomize_battle_backgrounds.setChecked)

        layout.addWidget(HorizontalLine(main_widget))

        # Job randomization

        randomize_job_worlds = QCheckBox('Randomize the worlds jobs unlock in', main_widget)
        layout.addWidget(randomize_job_worlds)
        randomize_job_worlds.stateChanged.connect(lambda: handle_job_checkboxes(
            randomize_job_worlds, randomize_job_weapons, job_randomization_logic
        ))

        randomize_job_weapons = QCheckBox('Randomize job weapons', main_widget)
        layout.addWidget(randomize_job_weapons)
        randomize_job_weapons.stateChanged.connect(lambda: handle_job_checkboxes(
            randomize_job_worlds, randomize_job_weapons, job_randomization_logic
        ))

        job_randomization_logic = QCheckBox('Job Randomization Logic', main_widget)
        job_randomization_logic.setToolTip(
            'Un-hides hidden jobs and unlocks them in world 2 and 3 respectively.\n'
            'This prevents issues once the jobs are randomized, so every job is eventually available.'
        )
        job_randomization_logic.setEnabled(False)
        job_randomization_logic.setChecked(True)
        layout.addWidget(job_randomization_logic)

        layout.addWidget(HorizontalLine(main_widget))

        # Treasure Chest randomization

        randomize_treasure = QCheckBox('Randomize Treasure Chests', main_widget)
        layout.addWidget(randomize_treasure)

        layout.addWidget(HorizontalLine(main_widget))

        # NPC randomization

        randomize_npcs = QCheckBox('Randomize NPCs', main_widget)
        layout.addWidget(randomize_npcs)

        randomize_dl_enemy = QCheckBox('Randomize Dark Lord enemy model', main_widget)
        layout.addWidget(randomize_dl_enemy)

        layout.addStretch()

        bottom_layout = QHBoxLayout(layout.widget())

        seed_input_box = QLineEdit(main_widget)
        seed_input_box.setPlaceholderText('Seed (leave empty for random)')
        seed_input_box.setValidator(QIntValidator(0, max_seed_value))
        bottom_layout.addWidget(seed_input_box)

        do_randomization_button = QPushButton('Randomize!', main_widget)
        # This is really ugly but oh well
        do_randomization_button.pressed.connect(lambda: do_randomization(
            randomize_battles.isChecked(), randomize_battle_music.isChecked(), randomize_battle_backgrounds.isChecked(),
            randomize_job_worlds.isChecked(), randomize_job_weapons.isChecked(), job_randomization_logic.isChecked(),
            randomize_treasure.isChecked(), randomize_npcs.isChecked(), randomize_dl_enemy.isChecked(),
            seed_input_box.text()
        ))
        bottom_layout.addWidget(do_randomization_button)

        layout.addLayout(bottom_layout)

        self.setWindowTitle('Miitopia Randomizer v' + version)
        self.setMinimumSize(300, 500)

        if not os.path.exists(os.path.join('Input', 'romfs', 'cmn')):
            QMessageBox(
                QMessageBox.Icon.Critical,
                'No Input data found',
                'The folder ' +
                os.path.join('Input', 'romfs', 'cmn') + ' '
                'was not found.\n\n'
                'Make sure you copied the "cmn" folder from your romfs into "Input/romfs".'
            ).exec()
            sys.exit(1)


def do_randomization(randomize_battles: bool, randomize_battle_music: bool, randomize_battle_backgrounds: bool,
                     randomize_job_worlds: bool, randomize_job_weapons: bool, job_rando_logic: bool,
                     randomize_treasure: bool, randomize_npcs: bool, randomize_dl: bool, seed: str):
    if not seed:
        seed = random.randint(0, max_seed_value)
    else:
        seed = int(seed)
    random.seed(seed)

    clear_output_dir()

    is_switch = get_file_version() == 'Switch'
    if randomize_battles:
        if not randomization_wrapper(
                'battles', randomizationOptions.randomize_battles,
                [is_switch, randomize_battle_music, randomize_battle_backgrounds]):
            return
    if randomize_job_worlds or randomize_job_weapons:
        if not randomization_wrapper(
                'jobs', randomizationOptions.randomize_jobs,
                [job_rando_logic, randomize_job_worlds, randomize_job_weapons]):
            return
    if randomize_treasure:
        if not randomization_wrapper(
                'treasure', randomizationOptions.randomize_treasure):
            return
    if randomize_npcs:
        if not randomization_wrapper(
                'npcs', randomizationOptions.randomize_npcs,
                [is_switch]):
            return
    if randomize_dl:
        if not randomization_wrapper(
                'dark_lord', randomizationOptions.randomize_dl):
            return

    with open(os.path.join('Output', 'seed.txt'), 'w') as f:
        f.write(str(seed))

    msg = QMessageBox(
        QMessageBox.Icon.Information,
        'Randomization done!',
        'The randomization completed successfully.\n'
        f'The seed for this randomization was {seed}'
    )
    open_output_btn = msg.addButton('Open Output directory', QMessageBox.ButtonRole.ActionRole)
    msg.addButton(QMessageBox.StandardButton.Close)
    msg.exec()
    if msg.clickedButton() == open_output_btn:
        show_folder('Output')


def display_abort_message(missing_files: list[str]):
    text = 'The randomization could not be completed because the following files are missing:\n\n'
    for file in missing_files:
        full_path = os.path.join(base_input_dir, file)
        text += f'{full_path}\n'
    text += '\nPlease make sure you\'ve placed the "cmn" folder into the "Input/romfs" directory.'
    QMessageBox(
        QMessageBox.Icon.Critical,
        'Randomization aborted',
        text,
        QMessageBox.StandardButton.Ok
    ).exec()


def randomization_wrapper(required_files_name: str, func_to_call: Callable, args: list = None) -> bool:
    if args is None:
        args = []
    all_files_exist, missing_files = verify_input_files(required_files[required_files_name], False)
    if not all_files_exist:
        display_abort_message(missing_files)
        return False
    func_to_call(*args)
    return True


def handle_job_checkboxes(worlds: QCheckBox, weapons: QCheckBox, logic: QCheckBox):
    if worlds.isChecked() or weapons.isChecked():
        logic.setEnabled(True)
    else:
        logic.setEnabled(False)
        logic.setChecked(False)
