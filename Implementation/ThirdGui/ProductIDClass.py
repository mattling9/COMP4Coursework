from PyQt4.QtGui import *
from PyQt4.QtCore import *

class ProductIDClass(QWidget):
    """A representation of A Push Button Widget"""
    def __init__(self):
        super().__init__()
        self.layout = QHBoxLayout()
        self.widget = QWidget()
        self.label = QLabel("Product ID:")
        self.line_edit = QLineEdit()
        self.button = QPushButton("Find...")
        self.layout.addWidget(self.label)
        self.layout.addWidget(self.line_edit)
        self.layout.addWidget(self.button)
        self.setLayout(self.layout)
