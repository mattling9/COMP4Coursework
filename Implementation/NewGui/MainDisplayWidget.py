from PyQt4.QtGui import *
from PyQt4.QtCore import *
from PyQt4.QtSql import *

class MainDisplayWidget(QWidget):
    "A representation of the Display Widget"""
    def __init__(self):
        super().__init__()
        self.stacked_layout = QStackedLayout()
        self.setLayout(self.stacked_layout)
        self.model = None
        self.display_results_layout()
