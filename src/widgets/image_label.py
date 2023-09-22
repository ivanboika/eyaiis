from PyQt5.QtWidgets import QLabel
from PyQt5.QtCore import Qt
from PyQt5.QtGui import QPixmap


class ImageLabel(QLabel):
    def __init__(self):
        super().__init__()

        self.setAlignment(Qt.AlignCenter)
        self.setText('\n\n Drop Image Here \n\n')
        self.setStyleSheet('''
            QLabel{
                border: 1px solid #010203
            }
        ''')
        self.imagePath = ''

    def setPixmap(self, image):
        super().setPixmap(QPixmap(image))
        self.imagePath = image

    def text(self):
        return self.imagePath
