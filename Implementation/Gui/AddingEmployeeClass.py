import re
from PyQt4.QtGui import *
from PyQt4.QtCore import *
from PopUpMenuClass import *
from AddingRemovingData import *


class addEmployeeClass(QWidget):
    """a representation of Adding an Employee"""
    def __init__(self,ButtonText):
        super().__init__()
        self.resize(400,300)

        #User Name
        self.user_name_widget = QWidget()
        self.user_name_layout = QHBoxLayout()
        self.user_name_label = QLabel("Username: ")
        self.user_name_label.setFixedWidth(100)
        self.user_name_output = QLineEdit("")
        self.user_name_output.setReadOnly(True)
        self.user_name_layout.addWidget(self.user_name_label)
        self.user_name_layout.addWidget(self.user_name_output)
        self.user_name_widget.setLayout(self.user_name_layout)
        

        #First Name
        self.first_name_widget = QWidget()
        self.first_name_layout = QHBoxLayout()
        self.first_name_label = QLabel("First Name: ")
        self.first_name_label.setFixedWidth(100)
        self.first_name = QLineEdit("")
        self.first_name.textChanged.connect(self.validate_first_name)
        self.first_name.setPlaceholderText("First Name")
        self.first_name_output = QLineEdit("")
        self.first_name_output.setReadOnly(True)
        self.first_name_layout.addWidget(self.first_name_label)
        self.first_name_layout.addWidget(self.first_name_output)
        self.first_name_widget.setLayout(self.first_name_layout)

        #Last Name
        self.last_name_widget = QWidget()
        self.last_name_layout = QHBoxLayout()
        self.last_name_label = QLabel("Last Name: ")
        self.last_name_label.setFixedWidth(100)
        self.last_name = QLineEdit("")
        self.last_name.textChanged.connect(self.validate_last_name)
        self.last_name.setPlaceholderText("Last Name")
        self.last_name_output = QLineEdit("")
        self.last_name_output.setReadOnly(True)
        self.last_name_layout.addWidget(self.last_name_label)
        self.last_name_layout.addWidget(self.last_name_output)
        self.last_name_widget.setLayout(self.last_name_layout)

        #Email Address
        self.email_address_widget = QWidget()
        self.email_address_layout = QHBoxLayout()
        self.email_address_label = QLabel("Email Address: ")
        self.email_address_label.setFixedWidth(100)
        self.email_address = QLineEdit()
        self.email_address.textChanged.connect(self.validate_email)
        self.email_address.setPlaceholderText("Email Address")
        self.email_address_output = QLineEdit("")
        self.email_address_output.setReadOnly(True)
        self.email_address_layout.addWidget(self.email_address_label)
        self.email_address_layout.addWidget(self.email_address_output)
        self.email_address_widget.setLayout(self.email_address_layout)
        

        #Submit
        self.submit_button = QPushButton("Submit")
        self.submit_button.setObjectName('submit')
        self.submit_button.clicked.connect(self.update_preview)
        self.submit_button.setFixedSize(60,27)

        #Add Account
        self.add_account = QPushButton(ButtonText)
        self.add_account.clicked.connect(self.CreatePopUpWindow)
        self.add_account.setFixedSize(120, 27)

        self.spacer = QLabel()
        self.spacer.setFixedWidth(600)
        self.add_employee_layout = QHBoxLayout()
        self.add_employee_widget = QWidget()
        self.add_employee_layout.addWidget(self.spacer)
        self.add_employee_layout.addWidget(self.add_account)
        self.add_employee_widget.setLayout(self.add_employee_layout)
        #Creating Layouts and Adding Widgets
        self.main_layout = QGridLayout()
        self.main_widget = QWidget()
        self.info_box = QGroupBox()
        self.info_box.setTitle("Enter Employee Information")
        self.info_box_layout = QVBoxLayout()

        
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
        self.main_layout.addWidget(self.add_employee_widget, 6,0)
        self.setLayout(self.main_layout)

    def update_preview(self):
        first_name = self.first_name.text().strip('"')
        last_name = self.last_name.text().strip('"')
        employee_id = get_new_employee_id()
        full_name_list = [first_name[:1], last_name, str(employee_id)]
        user_name = ""
        self.user_name = user_name.join(full_name_list)
        self.user_name_output.setText(self.user_name)
        self.first_name_output.setText(self.first_name.text())
        self.last_name_output.setText(self.last_name.text())
        self.email_address_output.setText(self.email_address.text())

    def CreatePopUpWindow(self):
        self.pop_up_instance = PopUpWindow("Are You Sure You Want To Add The Employee?", QDialogButtonBox.Yes, QDialogButtonBox.No)
        self.pop_up_instance.buttonBox.button(QDialogButtonBox.Yes).clicked.connect(self.clicked_yes)
        self.pop_up_instance.buttonBox.button(QDialogButtonBox.No).clicked.connect(self.clicked_no)

    def AddEmployeeSucess(self):
        self.add_employee_instance = PopUpWindow("Employee Sucessfully Added! \n \n You can now log in with the following log in details: \n \n Username: {0} \n Password: password".format(self.user_name_output.text()), QDialogButtonBox.Ok, QDialogButtonBox.Cancel)
        self.add_employee_instance.buttonBox.button(QDialogButtonBox.Ok).clicked.connect(self.close_pop_ups)
        self.add_employee_instance.buttonBox.button(QDialogButtonBox.Cancel).clicked.connect(self.close_pop_ups)
        self.add_employee_instance.setFixedSize(400,300)

    def clicked_yes(self):
        self.password = change_password("password", 3)
        addingEmployee(self.user_name,
                       self.first_name.text(),
                       self.last_name.text(),
                       self.email_address.text(),
                       self.password)
        self.AddEmployeeSucess()


    def clicked_no(self):
        self.pop_up_instance.close()

    def close_pop_ups(self):
        self.add_employee_instance.close()
        self.pop_up_instance.close()

    #VALDIATION
    def validate_first_name(self):
        self.FirstName = self.first_name.text()
        self.pattern = re.compile("[A-Z]")
        self.first_name.setText(self.FirstName.capitalize())
        valid = self.pattern.match(self.FirstName.upper())
        if len(self.FirstName) > 1 and len(self.FirstName) < 18:
            if valid:
                self.first_name.setStyleSheet("""QLineEdit {
                                            border-style: solid;
                                            border-width: 1.5px;
                                            border-color : rgb(0,240,0);}"""                )
        else:
            self.first_name.setStyleSheet(          """QLineEdit {
                                            border-style: solid;
                                            border-width: 1px;
                                            border-color : rgb(200,200,200}""")

    def validate_last_name(self):
        self.LastName = self.last_name.text()
        self.pattern = re.compile("[A-Z]")
        self.last_name.setText(self.LastName.capitalize())
        valid = self.pattern.match(self.LastName.upper())
        if len(self.LastName) > 1 and len(self.LastName) < 18:
            if valid:
                self.last_name.setStyleSheet("""QLineEdit {
                                            border-style: solid;
                                            border-width: 1.5px;
                                            border-color : rgb(0,240,0);}"""                )
        else:
            self.last_name.setStyleSheet(          """QLineEdit {
                                            border-style: solid;
                                            border-width: 1px;
                                            border-color : rgb(200,200,200}""")

    def validate_email(self):
                self.Email = self.email_address.text()
                self.pattern = re.compile("[0-9A-Z]{2,18}[\@][0-9A-Z]{3,18}[\.][A-Z]{2,18}")
                valid = self.pattern.match(self.Email.upper())
                if valid:
                        self.email_address.setStyleSheet("""QLineEdit {
                                            border-style: solid;
                                            border-width: 1.5px;
                                            border-color : rgb(0,240,0);}"""                )
                else:
                        self.email_address.setStyleSheet(          """QLineEdit {
                                            border-style: solid;
                                            border-width: 1px;
                                            border-color : rgb(200,200,200}""")
