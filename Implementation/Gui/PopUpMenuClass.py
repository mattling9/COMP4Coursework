from PyQt4.QtGui import *
from PyQt4.QtCore import *
from CustomToolbarClass import *

class PopUpWindow(QDialog):
    def __init__(self, LabelText, button1, button2):
        super().__init__()
        style_sheet = """QDialog#main_window{
                                 background-color: white;
                                 border-style: solid;
                                 border-width: 2px;
                                 border-color: rgb(180,180,180);}
                         QLabel{
                                 font-family: Segoe UI;
                                 font-size: 12pt;
                                 color: rgb(70,70,70)}

                        QPushButton{
                                 font-family: Segoe UI;
                                 font-size: 11pt;
                                 font-weight: bold;
                                 color: white;
                                 background-color: rgb(0,240,0);
                                 border: 0px}


                        """
        self.setObjectName("main_window")
        self.setStyleSheet(style_sheet)
        self.setWindowFlags(Qt.FramelessWindowHint)
        self.title_bar = TitleBar()
        self.title_bar.minimise.clicked.connect(self.minimise_window)
        self.title_bar.close.clicked.connect(self.close_window)
        self.label = QLabel(LabelText)
        self.label.setAlignment(Qt.AlignCenter)
        self.buttonBox = QDialogButtonBox()
        self.buttonBox.setOrientation(Qt.Horizontal)
        self.buttonBox.setStandardButtons(button1 | button2)
        self.buttonBox.button(button1).setFixedSize(84,27)
        self.buttonBox.button(button2).setFixedSize(84,27)
        self.pop_up_layout = QVBoxLayout()
        self.pop_up_layout.addWidget(self.title_bar)
        self.pop_up_layout.addWidget(self.label)
        self.pop_up_layout.addWidget(self.buttonBox)
        self.setLayout(self.pop_up_layout)
        self.setFixedSize(400, 150)
        self.show()
        self.raise_()

    def minimise_window(self):
        self.showMinimized()

    def close_window(self):
        self.close()

    def mousePressEvent(self,event):

        if event.button() == Qt.LeftButton:
            self.moving = True; self.offset = event.pos()

    def mouseMoveEvent(self,event):
        try:
            if self.moving:
                self.move(event.globalPos()-self.offset)
        except AttributeError:
            pass

    
