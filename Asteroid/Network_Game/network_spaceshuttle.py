from datetime import time

from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtCore import pyqtSignal, QBasicTimer, QRectF, QPoint, QTimerEvent
import math
from Bullet import *
import Server
from Network_Game.network_bullet import *

rocketsList = ['Images/rocketship.png', 'Images/rocketship (1).png', 'Images/rocketship (3).png',
               'Images/rocketship (4).png', 'Images/rocketship (5).png', 'Images/rocketship (6).png',
               'Images/rocketship (7).png', 'Images/rocketship (8).png', 'Images/rocketship (9).png',
               'Images/rocketship (10).png', 'Images/rocketship (11).png', 'Images/rocketship (12).png',
               'Images/rocketship (13).png', 'Images/rocketship (14).png', 'Images/rocketship (15).png',
               'Images/rocketship (16).png', 'Images/rocketship (17).png', 'Images/rocketship (18).png',
               'Images/rocketship (19).png', 'Images/rocketship (20).png', 'Images/rocketship (21).png',
               'Images/rocketship (2).png', 'Images/rocketship (22).png', 'Images/rocketship (23).png',
               'Images/rocketship (24).png', 'Images/rocketship (25).png', 'Images/rocketship (26).png',
               'Images/rocketship (27).png', 'Images/rocketship (28).png', 'Images/rocketship (29).png',
               'Images/rocketship (30).png', 'Images/rocketship (31).png', 'Images/rocketship (32).png',
               'Images/rocketship (33).png', 'Images/rocketship (34).png', 'Images/rocketship (35).png',
               'Images/rocketship (36).png', 'Images/rocketship (37).png', 'Images/rocketship (38).png',
               'Images/rocketship (39).png', 'Images/rocketship (40).png', 'Images/rocketship (41).png',
               'Images/rocketship (42).png', 'Images/rocketship (43).png', 'Images/rocketship (44).png',
               'Images/rocketship (45).png', 'Images/rocketship (46).png', 'Images/rocketship (47).png',
               'Images/rocketship (48).png', 'Images/rocketship (49).png', 'Images/rocketship (50).png',
               'Images/rocketship (51).png', 'Images/rocketship (52).png', 'Images/rocketship (53).png',
               'Images/rocketship (54).png', 'Images/rocketship (55).png', 'Images/rocketship (56).png',
               'Images/rocketship (56).png', 'Images/rocketship (57).png', 'Images/rocketship (58).png',
               'Images/rocketship (59).png', 'Images/rocketship (60).png', 'Images/rocketship (61).png',
               'Images/rocketship (62).png', 'Images/rocketship (63).png', 'Images/rocketship (64).png',
               'Images/rocketship (65).png', 'Images/rocketship (66).png', 'Images/rocketship (67).png',
               'Images/rocketship (68).png', 'Images/rocketship (69).png', 'Images/rocketship (70).png',
               'Images/rocketship (71).png']

