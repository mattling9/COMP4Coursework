from PyQt4.QtGui import *
from PyQt4.QtCore import *
from PopUpMenuClass import *
from AddingRemovingData import *
from ErrorMessageClass import *


class deleteEmployeeClass(QWidget):
    """a representation of Adding an Employee"""
    def __init__(self,ButtonText):
        super().__init__()

        self.find_employee_id_layout = QHBoxLayout()
        self.find_employee_id_widget = QWidget()
        self.find_employee_id_label = QLabel("MemberID")
        self.find_employee_id_line_edit = QLineEdit()
        self.find_employee_id_button = QPushButton("Find...")
        self.find_employee_id_button.setFixedSize(84,27)
        self.find_employee_id_button.clicked.connect(self.find_employee_by_id)                                        
        self.find_employee_id_layout.addWidget(self.find_employee_id_label)
        self.find_employee_id_layout.addWidget(self.find_employee_id_line_edit)
        self.find_employee_id_layout.addWidget(self.find_employee_id_button)
        self.find_employee_id_widget.setLayout(self.find_employee_id_layout)
        

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
        self.email_address.setPlaceholderText("Email Address")
        self.email_address_output = QLineEdit("")
        self.email_address_output.setReadOnly(True)
        self.email_address_layout.addWidget(self.email_address_label)
        self.email_address_layout.addWidget(self.email_address_output)
        self.email_address_widget.setLayout(self.email_address_layout)
        

        #Submit
        self.submit_button = QPushButton("Submit")
        self.submit_button.clicked.connect(self.update_preview)
        self.submit_button.setFixedSize(60,27)
        self.submit_button.setObjectName("submit")

        #Add Account
        self.add_account = QPushButton(ButtonText)
        self.add_account.clicked.connect(self.CreatePopUpWindow)
        self.add_account.setShortcut(QKeySequence("CTRL+S"))
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

        self.main_widget = QWidget()
        self.main_layout.addWidget(self.info_box, 2,0)
        self.main_layout.addWidget(self.user_name_widget, 3,0)
        self.main_layout.addWidget(self.first_name_widget, 4,0)
        self.main_layout.addWidget(self.last_name_widget, 5,0)
        self.main_layout.addWidget(self.email_address_widget, 6,0)
        self.main_layout.addWidget(self.add_employee_widget, 7,0)
        self.main_widget.setLayout(self.main_layout)
        self.main_widget.setDisabled(True)

        self.display_layout = QVBoxLayout()
        self.display_layout.addWidget(self.find_employee_id_widget)
        self.display_layout.addWidget(self.main_widget)

        self.setLayout(self.display_layout)

    def update_preview(self):
        first_name = self.first_name.text().strip('"')
        last_name = self.last_name.text().strip('"')
        employee_id = self.find_employee_id_line_edit.text()
        full_name_list = [first_name[:1], last_name, employee_id]
        user_name = ""
        self.user_name = user_name.join(full_name_list)
        self.user_name_output.setText(self.user_name)
        self.first_name_output.setText(self.first_name.text())
        self.last_name_output.setText(self.last_name.text())
        self.email_address_output.setText(self.email_address.text())

    def CreatePopUpWindow(self):
        self.pop_up_instance = PopUpWindow("Are You Sure You Want To Delete The Employee?", QDialogButtonBox.Yes, QDialogButtonBox.No)
        self.pop_up_instance.buttonBox.button(QDialogButtonBox.Yes).clicked.connect(self.clicked_yes)
        self.pop_up_instance.buttonBox.button(QDialogButtonBox.No).clicked.connect(self.clicked_no)


    def AddEmployeeSucess(self):
        self.edit_employee_instance = PopUpWindow("Employee Sucessfully Deleted!", QDialogButtonBox.Ok, QDialogButtonBox.Cancel)
        self.edit_employee_instance.buttonBox.button(QDialogButtonBox.Ok).clicked.connect(self.close_pop_ups)
        self.edit_employee_instance.buttonBox.button(QDialogButtonBox.Cancel).clicked.connect(self.close_pop_ups)

    def clicked_yes(self):
        deletingEmployee(self.find_employee_id_line_edit.text())
        self.AddEmployeeSucess()


    def clicked_no(self):
        self.pop_up_instance.close()

    def close_pop_ups(self):
        self.edit_employee_instance.close()
        self.pop_up_instance.close()
        self.clear_fields()

    def find_employee_by_id(self):
        with sqlite3.connect("ProductDatabase.db") as db:
            employee_id = self.find_employee_id_line_edit.text()
            cursor = db.cursor()
            cursor.execute("SELECT * FROM Employee WHERE EmployeeID = ?",(employee_id,))
            employee_info = cursor.fetchall()
            db.commit()
            if employee_info[0][0] == 1:
                self.error = ErrorMessageClass("You are not authorised to delete the admin account")
                self.error.setFixedSize(400,150)
            elif employee_info:
                self.main_widget.setEnabled(True)
                self.first_name.setText(employee_info[0][2])
                self.first_name.setReadOnly(True)
                self.last_name.setText(employee_info[0][3])
                self.last_name.setReadOnly(True)
                self.email_address.setText(employee_info[0][4])
                self.email_address.setReadOnly(True)
                self.user_name_output.setText(employee_info[0][1])
                self.first_name_output.setText(self.first_name.text())
                self.last_name_output.setText(self.last_name.text())
                self.email_address_output.setText(self.email_address.text())
                                       
            if not employee_info:
                self.error = ErrorMessageClass("No user found with Member ID: {0}".format(self.find_employee_id_line_edit.text()))
                self.error.setFixedSize(400,150)
                self.clear_fields()

    def clear_fields(self):
        self.find_employee_id_line_edit.setText("")
        self.main_widget.setDisabled(True)
        self.first_name.setText("")
        self.last_name.setText("")
        self.email_address.setText("")
        self.user_name_output.setText("")
        self.first_name_output.setText("")
        self.last_name_output.setText("")
        self.email_address_output.setText("")
