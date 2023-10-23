# This Python file uses the following encoding: utf-8
import sys
from connection import *
from PySide6.QtWidgets import QApplication, QWidget
from ui_form import Ui_Widget
from dialogWidget import MyDialog
from sort import SortWidget
from operator import attrgetter


def sort_by_field(obj_list, field_name, reverse=False):
    key_function = attrgetter(field_name)
    return sorted(obj_list, key=key_function, reverse=reverse)


class MyWidget(QWidget):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.ui = Ui_Widget()
        self.ui.setupUi(self)
        self.setup()

        self.setLayout(self.ui.gridLayout)
        self.controller = Controller()

        self.addresses = []
        self.page = 0
        self.pages = 0
        self.objects = []
        self.status = ""

        self.reload()

        self.set_global_status(False)

    def update_list(self):
        self.pages = len(self.objects)
        if self.pages != 0:
            self.page = 0
            self.moveItem()

    def reload(self):
        self.objects = self.controller.get_all_objects()
        self.pages = len(self.objects)
        if self.pages != 0:
            self.page = 0
            self.moveItem()

    def set_global_status(self, status: bool):
        self.ui.lineEdit.setEnabled(status)
        self.ui.address.setEnabled(status)
        self.ui.age.setEnabled(status)
        self.ui.time.setEnabled(status)
        self.ui.checkBox.setEnabled(status)

    def moveItem(self):
        current = self.objects[self.page]
        self.ui.lineEdit.setText(current.name)
        self.ui.address.setText(current.address)
        self.ui.age.setText(str(current.age))
        self.ui.time.setText(str(current.date))
        self.ui.checkBox.setChecked(current.is_vip)

    def setup(self):
        self.ui.addBtn.clicked.connect(self.clickedAdd)
        self.ui.submitBtn.clicked.connect(self.clickedSubmit)
        self.ui.nextBtn.clicked.connect(self.clickedNext)
        self.ui.prevBtn.clicked.connect(self.clickedPrev)
        self.ui.cancelBtn.clicked.connect(self.clickedCancel)
        self.ui.pushButton.clicked.connect(self.searchClicked)
        self.ui.delete_2.clicked.connect(self.deleteClicked)
        self.ui.editBtn.clicked.connect(self.editClicked)
        self.ui.export_2.clicked.connect(self.export)
        self.ui.sortBtn.clicked.connect(self.sort)

    def sort(self):
        sortWidget = SortWidget()
        how_sort = sortWidget.exec()
        self.objects = sort_by_field(self.objects, how_sort)
        self.update_list()

    def export(self):
        with open("save.txt", "w") as file:
            for item in self.objects:
                file.write(item.__str__() + '\n')

    def editClicked(self):
        self.status = "edit"
        self.set_global_status(True)

    def deleteClicked(self):
        self.controller.delete_object(self.objects[self.page])
        self.reload()

    def clickedAdd(self):
        self.status = "add"
        self.set_global_status(True)

        self.ui.lineEdit.setText("")
        self.ui.address.setText("")
        self.ui.age.setText("")
        self.ui.time.setText("")
        self.ui.checkBox.setChecked(False)

    def clickedSubmit(self):
        if self.status == "add":
            self.controller.create_object(name=self.ui.lineEdit.text(), is_vip=self.ui.checkBox.isChecked(),
                                          address=self.ui.address.text(), time=self.ui.time.text(), age=self.ui.age.text())

        elif self.status == "edit":
            self.objects[self.page].name = self.ui.lineEdit.text()
            self.objects[self.page].is_vip = self.ui.checkBox.isChecked()
            self.objects[self.page].address = self.ui.address.text()
            self.objects[self.page].age = self.ui.age.text()
            self.objects[self.page].date = datetime.strptime(self.ui.time.text(), date_format)

            self.controller.edit_object(self.objects[self.page])
        elif self.status == "None":
            pass

        self.reload()
        self.set_global_status(False)
        self.status = "None"

    def clickedNext(self):
        self.page += 1
        if self.page < self.pages and self.pages != 1:
            self.moveItem()
        else:
            self.page -= 1

    def clickedPrev(self):
        self.page -= 1
        if self.page >= 0 and self.pages != 1:
            self.moveItem()
        else:
            self.page += 1

    def clickedCancel(self):
        self.reload()
        self.set_global_status(False)
        self.status = "None"

    def searchClicked(self):
        searchDialog = MyDialog(self.objects, self.page)
        self.page = searchDialog.exec()
        self.moveItem()


if __name__ == "__main__":
    app = QApplication(sys.argv)
    widget = MyWidget()
    widget.show()
    sys.exit(app.exec())
