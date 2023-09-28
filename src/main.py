import sys
import qtmodern.styles
import qtmodern.windows
import qtmodern.resources

from src.screens.main_window import Main
from PyQt5.QtWidgets import QApplication


if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = Main()
    qtmodern.styles.dark(app)
    mw = qtmodern.windows.ModernWindow(window)
    mw.show()

    sys.exit(app.exec())
