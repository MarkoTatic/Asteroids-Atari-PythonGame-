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


class Asteroid(QLabel):
    def __init__(self, w, h, scene: QGraphicsScene, uniqueIdenfier, isTour, asteroid_size):
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
        self.xFull = float(float(random.randrange(0, 500)))#pocetne koordinate asteroida
        self.yFull = float(float(random.randrange(0, 450)))#pocetne koordinate asteroida
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
        global ast_0
        global tmp
        global coordinatesOfRocketsss
        global levelOfAsteroid
        global isDestroyedThisObj1
        if Server.activeAsteroids[self.uniqueIdenfier] == 0:
            ast_0 += 1
            # if(numberObj == 3):
            # numberObj = 0
            ast_0 = ast_0 % 4
            #        print(ast_0)
            startPath = "Images/AsteroidsImg/large/c100"
            endPath = ".png"
            # if(numberObj % 2 == 0):
            #     i = (i - 1) % 16
            # else:
            i = (i + 1) % 16
            if i < 10:
                fullPath = (startPath + '0' + str(i) + endPath)
            else:
                fullPath = (startPath + str(i) + endPath)

            cropedImage = self.setAssteroidSize(fullPath)
            self.setImage(cropedImage)
            if (ast_0 % 2 == 0):
                self.angle = self.angle - ast_0
            else:
                self.angle = self.angle + ast_0

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
                    self.myScene.label2.setText(
                        "Player1 lives--->[" + Server.player1Lives.__str__() + "] score--->[" + Server.player1Score.__str__() + "]")
                    Server.activeAsteroids[self.uniqueIdenfier] = 1
                    self.hide()

                    if self.level_of_current_asterid == 3:
                        self.myScene.createMediumAsteroids()
                        self.level_of_current_asterid = 2
                    elif self.level_of_current_asterid == 2:
                        self.myScene.createSmallAsteroids()
                        self.level_of_current_asterid = 1
                    print("ASTEROID IS DESTROYED TOO!!!")
                    if Server.player1Lives == 0:  # ako je izgubio sve zivote da iskoci iz igrce
                        player_id = 1
                        self.myScene.game_is_over(player_id)
                else:
                    if self.level_of_current_asterid == 3:
                        self.myScene.createMediumAsteroids()
                        self.level_of_current_asterid = 2
                    elif self.level_of_current_asterid == 2:
                        self.myScene.createSmallAsteroids()
                        self.level_of_current_asterid = 1
                    if Server.currentRound == 0:
                        Server.player1Lives = Server.player1Lives - 1
                        self.myScene.label2.setText("Player1 lives--->[" + Server.player1Lives.__str__() + "] score--->[" + Server.player1Score.__str__() + "]")
                        Server.activeAsteroids[self.uniqueIdenfier] = 1
                        self.hide()
                    elif Server.currentRound == 1:
                        Server.player3Lives = Server.player3Lives - 1
                        self.myScene.label6.setText("Player3 lives--->[" + Server.player3Lives.__str__() + "] score--->[" + Server.player3Score.__str__() + "]")
                        Server.activeAsteroids[self.uniqueIdenfier] = 1
                        self.hide()
                    elif Server.currentRound == 2 and Server.Win0 == 1:
                        Server.player5Lives = Server.player5Lives - 1
                        self.myScene.label2.setText(
                            "Player1 lives--->[" + Server.player5Lives.__str__() + "] score--->[" + Server.player5Score.__str__() + "]")
                        self.myScene.label2.setStyleSheet(
                            "font: 9pt; color: #f03a54; font:bold; background-color: transparent; ")
                        Server.activeAsteroids[self.uniqueIdenfier] = 1
                        self.hide()
                    elif Server.currentRound == 2 and Server.Win0 == 2:
                        Server.player5Lives = Server.player5Lives - 1
                        self.myScene.label2.setText("Player2 lives--->[" + Server.player5Lives.__str__() + "] score--->[" + Server.player5Score.__str__() + "]")
                        self.myScene.label2.setStyleSheet(
                            "font: 9pt; color: yellow; font:bold; background-color: transparent; ")
                        Server.activeAsteroids[self.uniqueIdenfier] = 1
                        self.hide()
                    print("ASTEROID IS DESTROYED TOO!!!")
                    if (Server.player1Lives == 0 and Server.currentRound == 0):#ako je izgubio sve zivote da iskoci iz igrce
                        player_id = 10#rocket1
                        print("1111111111ARISMAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA")
                        Server.Died = 1
                        self.tounamentCheck()
                        self.myScene.game_is_over(player_id)
                    elif (Server.player5Lives == 0 and Server.currentRound == 2 and Server.Win0 == 1):
                        player_id = 12#rocket5
                        self.tounamentCheck()
                        self.myScene.game_is_over(player_id)
                    elif (Server.player3Lives == 0 and Server.currentRound == 1):
                        player_id = 31#rocket3
                        Server.Died2 = 3
                        self.tounamentCheck()
                        self.myScene.game_is_over(player_id)
                    elif (Server.player5Lives == 0 and Server.currentRound == 2 and Server.Win0 == 2):
                        player_id = 32#rocket5
                        self.tounamentCheck()
                        self.myScene.game_is_over(player_id)

                self.check_for_level_up()

            if (any(checkXCords in thisAsteroidXCoords for checkXCords in Server.coordinatesOfRocket2X) and any(
                    checkYCords in thisAsteroidYCoords for checkYCords in Server.coordinatesOfRocket2Y)):#provera za raketu2 da li je udarena
                # provera obuhvata turnir i multiplayer jer ce currentRound uvek inicjalno biti 0
                if self.is_tournament == False:
                    Server.player2Lives = Server.player2Lives - 1
                    self.myScene.label3.setText(
                        "Player2 lives--->[" + Server.player2Lives.__str__() + "] score--->[" + Server.player2Score.__str__() + "]")
                    Server.activeAsteroids[self.uniqueIdenfier] = 1
                    self.hide()
                    if self.level_of_current_asterid == 3:
                        self.myScene.createMediumAsteroids()
                        self.level_of_current_asterid = 2
                    elif self.level_of_current_asterid == 2:
                        self.myScene.createSmallAsteroids()
                        self.level_of_current_asterid = 1
                    print("ASTEROID IS DESTROYED TOO!!!")
                    if Server.player2Lives == 0:  # ako je izgubio sve zivote da iskoci iz igrce
                        player_id = 2
                        self.myScene.game_is_over(player_id)
                else:
                    if self.level_of_current_asterid == 3:
                        self.myScene.createMediumAsteroids()
                        self.level_of_current_asterid = 2
                    elif self.level_of_current_asterid == 2:
                        self.myScene.createSmallAsteroids()
                        self.level_of_current_asterid = 1
                    if Server.currentRound == 0:
                        Server.player2Lives = Server.player2Lives - 1
                        self.myScene.label3.setText("Player2 lives--->[" + Server.player2Lives.__str__() + "] score--->[" + Server.player2Score.__str__() + "]")
                        Server.activeAsteroids[self.uniqueIdenfier] = 1
                        self.hide()
                    elif Server.currentRound == 1:
                        Server.player4Lives = Server.player4Lives - 1
                        self.myScene.label7.setText(
                            "Player4 lives--->[" + Server.player4Lives.__str__() + "] score--->[" + Server.player4Score.__str__() + "]")
                        Server.activeAsteroids[self.uniqueIdenfier] = 1
                        self.hide()
                    elif Server.currentRound == 2 and Server.Win1 == 3:
                        Server.player6Lives = Server.player6Lives - 1
                        self.myScene.label6.setText("Player3 lives--->[" + Server.player6Lives.__str__() + "] score--->[" + Server.player6Score.__str__() + "]")
                        self.myScene.label6.setStyleSheet(
                            "font: 9pt; color: blue; font:bold; background-color: transparent; ")
                        Server.activeAsteroids[self.uniqueIdenfier] = 1
                        self.hide()
                    elif Server.currentRound == 2 and Server.Win1 == 4:
                        Server.player6Lives = Server.player6Lives - 1
                        self.myScene.label6.setText(
                            "Player4 lives--->[" + Server.player6Lives.__str__() + "] score--->[" + Server.player6Score.__str__() + "]")
                        self.myScene.label6.setStyleSheet(
                            "font: 9pt; color: green; font:bold; background-color: transparent; ")
                        Server.activeAsteroids[self.uniqueIdenfier] = 1
                        self.hide()
                    print("ASTEROID IS DESTROYED TOO!!!")
                    if (Server.player2Lives == 0 and Server.currentRound == 0):#ako je izgubio sve zivote da iskoci iz igrce
                        player_id = 20#rocket2
                        Server.Died = 2
                        self.tounamentCheck()
                        self.myScene.game_is_over(player_id)
                    elif (Server.player6Lives == 0 and Server.currentRound == 2 and Server.Win1 == 3):
                        player_id = 22#rocket6
                        self.tounamentCheck()
                        self.myScene.game_is_over(player_id)
                    elif (Server.player4Lives == 0 and Server.currentRound == 1):
                        player_id = 41#rocket4
                        Server.Died2 = 4
                        self.tounamentCheck()
                        self.myScene.game_is_over(player_id)
                    elif (Server.player6Lives == 0 and Server.currentRound == 2 and Server.Win1 == 4):
                        player_id = 42#rocket6
                        self.tounamentCheck()
                        self.myScene.game_is_over(player_id)

                self.check_for_level_up()

            #endRegion

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
                            if Server.currentRound == 0:
                                Server.activeAsteroids[self.uniqueIdenfier] = 1
                                if asteroid_size_for_points == 3:
                                    Server.player1Score = Server.player1Score + 100
                                elif asteroid_size_for_points == 2:
                                    Server.player1Score = Server.player1Score + 150
                                elif asteroid_size_for_points == 1:
                                    Server.player1Score = Server.player1Score + 200
                                self.myScene.label2.setText("Player1 lives--->[" + Server.player1Lives.__str__() + "] score--->[" + Server.player1Score.__str__() + "]")
                                self.hide()
                                self.yFull = 1234
                                self.xFull = 1234
                                self.check_for_level_up()
                                params3 = True
                                break
                            elif Server.currentRound == 1:
                                Server.activeAsteroids[self.uniqueIdenfier] = 1
                                if asteroid_size_for_points == 3:
                                    Server.player3Score = Server.player3Score + 100
                                elif asteroid_size_for_points == 2:
                                    Server.player3Score = Server.player3Score + 150
                                elif asteroid_size_for_points == 1:
                                    Server.player3Score = Server.player3Score + 200

                                self.myScene.label6.setText("Player3 lives--->[" + Server.player3Lives.__str__() + "] score--->[" + Server.player3Score.__str__() + "]")
                                self.hide()
                                self.yFull = 1234
                                self.xFull = 1234
                                self.check_for_level_up()
                                params3 = True
                                break
                            elif Server.currentRound == 2 and Server.Win0 == 1:
                                Server.activeAsteroids[self.uniqueIdenfier] = 1
                                if asteroid_size_for_points == 3:
                                    Server.player5Score = Server.player5Score + 100
                                elif asteroid_size_for_points == 2:
                                    Server.player5Score = Server.player5Score + 150
                                elif asteroid_size_for_points == 1:
                                    Server.player5Score = Server.player5Score + 200

                                print("wino1")
                                print(Server.player5Score)
                                self.myScene.label2.setText("Player1 lives--->[" + Server.player5Lives.__str__() + "] score--->[" + Server.player5Score.__str__() + "]")
                                self.myScene.label2.setStyleSheet(
                                    "font: 9pt; color: #f03a54; font:bold; background-color: transparent; ")
                                self.hide()
                                self.yFull = 1234
                                self.xFull = 1234
                                self.check_for_level_up()
                                params3 = True
                                break
                            elif Server.currentRound == 2 and Server.Win0 == 2:
                                Server.activeAsteroids[self.uniqueIdenfier] = 1
                                if asteroid_size_for_points == 3:
                                    Server.player5Score = Server.player5Score + 100
                                elif asteroid_size_for_points == 2:
                                    Server.player5Score = Server.player5Score + 150
                                elif asteroid_size_for_points == 1:
                                    Server.player5Score = Server.player5Score + 200

                                print("wino 2")
                                print(Server.player5Score)
                                self.myScene.label2.setText("Player2 lives--->[" + Server.player5Lives.__str__() + "] score--->[" + Server.player5Score.__str__() + "]")
                                self.myScene.label2.setStyleSheet(
                                    "font: 9pt; color: yellow; font:bold; background-color: transparent; ")
                                self.hide()
                                self.yFull = 1234
                                self.xFull = 1234
                                self.check_for_level_up()
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
                            if Server.currentRound == 0:
                                Server.activeAsteroids[self.uniqueIdenfier] = 1
                                if asteroid_size_for_points == 3:
                                    Server.player2Score = Server.player2Score + 100
                                elif asteroid_size_for_points == 2:
                                    Server.player2Score = Server.player2Score + 150
                                elif asteroid_size_for_points == 1:
                                    Server.player2Score = Server.player2Score + 200

                                self.myScene.label3.setText("Player2 lives--->[" + Server.player2Lives.__str__() + "] score--->[" + Server.player2Score.__str__() + "]")
                                self.hide()
                                self.yFull = 1234
                                self.xFull = 1234
                                self.check_for_level_up()
                                params3 = True
                                break
                            elif Server.currentRound == 1:
                                Server.activeAsteroids[self.uniqueIdenfier] = 1
                                if asteroid_size_for_points == 3:
                                    Server.player4Score = Server.player4Score + 100
                                elif asteroid_size_for_points == 2:
                                    Server.player4Score = Server.player4Score + 150
                                elif asteroid_size_for_points == 1:
                                    Server.player4Score = Server.player4Score + 200

                                self.myScene.label7.setText("Player4 lives--->[" + Server.player4Lives.__str__() + "] score--->[" + Server.player4Score.__str__() + "]")
                                self.hide()
                                self.yFull = 1234
                                self.xFull = 1234
                                self.check_for_level_up()
                                params3 = True
                                break
                            elif Server.currentRound == 2 and Server.Win1 == 3:
                                Server.activeAsteroids[self.uniqueIdenfier] = 1
                                if asteroid_size_for_points == 3:
                                    Server.player6Score = Server.player6Score + 100
                                elif asteroid_size_for_points == 2:
                                    Server.player6Score = Server.player6Score + 150
                                elif asteroid_size_for_points == 1:
                                    Server.player6Score = Server.player6Score + 200

                                print("wino 3")
                                print(Server.player6Score)
                                self.myScene.label6.setText("Player3 lives--->[" + Server.player6Lives.__str__() + "] score--->[" + Server.player6Score.__str__() + "]")
                                self.myScene.label6.setStyleSheet(
                                    "font: 9pt; color: blue; font:bold; background-color: transparent; ")
                                self.hide()
                                self.yFull = 1234
                                self.xFull = 1234
                                self.check_for_level_up()
                                params3 = True
                                break
                            elif Server.currentRound == 2 and Server.Win1 == 4:
                                Server.activeAsteroids[self.uniqueIdenfier] = 1
                                if asteroid_size_for_points == 3:
                                    Server.player6Score = Server.player6Score + 100
                                elif asteroid_size_for_points == 2:
                                    Server.player6Score = Server.player6Score + 150
                                elif asteroid_size_for_points == 1:
                                    Server.player6Score = Server.player6Score + 200

                                print("wino 4")
                                print(Server.player6Score)
                                self.myScene.label6.setText("Player4 lives--->[" + Server.player6Lives.__str__() + "] score--->[" + Server.player6Score.__str__() + "]")
                                self.myScene.label6.setStyleSheet(
                                    "font: 9pt; color: green; font:bold; background-color: transparent; ")
                                self.hide()
                                self.yFull = 1234
                                self.xFull = 1234
                                self.check_for_level_up()
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

        #if Server.tournamentActivated == True:
            #self.tounamentCheck()

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
            self.bonus_1000_points_for_lvl_pass()
            self.myScene.label4.setText("Level : " + Server.level.__str__())
            self.myScene.createAsteroids()


    def tounamentCheck(self):
        if self.is_tournament == True:
            if Server.currentRound == 0 and Server.player1Lives == 0 and Server.player2Lives == 0:
                Server.level = 0
                Server.currentRound = 1
                Server.bar_jedan_je_ziv_asteroid = False
                self.myScene.label6.show()
                self.myScene.label7.show()
                self.myScene.setPlayers(self.myScene.label2, self.myScene.label3)
                if self.is_tournament == True:
                    for key, value in Server.activeAsteroids.items():  # sakrij preostale asteroide
                        # do something with value
                        Server.activeAsteroids[key] = 1
                    if len(Server.activeBigAsteroids) != 0:
                        vals = len(Server.activeBigAsteroids).__int__()
                        for valueArray in range(vals):
                            Server.activeBigAsteroids[valueArray].hide()
                            Server.activeBigAsteroids[valueArray].move(1234, 1234)

            elif Server.currentRound == 1 and Server.player3Lives == 0 and Server.player4Lives == 0:
                Server.level = 0
                Server.currentRound = 2
                Server.bar_jedan_je_ziv_asteroid = False
                self.myScene.setPlayers(self.myScene.label6, self.myScene.label7)
                if self.is_tournament == True:
                    for key, value in Server.activeAsteroids.items():  # sakrij preostale asteroide
                        # do something with value
                        Server.activeAsteroids[key] = 1
                    if len(Server.activeBigAsteroids) != 0:
                        vals = len(Server.activeBigAsteroids).__int__()
                        for valueArray in range(vals):
                            Server.activeBigAsteroids[valueArray].hide()
                            Server.activeBigAsteroids[valueArray].move(1234, 1234)

        elif self.is_tournament == False:
            print("Not tour")

    def bonus_1000_points_for_lvl_pass(self):
        if self.is_tournament == False:
            if Server.player1Lives != 0:
                Server.player1Score = Server.player1Score + 1000
                self.myScene.label2.setText("Player1 lives--->[" + Server.player1Lives.__str__() + "] score--->[" + Server.player1Score.__str__() + "]")
            if Server.player2Lives != 0 and Server.is_multiplayer == True:
                Server.player2Score = Server.player2Score + 1000
                self.myScene.label3.setText(
                    "Player2 lives--->[" + Server.player2Lives.__str__() + "] score--->[" + Server.player2Score.__str__() + "]")
        else:
            if Server.currentRound == 0:
                if Server.player1Lives != 0:
                    Server.player1Score = Server.player1Score + 1000
                    self.myScene.label2.setText(
                        "Player1 lives--->[" + Server.player1Lives.__str__() + "] score--->[" + Server.player1Score.__str__() + "]")
                if Server.player2Lives != 0:
                    Server.player2Score = Server.player2Score + 1000
                    self.myScene.label3.setText(
                        "Player2 lives--->[" + Server.player2Lives.__str__() + "] score--->[" + Server.player2Score.__str__() + "]")
            elif Server.currentRound == 1 and Server.level >= 2: # da ne bi automatski povecao
                if Server.player3Lives != 0:
                    Server.player3Score = Server.player3Score + 1000
                    self.myScene.label6.setText(
                        "Player3 lives--->[" + Server.player3Lives.__str__() + "] score--->[" + Server.player3Score.__str__() + "]")
                if Server.player4Lives != 0:
                    Server.player4Score = Server.player4Score + 1000
                    self.myScene.label7.setText(
                        "Player4 lives--->[" + Server.player4Lives.__str__() + "] score--->[" + Server.player4Score.__str__() + "]")
            elif Server.currentRound == 2 and Server.level >= 2:
                if Server.Win0 == 1 and Server.player5Lives != 0:
                    Server.player5Score = Server.player5Score + 1000
                    self.myScene.label2.setText(
                        "Player1 lives--->[" + Server.player5Lives.__str__() + "] score--->[" + Server.player5Score.__str__() + "]")
                elif Server.Win0 == 2 and Server.player5Lives != 0:
                    Server.player5Score = Server.player5Score + 1000
                    self.myScene.label2.setText(
                        "Player2 lives--->[" + Server.player5Lives.__str__() + "] score--->[" + Server.player5Score.__str__() + "]")

                if Server.Win1 == 3 and Server.player6Lives != 0:
                    Server.player6Score = Server.player6Score + 1000
                    self.myScene.label6.setText(
                        "Player3 lives--->[" + Server.player6Lives.__str__() + "] score--->[" + Server.player6Score.__str__() + "]")
                elif Server.Win1 == 4 and Server.player6Lives != 0:
                    Server.player6Score = Server.player6Score + 1000
                    self.myScene.label6.setText(
                        "Player4 lives--->[" + Server.player6Lives.__str__() + "] score--->[" + Server.player6Score.__str__() + "]")