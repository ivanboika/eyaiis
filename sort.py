from ui_sort import Ui_Form
from PySide6.QtWidgets import QDialog


class SortWidget(QDialog):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.srt = Ui_Form()
        self.srt.setupUi(self)
        self.sortpos = ""

    def exec(self) -> int:
        super().exec()
        if self.srt.radioButton.isChecked():
            self.sortpos = "name"
        elif self.srt.radioButton_3.isChecked():
            self.sortpos = "age"
        elif self.srt.radioButton_2.isChecked():
            self.sortpos = "is_vip"
        elif self.srt.radioButton_4.isChecked():
            self.sortpos = "date"
        elif self.srt.radioButton_5.isChecked():
            self.sortpos = "address"
        return self.sortpos
