from PyQt4.QtGui import *
from PyQt4.QtCore import *
from PyQt4.QtSql import *

class ProductSearchWidget(QWidget):
    "A representation of the Product Search Widget"""
    def __init__(self):
        super().__init__()
        self.layout = self.ProductSearchLayout()
        self.setLayout(layout)

    def ProductSearchLayout(self):
        names = ["Dog", "Cat", "Fish", "Pets", "Bird", "Reptile", "Equine"]
        positions = [(i,j) for i in range(5) for j in range(4)]
        for position, name in zip(positions, names):
            button = QPushButton(name)
            self.ProductMenu.addWidget(button, *position)

        self.ProductMenu = QGridLayout()

        
        
