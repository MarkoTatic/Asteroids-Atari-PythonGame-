from PyQt5.QtCore import QCoreApplication, QUrl, QObject, QThread
from PyQt5.QtMultimedia import QMediaPlaylist, QMediaPlayer, QMediaContent
import sys

class musicPlayer(QObject):
    def __init__(self):
        super().__init__()
        self.playlist = QMediaPlaylist()
        self.url = QUrl.fromLocalFile('Music/1.mp3')
        self.playlist.addMedia(QMediaContent(self.url))
        self.url = QUrl.fromLocalFile('Music/2.mp3')
        self.playlist.addMedia(QMediaContent(self.url))
        self.url = QUrl.fromLocalFile('Music/3.mp3')
        self.playlist.addMedia(QMediaContent(self.url))
        self.url = QUrl.fromLocalFile('Music/4.mp3')
        self.playlist.addMedia(QMediaContent(self.url))
        self.playlist.setPlaybackMode(QMediaPlaylist.Loop)
        print("stigao do 1")
        self.player = QMediaPlayer()
        self.player.setPlaylist(self.playlist)
        self.player.play()
        print("stigao do 2")
        #self.player.setMuted(True)