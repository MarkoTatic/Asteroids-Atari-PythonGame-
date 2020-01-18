from PyQt5.QtWidgets import QMainWindow, QDesktopWidget, QGraphicsTransform, QShortcut
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtCore import pyqtSignal, QBasicTimer, QRectF, QPoint, QTimerEvent, Qt
from PyQt5.QtWidgets import QLabel, QApplication, QGridLayout, QWidget, QVBoxLayout, QGraphicsView, QGraphicsScene
from PyQt5.QtGui import QPixmap, QTransform, QKeySequence
from math import cos, sin, radians
import  math
import random
import Server

class Bonus(QLabel):
    def __init__(self, w, h, randW, randH, scene: QGraphicsScene):
        super().__init__()
        self.width = w
        self.height = h
        self.myScene = scene
        self.move(randW, randH)
        param = "Images/hh5.png"
        self.setPixmap(QtGui.QPixmap(param))
