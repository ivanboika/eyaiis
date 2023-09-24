from PyQt5.QtWidgets import QDialog, QGridLayout, QLabel, QSlider, QPushButton, QCheckBox
from src.widgets.image_label import ImageLabel, QPixmap
from PyQt5.QtCore import Qt
from win32api import GetSystemMetrics
import cv2
import numpy as np
from PIL import Image as im

style = 'border: 1px solid #010203'


class Main(QDialog):
    def __init__(self):
        super().__init__()
        self.setAcceptDrops(True)
        self.setWindowTitle('Lab1')

        self.ly = QGridLayout()

        self.start_image = ImageLabel()
        self.start_image.setStyleSheet(style)
        self.noise_image = QLabel()
        self.noise_image.setStyleSheet(style)
        self.edit_image = QLabel()
        self.edit_image.setStyleSheet(style)

        self.blurCheckBox = QCheckBox()
        self.closingCheckBox = QCheckBox()

        self.noise_slider = QSlider(Qt.Horizontal)
        self.threshold_slider = QSlider(Qt.Horizontal)

        self.noice_label = QLabel('Noice value: ')
        self.noice_label.setStyleSheet(style)
        self.threshold_label = QLabel('Threshold value: ')
        self.threshold_label.setStyleSheet(style)

        self.startBtn = QPushButton('Start')
        self.startBtn.setToolTip('Starts adding noise to the image')
        self.restoreBtn = QPushButton('Restore')
        self.restoreBtn.setToolTip('Restores image')
        self.restartBtn = QPushButton('Restart')
        self.restartBtn.setToolTip('Sets everything to zero and deleted images')

        self.ly_internal = QGridLayout()

        self.setup()

    def start_clicked(self):
        if self.start_image.text() == '':
            pass
        else:
            image = cv2.imread(self.start_image.text(), cv2.IMREAD_GRAYSCALE)
            mean = 0
            noise = np.random.normal(mean, self.noise_slider.value() / 10, image.shape).astype(np.uint8)
            noisy_image = cv2.add(image, noise)
            data = im.fromarray(noisy_image)

            data.save('image.png')
            self.noise_image.setPixmap(QPixmap('image.png'))

    def restart_clicked(self):
        self.noise_slider.setValue(0)
        self.threshold_slider.setValue(0)
        self.start_image.setPixmap(QPixmap())
        self.noise_image.setPixmap(QPixmap())
        self.edit_image.setPixmap(QPixmap())

    def restore_clicked(self):
        noisy_image = cv2.imread('image.png', cv2.IMREAD_GRAYSCALE)

        height, width = noisy_image.shape

        if self.blurCheckBox.isChecked():
            noisy_image = cv2.GaussianBlur(noisy_image, (1, 1), cv2.BORDER_DEFAULT)

        for i in range(height - 1):
            for j in range(width - 1):
                middle = 0
                if i == 0 and j == 0:
                    middle = (noisy_image[i][j + 1] / 8 + noisy_image[i][j + 2] / 8 +
                              noisy_image[i + 1][j] / 8 + noisy_image[i + 1][j + 1] / 8 +
                              noisy_image[i + 1][j + 2] / 8 + noisy_image[i + 2][j] / 8 +
                              noisy_image[i + 2][j + 1] / 8 + noisy_image[i][j + 2] / 8)
                elif i == 0:
                    middle = (noisy_image[i][j - 1] / 5 +
                              noisy_image[i][j + 1] / 5 +
                              noisy_image[i + 1][j - 1] / 5 + noisy_image[i + 1][j + 1] / 5 +
                              noisy_image[i + 1][j] / 5)
                elif j == 0:
                    middle = (noisy_image[i + 1][j] / 5 +
                              noisy_image[i - 1][j] / 5 +
                              noisy_image[i + 1][j + 1] / 5 + noisy_image[i - 1][j + 1] / 5 +
                              noisy_image[i][j + 1] / 5)
                elif i == height and j == 0:
                    middle = (noisy_image[i][j + 1] / 8 + noisy_image[i][j + 2] / 8 +
                              noisy_image[i - 1][j + 1] / 8 + noisy_image[i - 1][j + 2] / 8 +
                              noisy_image[i - 1][j] / 8 + noisy_image[i - 2][j] / 8 +
                              noisy_image[i - 2][j + 1] / 8 + noisy_image[i - 2][j + 2] / 8)
                elif i == 0 and j == width:
                    middle = (noisy_image[i][j - 1] / 8 + noisy_image[i][j - 2] / 8 +
                              noisy_image[i + 1][j] / 8 + noisy_image[i + 1][j - 1] / 8 +
                              noisy_image[i + 1][j - 2] / 8 + noisy_image[i + 2][j] / 8 +
                              noisy_image[i + 2][j - 1] / 8 + noisy_image[i + 2][j - 2] / 8)
                elif i == height:
                    middle = (noisy_image[i][j - 1] / 5 +
                              noisy_image[i][j + 1] / 5 +
                              noisy_image[i - 1][j] / 5 + noisy_image[i - 1][j + 1] / 5 +
                              noisy_image[i - 1][j - 1] / 5)
                elif j == width:
                    middle = (noisy_image[i - 1][j] / 5 +
                              noisy_image[i + 1][j] / 5 +
                              noisy_image[i][j - 1] / 5 + noisy_image[i + 1][j - 1] / 5 +
                              noisy_image[i - 1][j - 1] / 5)
                elif i == height and j == width:
                    middle = (noisy_image[i - 1][j] / 8 + noisy_image[i - 2][j] / 8 +
                              noisy_image[i][j - 1] / 8 + noisy_image[i - 1][j - 1] / 8 +
                              noisy_image[i - 2][j - 1] / 8 + noisy_image[i][j - 2] / 8 +
                              noisy_image[i - 1][j - 2] / 8 + noisy_image[i - 2][j - 2] / 8)
                else:
                    middle = (noisy_image[i + 1][j] / 8 + noisy_image[i - 1][j] / 8 +
                              noisy_image[i][j + 1] / 8 + noisy_image[i][j - 1] / 8 +
                              noisy_image[i + 1][j + 1] / 8 + noisy_image[i - 1][j - 1] / 8 +
                              noisy_image[i + 1][j - 1] / 8 + noisy_image[i - 1][j + 1] / 8)

                delta_q = noisy_image[i][j] - middle
                if delta_q > self.threshold_slider.value():
                    noisy_image[i][j] = middle
                else:
                    pass
                #print(delta_q)
        if self.closingCheckBox.isChecked():
            noisy_image = cv2.morphologyEx(noisy_image, cv2.MORPH_CLOSE, (3, 3))
        data = im.fromarray(noisy_image)
        data.save('restored.png')
        self.edit_image.setPixmap(QPixmap('restored.png'))

    def slider_noice_value_changed(self):
        self.noice_label.setText('Noice value: ' + str(self.noise_slider.value()))

    def slider_threshold_value_changed(self):
        self.threshold_label.setText('Threshold value: ' + str(self.threshold_slider.value()))

    def setup(self):
        self.noise_image.setStyleSheet(style)
        self.edit_image.setStyleSheet(style)

        self.noise_slider.setMinimum(0)
        self.noise_slider.setMaximum(100)
        self.noise_slider.setSingleStep(1)
        self.threshold_slider.setMinimum(0)
        self.threshold_slider.setSingleStep(1)
        self.threshold_slider.setMaximum(255)

        self.ly_internal.addWidget(self.noice_label, 0, 3, Qt.AlignmentFlag.AlignLeft)
        self.ly_internal.addWidget(self.noise_slider, 1, 3, Qt.AlignmentFlag.AlignLeft)
        self.ly_internal.addWidget(self.threshold_label, 0, 4, Qt.AlignmentFlag.AlignLeft)
        self.ly_internal.addWidget(self.threshold_slider, 1, 4, Qt.AlignmentFlag.AlignLeft)

        self.ly_internal.addWidget(QLabel('Gaussian Blur -> '), 0, 1, Qt.AlignmentFlag.AlignLeft | Qt.AlignCenter)
        self.ly_internal.addWidget(QLabel('Closing -> '), 1, 1, Qt.AlignmentFlag.AlignLeft | Qt.AlignCenter)
        self.ly_internal.addWidget(self.blurCheckBox, 0, 2, Qt.AlignmentFlag.AlignLeft)
        self.ly_internal.addWidget(self.closingCheckBox, 1, 2, Qt.AlignmentFlag.AlignLeft)

        self.ly_internal.addWidget(self.startBtn, 0, 0, Qt.AlignmentFlag.AlignBottom)
        self.ly_internal.addWidget(self.restoreBtn, 1, 0, Qt.AlignmentFlag.AlignBottom)
        self.ly_internal.addWidget(self.restartBtn, 2, 0, Qt.AlignmentFlag.AlignBottom)

        self.ly.addLayout(self.ly_internal, 0, 0, 3, 3, Qt.AlignmentFlag.AlignTop)

        self.ly.addWidget(QLabel('Started image'), 1, 0, Qt.AlignmentFlag.AlignBottom | Qt.AlignmentFlag.AlignCenter)
        self.ly.addWidget(QLabel('Noised image'), 1, 1, Qt.AlignmentFlag.AlignBottom | Qt.AlignmentFlag.AlignCenter)
        self.ly.addWidget(QLabel('Edited image'), 1, 2, Qt.AlignmentFlag.AlignBottom | Qt.AlignmentFlag.AlignCenter)

        self.ly.addWidget(self.start_image, 2, 0)
        self.ly.addWidget(self.noise_image, 2, 1)
        self.ly.addWidget(self.edit_image, 2, 2)
        self.ly.setSpacing(5)

        self.setLayout(self.ly)
        self.setMinimumSize(GetSystemMetrics(0) / 3, GetSystemMetrics(1) / 3)

        self.noise_slider.valueChanged.connect(self.slider_noice_value_changed)
        self.threshold_slider.valueChanged.connect(self.slider_threshold_value_changed)
        self.startBtn.clicked.connect(self.start_clicked)
        self.restartBtn.clicked.connect(self.restart_clicked)
        self.restoreBtn.clicked.connect(self.restore_clicked)

    def dragEnterEvent(self, event):
        if event.mimeData().hasImage:
            event.accept()
        else:
            event.ignore()

    def dragMoveEvent(self, event):
        if event.mimeData().hasImage:
            event.accept()
        else:
            event.ignore()

    def dropEvent(self, event):
        if event.mimeData().hasImage:
            event.setDropAction(Qt.CopyAction)
            self.filePath = event.mimeData().urls()[0].toLocalFile()
            self.set_image(self.filePath)

            event.accept()
        else:
            event.ignore()

    def set_image(self, file_path):
        self.start_image.setPixmap(file_path)
        self.adjustSize()
