import sys
from PyQt4.QtCore import *
from PyQt4.QtGui import *


class TitleBar(QDialog):
    def __init__(self, parent=None):
        QWidget.__init__(self, parent)
        self.setWindowFlags(Qt.FramelessWindowHint)

        self.minimise = QToolButton()
        self.minimise.setIcon(QIcon(".\SystemImages\minimize.png"))
        self.minimise.setFixedSize(30,30)
        self.minimise.setObjectName('minimise_button')

        self.close = QToolButton()
        self.close.setIcon(QIcon(".\SystemImages\close.png"))
        self.close.setFixedSize(30,30)
        self.close.setObjectName('close_button')

        self.label = QLabel("Beacon Vets Stock Control")
        self.label.setObjectName('label')

        self.main_layout = QHBoxLayout()
        self.main_layout.addWidget(self.label)
        self.main_layout.addWidget(self.minimise)
        self.main_layout.addWidget(self.close)
        self.main_layout.insertStretch(1,500)
        self.main_layout.setSpacing(0)
        self.setLayout(self.main_layout)

        self.setFixedHeight(40)
        self.setStyleSheet("""QMainWindow{
                                          background-color: white;
                                          font-color: black;
                                          font-family: Segoe UI}
                              QToolButton#minimise_button{
                                          background-color: white;
                                          border: 0px;}
                              QToolButton#minimise_button:hover{
                                          background-color: rgb(188,188,188);
                                          border: 0px;}
                              QToolButton#minimise_button:pressed{
                                          background-color: rgb(0,240,0);}
                                          
                              QToolButton#close_button{
                                          background-color: white;
                                          border: 0px;}
                              QToolButton#close_button:hover{
                                          background-color: rgb(220,39,39);
                                          border: 0px;}
                              QToolButton#close_button:pressed{
                                          background-color: rgb(130,21,21);}
                              QLabel#label{font-family: Segoe UI;
                                          font-size: 13pt;
                                          color: rgb(100,100,100);}
                              QWidget#titlebar{
                                          background-color: white;}
                               """)
