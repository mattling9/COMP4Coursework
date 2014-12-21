from PyQt4.QtGui import *
from PyQt4.QtCore import *

class addEmployee(QWidget):
    """a representation of Adding an Employee"""
    def __init__(self):
        super().__init__()
        self.resize(400,300)
        addEmployee()

    def addEmployee(self):
        #Title
        self.title = QLabel("Adding New Employee")
        self.title.setAlignment(Qt.AlignCenter)
        font = QFont()
        font.setPointSize(18)
        font.setBold(True)
        self.title.setFont(font)

        #User Name
        self.user_name_widget = QWidget()
        self.user_name_layout = QHBoxLayout()
        self.user_name_label = QLabel("Username: ")
        self.user_name_label.setFixedWidth(80)
        self.user_name_output = QLineEdit("mling34")
        self.user_name_output.setReadOnly(True)
        self.user_name_layout.addWidget(self.user_name_label)
        self.user_name_layout.addWidget(self.user_name_output)
        self.user_name_widget.setLayout(self.user_name_layout)
        

        #First Name
        self.first_name_widget = QWidget()
        self.first_name_layout = QHBoxLayout()
        self.first_name_label = QLabel("First Name: ")
        self.first_name_label.setFixedWidth(80)
        self.first_name = QLineEdit()
        self.first_name.setPlaceholderText("First Name")
        self.first_name_output = QLineEdit("Matt")
        self.first_name_output.setReadOnly(True)
        self.first_name_layout.addWidget(self.first_name_label)
        self.first_name_layout.addWidget(self.first_name_output)
        self.first_name_widget.setLayout(self.first_name_layout)

        #Last Name
        self.last_name_widget = QWidget()
        self.last_name_layout = QHBoxLayout()
        self.last_name_label = QLabel("Last Name: ")
        self.last_name_label.setFixedWidth(80)
        self.last_name = QLineEdit()
        self.last_name.setPlaceholderText("Last Name")
        self.last_name_output = QLineEdit("Ling")
        self.last_name_output.setReadOnly(True)
        self.last_name_layout.addWidget(self.last_name_label)
        self.last_name_layout.addWidget(self.last_name_output)
        self.last_name_widget.setLayout(self.last_name_layout)

        #Email Address
        self.email_address_widget = QWidget()
        self.email_address_layout = QHBoxLayout()
        self.email_address_label = QLabel("Email Address: ")
        self.email_address_label.setFixedWidth(80)
        self.email_address = QLineEdit()
        self.email_address.setPlaceholderText("Email Address")
        self.email_address_output = QLineEdit("mattling9@gmail.com")
        self.email_address_output.setReadOnly(True)
        self.email_address_layout.addWidget(self.email_address_label)
        self.email_address_layout.addWidget(self.email_address_output)
        self.email_address_widget.setLayout(self.email_address_layout)

        #Submit
        self.submit_button = QPushButton("Submit")
        self.submit_button.setFixedWidth(60)

        #Add Account
        self.add_account = QPushButton("Add Account")

        #Creating Layouts and Adding Widgets
        self.main_layout = QGridLayout()
        self.main_widget = QWidget()
        self.info_box = QGroupBox()
        self.info_box.setTitle("Enter Employee Information")
        self.info_box_layout = QVBoxLayout()

        
        self.main_layout.addWidget(self.title, 0,0)
        self.info_box_layout.addWidget(self.first_name)
        self.info_box_layout.addWidget(self.last_name)
        self.info_box_layout.addWidget(self.email_address)
        self.info_box_layout.addWidget(self.submit_button)
        self.info_box.setLayout(self.info_box_layout)
        self.main_layout.addWidget(self.info_box, 1,0)
        self.main_layout.addWidget(self.user_name_widget, 2,0)
        self.main_layout.addWidget(self.first_name_widget, 3,0)
        self.main_layout.addWidget(self.last_name_widget, 4,0)
        self.main_layout.addWidget(self.email_address_widget, 5,0)
        self.main_layout.addWidget(self.add_account, 6,0)
        self.main_widget.setLayout(self.main_layout)
        self.setCentralWidget(self.main_widget)
