from PyQt4.QtGui import *
from PyQt4.QtCore import *
from PopUpMenuClass import *



class ChangePasswordClass(QWidget):
    def __init__(self, LabelText, signal):
        super().__init__()

        self.bold = QFont()
        self.bold.setBold(True)
        self.bold.setPointSize(16)

        self.forgot_password = QLabel("Change Your Password")
        self.forgot_password.setObjectName("forgot_password")
        self.forgot_password.setFont(self.bold)
        self.forgot_password.setAlignment(Qt.AlignCenter)
        
        self.description = QLabel(LabelText)
        #self.description.setAlignment(Qt.AlignCenter)
        
        self.password1 = QLineEdit()
        self.password1.setEchoMode(2)
        self.password1.setPlaceholderText("Password")
        self.password2 = QLineEdit()
        self.password2.setEchoMode(2)
        self.password2.setPlaceholderText("Repeat password")

        self.code_layout = QHBoxLayout()
        self.code_widget = QWidget()
        self.code_label = QLabel("4 Digit Code: ")
        self.code = QLineEdit()
        self.code_layout.addWidget(self.code_label)
        self.code_layout.addWidget(self.code)
        self.code_widget.setLayout(self.code_layout)

        self.button_layout = QHBoxLayout()
        self.button_widget = QWidget()
        self.spacer = QWidget()
        self.spacer.setFixedWidth(450)
        self.button = QPushButton("Next")
        self.button.setFixedSize(84, 27)
        self.button_layout.addWidget(self.spacer)
        self.button_layout.addWidget(self.button)
        self.button_widget.setLayout(self.button_layout)

        
        self.main_layout = QVBoxLayout()

        self.vertical_spacer = QWidget()
        self.vertical_spacer.setFixedHeight(200)
        
        self.main_layout.addWidget(self.forgot_password)
        self.main_layout.addWidget(self.description)
        self.main_layout.addWidget(self.password1)
        self.main_layout.addWidget(self.password2)
        if signal == 1:
            self.main_layout.addWidget(self.code_widget)
        self.main_layout.addWidget(self.button_widget)
        self.main_layout.addWidget(self.vertical_spacer)
        self.setLayout(self.main_layout)
            

        
        
