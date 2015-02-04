import sys
from PyQt4.QtCore import *
from PyQt4.QtGui import *
from ExtendedQLabel import *


class logInClass(QWidget):
    
    def __init__(self):
        super().__init__()
        """A representation of the log in screen"""
        
        self.username_label = QLabel("Username: ")
        self.password_label = QLabel("Password: ")
        self.username = QLineEdit()
        self.password = QLineEdit()

        self.font = QFont()
        self.font.setUnderline(True)
        self.forgot_password = ExtendedQLabel(" Forgot Password?")
        self.forgot_password.setFont(self.font)
        self.forgot_password.setAlignment(Qt.AlignCenter)
        self.palette = QPalette(self.forgot_password.palette())
        self.palette.setColor(QPalette.WindowText, QColor(Qt.blue))
        self.forgot_password.setPalette(self.palette)
        self.forgot_password.setToolTip("Click this link if you have forgotten your password.")
        self.connect(self.forgot_password, SIGNAL('clicked()'), self.button_clicked)
        self.forgot_password.setFixedWidth(100)
        self.forgot_password.setFixedHeight(40)

        
        self.enter_button = QPushButton()
        self.enter_button.setFixedWidth(50)
        self.enter_button.setIcon(QIcon("./arrow.png"))
        self.enter_button.clicked.connect(self.find_account)


        self.spacer = QLabel()
        self.spacer.setFixedWidth(210)

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
        self.main_layout.addWidget(self.spacer)
        self.main_layout.addWidget(self.log_in_widget)

        self.setLayout(self.main_layout)

    def button_clicked(self):
        print("button clicked")

    def find_account(self):
        print("Account Not in Database")

