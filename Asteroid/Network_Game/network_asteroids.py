from PyQt5.QtWidgets import QMainWindow, QDesktopWidget, QGraphicsTransform, QShortcut
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtCore import pyqtSignal, QBasicTimer, QRectF, QPoint, QTimerEvent, Qt
from PyQt5.QtWidgets import QLabel, QApplication, QGridLayout, QWidget, QVBoxLayout, QGraphicsView, QGraphicsScene
from PyQt5.QtGui import QPixmap, QTransform, QKeySequence
from math import cos, sin, radians
import  math
import random
import Server
from game_over_scene import *
i = 1
ast_0 = 0
tmp = []
levelOfAsteroid = 2
isDestroyedThisObj1 = 0
tmpss = 0


class NetworkAsteroid(QLabel):
    def __init__(self, w, h, scene: QGraphicsScene, uniqueIdenfier, isTour, asteroid_size, positionCounter):
        super().__init__()
        global i
        global tmpss
        self.size = 3
        self.am_i_alive = 0
        self.width = w
        self.height = h
        self.myScene = scene
        self.is_tournament = isTour
        self.uniqueIdenfier = uniqueIdenfier
        self.level_of_current_asterid = asteroid_size
        self.moveX = float(0)
        self.moveY = float(1)
        self.xFull = float(1 + positionCounter*12)#pocetne koordinate asteroida
        self.yFull = float(1 + positionCounter*12)#pocetne koordinate asteroida
        tmpss = tmpss + 20
        self.angle = 90
        self.timer = QBasicTimer()
        self.timer.start(60, self)

    def setImage(self, param):
        self.setPixmap(QtGui.QPixmap(param))

    def setAssteroidSize(self, fullPath):
        global levelOfAsteroid
        bigImage = QPixmap(fullPath)
        if self.level_of_current_asterid == 3:
            cropedImage = bigImage.scaled(60, 60, Qt.IgnoreAspectRatio, Qt.FastTransformation)
        elif self.level_of_current_asterid == 2:
            cropedImage = bigImage.scaled(45, 45, Qt.IgnoreAspectRatio, Qt.FastTransformation)
        else:
            cropedImage = bigImage.scaled(30, 30, Qt.IgnoreAspectRatio, Qt.FastTransformation)
        return cropedImage


    def whileTrue(self):
        global i
        #global ast_0
        global tmp
        global coordinatesOfRocketsss
        global levelOfAsteroid
        global isDestroyedThisObj1
        if Server.activeAsteroids[self.uniqueIdenfier] == 0:
            #ast_0 += 1
            #ast_0 = ast_0 % 4
            startPath = "Images/AsteroidsImg/large/c100"
            endPath = ".png"
            i = (i + 1) % 16
            if i < 10:
                fullPath = (startPath + '0' + str(i) + endPath)
            else:
                fullPath = (startPath + str(i) + endPath)

            cropedImage = self.setAssteroidSize(fullPath)
            self.setImage(cropedImage)
            #if (ast_0 % 2 == 0):
            #    self.angle = self.angle - ast_0
            #else:
            #    self.angle = self.angle + ast_0

            self.moveX = cos(radians(self.angle))
            self.moveY = sin(radians(self.angle))
            if self.level_of_current_asterid == 3:
                self.yFull = float(self.yFull).__sub__(self.moveY * Server.level + 1)#moze i (self.moveY * ((Server.level // 10) + 1) jer ovako trenutno dosta brze ubrzava
                self.xFull = float(self.xFull).__add__(self.moveX * Server.level + 1)
            elif self.level_of_current_asterid == 2:
                self.yFull = float(self.yFull).__sub__(self.moveY * Server.level + 2)
                self.xFull = float(self.xFull).__add__(self.moveX * Server.level + 2)
            elif self.level_of_current_asterid == 1:
                self.yFull = float(self.yFull).__sub__(self.moveY * Server.level + 3)
                self.xFull = float(self.xFull).__add__(self.moveX * Server.level + 3)
            self.move(self.xFull, self.yFull)

            #region unistavanje asteroida
            inttX = int(round(self.xFull))
            inttY = int(round(self.yFull))

            ccc = 0
            vvv = 0
            tmpss = 0
            thisAsteroidXCoords = []
            thisAsteroidYCoords = []

            thisAsteroidXCoords.clear()
            thisAsteroidYCoords.clear()
            for ccc in range(40):
                tmpss = inttX + ccc
                thisAsteroidXCoords.append(tmpss)
                ccc = ccc + 1
            for vvv in range(40):
                tmpss2 = inttY + vvv
                thisAsteroidYCoords.append(tmpss2)
                vvv = vvv + 1
            vvv = 0

            if (any(checkXCords in thisAsteroidXCoords for checkXCords in Server.coordinatesOfRocket1X) and any(
                    checkYCords in thisAsteroidYCoords for checkYCords in Server.coordinatesOfRocket1Y)):#provera za raketu1 da li je udarena
                if self.is_tournament == False:
                    Server.player1Lives = Server.player1Lives - 1
                    Server.activeAsteroids[self.uniqueIdenfier] = 1
                    self.hide()
                    print("ASTEROID IS DESTROYED TOO!!!")
                    if self.level_of_current_asterid == 3:
                        self.myScene.createMediumAsteroids()
                        self.level_of_current_asterid = 2
                    elif self.level_of_current_asterid == 2:
                        self.myScene.createSmallAsteroids()
                        self.level_of_current_asterid = 1


                    self.myScene.label11.setText("Player1 lives--->[" + Server.player1Lives.__str__() + "] score--->[" + Server.player1Score.__str__() + "]")
                    self.check_for_level_up()
                if Server.player1Lives == 0:  # ako je izgubio sve zivote da iskoci iz igrce
                    player_id = 1
                    self.myScene.game_is_over(player_id)

            if (any(checkXCords in thisAsteroidXCoords for checkXCords in Server.coordinatesOfRocket2X) and any(
                    checkYCords in thisAsteroidYCoords for checkYCords in Server.coordinatesOfRocket2Y)):#provera za raketu2 da li je udarena
                if self.is_tournament == False:
                    Server.player2Lives = Server.player2Lives - 1
                    Server.activeAsteroids[self.uniqueIdenfier] = 1
                    self.hide()
                    print("ASTEROID IS DESTROYED TOO!!!")
                    if self.level_of_current_asterid == 3:
                        self.myScene.createMediumAsteroids()
                        self.level_of_current_asterid = 2
                    elif self.level_of_current_asterid == 2:
                        self.myScene.createSmallAsteroids()
                        self.level_of_current_asterid = 1




                    self.myScene.label22.setText(
                        "Player2 lives--->[" + Server.player2Lives.__str__() + "] score--->[" + Server.player2Score.__str__() + "]")
                    self.check_for_level_up()
                if Server.player2Lives == 0:  # ako je izgubio sve zivote da iskoci iz igrce
                    player_id = 2
                    self.myScene.game_is_over(player_id)
              #  self.check_for_level_up()

            if (any(checkXCords in thisAsteroidXCoords for checkXCords in Server.coordinatesOfRocket3X) and any(
                    checkYCords in thisAsteroidYCoords for checkYCords in Server.coordinatesOfRocket3Y)):#provera za raketu2 da li je udarena
                if self.is_tournament == False:
                    Server.player3Lives = Server.player3Lives - 1
                    Server.activeAsteroids[self.uniqueIdenfier] = 1
                    self.hide()
                    print("ASTEROID IS DESTROYED TOO!!!")
                    if self.level_of_current_asterid == 3:
                        self.myScene.createMediumAsteroids()
                        self.level_of_current_asterid = 2
                    elif self.level_of_current_asterid == 2:
                        self.myScene.createSmallAsteroids()
                        self.level_of_current_asterid = 1

                    self.myScene.label33.setText(
                        "Player3 lives--->[" + Server.player3Lives.__str__() + "] score--->[" + Server.player3Score.__str__() + "]")
                    self.check_for_level_up()
                if Server.player3Lives == 0:  # ako je izgubio sve zivote da iskoci iz igrce
                    player_id = 3
                    self.myScene.game_is_over(player_id)


            if (any(checkXCords in thisAsteroidXCoords for checkXCords in Server.coordinatesOfRocket4X) and any(
                    checkYCords in thisAsteroidYCoords for checkYCords in Server.coordinatesOfRocket4Y)):#provera za raketu2 da li je udarena
                if self.is_tournament == False:
                    Server.player4Lives = Server.player4Lives - 1
                    Server.activeAsteroids[self.uniqueIdenfier] = 1
                    self.hide()
                    print("ASTEROID IS DESTROYED TOO!!!")
                    if self.level_of_current_asterid == 3:
                        self.myScene.createMediumAsteroids()
                        self.level_of_current_asterid = 2
                    elif self.level_of_current_asterid == 2:
                        self.myScene.createSmallAsteroids()
                        self.level_of_current_asterid = 1

                    self.myScene.label44.setText(
                        "Player4 lives--->[" + Server.player4Lives.__str__() + "] score--->[" + Server.player4Score.__str__() + "]")
                    self.check_for_level_up()
                if Server.player4Lives == 0:  # ako je izgubio sve zivote da iskoci iz igrce
                    player_id = 4
                    self.myScene.game_is_over(player_id)

            expandBulletX = []
            expandBulletY = []
            params3 = False
            for key, value in Server.bulletsCollection1X.items():#provera da li je asteroid udario u metak od rakete1
                if params3 == True:
                    break
                expandBulletX.clear()
                for xb in range(3):
                    expandBulletX.append(value + xb)
                if any(cx in expandBulletX for cx in thisAsteroidXCoords):
                    for key2, val2 in Server.bulletsCollection1Y.items():
                        expandBulletY.clear()
                        for yb in range(3):
                            expandBulletY.append(val2 + yb)
                        if any(cy in expandBulletY for cy in thisAsteroidYCoords) and key == key2:
                            asteroid_size_for_points = self.level_of_current_asterid
                            if self.level_of_current_asterid == 3:
                                self.myScene.createMediumAsteroids()
                                self.level_of_current_asterid = 2
                            elif self.level_of_current_asterid == 2:
                                self.myScene.createSmallAsteroids()
                                self.level_of_current_asterid = 1

                            self.check_for_level_up()
                            if Server.currentRound == 0:
                                Server.activeAsteroids[self.uniqueIdenfier] = 1
                                Server.player1Score += 300
                                self.myScene.label11.setText(
                                    "Player1 lives--->[" + Server.player1Lives.__str__() + "] score--->[" + Server.player1Score.__str__() + "]")
                                self.hide()
                                self.yFull = 1234
                                self.xFull = 1234
                                params3 = True
                                break

            expandBulletY.clear()
            expandBulletX.clear()
            for key, value in Server.bulletsCollection2X.items():#provera da li je asteroid udario u metak od rakete2
                if params3 == True:
                    break
                expandBulletX.clear()
                expandBulletX.append(value)
                if any(cx in expandBulletX for cx in thisAsteroidXCoords):
                    for key2, val2 in Server.bulletsCollection2Y.items():
                        expandBulletY.clear()
                        expandBulletY.append(val2)
                        if any(cy in expandBulletY for cy in thisAsteroidYCoords) and key == key2:
                            asteroid_size_for_points = self.level_of_current_asterid
                            if self.level_of_current_asterid == 3:
                                self.myScene.createMediumAsteroids()
                                self.level_of_current_asterid = 2
                            elif self.level_of_current_asterid == 2:
                                self.myScene.createSmallAsteroids()
                                self.level_of_current_asterid = 1

                            self.check_for_level_up()
                            if Server.currentRound == 0:
                                Server.activeAsteroids[self.uniqueIdenfier] = 1
                                Server.player2Score += 300
                                self.myScene.label22.setText(
                                    "Player2 lives--->[" + Server.player2Lives.__str__() + "] score--->[" + Server.player2Score.__str__() + "]")
                                self.hide()
                                self.yFull = 1234
                                self.xFull = 1234
                                params3 = True
                                break


            expandBulletY.clear()
            expandBulletX.clear()

            for key, value in Server.bulletsCollection3X.items():#provera da li je asteroid udario u metak od rakete2
                if params3 == True:
                    break
                expandBulletX.clear()
                expandBulletX.append(value)
                if any(cx in expandBulletX for cx in thisAsteroidXCoords):
                    for key2, val2 in Server.bulletsCollection3Y.items():
                        expandBulletY.clear()
                        expandBulletY.append(val2)
                        if any(cy in expandBulletY for cy in thisAsteroidYCoords) and key == key2:
                            asteroid_size_for_points = self.level_of_current_asterid
                            if self.level_of_current_asterid == 3:
                                self.myScene.createMediumAsteroids()
                                self.level_of_current_asterid = 2
                            elif self.level_of_current_asterid == 2:
                                self.myScene.createSmallAsteroids()
                                self.level_of_current_asterid = 1

                            self.check_for_level_up()
                            if Server.currentRound == 0:
                                Server.activeAsteroids[self.uniqueIdenfier] = 1
                                Server.player3Score += 300
                                self.myScene.label33.setText(
                                    "Player3 lives--->[" + Server.player3Lives.__str__() + "] score--->[" + Server.player3Score.__str__() + "]")
                                self.hide()
                                self.yFull = 1234
                                self.xFull = 1234
                                params3 = True
                                break


            expandBulletY.clear()
            expandBulletX.clear()

            for key, value in Server.bulletsCollection4X.items():#provera da li je asteroid udario u metak od rakete2
                if params3 == True:
                    break
                expandBulletX.clear()
                expandBulletX.append(value)
                if any(cx in expandBulletX for cx in thisAsteroidXCoords):
                    for key2, val2 in Server.bulletsCollection4Y.items():
                        expandBulletY.clear()
                        expandBulletY.append(val2)
                        if any(cy in expandBulletY for cy in thisAsteroidYCoords) and key == key2:
                            asteroid_size_for_points = self.level_of_current_asterid
                            if self.level_of_current_asterid == 3:
                                self.myScene.createMediumAsteroids()
                                self.level_of_current_asterid = 2
                            elif self.level_of_current_asterid == 2:
                                self.myScene.createSmallAsteroids()
                                self.level_of_current_asterid = 1

                            self.check_for_level_up()
                            if Server.currentRound == 0:
                                Server.activeAsteroids[self.uniqueIdenfier] = 1
                                Server.player4Score += 300
                                self.myScene.label44.setText(
                                    "Player4 lives--->[" + Server.player4Lives.__str__() + "] score--->[" + Server.player4Score.__str__() + "]")
                                self.hide()
                                self.yFull = 1234
                                self.xFull = 1234
                                params3 = True
                                break


            expandBulletY.clear()
            expandBulletX.clear()

            if (math.floor(self.yFull) <= -10):
                self.yFull = 500
            elif (math.floor(self.yFull) >= 500):
                self.yFull = 0
            elif (math.floor(self.xFull) <= -22):
                self.xFull = 559
            elif (math.floor(self.xFull) >= 600):
                self.xFull = -21.0
        else:
            self.yFull = 1234
            self.xFull = 1234

    def timerEvent(self, a0: 'QTimerEvent'):
        self.whileTrue()


    def check_for_level_up(self):
        Server.num_of_active_asteroids = Server.num_of_active_asteroids - 1
        print("Perica merica")
        if Server.num_of_active_asteroids == 0:
            Server.bar_jedan_je_ziv_asteroid = False

        if Server.bar_jedan_je_ziv_asteroid == True:
            print("Jos je bar jedan ziv asteroid")
        elif Server.bar_jedan_je_ziv_asteroid == False:
            print("Svi asteroidi su mrtvi")
            Server.level = Server.level + 1
            Server.bar_jedan_je_ziv_asteroid = True
            Server.num_of_active_asteroids = 7 * Server.level
            #self.bonus_1000_points_for_lvl_pass()
            self.myScene.labelLevel.setText("Level : " + Server.level.__str__())
            self.myScene.createAsteroids()

