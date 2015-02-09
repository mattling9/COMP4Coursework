import sys, time

from PyQt4.QtCore import *
from PyQt4.QtGui import *

class animatedSplashScreen(QSplashScreen):
    def __init__(self, movie, flags, parent = None):
        movie.jumpToFrame(0)
        pixmap = QPixmap(movie.frameRect().size())
        QSplashScreen.__init__(self, pixmap)
        self.movie = movie
        self.movie.frameChanged.connect(self.repaint)
    
    def showEvent(self, event):
       self.movie.start()
     
    def hideEvent(self, event):
        self.movie.stop()
     
    def paintEvent(self, event):
        painter = QPainter(self)
        pixmap = self.movie.currentPixmap()
        self.setMask(pixmap.mask())
        painter.drawPixmap(0, 0, pixmap)
      
    def sizeHint(self):
        return self.movie.scaledSize()