rocketsList1 = ['Images/rocketship2.png', 'Images/rocketship2 (1).png', 'Images/rocketship2 (2).png',
                'Images/rocketship2 (3).png', 'Images/rocketship2 (4).png', 'Images/rocketship2 (5).png'
    , 'Images/rocketship2 (6).png', 'Images/rocketship2 (7).png', 'Images/rocketship2 (8).png'
    , 'Images/rocketship2 (9).png', 'Images/rocketship2 (10).png', 'Images/rocketship2 (11).png'
    , 'Images/rocketship2 (12).png', 'Images/rocketship2 (13).png', 'Images/rocketship2 (14).png'
    , 'Images/rocketship2 (15).png', 'Images/rocketship2 (16).png', 'Images/rocketship2 (17).png'
    , 'Images/rocketship2 (18).png', 'Images/rocketship2 (19).png', 'Images/rocketship2 (20).png'
    , 'Images/rocketship2 (21).png', 'Images/rocketship2 (22).png', 'Images/rocketship2 (23).png'
    , 'Images/rocketship2 (24).png', 'Images/rocketship2 (25).png', 'Images/rocketship2 (26).png'
    , 'Images/rocketship2 (27).png', 'Images/rocketship2 (28).png', 'Images/rocketship2 (29).png'
    , 'Images/rocketship2 (30).png', 'Images/rocketship2 (31).png', 'Images/rocketship2 (32).png'
    , 'Images/rocketship2 (33).png', 'Images/rocketship2 (34).png', 'Images/rocketship2 (35).png'
    , 'Images/rocketship2 (36).png', 'Images/rocketship2 (37).png', 'Images/rocketship2 (38).png'
    , 'Images/rocketship2 (39).png', 'Images/rocketship2 (40).png', 'Images/rocketship2 (41).png'
    , 'Images/rocketship2 (42).png', 'Images/rocketship2 (43).png', 'Images/rocketship2 (44).png'
    , 'Images/rocketship2 (45).png', 'Images/rocketship2 (46).png', 'Images/rocketship2 (47).png'
    , 'Images/rocketship2 (48).png', 'Images/rocketship2 (49).png', 'Images/rocketship2 (50).png'
    , 'Images/rocketship2 (51).png', 'Images/rocketship2 (52).png', 'Images/rocketship2 (53).png'
    , 'Images/rocketship2 (54).png', 'Images/rocketship2 (55).png', 'Images/rocketship2 (56).png'
    , 'Images/rocketship2 (57).png', 'Images/rocketship2 (58).png', 'Images/rocketship2 (59).png'
    , 'Images/rocketship2 (60).png', 'Images/rocketship2 (61).png', 'Images/rocketship2 (62).png'
    , 'Images/rocketship2 (63).png', 'Images/rocketship2 (64).png', 'Images/rocketship2 (65).png'
    , 'Images/rocketship2 (66).png', 'Images/rocketship2 (67).png', 'Images/rocketship2 (68).png'
    , 'Images/rocketship2 (69).png', 'Images/rocketship2 (70).png', 'Images/rocketship2 (71).png']

rocketsList2 = ['Images/rocketship3.png', 'Images/rocketship3 (1).png', 'Images/rocketship3 (2).png',
                'Images/rocketship3 (3).png', 'Images/rocketship3 (4).png', 'Images/rocketship3 (5).png'
    , 'Images/rocketship3 (6).png', 'Images/rocketship3 (7).png', 'Images/rocketship3 (8).png'
    , 'Images/rocketship3 (9).png', 'Images/rocketship3 (10).png', 'Images/rocketship3 (11).png'
    , 'Images/rocketship3 (12).png', 'Images/rocketship3 (13).png', 'Images/rocketship3 (14).png'
    , 'Images/rocketship3 (15).png', 'Images/rocketship3 (16).png', 'Images/rocketship3 (17).png'
    , 'Images/rocketship3 (18).png', 'Images/rocketship3 (19).png', 'Images/rocketship3 (20).png'
    , 'Images/rocketship3 (21).png', 'Images/rocketship3 (22).png', 'Images/rocketship3 (23).png'
    , 'Images/rocketship3 (24).png', 'Images/rocketship3 (25).png', 'Images/rocketship3 (26).png'
    , 'Images/rocketship3 (27).png', 'Images/rocketship3 (28).png', 'Images/rocketship3 (29).png'
    , 'Images/rocketship3 (30).png', 'Images/rocketship3 (31).png', 'Images/rocketship3 (32).png'
    , 'Images/rocketship3 (33).png', 'Images/rocketship3 (34).png', 'Images/rocketship3 (35).png'
    , 'Images/rocketship3 (36).png', 'Images/rocketship3 (37).png', 'Images/rocketship3 (38).png'
    , 'Images/rocketship3 (39).png', 'Images/rocketship3 (40).png', 'Images/rocketship3 (41).png'
    , 'Images/rocketship3 (42).png', 'Images/rocketship3 (43).png', 'Images/rocketship3 (44).png'
    , 'Images/rocketship3 (45).png', 'Images/rocketship3 (46).png', 'Images/rocketship3 (47).png'
    , 'Images/rocketship3 (48).png', 'Images/rocketship3 (49).png', 'Images/rocketship3 (50).png'
    , 'Images/rocketship3 (51).png', 'Images/rocketship3 (52).png', 'Images/rocketship3 (53).png'
    , 'Images/rocketship3 (54).png', 'Images/rocketship3 (55).png', 'Images/rocketship3 (56).png'
    , 'Images/rocketship3 (57).png', 'Images/rocketship3 (58).png', 'Images/rocketship3 (59).png'
    , 'Images/rocketship3 (60).png', 'Images/rocketship3 (61).png', 'Images/rocketship3 (62).png'
    , 'Images/rocketship3 (63).png', 'Images/rocketship3 (64).png', 'Images/rocketship3 (65).png'
    , 'Images/rocketship3 (66).png', 'Images/rocketship3 (67).png', 'Images/rocketship3 (68).png'
    , 'Images/rocketship3 (69).png', 'Images/rocketship3 (70).png', 'Images/rocketship3 (71).png']

