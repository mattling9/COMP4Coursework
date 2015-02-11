from PyQt4.QtGui import *
from PyQt4.QtCore import *
from CustomToolbarClass import *

class ErrorMessageClass(QDialog):
    """a representation of the Error Window"""
    def __init__(self, LabelText):
        super().__init__()
        self.setWindowFlags(Qt.FramelessWindowHint)
        self.setObjectName("main_window")
        self.title_bar = TitleBar()
        self.title_bar.minimise.clicked.connect(self.minimise_main_window)
        self.title_bar.close.clicked.connect(self.close_main_window)

        style_sheet = """QDialog#main_window{
                                 background-color: white;
                                 font-family: Segoe UI;
                                 font-size: 12pt;
                                 color: rgb(70,70,70);
                                 border-style: solid;
                                 border-color: rgb(180,180,180);
                                 border-width: 2px;}
                        QLabel{
                                 font-family: Segoe UI;
                                 font-size: 12pt;
                                 color: rgb(70,70,70);}

                        QPushButton{
                                 font-family: Segoe UI;
                                 font-size: 11pt;
                                 font-weight: bold;
                                 color: white;
                                 background-color: rgb(0,240,0);
                                 border: 0px}
                               
                       QPushButton:pressed{
                                 font-family: Segoe UI;
                                 font-size: 11pt;
                                 font-color: white;
                                 background-color: rgb(0,210,0);}
                 }"""

        
        self.label = QLabel(LabelText)
        self.label.setAlignment(Qt.AlignCenter)
        self.buttonBox = QDialogButtonBox()
        self.buttonBox.setOrientation(Qt.Horizontal)
        self.buttonBox.setStandardButtons(QDialogButtonBox.Ok )
        self.buttonBox.button(QDialogButtonBox.Ok).setShortcut(QKeySequence("Return"))
        self.buttonBox.button(QDialogButtonBox.Ok).setFixedSize(84,27)
        self.buttonBox.button(QDialogButtonBox.Ok).clicked.connect(self.close_window)
        self.pop_up_layout = QVBoxLayout()
        self.pop_up_widget = QWidget()
        self.pop_up_layout.addWidget(self.title_bar)
        self.pop_up_layout.addWidget(self.label)
        self.pop_up_layout.addWidget(self.buttonBox)
        self.pop_up_widget.setLayout(self.pop_up_layout)
        self.setLayout(self.pop_up_layout)
        self.setStyleSheet(style_sheet)
        self.move(700,430)
        self.show()
        self.raise_()
        

    def close_window(self):
        self.close()

    def minimise_main_window(self):
        self.showMinimized()

    def close_main_window(self):
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
