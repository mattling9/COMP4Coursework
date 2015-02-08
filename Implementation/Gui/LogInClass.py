import sys
from PyQt4.QtCore import *
from PyQt4.QtGui import *
from ExtendedQLabel import *
from AddingRemovingData import *


class logInClass(QWidget):
    
    def __init__(self):
        super().__init__()
        """A representation of the log in screen"""
        log_in_sucess = False
        self.return_signal = None
        self.username_label = QLabel("Username: ")
        self.username_label.setFixedWidth(80)
        self.password_label = QLabel("Password: ")
        self.password_label.setFixedWidth(80)
        self.username = QLineEdit()
        self.username.setPlaceholderText("Username:")
        self.username.setFixedWidth(200)
        self.password = QLineEdit()
        self.password.setPlaceholderText("Password")
        self.password.setEchoMode(2)
        self.password.setFixedWidth(200)

        self.font = QFont()
        self.font.setUnderline(True)
        self.forgot_password = ExtendedQLabel(" Forgot Username or Password?")
        self.forgot_password.setAlignment(Qt.AlignCenter)
        self.forgot_password.setObjectName("blue_password")
        self.forgot_password.setFont(self.font)
        self.forgot_password.setAlignment(Qt.AlignCenter)
        self.forgot_password.setToolTip("Click this link if you have forgotten your password.")
        self.forgot_password.setFixedSize(220, 40)


        
        self.enter_button = QPushButton("Sign In")
        self.enter_button.setFixedWidth(80)
        self.enter_button.setFixedHeight(27)

        self.description = QLabel("Sign In")

        self.logo = QLabel()
        self.pixmap = QPixmap(".\SystemImages\SystemLogo.png")
        self.scaled_pixmap = self.pixmap.scaled(200, 200, Qt.IgnoreAspectRatio, Qt.FastTransformation)
        self.logo.setPixmap(self.scaled_pixmap)
        self.logo.setAlignment(Qt.AlignCenter)

        #spacers


        self.spacer = QLabel()
        self.spacer.setFixedWidth(0)
        



        self.log_in_layout = QGridLayout()
        self.log_in_widget = QWidget()
        self.log_in_layout.addWidget(self.username_label, 0,0)
        self.log_in_layout.addWidget(self.username, 0,1)
        self.log_in_layout.addWidget(self.password_label, 1,0)
        self.log_in_layout.addWidget(self.password, 1,1)
        self.log_in_layout.addWidget(self.enter_button, 1,2)
        self.log_in_layout.addWidget(self.forgot_password, 2,1)
        self.log_in_widget.setLayout(self.log_in_layout)
        self.log_in_widget.setFixedWidth(400)

        self.align_layout = QHBoxLayout()
        self.align_widget = QWidget()
        self.align_layout.addWidget(self.spacer)
        self.align_layout.addWidget(self.log_in_widget)
        self.align_widget.setLayout(self.align_layout)



        self.main_widget = QWidget()
        self.main_layout = QVBoxLayout()
        self.main_layout.addWidget(self.logo)
        self.main_layout.addWidget(self.align_widget)
        self.setLayout(self.main_layout)
        

