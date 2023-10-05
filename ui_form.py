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
from PySide6.QtWidgets import (QApplication, QGridLayout, QLabel, QLineEdit,
    QPushButton, QSizePolicy, QTextEdit, QWidget)

class Ui_Widget(object):
    def setupUi(self, Widget):
        if not Widget.objectName():
            Widget.setObjectName(u"Widget")
        Widget.resize(948, 585)
        Widget.setStyleSheet(u"background-color: rgb(234, 244, 255);")
        self.gridLayoutWidget = QWidget(Widget)
        self.gridLayoutWidget.setObjectName(u"gridLayoutWidget")
        self.gridLayoutWidget.setGeometry(QRect(90, 70, 751, 451))
        self.gridLayout = QGridLayout(self.gridLayoutWidget)
        self.gridLayout.setObjectName(u"gridLayout")
        self.gridLayout.setHorizontalSpacing(6)
        self.gridLayout.setVerticalSpacing(5)
        self.gridLayout.setContentsMargins(0, 5, 5, 5)
        self.pushButton = QPushButton(self.gridLayoutWidget)
        self.pushButton.setObjectName(u"pushButton")

        self.gridLayout.addWidget(self.pushButton, 4, 4, 1, 1)

        self.loadBtn = QPushButton(self.gridLayoutWidget)
        self.loadBtn.setObjectName(u"loadBtn")

        self.gridLayout.addWidget(self.loadBtn, 5, 4, 1, 1)

        self.saveBtn = QPushButton(self.gridLayoutWidget)
        self.saveBtn.setObjectName(u"saveBtn")

        self.gridLayout.addWidget(self.saveBtn, 6, 4, 1, 1)

        self.textEdit = QTextEdit(self.gridLayoutWidget)
        self.textEdit.setObjectName(u"textEdit")
        self.textEdit.setReadOnly(False)

        self.gridLayout.addWidget(self.textEdit, 1, 2, 8, 2)

        self.nextBtn = QPushButton(self.gridLayoutWidget)
        self.nextBtn.setObjectName(u"nextBtn")

        self.gridLayout.addWidget(self.nextBtn, 9, 3, 1, 1)

        self.lineEdit = QLineEdit(self.gridLayoutWidget)
        self.lineEdit.setObjectName(u"lineEdit")
        self.lineEdit.setAlignment(Qt.AlignCenter)
        self.lineEdit.setReadOnly(False)

        self.gridLayout.addWidget(self.lineEdit, 0, 2, 1, 2)

        self.submitBtn = QPushButton(self.gridLayoutWidget)
        self.submitBtn.setObjectName(u"submitBtn")

        self.gridLayout.addWidget(self.submitBtn, 2, 4, 1, 1)

        self.cancelBtn = QPushButton(self.gridLayoutWidget)
        self.cancelBtn.setObjectName(u"cancelBtn")

        self.gridLayout.addWidget(self.cancelBtn, 3, 4, 1, 1)

        self.addBtn = QPushButton(self.gridLayoutWidget)
        self.addBtn.setObjectName(u"addBtn")

        self.gridLayout.addWidget(self.addBtn, 1, 4, 1, 1)

        self.label_2 = QLabel(self.gridLayoutWidget)
        self.label_2.setObjectName(u"label_2")
        self.label_2.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)

        self.gridLayout.addWidget(self.label_2, 1, 0, 1, 1)

        self.prevBtn = QPushButton(self.gridLayoutWidget)
        self.prevBtn.setObjectName(u"prevBtn")

        self.gridLayout.addWidget(self.prevBtn, 9, 2, 1, 1)

        self.label = QLabel(self.gridLayoutWidget)
        self.label.setObjectName(u"label")
        self.label.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)

        self.gridLayout.addWidget(self.label, 0, 0, 1, 1)

        self.pushButton_4 = QPushButton(self.gridLayoutWidget)
        self.pushButton_4.setObjectName(u"pushButton_4")

        self.gridLayout.addWidget(self.pushButton_4, 7, 4, 1, 1)


        self.retranslateUi(Widget)

        QMetaObject.connectSlotsByName(Widget)
    # setupUi

    def retranslateUi(self, Widget):
        Widget.setWindowTitle(QCoreApplication.translate("Widget", u"Simple Address Book", None))
        self.pushButton.setText(QCoreApplication.translate("Widget", u"Search", None))
        self.loadBtn.setText(QCoreApplication.translate("Widget", u"Load", None))
        self.saveBtn.setText(QCoreApplication.translate("Widget", u"Save", None))
        self.nextBtn.setText(QCoreApplication.translate("Widget", u"Next", None))
        self.submitBtn.setText(QCoreApplication.translate("Widget", u"Submit", None))
        self.cancelBtn.setText(QCoreApplication.translate("Widget", u"Cancel", None))
        self.addBtn.setText(QCoreApplication.translate("Widget", u"Add", None))
        self.label_2.setText(QCoreApplication.translate("Widget", u"Address:", None))
        self.prevBtn.setText(QCoreApplication.translate("Widget", u"Previous", None))
        self.label.setText(QCoreApplication.translate("Widget", u"Name:", None))
        self.pushButton_4.setText(QCoreApplication.translate("Widget", u"Export", None))
    # retranslateUi

