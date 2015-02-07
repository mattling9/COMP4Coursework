from PyQt4.QtGui import *
from PyQt4.QtCore import *
from PopUpMenuClass import *



class PasswordResetClass(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle('Menu Button Test')
        self.setFixedSize(600, 400)

        self.forgot_password = QLabel("Forgot Your Password?")
        self.forgot_password.setObjectName('forgot_password')
        self.forgot_password.setAlignment(Qt.AlignCenter)
        
        self.description = QLabel("Enter your email address and we will email you your account details.")
        #self.description.setAlignment(Qt.AlignCenter)
        
        self.email_address = QLineEdit()
        self.email_address.setPlaceholderText("Email address")
        self.email_address.setFixedWidth(550)


        self.button_layout = QHBoxLayout()
        self.button_widget = QWidget()
        self.spacer = QWidget()
        self.spacer.setFixedWidth(450)
        self.button = QPushButton("Next")
        self.button.setFixedWidth(80)
        self.button.setFixedHeight(27)
        self.button_layout.addWidget(self.spacer)
        self.button_layout.addWidget(self.button)
        self.button_widget.setLayout(self.button_layout)

        
        self.main_layout = QVBoxLayout()

        self.vertical_spacer = QWidget()
        self.vertical_spacer.setFixedHeight(200)
        
        self.main_layout.addWidget(self.forgot_password)
        self.main_layout.addWidget(self.description)
        self.main_layout.addWidget(self.email_address)
        self.main_layout.addWidget(self.button_widget)
        self.main_layout.addWidget(self.vertical_spacer)
        self.setLayout(self.main_layout)
