from ui_dialog import Ui_Dialog
from PySide6.QtWidgets import QDialog, QMessageBox


class MyDialog(QDialog):
    def __init__(self, addresses, pos, parent=None):
        super().__init__(parent)
        self.returnPos = pos
        self.addresses = addresses
        self.dg = Ui_Dialog()
        self.dg.setupUi(self)
        self.setWindowTitle('Search record')

        self.setLayout(self.dg.formLayout)

        self.dg.pushButton.clicked.connect(self.searchClicked)
        self.dg.pushButton_2.clicked.connect(self.close)

    def searchClicked(self):
        exist = False
        msg = QMessageBox()
        msg.setWindowTitle('Search')
        msg.setStandardButtons(QMessageBox.Ok)

        for item in self.addresses:
            if item.name == self.dg.lineEdit.text():
                exist = True
                self.returnPos = self.addresses.index(item)
                msg.setText(f'Your record \'{self.dg.lineEdit.text()}\' was found!')
                msg.exec()
                self.close()

        if not exist:
            msg.setText(f'Your record \'{self.dg.lineEdit.text()}\' was not found!')
            msg.setStandardButtons(QMessageBox.Ok)
            msg.exec()
        self.dg.lineEdit.clear()

    def exec(self) -> int:
        super().exec()
        return self.returnPos
