from PyQt5.QtWidgets import QApplication, QLabel, QMainWindow, QPushButton, QWidget
from PyQt5.QtCore import Qt
from PyQt5.QtGui import QImage, QPalette, QBrush, QIcon, QPixmap, QMoveEvent
from PyQt5 import  QtCore

from MainWindow import *
import sys
import multiprocessing as mp
import time


class PauseWindow(QMainWindow):
    def __init__(self, window):
        super(PauseWindow, self).__init__()

        self.setWindowTitle("Paused")
        self.setFixedSize(600, 500)

        self.label = QLabel(self)
        self.pixmap = QPixmap('Images/img.png')
        self.label.setPixmap(self.pixmap)
        self.label.resize(600, 500)

        self.mainLabel = QLabel("PAUSED", self)
        self.mainLabel.resize(235, 100)
        self.mainLabel.setStyleSheet("color: white; font-size:32px; font:bold")
        self.mainLabel.move(235, 0)
        self.backToMain = MainWindow()

        self.returnBtn = QPushButton("Return to game", self)
        self.returnBtn.setStyleSheet("QPushButton{"
                                     "color: white; background-color: transparent; font:bold; border-style: outset; border-width: 2px; border-color: white"
                                     "}"
                                     "QPushButton:hover{"
                                     "background-color: #3F7FBF"
                                     "}")
        self.returnBtn.resize(100, 50)
        self.returnBtn.move(250, 150)
        self.returnBtn.clicked.connect(self.close)


        self.exitBtn = QPushButton("Exit game", self)
        self.exitBtn.setStyleSheet("QPushButton{"
                                   "color: white; background-color: transparent; font:bold; border-style: outset; border-width: 2px; border-color: white"
                                   "}"
                                   "QPushButton:hover{"
                                   "background-color: #C14242"
                                   "}")
        self.exitBtn.resize(100, 50)
        self.exitBtn.move(250, 230)
        self.exitBtn.clicked.connect(self.close)

    def keyPressEvent(self, event):
        if event.key() == QtCore.Qt.Key_Escape:
          self.window().hide()