import sys
from PyQt4.QtGui import *

class AnimalButtonWidget(QWidget):
    """A representation of an animal widget"""
    def __init__(self):
        super().__init__()
        self.MainLayout = self.Layout()
        self.setLayout(self.MainLayout)
        
    
    def Layout(self):
        pass
        

    
