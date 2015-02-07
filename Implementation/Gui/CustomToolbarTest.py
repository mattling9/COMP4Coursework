import sys
from PyQt4.QtCore import *
from PyQt4.QtGui import *


class TitleBar(QDialog):
    def __init__(self, parent=None):
        QWidget.__init__(self, parent)
        self.setWindowFlags(Qt.FramelessWindowHint)

        minimise = QToolButton()
        minimise.setIcon(QIcon(".\SystemImages\minimize.png"))
        minimise.setFixedSize(40,40)
        minimise.clicked.connect(self.minimise_main_window)
        minimise.setObjectName('minimise_button')

        close = QToolButton()
        close.setIcon(QIcon(".\SystemImages\close.png"))
        close.setFixedSize(40,40)
        close.clicked.connect(self.close_main_window)
        close.setObjectName('close_button')

        self.label = QLabel("Beacon Vets Stock Control")
        self.label.setObjectName('label')

        self.main_layout = QHBoxLayout()
        self.main_layout.addWidget(self.label)
        self.main_layout.addWidget(minimise)
        self.main_layout.addWidget(close)
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

    def minimise_main_window(self):
        main_window.showMinimized()

    def close_main_window(self):
        main_window.close()

    def mousePressEvent(self,event):

        if event.button() == Qt.LeftButton:
            main_window.moving = True; main_window.offset = event.pos()

    def mouseMoveEvent(self,event):
        try:
            if main_window.moving:
                main_window.move(event.globalPos()-main_window.offset)
        except AttributeError:
            pass
        
class mainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowFlags(Qt.FramelessWindowHint)
        self.resize(400, 400)
        self.title_bar = TitleBar()
        self.title_bar.setObjectName('titlebar')
        self.message = QLabel("hello world")
        
        self.main_layout = QVBoxLayout()
        self.main_widget = QWidget()
        self.main_layout.addWidget(self.title_bar)
        self.main_layout.addWidget(self.message)
        self.main_widget.setLayout(self.main_layout)
        self.setCentralWidget(self.main_widget)
        


if __name__ == '__main__':
    app = QApplication(sys.argv)
    main_window = mainWindow()

    main_window.show()