rocketsList3 = ['Images/rocketship4.png', 'Images/rocketship4 (1).png', 'Images/rocketship4 (2).png',
                'Images/rocketship4 (3).png', 'Images/rocketship4 (4).png', 'Images/rocketship4 (5).png'
    , 'Images/rocketship4 (6).png', 'Images/rocketship4 (7).png', 'Images/rocketship4 (8).png'
    , 'Images/rocketship4 (9).png', 'Images/rocketship4 (10).png', 'Images/rocketship4 (11).png'
    , 'Images/rocketship4 (12).png', 'Images/rocketship4 (13).png', 'Images/rocketship4 (14).png'
    , 'Images/rocketship4 (15).png', 'Images/rocketship4 (16).png', 'Images/rocketship4 (17).png'
    , 'Images/rocketship4 (18).png', 'Images/rocketship4 (19).png', 'Images/rocketship4 (20).png'
    , 'Images/rocketship4 (21).png', 'Images/rocketship4 (22).png', 'Images/rocketship4 (23).png'
    , 'Images/rocketship4 (24).png', 'Images/rocketship4 (25).png', 'Images/rocketship4 (26).png'
    , 'Images/rocketship4 (27).png', 'Images/rocketship4 (28).png', 'Images/rocketship4 (29).png'
    , 'Images/rocketship4 (30).png', 'Images/rocketship4 (31).png', 'Images/rocketship4 (32).png'
    , 'Images/rocketship4 (33).png', 'Images/rocketship4 (34).png', 'Images/rocketship4 (35).png'
    , 'Images/rocketship4 (36).png', 'Images/rocketship4 (37).png', 'Images/rocketship4 (38).png'
    , 'Images/rocketship4 (39).png', 'Images/rocketship4 (40).png', 'Images/rocketship4 (41).png'
    , 'Images/rocketship4 (42).png', 'Images/rocketship4 (43).png', 'Images/rocketship4 (44).png'
    , 'Images/rocketship4 (45).png', 'Images/rocketship4 (46).png', 'Images/rocketship4 (47).png'
    , 'Images/rocketship4 (48).png', 'Images/rocketship4 (49).png', 'Images/rocketship4 (50).png'
    , 'Images/rocketship4 (51).png', 'Images/rocketship4 (52).png', 'Images/rocketship4 (53).png'
    , 'Images/rocketship4 (54).png', 'Images/rocketship4 (55).png', 'Images/rocketship4 (56).png'
    , 'Images/rocketship4 (57).png', 'Images/rocketship4 (58).png', 'Images/rocketship4 (59).png'
    , 'Images/rocketship4 (60).png', 'Images/rocketship4 (61).png', 'Images/rocketship4 (62).png'
    , 'Images/rocketship4 (63).png', 'Images/rocketship4 (64).png', 'Images/rocketship4 (65).png'
    , 'Images/rocketship4 (66).png', 'Images/rocketship4 (67).png', 'Images/rocketship4 (68).png'
    , 'Images/rocketship4 (69).png', 'Images/rocketship4 (70).png', 'Images/rocketship4 (71).png']


