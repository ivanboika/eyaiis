# This Python file uses the following encoding: utf-8
import sys
import json

from PySide6.QtWidgets import QApplication, QWidget, QMessageBox, QFileDialog
from AddressBook import AddressBook

# Important:
# You need to run the following command to generate the ui_form.py file
#     pyside6-uic form.ui -o ui_form.py, or
#     pyside2-uic form.ui -o ui_form.py
from ui_form import Ui_Widget
from dialogWidget import MyDialog


class MyWidget(QWidget):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.ui = Ui_Widget()
        self.ui.setupUi(self)
        self.setup()
        self.ui.lineEdit.setReadOnly(True)
        self.ui.textEdit.setReadOnly(True)
        self.setLayout(self.ui.gridLayout)

        self.ui.submitBtn.setText('Edit')
        self.ui.cancelBtn.setText('Remove')

        self.addresses = []
        self.page = 0
        self.pages = 0
        self.path = 'address.json'
        with open(self.path, "r") as read_file:
            data = json.load(read_file)
            for item in data['addresses']:
                self.addresses.append(AddressBook(name=item['name'], address=item['address']))

        self.pages = len(self.addresses)
        self.moveItem()

    def moveItem(self):
        self.ui.lineEdit.setText(self.addresses[self.page].name)
        self.ui.textEdit.setText(self.addresses[self.page].address)

    def setup(self):
        self.ui.addBtn.clicked.connect(self.clickedAdd)
        self.ui.submitBtn.clicked.connect(self.clickedSubmit)
        self.ui.nextBtn.clicked.connect(self.clickedNext)
        self.ui.prevBtn.clicked.connect(self.clickedPrev)
        self.ui.cancelBtn.clicked.connect(self.clickedCancel)
        self.ui.pushButton.clicked.connect(self.searchClicked)
        self.ui.saveBtn.clicked.connect(self.saveClicked)
        self.ui.loadBtn.clicked.connect(self.loadClicked)
        self.ui.pushButton_4.clicked.connect(self.exportClicked)

    def exportClicked(self):
        filename, _ = QFileDialog.getSaveFileName(self, "Save file", "addressBook.txt", "Data Files (*.txt)")
        if filename:
            with open(filename, "w") as file:
                for item in self.addresses:
                    file.write(item.__export__())

    def loadClicked(self):
        book, _ = QFileDialog.getOpenFileName(self, "Open Address Book", "", "Data Files (*.json)")
        if book != '':
            self.path = book
            self.addresses = []
            with open(book, "r") as read_file:
                data = json.load(read_file)

                for item in data['addresses']:
                    self.addresses.append(AddressBook(name=item['name'], address=item['address']))
            self.pages = len(self.addresses)
            self.page = 0
            self.moveItem()

    def saveClicked(self):
        dict_ = {"addresses": []}
        for item in self.addresses:
            dict_["addresses"].append(item.__dict__())

        queota = QMessageBox.question(self, 'Save', 'Save to the new file?', QMessageBox.Ok | QMessageBox.No)

        if queota == QMessageBox.No:
            with open(self.path, "w") as write_file:
                json.dump(dict_, write_file)
        else:
            filename, _ = QFileDialog.getSaveFileName(self, "Save file", "", "Data Files (*.json)")
            if filename:
                with open(filename, "w") as file:
                    json.dump(dict_, file)

    def clickedAdd(self):
        if self.ui.addBtn.text() == 'Add':
            self.ui.lineEdit.setText('')
            self.ui.textEdit.setText('')
            self.ui.lineEdit.setReadOnly(False)
            self.ui.textEdit.setReadOnly(False)
            self.ui.submitBtn.setText('Submit')
            self.ui.cancelBtn.setText('Cancel')
        else:  # update
            newName = self.ui.lineEdit.text()
            newAddress = self.ui.textEdit.toPlainText()
            self.addresses.remove(self.addresses[self.page])
            self.addresses.append(AddressBook(name=newName, address=newAddress))
            self.ui.addBtn.setText('Add')
            self.ui.lineEdit.setReadOnly(True)
            self.ui.textEdit.setReadOnly(True)

    def clickedSubmit(self):
        if self.ui.submitBtn.text() == 'Submit':
            name = self.ui.lineEdit.text()
            address = self.ui.textEdit.toPlainText()
            exists = False
            for item in self.addresses:
                if name == item.name:
                    warning = QMessageBox()
                    warning.setIcon(QMessageBox.Warning)
                    warning.setWindowTitle('Warning!')
                    warning.setText('This name already exists!')
                    warning.exec()
                    exists = True
            if not exists:
                self.addresses.append(AddressBook(name=name, address=address))
                self.pages = len(self.addresses)
                self.ui.submitBtn.setText('Edit')
                self.ui.cancelBtn.setText('Remove')
        elif self.ui.submitBtn.text() == 'Edit':
            self.ui.addBtn.setText('Update')
            self.ui.submitBtn.setText('Cancel')
            self.ui.lineEdit.setReadOnly(False)
            self.ui.textEdit.setReadOnly(False)
        else:  # Cancel
            self.ui.addBtn.setText('Add')
            self.ui.submitBtn.setText('Edit')
            self.ui.lineEdit.setReadOnly(True)
            self.ui.textEdit.setReadOnly(True)
            self.moveItem()

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
        if self.ui.cancelBtn.text() == 'Cancel':
            self.moveItem()
            self.ui.lineEdit.setReadOnly(True)
            self.ui.textEdit.setReadOnly(True)
            self.ui.submitBtn.setText('Edit')
            self.ui.cancelBtn.setText('Remove')
        else:
            name = self.ui.lineEdit.text()
            for item in self.addresses:
                if item.name == name:
                    confirmMessage = QMessageBox()
                    confirmMessage.setIcon(QMessageBox.Warning)
                    confirmMessage.setWindowTitle('Confirm')
                    confirmMessage.setStandardButtons(QMessageBox.Cancel | QMessageBox.Ok)
                    confirmMessage.setText(f'Are you sure that you want to delete \'{name}\'?')
                    if confirmMessage.exec() == QMessageBox.Ok:
                        successMessage = QMessageBox()
                        successMessage.setWindowTitle('Hooray')
                        successMessage.setText(f'Successfully deleted \'{name}\'!')
                        successMessage.setStandardButtons(QMessageBox.Ok)
                        successMessage.exec()
                        self.addresses.remove(item)
            self.page = 0
            self.pages = len(self.addresses)
            self.moveItem()

    def searchClicked(self):
        searchDialog = MyDialog(self.addresses, self.page)
        self.page = searchDialog.exec()
        self.moveItem()


if __name__ == "__main__":
    app = QApplication(sys.argv)
    widget = MyWidget()
    widget.show()
    sys.exit(app.exec())
