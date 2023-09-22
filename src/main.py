import sys

from src.screens.main_window import Main
from PyQt5.QtWidgets import QApplication


if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = Main()
    window.exec()

    app.exec()
