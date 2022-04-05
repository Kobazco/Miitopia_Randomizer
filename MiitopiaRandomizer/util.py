import csv
import logging
import os
import random
import shutil
import subprocess
import sys
from io import StringIO

import sarc

from MiitopiaRandomizer.const import base_input_dir, base_output_dir

logger = logging.getLogger('Util')


def get_csv_rows_from_file(file_path: str) -> list[list[str]]:
    with open(file_path, newline='') as f:
        return [*csv.reader(f)]


def get_csv_rows_from_sarc(sarc_or_filename: sarc.SARC | str, file_in_sarc: str) -> list[list[str]]:
    if isinstance(sarc_or_filename, sarc.SARC):
        sarc_reader = sarc_or_filename
    else:
        with open(sarc_or_filename, 'rb') as f:
            sarc_reader = sarc.read_file_and_make_sarc(f)
    file_data = StringIO(
        sarc_reader.get_file_data(file_in_sarc).tobytes().decode(),
        newline=''
    )
    csv_reader = csv.reader(file_data)
    return [*csv_reader]


def get_csv_rows_from_input_sarc(file_path: str, file_in_sarc: str):
    return get_csv_rows_from_sarc(os.path.join(base_input_dir, file_path), file_in_sarc)


def get_writer_from_output_sarc(file_path: str):
    with open(os.path.join(base_output_dir, file_path), 'rb') as f:
        return sarc.read_sarc_and_make_writer(f)


def get_data_file_path(file_path: str) -> str:
    if getattr(sys, 'frozen', False) and hasattr(sys, '_MEIPASS'):
        return os.path.join(sys._MEIPASS, 'Data', file_path)
    return os.path.join('Data', file_path)


def write_sarc_to_output(writer: sarc.SARCWriter, file_path: str):
    with open(os.path.join(base_output_dir, file_path), 'wb') as f:
        writer.write(f)


def randomize_csv_rows(csv_data: list[list[str]], columns_to_randomize: list[int]) -> bytes:
    # Read in all the rows
    all_possible_randomized_values: dict[int, list[str]] = {}
    for num in columns_to_randomize:
        elements: list[str] = []
        for row in csv_data:
            elements.append(row[num])
        random.shuffle(elements)
        all_possible_randomized_values[num] = elements

    randomized_data = StringIO()
    writer = csv.writer(randomized_data)
    for row in csv_data:
        randomized_row = row.copy()
        for num in columns_to_randomize:
            randomized_row[num] = all_possible_randomized_values[num].pop()
        writer.writerow(randomized_row)
    randomized_data.seek(0)
    return randomized_data.read().encode()


def verify_input_files(file_list: list[str], exit_when_missing=True) -> tuple[bool, list[str]]:
    """
    Verifies if files in the input directory are present
    :param file_list: The files to check
    :param exit_when_missing: If True, the function will exit the whole program if a file is missing
    :return: bool -> False if files are missing; list -> the files that are missing
    """
    missing_files: list[str] = []
    for file in file_list:
        full_file_path = os.path.join(base_input_dir, file)
        if not os.path.exists(full_file_path):
            if exit_when_missing:
                print(f'File {file} is missing, can\'t continue!')
                sys.exit(1)
            missing_files.append(file)
    return not bool(missing_files), missing_files


def copy_input_to_output(file_path: str):
    # Don't overwrite the file if it already exists
    if os.path.exists(os.path.join(base_output_dir, file_path)):
        return
    os.makedirs(os.path.join(base_output_dir, os.path.dirname(file_path)), exist_ok=True)
    shutil.copyfile(os.path.join(base_input_dir, file_path), os.path.join(base_output_dir, file_path))


def clear_output_dir():
    if os.path.isdir('Output'):
        shutil.rmtree('Output')
    os.makedirs(base_output_dir)


def read_input_sarc(file_path: str) -> sarc.SARC:
    with open(os.path.join(base_input_dir, file_path), 'rb') as f:
        return sarc.read_file_and_make_sarc(f)


def get_file_version() -> str:
    """
    Figures out if the input files are from a 3DS or a Switch version

    :return: '3DS', 'Switch', or 'Unknown'
    """
    world01_path = os.path.join('stage', 'World01.sarc')
    file_exists, _ = verify_input_files([world01_path], False)
    if not file_exists:
        return 'Unknown'
    sarc_reader = read_input_sarc(world01_path)
    # This file is only present in the Switch version
    if 'W1_0_20_Horse_enemy.csv' in sarc_reader.list_files():
        return 'Switch'
    return '3DS'


def show_folder(folder_path: str):
    full_path = os.path.abspath(folder_path)
    if sys.platform == 'win32':
        os.startfile(full_path)
    else:
        subprocess.run(['xdg-open', full_path])
