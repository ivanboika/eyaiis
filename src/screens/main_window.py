from PyQt5.QtWidgets import QDialog, QGridLayout, QLabel, QSlider, QPushButton,QCheckBox, QProgressBar, QDockWidget, QVBoxLayout, QHBoxLayout
from src.widgets.image_label import ImageLabel, QPixmap
from PyQt5.QtCore import Qt, QSize
from PyQt5.QtGui import QIcon
from win32api import GetSystemMetrics
import cv2
import numpy as np
from PIL import Image as im

style = 'border: 1px solid #010203;' \
        'border-radius: 10px;'


class Main(QDialog):
    def __init__(self):
        super().__init__()
        self.setAcceptDrops(True)
        self.setWindowTitle('Deleting noise from image')

        self.ly = QGridLayout()

        self.start_image = ImageLabel()
        self.start_image.setStyleSheet(style)
        self.noise_image = QLabel()
        self.noise_image.setStyleSheet(style)
        self.edit_image = QLabel()
        self.edit_image.setStyleSheet(style)

        self.blurCheckBox = QCheckBox()
        self.closingCheckBox = QCheckBox()

        self.progress = QProgressBar()
        self.progress.setStyleSheet("margin: 0.5px;"
                                    "text-align: center;"
                                    "border-radius: 5px;")

        self.noise_slider = QSlider(Qt.Horizontal)
        self.threshold_slider = QSlider(Qt.Horizontal)

        self.noice_label = QLabel('Noice value: ')
        self.progress_label = QLabel('Progress: ')
        self.threshold_label = QLabel('Threshold value: ')

        self.startBtn = QPushButton()
        self.restoreBtn = QPushButton()
        self.restartBtn = QPushButton()
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
        self.progress.setValue(0)
        noisy_image = cv2.imread('image.png', cv2.IMREAD_GRAYSCALE)
        self.progress.setValue(5)
        height, width = noisy_image.shape

        if self.blurCheckBox.isChecked():
            noisy_image = cv2.GaussianBlur(noisy_image, (1, 1), cv2.BORDER_DEFAULT)
        self.progress.setValue(10)

        for i in range(height - 1):
            for j in range(width - 1):
                if self.progress.value() < 90:
                    self.progress.setValue(self.progress.value() + 1)
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
        self.progress.setValue(90)
        data = im.fromarray(noisy_image)
        data.save('restored.png')
        self.edit_image.setPixmap(QPixmap('restored.png'))
        self.progress.setValue(100)

    def slider_noice_value_changed(self):
        self.noice_label.setText('Noice value: ' + str(self.noise_slider.value()))

    def slider_threshold_value_changed(self):
        self.threshold_label.setText('Threshold value: ' + str(self.threshold_slider.value()))

    def settings(self):
        self.noise_image.setStyleSheet(style)
        self.edit_image.setStyleSheet(style)

        self.startBtn.setIcon(QIcon('./static/start.png'))
        self.startBtn.setIconSize(QSize(80, 50))
        self.startBtn.setToolTip('Starts adding noise to the image')

        self.restoreBtn.setIcon(QIcon('./static/restore.png'))
        self.restoreBtn.setIconSize(QSize(80, 50))
        self.restoreBtn.setToolTip('Restores image')

        self.restartBtn.setIcon(QIcon('./static/restart.png'))
        self.restartBtn.setIconSize(QSize(80, 50))
        self.restartBtn.setToolTip('Sets everything to zero and deletes images')

        self.noise_slider.setMinimum(0)
        self.noise_slider.setMaximum(100)
        self.noise_slider.setSingleStep(1)
        self.threshold_slider.setMinimum(0)
        self.threshold_slider.setSingleStep(1)
        self.threshold_slider.setMaximum(255)

        self.setMinimumSize(GetSystemMetrics(0) / 3, GetSystemMetrics(1) / 3)

        self.noise_slider.valueChanged.connect(self.slider_noice_value_changed)
        self.threshold_slider.valueChanged.connect(self.slider_threshold_value_changed)
        self.startBtn.clicked.connect(self.start_clicked)
        self.restartBtn.clicked.connect(self.restart_clicked)
        self.restoreBtn.clicked.connect(self.restore_clicked)
        self.progress.valueChanged.connect(self.update_bar)

    def setup(self):
        self.ly_internal.addWidget(self.noice_label, 0, 0, Qt.AlignmentFlag.AlignLeft)
        self.ly_internal.addWidget(self.noise_slider, 0, 1, Qt.AlignmentFlag.AlignLeft)
        self.ly_internal.addWidget(self.threshold_label, 1, 0, Qt.AlignmentFlag.AlignLeft)
        self.ly_internal.addWidget(self.threshold_slider, 1, 1, Qt.AlignmentFlag.AlignLeft)

        self.ly_internal.addWidget(self.progress_label, 4, 0, Qt.AlignLeft)
        self.ly_internal.addWidget(self.progress, 4, 1, Qt.AlignLeft)

        self.ly_internal.addWidget(QLabel('Gaussian Blur -> '), 2, 0, Qt.AlignmentFlag.AlignLeft | Qt.AlignCenter)
        self.ly_internal.addWidget(QLabel('Closing -> '), 3, 0, Qt.AlignmentFlag.AlignLeft | Qt.AlignCenter)
        self.ly_internal.addWidget(self.blurCheckBox, 2, 1, Qt.AlignmentFlag.AlignLeft)
        self.ly_internal.addWidget(self.closingCheckBox, 3, 1, Qt.AlignmentFlag.AlignLeft)

        self.ly.addLayout(self.ly_internal, 0, 1, 2, 2, Qt.AlignmentFlag.AlignTop)

        vly = QVBoxLayout()
        vly.addWidget(self.startBtn)
        vly.addWidget(self.restoreBtn)
        vly.addWidget(self.restartBtn)
        self.ly.addLayout(vly, 0, 0, 2, 1, Qt.AlignmentFlag.AlignLeft)

        self.ly.addWidget(QLabel('Started image'), 1, 0, Qt.AlignmentFlag.AlignBottom | Qt.AlignmentFlag.AlignCenter)
        self.ly.addWidget(QLabel('Noised image'), 1, 1, Qt.AlignmentFlag.AlignBottom | Qt.AlignmentFlag.AlignCenter)
        self.ly.addWidget(QLabel('Edited image'), 1, 2, Qt.AlignmentFlag.AlignBottom | Qt.AlignmentFlag.AlignCenter)

        im_ly = QHBoxLayout()
        im_ly.addWidget(self.start_image)
        im_ly.addWidget(self.noise_image)
        im_ly.addWidget(self.edit_image)

        self.ly.addLayout(im_ly, 2, 0, 1, 3)

        self.ly.setSpacing(5)
        self.settings()
        self.setLayout(self.ly)

    def update_bar(self):
        self.progress_label.setText('Progress: ' + str(self.progress.value()) + '%')

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