class NetworkSpaceShuttle(QLabel):
    upRocket1 = pyqtSignal()
    fireRocket1 = pyqtSignal()
    leftRocket1 = pyqtSignal()
    rightRocket1 = pyqtSignal()
    upRocket2 = pyqtSignal()
    fireRocket2 = pyqtSignal()
    leftRocket2 = pyqtSignal()
    rightRocket2 = pyqtSignal()
    upRocket3 = pyqtSignal()
    fireRocket3 = pyqtSignal()
    leftRocket3 = pyqtSignal()
    rightRocket3 = pyqtSignal()
    upRocket4 = pyqtSignal()
    fireRocket4 = pyqtSignal()
    leftRocket4 = pyqtSignal()
    rightRocket4 = pyqtSignal()

    def __init__(self, w, h, scene: QGraphicsScene, num):
        super().__init__()
        self.meci = []
        self.width = w
        self.height = h
        self.myScene = scene
        self.numJMBG = num
        if self.numJMBG == 1:
            self.setPixmap(QtGui.QPixmap('Images/rocketship.png'))  # Player1 = crveni
        elif self.numJMBG == 2:
            self.setPixmap(QtGui.QPixmap('Images/rocketship2.png'))  # Player2 = zuti
        elif self.numJMBG == 3:
            self.setPixmap(QtGui.QPixmap('Images/rocketship3.png'))  # Player3 = plavi
        elif self.numJMBG == 4:
            self.setPixmap(QtGui.QPixmap('Images/rocketship4.png'))  # Player4 = zeleni
        self.moveX = float(0)
        self.moveY = float(1)
        self.xFull = float(270)
        self.yFull = float(200)
        self.angle = 90
        self.move(270, 200)
        # region inizilatioin of signals for rocket1 and rocket2
        self.upRocket1.connect(self.up1_function)
        self.leftRocket1.connect(self.left1_function)
        self.rightRocket1.connect(self.right1_function)
        self.fireRocket1.connect(self.fire1_function)
        self.upRocket2.connect(self.up2_function)
        self.leftRocket2.connect(self.left2_function)
        self.rightRocket2.connect(self.right2_function)
        self.fireRocket2.connect(self.fire2_function)
        self.upRocket3.connect(self.up3_function)
        self.leftRocket3.connect(self.left3_function)
        self.rightRocket3.connect(self.right3_function)
        self.fireRocket3.connect(self.fire3_function)
        self.upRocket4.connect(self.up4_function)
        self.leftRocket4.connect(self.left4_function)
        self.rightRocket4.connect(self.right4_function)
        self.fireRocket4.connect(self.fire4_function)
        # endregion
        self.timer = QBasicTimer()
        self.timer.start(30, self)

    def setRocketImage(self, param):
        self.setPixmap(QtGui.QPixmap(param))

    def positionsExpand(self):
        current_x_coords = int(round(self.x()))
        current_y_coords = int(round(self.y()))
        if self.numJMBG == 1:
            Server.coordinatesOfRocket1X.clear()
            Server.coordinatesOfRocket1Y.clear()
            # region ->logika da se raketa gleda kao 20x20 px po x i y koordinati
            tmp = 0
            for tmpX1 in range(40):
                tmp = tmpX1 + current_x_coords
                Server.coordinatesOfRocket1X.append(tmp)
                tmpX1 = tmpX1 + 1
            tmp = 0
            for tmpY1 in range(40):
                tmp = tmpY1 + current_y_coords
                Server.coordinatesOfRocket1Y.append(tmp)
                tmpY1 = tmpY1 + 1
            tmp = 0
            # end region
        elif self.numJMBG == 2:
            # self.setPixmap(QtGui.QPixmap('Images/rocketship2.png'))
            Server.coordinatesOfRocket2X.clear()
            Server.coordinatesOfRocket2Y.clear()
            # region ->logika da se raketa gleda kao 20x20 px po x i y koordinati
            tmp = 0
            for tmpX1 in range(40):
                tmp = tmpX1 + current_x_coords
                Server.coordinatesOfRocket2X.append(tmp)
                tmpX1 = tmpX1 + 1
            tmp = 0
            for tmpY1 in range(40):
                tmp = tmpY1 + current_y_coords
                Server.coordinatesOfRocket2Y.append(tmp)
                tmpY1 = tmpY1 + 1
            tmp = 0
        elif self.numJMBG == 3:
            # self.setPixmap(QtGui.QPixmap('Images/rocketship2.png'))
            Server.coordinatesOfRocket3X.clear()
            Server.coordinatesOfRocket3Y.clear()
            # region ->logika da se raketa gleda kao 20x20 px po x i y koordinati
            tmp = 0
            for tmpX1 in range(40):
                tmp = tmpX1 + current_x_coords
                Server.coordinatesOfRocket3X.append(tmp)
                tmpX1 = tmpX1 + 1
            tmp = 0
            for tmpY1 in range(40):
                tmp = tmpY1 + current_y_coords
                Server.coordinatesOfRocket3Y.append(tmp)
                tmpY1 = tmpY1 + 1
            tmp = 0
        elif self.numJMBG == 4:
            # self.setPixmap(QtGui.QPixmap('Images/rocketship2.png'))
            Server.coordinatesOfRocket4X.clear()
            Server.coordinatesOfRocket4Y.clear()
            # region ->logika da se raketa gleda kao 20x20 px po x i y koordinati
            tmp = 0
            for tmpX1 in range(40):
                tmp = tmpX1 + current_x_coords
                Server.coordinatesOfRocket4X.append(tmp)
                tmpX1 = tmpX1 + 1
            tmp = 0
            for tmpY1 in range(40):
                tmp = tmpY1 + current_y_coords
                Server.coordinatesOfRocket4Y.append(tmp)
                tmpY1 = tmpY1 + 1
            tmp = 0
            # end region

    def up1_function(self):
        self.positionsExpand()
        self.yFull = float(self.yFull).__sub__(self.moveY * 8 * ((Server.level // 10) + 1))  # puno je da ide *Server.level, mnogo bi ubrzao, a mora * jer samo + radi shift
        self.xFull = float(self.xFull).__add__(self.moveX * 8 * ((Server.level // 10) + 1))
        self.move(self.xFull, self.yFull)
        if (math.floor(self.yFull) <= -20):
            self.yFull = 500
        elif (math.floor(self.yFull) >= 500):
            self.yFull = 0
        elif (math.floor(self.xFull) <= -22):
            self.xFull = 559
        elif (math.floor(self.xFull) >= 560):
            self.xFull = -21.0
        self.update()

    def left1_function(self):
        self.positionsExpand()
        Server.i = (Server.i + 1) % 72
        self.setRocketImage(rocketsList[Server.i])  # ako nije turnir ovaj je uvek crveni
        self.angle = self.angle + 5
        self.moveX = cos(radians(self.angle))
        self.moveY = sin(radians(self.angle))
        self.update()

    def right1_function(self):
        self.positionsExpand()
        self.angle = self.angle - 5
        Server.i = (Server.i - 1) % 72
        self.setRocketImage(rocketsList[Server.i])  # ako nije turnir ovaj je uvek crveni
        self.moveX = cos(radians(self.angle))
        self.moveY = sin(radians(self.angle))
        self.update()

    def fire1_function(self):
        self.positionsExpand()
        metak = NetworkBullet(self.x(), self.y(), self.angle, Server.i, self.myScene, 1)  # last parameter is rocket id
        self.meci.append(metak)
        self.update()

    def up2_function(self):
        self.yFull = float(self.yFull).__sub__(self.moveY * 8 * ((Server.level // 10) + 1))
        self.xFull = float(self.xFull).__add__(self.moveX * 8 * ((Server.level // 10) + 1))
        self.move(self.xFull, self.yFull)
        if (math.floor(self.yFull) <= -20):
            self.yFull = 500
        elif (math.floor(self.yFull) >= 500):
            self.yFull = 0
        elif (math.floor(self.xFull) <= -22):
            self.xFull = 559
        elif (math.floor(self.xFull) >= 560):
            self.xFull = -21.0
        self.update()

    def left2_function(self):
        self.positionsExpand()
        Server.i2 = (Server.i2 + 1) % 72
        self.setRocketImage(rocketsList1[Server.i2])  # ako nije turnir ovaj je uvek zuti
        self.angle = self.angle + 5
        self.moveX = cos(radians(self.angle))
        self.moveY = sin(radians(self.angle))
        self.update()

    def right2_function(self):
        self.positionsExpand()
        Server.i2 = (Server.i2 - 1) % 72
        self.setRocketImage(rocketsList1[Server.i2])  # ako nije turnir ovaj je uvek zuti
        self.angle = self.angle - 5
        self.moveX = cos(radians(self.angle))
        self.moveY = sin(radians(self.angle))
        self.update()

    def fire2_function(self):
        self.positionsExpand()
        metak = NetworkBullet(self.x(), self.y(), self.angle, Server.i2, self.myScene, 2)  # last parameter is rocket id
        self.meci.append(metak)
        self.update()






    def up3_function(self):
        self.yFull = float(self.yFull).__sub__(self.moveY * 8 * ((Server.level // 10) + 1))
        self.xFull = float(self.xFull).__add__(self.moveX * 8 * ((Server.level // 10) + 1))
        self.move(self.xFull, self.yFull)
        if (math.floor(self.yFull) <= -20):
            self.yFull = 500
        elif (math.floor(self.yFull) >= 500):
            self.yFull = 0
        elif (math.floor(self.xFull) <= -22):
            self.xFull = 559
        elif (math.floor(self.xFull) >= 560):
            self.xFull = -21.0
        self.update()

    def left3_function(self):
        self.positionsExpand()
        Server.i3 = (Server.i3 + 1) % 72
        self.setRocketImage(rocketsList2[Server.i3])  # ako nije turnir ovaj je uvek zuti
        self.angle = self.angle + 5
        self.moveX = cos(radians(self.angle))
        self.moveY = sin(radians(self.angle))
        self.update()

    def right3_function(self):
        self.positionsExpand()
        Server.i3 = (Server.i3 - 1) % 72
        self.setRocketImage(rocketsList2[Server.i3])  # ako nije turnir ovaj je uvek zuti
        self.angle = self.angle - 5
        self.moveX = cos(radians(self.angle))
        self.moveY = sin(radians(self.angle))
        self.update()

    def fire3_function(self):
        self.positionsExpand()
        metak = NetworkBullet(self.x(), self.y(), self.angle, Server.i3, self.myScene, 3)  # last parameter is rocket id
        self.meci.append(metak)
        self.update()



    def up4_function(self):
        self.yFull = float(self.yFull).__sub__(self.moveY * 8 * ((Server.level // 10) + 1))
        self.xFull = float(self.xFull).__add__(self.moveX * 8 * ((Server.level // 10) + 1))
        self.move(self.xFull, self.yFull)
        if (math.floor(self.yFull) <= -20):
            self.yFull = 500
        elif (math.floor(self.yFull) >= 500):
            self.yFull = 0
        elif (math.floor(self.xFull) <= -22):
            self.xFull = 559
        elif (math.floor(self.xFull) >= 560):
            self.xFull = -21.0
        self.update()

    def left4_function(self):
        self.positionsExpand()
        Server.i4 = (Server.i4 + 1) % 72
        self.setRocketImage(rocketsList3[Server.i4])  # ako nije turnir ovaj je uvek zuti
        self.angle = self.angle + 5
        self.moveX = cos(radians(self.angle))
        self.moveY = sin(radians(self.angle))
        self.update()

    def right4_function(self):
        self.positionsExpand()
        Server.i4 = (Server.i4 - 1) % 72
        self.setRocketImage(rocketsList3[Server.i4])  # ako nije turnir ovaj je uvek zuti
        self.angle = self.angle - 5
        self.moveX = cos(radians(self.angle))
        self.moveY = sin(radians(self.angle))
        self.update()

    def fire4_function(self):
        self.positionsExpand()
        metak = NetworkBullet(self.x(), self.y(), self.angle, Server.i4, self.myScene, 4)  # last parameter is rocket id
        self.meci.append(metak)
        self.update()


    def timerEvent(self, a0: 'QTimerEvent'):
        if len(self.meci) > 0:
            for metak in self.meci:
                metak.kreni.emit()
