import sys
from PyQt4.QtCore import *
from PyQt4.QtGui import *
from ExtendedQLabel import *

class MainWindow(QMainWindow):
    
    def __init__(self):
        super().__init__()
        """A representation of the log in screen"""
        #STYLE
        self.setWindowFlags(Qt.FramelessWindowHint)
        self.setStyleSheet("""font-family: Segoe UI;
                           font-size: 12pt;
                           background-color: white;""")


        self.minimize= QToolButton(self);
        self.minimize.setIcon(QtGui.QIcon(''));

        self.maximize=QtGui.QToolButton(self);
        self.maximize.setIcon(QtGui.QIcon('img/max.png'));

        close=QtGui.QToolButton(self);
        close.setIcon(QtGui.QIcon('img/close.png'));

        self.minimize.setMinimumHeight(10);
        close.setMinimumHeight(10);
        self.maximize.setMinimumHeight(10);

        self.title_bar = QTitleBar()
        #STYLE
        self.setFixedSize(600,400)        
        self.username_label = QLabel("Username:")
        self.password_label = QLabel("Password:")
        self.username = QLineEdit()
        self.password = QLineEdit()
        self.password.setEchoMode(2)

        self.font = QFont()
        self.font.setUnderline(True)
        self.forgot_password = ExtendedQLabel("Forgot Password?")
        self.forgot_password.setFont(self.font)
        self.forgot_password.setAlignment(Qt.AlignCenter)
        self.palette = QPalette(self.forgot_password.palette())
        self.palette.setColor(QPalette.WindowText, QColor(Qt.blue))
        self.forgot_password.setPalette(self.palette)
        self.forgot_password.setToolTip("Click this link if you have forgotten your password.")
        self.connect(self.forgot_password, SIGNAL('clicked()'), self.button_clicked)
        self.forgot_password.setFixedWidth(130)
        self.forgot_password.setFixedHeight(40)

        
        self.enter_button = QPushButton("Sign In")
        self.enter_button.setFixedWidth(80)
        self.enter_button.setFixedHeight(26)
        self.enter_button.clicked.connect(self.find_account)
        self.enter_button.setStyleSheet("""background-color: rgb(0,240,0);
                                           color: #FFFFFF;
                                           border: none;
                                           font-family:
                                           Segoe UI;
                                           font-size: 11pt;
                                           font-weight: bold;""")
        self.enter_button.pressed.connect(self.change_colour1)
        self.enter_button.released.connect(self.change_colour2)


        self.spacer = QLabel()
        self.spacer.setFixedWidth(90)

        self.log_in_widget = QWidget()
        self.log_in_layout = QGridLayout()
        self.log_in_layout.addWidget(self.spacer, 0,0)
        self.log_in_layout.addWidget(self.username_label, 0,1)
        self.log_in_layout.addWidget(self.username, 0,2)
        self.log_in_layout.addWidget(self.spacer, 0,3)
        self.log_in_layout.addWidget(self.spacer, 1,0)
        self.log_in_layout.addWidget(self.password_label, 1,1)
        self.log_in_layout.addWidget(self.password, 1,2)
        self.log_in_layout.addWidget(self.spacer, 1,4)
        self.log_in_layout.addWidget(self.enter_button, 1,3)
        self.log_in_layout.addWidget(self.forgot_password, 2,2)
        self.log_in_layout.addWidget(self.spacer, 3,0)
        self.log_in_widget.setLayout(self.log_in_layout)

        self.main_widget = QWidget()
        self.main_layout = QVBoxLayout()
        self.main_layout.addWidget(self.title_bar)
        self.main_layout.addWidget(self.spacer)
        self.main_layout.addWidget(self.log_in_widget)
        self.main_widget.setLayout(self.main_layout)

        self.setCentralWidget(self.main_widget)

    def button_clicked(self):
        print("button clicked")

    def find_account(self):
        print("Account Not in Database")

    def change_colour1(self):
        if self.enter_button.pressed:
            self.enter_button.setStyleSheet("""background-color: rgb(0,210,0);
                                               color: #FFFFFF;
                                               border: none;
                                               font-family:
                                               Segoe UI;
                                               font-size: 11pt;
                                               font-weight: bold;""")
    def change_colour2(self):
            self.enter_button.setStyleSheet("""background-color: rgb(0,240,0);
                                               color: #FFFFFF;
                                               border: none;
                                               font-family:
                                               Segoe UI;
                                               font-size: 11pt;
                                               font-weight: bold;""")
        

def main():
    app = QApplication(sys.argv)
    main_window = MainWindow()
    main_window.show()
    main_window.raise_()
    sys.exit(app.exec_())

if __name__ == '__main__':
    main()
