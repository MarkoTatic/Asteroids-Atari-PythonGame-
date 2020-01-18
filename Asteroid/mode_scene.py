from PyQt5.QtCore import QSize, QDir, Qt
from PyQt5.QtGui import QBrush, QFont, QPalette, QFontDatabase, QImage, QPixmap
from PyQt5.QtWidgets import QGraphicsView, QGraphicsScene, QApplication, QPushButton, QLabel


class ModeScene(QGraphicsScene):
    def __init__(self, parent, width, height):
        super().__init__(parent)
        self.width = width
        self.height = height
        self.parent = parent

        self.label = QLabel()
        self.pixmap = QPixmap('Images/img.png')
        self.label.setPixmap(self.pixmap)
        self.label.resize(self.width-2, self.height-2)
        self.addWidget(self.label)

        self.mainLabel = QLabel("SELECT MODE")
        self.mainLabel.resize(230, 100)
        self.mainLabel.setStyleSheet("color: white; font-size:32px; font:bold; background:transparent")
        self.mainLabel.move(180, 0)
        self.addWidget(self.mainLabel)


        self.singlPlyBtn = QPushButton("Singleplayer")
        self.singlPlyBtn.setStyleSheet("QPushButton{"
                                       "color: white; background-color: transparent; font:bold; border-style: outset; border-width: 2px; border-color: white"
                                       "}"
                                       "QPushButton:hover{"
                                       "background-color: #3F7FBF"
                                       "}")
        self.singlPlyBtn.resize(100, 50)
        self.singlPlyBtn.move(250, 100)
        self.addWidget(self.singlPlyBtn)

        self.multiPlayerBtn = QPushButton("Multiplayer")
        self.multiPlayerBtn.setStyleSheet("QPushButton{"
                                       "color: white; background-color: transparent; font:bold; border-style: outset; border-width: 2px; border-color: white"
                                       "}"
                                       "QPushButton:hover{"
                                       "background-color: #3F7FBF"
                                       "}")
        self.multiPlayerBtn.resize(100, 50)
        self.multiPlayerBtn.move(250, 165)
        self.addWidget(self.multiPlayerBtn)

        self.tournamentBtn = QPushButton("Tournament")
        self.tournamentBtn.setStyleSheet("QPushButton{"
                                          "color: white; background-color: transparent; font:bold; border-style: outset; border-width: 2px; border-color: white"
                                          "}"
                                          "QPushButton:hover{"
                                          "background-color: #3F7FBF"
                                          "}")
        self.tournamentBtn.resize(100, 50)
        self.tournamentBtn.move(250, 230)
        self.addWidget(self.tournamentBtn)


        self.returnBtn = QPushButton("Return")
        self.returnBtn.setStyleSheet("QPushButton{"
                                     "color: white; background-color: transparent; font:bold; border-style: outset; border-width: 2px; border-color: white"
                                     "}"
                                     "QPushButton:hover{"
                                     "background-color: #C14242"
                                     "}")
        self.returnBtn.resize(100, 50)
        self.returnBtn.move(250, 360)
        self.addWidget(self.returnBtn)

        self.network = QPushButton("Network")
        self.network.setStyleSheet("QPushButton{"
                                   "color: white; background-color: transparent; font:bold; border-style: outset; border-width: 2px; border-color: white"
                                   "}"
                                   "QPushButton:hover{"
                                   "background-color: #C14242"
                                   "}")
        self.network.resize(100, 50)
        self.network.move(250, 295)
        self.addWidget(self.network)
