import sys
from welcome_scene import *
from mode_scene import *
from game_scene import *
from about_scene import *
from tournament import *
from Network_Game.game_scene_network import *
import Network_Game.network_constants
import Server
from  music import musicPlayer
from multiprocessing import Process
from threading import Thread
from PyQt5.QtCore import QThread, QProcess

class MainWindow(QGraphicsView):

    def __init__(self):
        super().__init__()
        self.widths = 602
        self.heights = 502
        self.rect().center()
        self.setFixedWidth(self.widths)
        self.setFixedHeight(self.heights)
        self.welcomeScene = WelcomeScene(self, self.widths, self.heights)
        self.welcomeScene.newGameBtn.clicked.connect(self.GameMode)
        self.welcomeScene.aboutGameBtn.clicked.connect(self.AboutGame)
        self.welcomeScene.exitBtn.clicked.connect(self.ExitGame)
        self.modeScene = None
        self.gameScene = None
        self.aboutScene = None
        self.networkScene = None
        self.setScene(self.welcomeScene)
        self.show()        

    def GameMode(self):
        self.modeScene = ModeScene(self, self.widths, self.heights)
        self.modeScene.singlPlyBtn.clicked.connect(self.Singleplayer)
        self.modeScene.returnBtn.clicked.connect(self.ReturnToWelcome)
        self.modeScene.multiPlayerBtn.clicked.connect(self.Multiplayer)
        self.modeScene.tournamentBtn.clicked.connect(self.MultiplayerTournament)
        self.modeScene.network.clicked.connect(self.NetworkGame)
        self.setScene(self.modeScene)

    def AboutGame(self):
        self.aboutScene = AboutScene(self, self.widths, self.heights)
        self.aboutScene.returnBtn.clicked.connect(self.ReturnToWelcome)
        self.setScene(self.aboutScene)

    def ExitGame(self):
        self.close()

    def Singleplayer(self):
        self.gameScene = GameScene(self, self.widths, self.heights, 1)#last parameter is number of players
        Server.is_multiplayer = False
        self.setScene(self.gameScene)

    def Multiplayer(self):
        self.gameScene = GameScene(self, self.widths, self.heights, 2)#last parameter is number of players
        Server.is_multiplayer = True
        self.setScene(self.gameScene)

    def MultiplayerTournament(self):
        self.tournament = Tournament(self, self.widths, self.heights)
        self.setScene(self.tournament)

    def ReturnToWelcome(self):
        self.setScene(self.welcomeScene)

    def NetworkGame(self):
        self.networkScene = NetworkScene(self, self.widths, self.heights)
        self.networkScene.checkPlayers.clicked.connect(self.CheckConnections)
        if Server.second_player_is_here == True:
            self.setScene(self.networkScene)
            self.networkScene.alfa()
        else:
            self.setScene(self.networkScene)

    def CheckConnections(self):
        self.networkScene.alfa()


if __name__ == '__main__':
    app = QApplication([])
    mw = MainWindow()
    mp = musicPlayer()
    musicProces = QProcess(mp)
    musicProces.start()
    sys.exit(app.exec_())
    

