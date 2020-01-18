from SpaceShuttle import *
from Asteroid import *
from bonus import *
from game_over_scene import *
from welcome_scene import *
from main import *
from PyQt5.QtCore import pyqtSignal, QBasicTimer, QRectF, QPoint, QTimerEvent, Qt
import multiprocessing as mp
from threading import Thread
import time
import random
from key_notifier import KeyNotifier


activeMediumAsteroids = []
activeSmallAsteroids = []

class Tournament(QGraphicsScene):
    def __init__(self, parent, width, height):
        super().__init__(parent)
        Server.tournamentActivated = True
        global activeMediumAsteroids
        global activeSmallAsteroids
        self.width = width
        self.height = height
        self.setSceneRect(0, 0, self.width - 2, self.height - 2)
        self.sceneParent = parent
        self.queue = mp.Queue()
        self.firstrelease = False
        self.gameOverScene = None
        self.keyList = []
        self.timer = QBasicTimer()
        self.timer.start(2000, self)


        self.key_notifier = KeyNotifier()
        self.key_notifier.key_signal.connect(self.__update_position__)
        self.key_notifier.start()

        self.label = QLabel()
        self.pixmap = QPixmap('Images/img2.png')
        self.label.setPixmap(self.pixmap)
        self.label.resize(600, 500)
        self.addWidget(self.label)

        # self.bonus = None

        self.rocketnumber1 = SpaceShuttle(self.width, self.height, self, 1)
        self.rocketnumber1.resize(60,
                                  50)  # slika je 50x50 ali se glupo okrece tako da je bolje ovako da bi se uvek videla cela
        self.rocketnumber1.setStyleSheet("background:transparent")


        self.rocketnumber2 = SpaceShuttle(self.width, self.height, self, 2)
        self.rocketnumber2.resize(60,
                                  50)  # slika je 50x50 ali se glupo okrece tako da je bolje ovako da bi se uvek videla cela
        self.rocketnumber2.setStyleSheet("background:transparent")





        self.queue.put('go')
        self.createAsteroids()


        print("DONE")

        self.label2 = QLabel(
            "Player1 lives--->[" + Server.player1Lives.__str__() + "] score--->[" + Server.player1Score.__str__() + "]")
        self.label2.resize(400, 30)
        self.label2.move(5, 440)
        self.label2.setStyleSheet("font: 9pt; color: #f03a54; font:bold; background-color: transparent; ")
        self.addWidget(self.label2)

        self.label3 = QLabel(
            "Player2 lives--->[" + Server.player2Lives.__str__() + "] score--->[" + Server.player2Score.__str__() + "]")
        self.label3.resize(400, 30)
        self.label3.move(5, 470)
        self.label3.setStyleSheet("font: 9pt; color: yellow; font:bold; background-color: transparent; ")
        self.addWidget(self.label3)

        self.label6 = QLabel(
            "Player3 lives--->[" + Server.player3Lives.__str__() + "] score--->[" + Server.player3Score.__str__() + "]")
        self.label6.resize(400, 30)
        self.label6.move(320, 440)
        self.label6.setStyleSheet("font: 9pt; color: blue; font:bold; background-color: transparent; ")
        self.addWidget(self.label6)

        self.label7 = QLabel(
            "Player4 lives--->[" + Server.player4Lives.__str__() + "] score--->[" + Server.player4Score.__str__() + "]")
        self.label7.resize(400, 30)
        self.label7.move(320, 470)
        self.label7.setStyleSheet("font: 9pt; color: green; font:bold; background-color: transparent; ")
        self.addWidget(self.label7)

        self.setPlayers(self.label6, self.label7)

        self.label4 = QLabel("Level : " + Server.level.__str__())
        self.label4.resize(400, 30)
        self.label4.move(500, 10)
        self.label4.setStyleSheet("font: 9pt; color: white; font: bold; background-color: transparent;")
        self.addWidget(self.label4)

    def setPlayers(self, label1Hide, label2Hide):
        if Server.currentRound == 0:
            self.addWidget(self.rocketnumber1)
            self.addWidget(self.rocketnumber2)
            label1Hide.hide()
            label2Hide.hide()

        elif Server.currentRound == 1:
            self.rocketnumber1.hide()
            self.rocketnumber2.hide()
            Server.level = 0
            Server.coordinatesOfRocket1X.clear()
            Server.coordinatesOfRocket1Y.clear()
            Server.coordinatesOfRocket2X.clear()
            Server.coordinatesOfRocket2Y.clear()
            Server.bulletsCollection1X.clear()
            Server.bulletsCollection1Y.clear()
            Server.bulletsCollection2X.clear()
            Server.bulletsCollection2Y.clear()
            Server.i = 1
            Server.i2 = 1
            Server.i3 = 1
            Server.i4 = 1
            self.rocketnumber3 = SpaceShuttle(self.width, self.height, self, 1)
            self.rocketnumber3.resize(60,
                                      50)  # slika je 50x50 ali se glupo okrece tako da je bolje ovako da bi se uvek videla cela
            self.rocketnumber3.setStyleSheet("background:transparent")

            self.rocketnumber4 = SpaceShuttle(self.width, self.height, self, 2)
            self.rocketnumber4.resize(60,
                                      50)  # slika je 50x50 ali se glupo okrece tako da je bolje ovako da bi se uvek videla cela
            self.rocketnumber4.setStyleSheet("background:transparent")

            self.addWidget(self.rocketnumber3)
            self.addWidget(self.rocketnumber4)
            label1Hide.hide()
            label2Hide.hide()

        elif Server.currentRound == 2:#napraviti nove rakete samo im zapamtiti id zbog player naziva
            self.rocketnumber3.hide()
            self.rocketnumber4.hide()
            Server.level = 0
            Server.coordinatesOfRocket1X.clear()
            Server.coordinatesOfRocket1Y.clear()
            Server.coordinatesOfRocket2X.clear()
            Server.coordinatesOfRocket2Y.clear()
            Server.bulletsCollection1X.clear()
            Server.bulletsCollection1Y.clear()
            Server.bulletsCollection2X.clear()
            Server.bulletsCollection2Y.clear()
            Server.i = 1
            Server.i2 = 1
            Server.i3 = 1
            Server.i4 = 1
            if Server.player1Score > Server.player2Score:
                Server.Win0 = 1
            elif Server.player1Score < Server.player2Score:
                Server.Win0 = 2
            elif Server.player1Score == Server.player2Score:
                if Server.Died == 1: # ako je p1 prvi poginuo
                    Server.Win0 = 1
                else:
                    Server.Win0 = 2

            if Server.player3Score > Server.player4Score:
                Server.Win1 = 3
            elif Server.player3Score < Server.player4Score:
                Server.Win1 = 4
            elif Server.player3Score == Server.player4Score:
                if Server.Died2 == 3:
                    Server.Win1 = 3
                else:
                    Server.Win1 = 4
            print("Server.Died -> " + Server.Died.__str__())
            print("Win0 -> " + Server.Win0.__str__())
            print("Win1 -> " + Server.Win1.__str__())
            Server.player1Lives = 3
            Server.player2Lives = 3
            Server.player3Lives = 3
            Server.player4Lives = 3
            Server.player1Score = 0
            Server.player2Score = 0
            Server.player3Score = 0
            Server.player4Score = 0
            self.rocketnumber5 = SpaceShuttle(self.width, self.height, self, 1)
            self.rocketnumber5.resize(60,
                                      50)  # slika je 50x50 ali se glupo okrece tako da je bolje ovako da bi se uvek videla cela
            self.rocketnumber5.setStyleSheet("background:transparent")

            self.rocketnumber6 = SpaceShuttle(self.width, self.height, self, 2)
            self.rocketnumber6.resize(60,
                                      50)  # slika je 50x50 ali se glupo okrece tako da je bolje ovako da bi se uvek videla cela
            self.rocketnumber6.setStyleSheet("background:transparent")

            self.addWidget(self.rocketnumber5)
            self.addWidget(self.rocketnumber6)
            label1Hide.hide()
            label2Hide.hide()

            # postavlja pobednika iz prvog meca
            if Server.Win0 == 1:
                #self.addWidget(self.rocketnumber1)
                self.label2.setText("Player1 lives--->[" + Server.player5Lives.__str__() + "] score--->[" + Server.player5Score.__str__() + "]")
                self.label2.setStyleSheet("font: 9pt; color: #f03a54; font:bold; background-color: transparent; ")
                self.label2.show()
            elif Server.Win0 == 2:
                #self.addWidget(self.rocketnumber2)
                self.label2.setText("Player2 lives--->[" + Server.player5Lives.__str__() + "] score--->[" + Server.player5Score.__str__() + "]")
                self.label2.setStyleSheet("font: 9pt; color: yellow; font:bold; background-color: transparent; ")
                self.label2.show()
            # postavlja pobednika iz drugog meca
            if Server.Win1 == 3:
                #self.addWidget(self.rocketnumber3)
                self.label6.setText(
                    "Player3 lives--->[" + Server.player6Lives.__str__() + "] score--->[" + Server.player6Score.__str__() + "]")
                self.label6.setStyleSheet("font: 9pt; color: blue; font:bold; background-color: transparent; ")
                self.label6.show()
            elif Server.Win1 == 4:
                #self.addWidget(self.rocketnumber4)
                self.label6.setText(
                    "Player4 lives--->[" + Server.player6Lives.__str__() + "] score--->[" + Server.player6Score.__str__() + "]")
                self.label6.setStyleSheet("font: 9pt; color: green; font:bold; background-color: transparent; ")
                self.label6.show()

    def createAsteroids(self):
        o = 0
        print("Create big for second rounds")
        print(Server.level)
        for o in range(Server.level):
            self.asteroid_0 = Asteroid(self.width, self.height, self, Server.asteroid_id.__str__(), True, 3)
            self.asteroid_0.setFocus()  # mozda i ne mora posto je timer tamo
            self.asteroid_0.setStyleSheet("background:transparent")
            self.asteroid_0.resize(60, 50)
            self.addWidget(self.asteroid_0)
            Server.activeBigAsteroids.append(self.asteroid_0)
            Server.activeAsteroids[Server.asteroid_id.__str__()] = 0
            Server.asteroid_id = Server.asteroid_id.__int__() + 1

    def createMediumAsteroids(self):
        o = 0
        for o in range(2):
            self.asteroid_0 = Asteroid(self.width, self.height, self, Server.asteroid_id.__str__(), True, 2)
            self.asteroid_0.setFocus()  # mozda i ne mora posto je timer tamo
            self.asteroid_0.setStyleSheet("background:transparent")
            self.asteroid_0.resize(60, 50)
            self.addWidget(self.asteroid_0)
            Server.activeBigAsteroids.append(self.asteroid_0)
            Server.activeAsteroids[Server.asteroid_id.__str__()] = 0
            Server.asteroid_id = Server.asteroid_id.__int__() + 1

    def createSmallAsteroids(self):
        o = 0
        for o in range(2):
            self.asteroid_0 = Asteroid(self.width, self.height, self, Server.asteroid_id.__str__(), True, 1)
            self.asteroid_0.setFocus()  # mozda i ne mora posto je timer tamo
            self.asteroid_0.setStyleSheet("background:transparent")
            self.asteroid_0.resize(60, 50)
            self.addWidget(self.asteroid_0)
            Server.activeBigAsteroids.append(self.asteroid_0)
            Server.activeAsteroids[Server.asteroid_id.__str__()] = 0
            Server.asteroid_id = Server.asteroid_id.__int__() + 1

    def game_is_over(self,
                     playerId):  # ako je game over proveri za kog igraca je game over ako je multiplayer, onog drugog pusti da jos igra
        """if self.players_number == 1:  # ako je singleplyaer cim ima 0 lives znaci mrtav je znaci game_over je
            self.gameOverScene = GameOver(self, self.width, self.height)
            self.gameOverScene.returnBtn.clicked.connect(self.menus)
            self.gameOverScene.label4.hide()  # hide that player2 is winner
            self.gameOverScene.label3.hide()  # hide player2 score bcs this is singleplayer
            self.sceneParent.setScene(self.gameOverScene)"""

        if playerId == 10:
            Server.coordinatesOfRocket1X.clear()
            Server.coordinatesOfRocket1Y.clear()
            #if Server.currentRound == 0:
            self.rocketnumber1.hide()
            self.rocketnumber1.move(1000, 1000)
        elif playerId == 20:
            Server.coordinatesOfRocket2X.clear()
            Server.coordinatesOfRocket2Y.clear()
            self.rocketnumber2.hide()
            self.rocketnumber2.move(1000, 1000)
        elif playerId == 12:
            Server.coordinatesOfRocket1X.clear()
            Server.coordinatesOfRocket1Y.clear()
            self.rocketnumber5.hide()
            self.rocketnumber5.move(1000, 1000)
        elif playerId == 31:
            Server.coordinatesOfRocket1X.clear()
            Server.coordinatesOfRocket1Y.clear()
            self.rocketnumber3.hide()
            self.rocketnumber3.move(1000, 1000)
        elif playerId == 32:
            Server.coordinatesOfRocket1X.clear()
            Server.coordinatesOfRocket1Y.clear()
            self.rocketnumber5.hide()
            self.rocketnumber5.move(1000, 1000)
        elif playerId == 41:
            Server.coordinatesOfRocket2X.clear()
            Server.coordinatesOfRocket2Y.clear()
            self.rocketnumber4.hide()
            self.rocketnumber4.move(1000, 1000)
        elif playerId == 22:
            Server.coordinatesOfRocket2X.clear()
            Server.coordinatesOfRocket2Y.clear()
            self.rocketnumber6.hide()
            self.rocketnumber6.move(1000, 1000)
        elif playerId == 42:
            Server.coordinatesOfRocket2X.clear()
            Server.coordinatesOfRocket2Y.clear()
            self.rocketnumber6.hide()
            self.rocketnumber6.move(1000, 1000)

        if Server.currentRound == 2 and Server.player5Lives == 0 and Server.player6Lives == 0:
            self.gameOverScene = GameOver(self, self.width, self.height)
            self.gameOverScene.returnBtn.clicked.connect(self.menus)
            if Server.player5Score > Server.player6Score:
                self.gameOverScene.label4.hide()
                self.gameOverScene.label3.hide()
                self.gameOverScene.label2.hide()
                self.gameOverScene.label5.hide()
                if Server.Win0 == 1:
                    self.gameOverScene.label6.setText("Player1 Win")
                    self.gameOverScene.label6.setStyleSheet("font: 9pt; color: #f03a54; font:bold; background-color: transparent; ")
                else:
                    self.gameOverScene.label6.setText("Player2 Win")
                    self.gameOverScene.label6.setStyleSheet("font: 9pt; color: yellow; font:bold; background-color: transparent; ")
            elif Server.player5Score < Server.player6Score:
                self.gameOverScene.label4.hide()
                self.gameOverScene.label3.hide()
                self.gameOverScene.label2.hide()
                self.gameOverScene.label5.hide()
                if Server.Win1 == 3:
                    self.gameOverScene.label6.setText("Player3 Win")
                    self.gameOverScene.label6.setStyleSheet("font: 9pt; color: blue; font:bold; background-color: transparent; ")
                else:
                    self.gameOverScene.label6.setText("Player4 Win")
                    self.gameOverScene.label6.setStyleSheet("font: 9pt; color: green; font:bold; background-color: transparent; ")
            else:
                self.gameOverScene.label4.hide()
                self.gameOverScene.label3.hide()
                self.gameOverScene.label2.hide()
                self.gameOverScene.label5.hide()
                self.gameOverScene.label6.setText("Tied")
            self.sceneParent.setScene(self.gameOverScene)

    def menus(self):
        self.sceneParent.ExitGame()

    def keyPressEvent(self, event):
        self.key_notifier.add_key(event.key())

    def keyReleaseEvent(self, event):
        self.key_notifier.rem_key(event.key())

    def __update_position__(self, key):
        # time.sleep(1)
        if key == Qt.Key_W:  # dodata logika da moze da se pomera samo ako je idalje ziva ta raketa
            if Server.currentRound == 0 and Server.player2Lives > 0:
                self.rocketnumber2.upRocket2.emit()
            elif Server.currentRound == 1 and Server.player4Lives > 0:
                self.rocketnumber4.upRocket2.emit()
            elif Server.currentRound == 2 and Server.player6Lives > 0:
                self.rocketnumber6.upRocket2.emit()
        elif key == Qt.Key_A:
            if Server.currentRound == 0 and Server.player2Lives > 0:
                self.rocketnumber2.leftRocket2.emit()
            elif Server.currentRound == 1 and Server.player4Lives > 0:
                self.rocketnumber4.leftRocket2.emit()
            elif Server.currentRound == 2 and Server.player6Lives > 0:
                self.rocketnumber6.leftRocket2.emit()
        elif key == Qt.Key_D:
            if Server.currentRound == 0 and Server.player2Lives > 0:
                self.rocketnumber2.rightRocket2.emit()
            elif Server.currentRound == 1 and Server.player4Lives > 0:
                self.rocketnumber4.rightRocket2.emit()
            elif Server.currentRound == 2 and Server.player6Lives > 0:
                self.rocketnumber6.rightRocket2.emit()
        elif key == Qt.Key_S:
            if Server.currentRound == 0 and Server.player2Lives > 0:
                self.rocketnumber2.fireRocket2.emit()
            elif Server.currentRound == 1 and Server.player4Lives > 0:
                self.rocketnumber4.fireRocket2.emit()
            elif Server.currentRound == 2 and Server.player6Lives > 0:
                self.rocketnumber6.fireRocket2.emit()
        elif key == Qt.Key_Up:
            if Server.currentRound == 0 and Server.player1Lives > 0:
                self.rocketnumber1.upRocket1.emit()
            elif Server.currentRound == 1  and Server.player3Lives > 0:
                self.rocketnumber3.upRocket1.emit()
            elif Server.currentRound == 2  and Server.player5Lives > 0:
                self.rocketnumber5.upRocket1.emit()
        elif key == Qt.Key_Right:
            if Server.currentRound == 0 and Server.player1Lives > 0:
                self.rocketnumber1.rightRocket1.emit()
            elif Server.currentRound == 1 and Server.player3Lives > 0:
                self.rocketnumber3.rightRocket1.emit()
            elif Server.currentRound == 2 and Server.player5Lives > 0:
                self.rocketnumber5.rightRocket1.emit()
        elif key == Qt.Key_Left:
            if Server.currentRound == 0 and Server.player1Lives > 0:
                self.rocketnumber1.leftRocket1.emit()
            elif Server.currentRound == 1 and Server.player3Lives > 0:
                self.rocketnumber3.leftRocket1.emit()
            elif Server.currentRound == 2 and Server.player5Lives > 0:
                self.rocketnumber5.leftRocket1.emit()
        elif key == Qt.Key_Space:
            if Server.currentRound == 0 and Server.player1Lives > 0:
                self.rocketnumber1.fireRocket1.emit()
            elif Server.currentRound == 1 and Server.player3Lives > 0:
                self.rocketnumber3.fireRocket1.emit()
            elif Server.currentRound == 2 and Server.player5Lives > 0:
                self.rocketnumber5.fireRocket1.emit()

    def timerEvent(self, a0: 'QTimerEvent'):
        if Server.bonus_time < 15:
            Server.bonus_time = Server.bonus_time + 1
        elif Server.bonus_time == 15:
            Server.bonus_x_coordinate = random.randrange(0, 500)
            Server.bonus_y_coordinate = random.randrange(0, 450)
            Server.bonus_x_expanded.clear()
            Server.bonus_y_expanded.clear()
            tmpXX = 0
            for tmpXX in range(50):
                Server.bonus_x_expanded.append(tmpXX + Server.bonus_x_coordinate)  # prosirivanje koordinata bonusa
            tmpYY = 0
            for tmpYY in range(50):
                Server.bonus_y_expanded.append(tmpYY + Server.bonus_y_coordinate)  # prosirivanje koordinata bonusa
            self.bonus = Bonus(self.width, self.height, Server.bonus_x_coordinate, Server.bonus_y_coordinate, self)
            self.bonus.setStyleSheet("background:transparent")
            self.addWidget(self.bonus)
            Server.bonus_time = Server.bonus_time + 1
        elif Server.bonus_time == 16 and Server.currentRound == 0: # ako igraju P1 i P2
            if (any(checkXCords in Server.bonus_x_expanded for checkXCords in Server.coordinatesOfRocket1X) and any(
                    checkYCords in Server.bonus_y_expanded for checkYCords in Server.coordinatesOfRocket1Y)):
                Server.player1Lives = Server.player1Lives + 1
                self.label2.setText(
                    "Player1 lives--->[" + Server.player1Lives.__str__() + "] score--->[" + Server.player1Score.__str__() + "]")
            if (any(checkXCords in Server.bonus_x_expanded for checkXCords in Server.coordinatesOfRocket2X) and any(
                    checkYCords in Server.bonus_y_expanded for checkYCords in Server.coordinatesOfRocket2Y)):
                Server.player2Lives = Server.player2Lives + 1
                self.label3.setText(
                    "Player2 lives--->[" + Server.player2Lives.__str__() + "] score--->[" + Server.player2Score.__str__() + "]")
            self.bonus.hide()
            self.bonus.move(1234, 1234)
            Server.bonus_time = 0
        elif Server.bonus_time == 16 and Server.currentRound == 1: # ako igraju P3 i P4
            if (any(checkXCords in Server.bonus_x_expanded for checkXCords in Server.coordinatesOfRocket1X) and any(
                    checkYCords in Server.bonus_y_expanded for checkYCords in Server.coordinatesOfRocket1Y)):
                Server.player3Lives = Server.player3Lives + 1
                self.label6.setText(
                    "Player3 lives--->[" + Server.player3Lives.__str__() + "] score--->[" + Server.player3Score.__str__() + "]")
            if (any(checkXCords in Server.bonus_x_expanded for checkXCords in Server.coordinatesOfRocket2X) and any(
                    checkYCords in Server.bonus_y_expanded for checkYCords in Server.coordinatesOfRocket2Y)):
                Server.player4Lives = Server.player4Lives + 1
                self.label7.setText(
                    "Player4 lives--->[" + Server.player4Lives.__str__() + "] score--->[" + Server.player4Score.__str__() + "]")
            self.bonus.hide()
            self.bonus.move(1234, 1234)
            Server.bonus_time = 0
        elif Server.bonus_time == 16 and Server.currentRound == 2: # pobednici
            if (any(checkXCords in Server.bonus_x_expanded for checkXCords in Server.coordinatesOfRocket1X) and any(
                    checkYCords in Server.bonus_y_expanded for checkYCords in Server.coordinatesOfRocket1Y)):
                if Server.Win0 == 1: # ako je bio pobedio P1
                    Server.player5Lives = Server.player5Lives + 1
                    self.label2.setText(
                        "Player1 lives--->[" + Server.player5Lives.__str__() + "] score--->[" + Server.player5Score.__str__() + "]")
                elif Server.Win0 == 2: # ako je bio pobedio P2
                    Server.player5Lives = Server.player5Lives + 1
                    self.label2.setText(
                        "Player2 lives--->[" + Server.player5Lives.__str__() + "] score--->[" + Server.player5Score.__str__() + "]")
            if (any(checkXCords in Server.bonus_x_expanded for checkXCords in Server.coordinatesOfRocket2X) and any(
                    checkYCords in Server.bonus_y_expanded for checkYCords in Server.coordinatesOfRocket2Y)):
                if Server.Win1 == 3:  # ako je bio pobedio P3
                    Server.player6Lives = Server.player6Lives + 1
                    self.label6.setText(
                        "Player3 lives--->[" + Server.player6Lives.__str__() + "] score--->[" + Server.player6Score.__str__() + "]")
                elif Server.Win1 == 4:  # ako je bio pobedio P4
                    Server.player6Lives = Server.player6Lives + 1
                    self.label6.setText(
                        "Player4 lives--->[" + Server.player6Lives.__str__() + "] score--->[" + Server.player6Score.__str__() + "]")
            self.bonus.hide()
            self.bonus.move(1234, 1234)
            Server.bonus_time = 0