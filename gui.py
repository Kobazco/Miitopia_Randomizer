import ctypes
import logging
import sys

from PyQt6.QtGui import QIcon
from PyQt6.QtWidgets import QApplication

from MiitopiaRandomizer.gui import MainWindow
from MiitopiaRandomizer.util import get_data_file_path


def main():
    app = QApplication(sys.argv)
    app.setWindowIcon(QIcon(get_data_file_path('icon.png')))
    window = MainWindow()
    window.show()
    sys.exit(app.exec())


if __name__ == '__main__':
    if sys.platform == 'win32':
        ctypes.windll.shell32.SetCurrentProcessExplicitAppUserModelID('miitopia.randomizer')
    logging.basicConfig(
        level=logging.INFO,
        format='[%(asctime)s] [%(name)s/%(levelname)s] %(message)s',
        datefmt='%H:%M:%S'
    )
    main()
