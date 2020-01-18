from PyQt5.QtCore import QSize, QDir, Qt
from PyQt5.QtGui import QBrush, QFont, QPalette, QFontDatabase, QImage, QPixmap
from PyQt5.QtWidgets import QGraphicsView, QGraphicsScene, QApplication, QPushButton, QLabel

class WelcomeScene(QGraphicsScene):
    def __init__(self, parent, width, height):
        super().__init__(parent)
        self.width = width
        self.height = height
        self.prnt = parent
        self.label = QLabel()
        self.pixmap = QPixmap('Images/img.png')
        self.label.setPixmap(self.pixmap)
        self.label.resize(self.width-2, self.height-2)
        self.addWidget(self.label)
        self.mainLabel = QLabel("ASTEROIDS")
        self.mainLabel.resize(200, 100)
        self.mainLabel.setStyleSheet("color: white; font-size:32px; font:bold; background:transparent")
        self.mainLabel.move(200, 0)
        self.addWidget(self.mainLabel)
        
        self.newGameBtn = QPushButton("New Game")
        self.newGameBtn.setStyleSheet("QPushButton{"
                                      "color: white; background-color: transparent; font:bold; border-style: outset; border-width: 2px; border-color: white"
                                      "}"
                                      "QPushButton:hover{"
                                      "background-color: #3F7FBF"
                                      "}")
        self.newGameBtn.resize(100, 50)
        self.newGameBtn.move(250, 100)
        self.addWidget(self.newGameBtn)

        self.aboutGameBtn = QPushButton("About game")
        self.aboutGameBtn.setStyleSheet("QPushButton{"
                                        "color: white; background-color: transparent; font:bold; border-style: outset; border-width: 2px; border-color: white"
                                        "}"
                                        "QPushButton:hover{"
                                        "background-color: #3F7FBF"
                                        "}")
        self.aboutGameBtn.resize(100, 50)
        self.aboutGameBtn.move(250, 165)
        self.addWidget(self.aboutGameBtn)

        self.exitBtn = QPushButton("Exit")
        self.exitBtn.setStyleSheet("QPushButton{"
                                   "color: white; background-color: transparent; font:bold; border-style: outset; border-width: 2px; border-color: white"
                                   "}"
                                   "QPushButton:hover{"
                                   "background-color: #C14242"
                                   "}")
        self.exitBtn.resize(100, 50)
        self.exitBtn.move(250, 230)
        self.addWidget(self.exitBtn)