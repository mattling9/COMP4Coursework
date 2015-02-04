import sys
from PyQt4.QtCore import *
from PyQt4.QtGui import *
from PushButtonClass import *

class MainWindow(QMainWindow):
    
    def __init__(self):
        super().__init__()
        self.setWindowTitle('Menu Button Test')
        self.setFixedSize(600, 400)

        self.bold = QFont()
        self.bold.setBold(True)
        self.bold.setPointSize(16)

        self.forgot_password = QLabel("Forgot Your Password?")
        self.forgot_password.setFont(self.bold)
        self.forgot_password.setAlignment(Qt.AlignCenter)
        
        self.description = QLabel("Enter your email address to reset your password.")
        #self.description.setAlignment(Qt.AlignCenter)
        
        self.email_address = QLineEdit()
        self.email_address.setPlaceholderText("Email address")


        self.button_layout = QHBoxLayout()
        self.button_widget = QWidget()
        self.spacer = QWidget()
        self.spacer.setFixedWidth(450)
        self.button = QPushButton("Next")
        self.button.setFixedWidth(80)
        self.button_layout.addWidget(self.spacer)
        self.button_layout.addWidget(self.button)
        self.button_widget.setLayout(self.button_layout)

        
        self.main_layout = QVBoxLayout()
        self.main_widget = QWidget()

        self.vertical_spacer = QWidget()
        self.vertical_spacer.setFixedHeight(200)
        
        self.main_layout.addWidget(self.forgot_password)
        self.main_layout.addWidget(self.description)
        self.main_layout.addWidget(self.email_address)
        self.main_layout.addWidget(self.button_widget)
        self.main_layout.addWidget(self.vertical_spacer)
        self.main_widget.setLayout(self.main_layout)
        self.setCentralWidget(self.main_widget)
    
        
        
        
        
def main():
    app = QApplication(sys.argv)
    main_window = MainWindow()
    main_window.show()
    main_window.raise_()
    sys.exit(app.exec_())


if __name__ == '__main__':
    main()
