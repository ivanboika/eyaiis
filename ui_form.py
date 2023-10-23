# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'form.ui'
##
## Created by: Qt User Interface Compiler version 6.5.3
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QBrush, QColor, QConicalGradient, QCursor,
    QFont, QFontDatabase, QGradient, QIcon,
    QImage, QKeySequence, QLinearGradient, QPainter,
    QPalette, QPixmap, QRadialGradient, QTransform)
from PySide6.QtWidgets import (QApplication, QCheckBox, QGridLayout, QHBoxLayout,
    QLabel, QLineEdit, QPushButton, QSizePolicy,
    QWidget)

class Ui_Widget(object):
    def setupUi(self, Widget):
        if not Widget.objectName():
            Widget.setObjectName(u"Widget")
        Widget.resize(948, 585)
        Widget.setStyleSheet(u"background-color: rgb(234, 244, 255);")
        self.gridLayoutWidget = QWidget(Widget)
        self.gridLayoutWidget.setObjectName(u"gridLayoutWidget")
        self.gridLayoutWidget.setGeometry(QRect(110, 40, 801, 411))
        self.gridLayout = QGridLayout(self.gridLayoutWidget)
        self.gridLayout.setObjectName(u"gridLayout")
        self.gridLayout.setHorizontalSpacing(6)
        self.gridLayout.setVerticalSpacing(5)
        self.gridLayout.setContentsMargins(5, 5, 5, 5)
        self.label_3 = QLabel(self.gridLayoutWidget)
        self.label_3.setObjectName(u"label_3")
        self.label_3.setLayoutDirection(Qt.RightToLeft)
        self.label_3.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)

        self.gridLayout.addWidget(self.label_3, 3, 0, 1, 1)

        self.label_5 = QLabel(self.gridLayoutWidget)
        self.label_5.setObjectName(u"label_5")
        self.label_5.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)

        self.gridLayout.addWidget(self.label_5, 4, 0, 1, 1)

        self.pushButton = QPushButton(self.gridLayoutWidget)
        self.pushButton.setObjectName(u"pushButton")
        self.pushButton.setStyleSheet(u"background-color: rgb(255, 238, 253);")

        self.gridLayout.addWidget(self.pushButton, 3, 4, 1, 1)

        self.address = QLineEdit(self.gridLayoutWidget)
        self.address.setObjectName(u"address")

        self.gridLayout.addWidget(self.address, 1, 1, 1, 1)

        self.label_2 = QLabel(self.gridLayoutWidget)
        self.label_2.setObjectName(u"label_2")
        self.label_2.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)

        self.gridLayout.addWidget(self.label_2, 1, 0, 1, 1)

        self.submitBtn = QPushButton(self.gridLayoutWidget)
        self.submitBtn.setObjectName(u"submitBtn")
        self.submitBtn.setStyleSheet(u"background-color: rgb(255, 238, 253);")

        self.gridLayout.addWidget(self.submitBtn, 1, 4, 1, 1)

        self.time = QLineEdit(self.gridLayoutWidget)
        self.time.setObjectName(u"time")

        self.gridLayout.addWidget(self.time, 4, 1, 1, 1)

        self.label = QLabel(self.gridLayoutWidget)
        self.label.setObjectName(u"label")
        self.label.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)

        self.gridLayout.addWidget(self.label, 0, 0, 1, 1)

        self.age = QLineEdit(self.gridLayoutWidget)
        self.age.setObjectName(u"age")

        self.gridLayout.addWidget(self.age, 2, 1, 1, 1)

        self.label_4 = QLabel(self.gridLayoutWidget)
        self.label_4.setObjectName(u"label_4")
        self.label_4.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)

        self.gridLayout.addWidget(self.label_4, 2, 0, 1, 1)

        self.cancelBtn = QPushButton(self.gridLayoutWidget)
        self.cancelBtn.setObjectName(u"cancelBtn")
        self.cancelBtn.setStyleSheet(u"background-color: rgb(255, 238, 253);")

        self.gridLayout.addWidget(self.cancelBtn, 2, 4, 1, 1)

        self.lineEdit = QLineEdit(self.gridLayoutWidget)
        self.lineEdit.setObjectName(u"lineEdit")
        self.lineEdit.setAlignment(Qt.AlignCenter)
        self.lineEdit.setReadOnly(False)

        self.gridLayout.addWidget(self.lineEdit, 0, 1, 1, 1)

        self.checkBox = QCheckBox(self.gridLayoutWidget)
        self.checkBox.setObjectName(u"checkBox")
        self.checkBox.setEnabled(True)
        self.checkBox.setLayoutDirection(Qt.LeftToRight)
        self.checkBox.setChecked(False)
        self.checkBox.setTristate(False)

        self.gridLayout.addWidget(self.checkBox, 3, 1, 1, 1)

        self.addBtn = QPushButton(self.gridLayoutWidget)
        self.addBtn.setObjectName(u"addBtn")
        self.addBtn.setStyleSheet(u"background-color: rgb(255, 238, 253);")

        self.gridLayout.addWidget(self.addBtn, 0, 4, 1, 1)

        self.delete_2 = QPushButton(self.gridLayoutWidget)
        self.delete_2.setObjectName(u"delete_2")
        self.delete_2.setStyleSheet(u"background-color: rgb(255, 238, 253);\n"
"background-color: rgb(255, 238, 253);")

        self.gridLayout.addWidget(self.delete_2, 5, 4, 1, 1)

        self.editBtn = QPushButton(self.gridLayoutWidget)
        self.editBtn.setObjectName(u"editBtn")
        self.editBtn.setStyleSheet(u"background-color: rgb(255, 238, 253);")

        self.gridLayout.addWidget(self.editBtn, 4, 4, 1, 1)

        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setSpacing(10)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.horizontalLayout.setContentsMargins(2, 2, 2, 2)
        self.export_2 = QPushButton(self.gridLayoutWidget)
        self.export_2.setObjectName(u"export_2")
        self.export_2.setStyleSheet(u"background-color: rgb(255, 238, 253);")

        self.horizontalLayout.addWidget(self.export_2)

        self.sortBtn = QPushButton(self.gridLayoutWidget)
        self.sortBtn.setObjectName(u"sortBtn")
        self.sortBtn.setStyleSheet(u"background-color: rgb(255, 238, 253);")

        self.horizontalLayout.addWidget(self.sortBtn)

        self.nextBtn = QPushButton(self.gridLayoutWidget)
        self.nextBtn.setObjectName(u"nextBtn")
        self.nextBtn.setStyleSheet(u"background-color: rgb(255, 238, 253);")

        self.horizontalLayout.addWidget(self.nextBtn)

        self.prevBtn = QPushButton(self.gridLayoutWidget)
        self.prevBtn.setObjectName(u"prevBtn")
        self.prevBtn.setStyleSheet(u"background-color: rgb(255, 238, 253);")

        self.horizontalLayout.addWidget(self.prevBtn)


        self.gridLayout.addLayout(self.horizontalLayout, 5, 1, 1, 1)


        self.retranslateUi(Widget)

        QMetaObject.connectSlotsByName(Widget)
    # setupUi

    def retranslateUi(self, Widget):
        Widget.setWindowTitle(QCoreApplication.translate("Widget", u"Simple Address Book", None))
        self.label_3.setText(QCoreApplication.translate("Widget", u"VIP", None))
        self.label_5.setText(QCoreApplication.translate("Widget", u"Time created at:", None))
        self.pushButton.setText(QCoreApplication.translate("Widget", u"Search", None))
        self.label_2.setText(QCoreApplication.translate("Widget", u"Address:", None))
        self.submitBtn.setText(QCoreApplication.translate("Widget", u"Submit", None))
        self.label.setText(QCoreApplication.translate("Widget", u"Name:", None))
        self.label_4.setText(QCoreApplication.translate("Widget", u"Age:", None))
        self.cancelBtn.setText(QCoreApplication.translate("Widget", u"Cancel", None))
        self.checkBox.setText("")
        self.addBtn.setText(QCoreApplication.translate("Widget", u"Add", None))
        self.delete_2.setText(QCoreApplication.translate("Widget", u"Delete", None))
        self.editBtn.setText(QCoreApplication.translate("Widget", u"Edit", None))
        self.export_2.setText(QCoreApplication.translate("Widget", u"Export to txt", None))
        self.sortBtn.setText(QCoreApplication.translate("Widget", u"Sort", None))
        self.nextBtn.setText(QCoreApplication.translate("Widget", u"Next", None))
        self.prevBtn.setText(QCoreApplication.translate("Widget", u"Previous", None))
    # retranslateUi

