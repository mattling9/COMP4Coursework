from PyQt4.QtGui import *
from PyQt4.QtCore import *
from PopUpMenuClass import *
from AddingRemovingData import *


class editEmployeeClass(QWidget):
    """a representation of Adding an Employee"""
    def __init__(self,ButtonText):
        super().__init__()

        self.find_employee_id_layout = QHBoxLayout()
        self.find_employee_id_widget = QWidget()
        self.find_employee_id_label = QLabel("MemberID")
        self.find_employee_id_line_edit = QLineEdit()
        self.find_employee_id_button = QPushButton("Find...")
        self.find_employee_id_button.clicked.connect(self.find_employee_by_id)                                        
        self.find_employee_id_layout.addWidget(self.find_employee_id_label)
        self.find_employee_id_layout.addWidget(self.find_employee_id_line_edit)
        self.find_employee_id_layout.addWidget(self.find_employee_id_button)
        self.find_employee_id_widget.setLayout(self.find_employee_id_layout)
        self.find_employee_id_widget.setFixedHeight(40)
        

        #User Name
        self.user_name_widget = QWidget()
        self.user_name_layout = QHBoxLayout()
        self.user_name_label = QLabel("Username: ")
        self.user_name_label.setFixedWidth(80)
        self.user_name_output = QLineEdit("")
        self.user_name_output.setReadOnly(True)
        self.user_name_layout.addWidget(self.user_name_label)
        self.user_name_layout.addWidget(self.user_name_output)
        self.user_name_widget.setLayout(self.user_name_layout)
        

        #First Name
        self.first_name_widget = QWidget()
        self.first_name_layout = QHBoxLayout()
        self.first_name_label = QLabel("First Name: ")
        self.first_name_label.setFixedWidth(80)
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
        self.last_name_label.setFixedWidth(80)
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
        self.email_address_label.setFixedWidth(80)
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
        self.submit_button.setFixedWidth(60)

        #Add Account
        self.add_account = QPushButton(ButtonText)
        self.add_account.clicked.connect(self.CreatePopUpWindow)

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
        self.main_layout.addWidget(self.add_account, 7,0)
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
        self.pop_up_instance = PopUpWindow("Beacon Vets Adding Employee", 300, 100)
        self.icon = QIcon(QPixmap("./images/Logo.jpg"))
        self.pop_up_instance.setWindowIcon(self.icon)
        self.label = QLabel("Are You Sure You Want To Edit The Employee?")
        self.label.setAlignment(Qt.AlignCenter)
        self.buttonBox = QDialogButtonBox()
        self.buttonBox.setOrientation(Qt.Horizontal)
        self.buttonBox.setStandardButtons(QDialogButtonBox.Yes | QDialogButtonBox.No)
        self.buttonBox.button(QDialogButtonBox.Yes).clicked.connect(self.clicked_yes)
        self.buttonBox.button(QDialogButtonBox.No).clicked.connect(self.clicked_no)
        self.pop_up_layout = QVBoxLayout()
        self.pop_up_widget = QWidget()
        self.pop_up_layout.addWidget(self.label)
        self.pop_up_layout.addWidget(self.buttonBox)
        self.pop_up_widget.setLayout(self.pop_up_layout)
        self.pop_up_instance.setCentralWidget(self.pop_up_widget)
        self.pop_up_instance.move(750,500)
        self.pop_up_instance.show()
        self.pop_up_instance.raise_()

    def AddEmployeeSucess(self):
        self.edit_employee_instance = PopUpWindow("Beacon Vets Adding Member", 300, 100)
        self.icon = QIcon(QPixmap("./images/Logo.jpg"))
        self.edit_employee_instance.setWindowIcon(self.icon)
        self.label = QLabel("Employee Sucessfully Edited!")
        self.label.setAlignment(Qt.AlignCenter)
        self.buttonBox = QDialogButtonBox()
        self.buttonBox.setOrientation(Qt.Horizontal)
        self.buttonBox.setStandardButtons(QDialogButtonBox.Ok | QDialogButtonBox.Cancel)
        self.buttonBox.button(QDialogButtonBox.Ok).clicked.connect(self.close_pop_ups)
        self.buttonBox.button(QDialogButtonBox.Cancel).clicked.connect(self.close_pop_ups)
        self.pop_up_layout = QVBoxLayout()
        self.pop_up_widget = QWidget()
        self.pop_up_layout.addWidget(self.label)
        self.pop_up_layout.addWidget(self.buttonBox)
        self.pop_up_widget.setLayout(self.pop_up_layout)
        self.edit_employee_instance.setCentralWidget(self.pop_up_widget)
        self.edit_employee_instance.move(800,450)
        self.edit_employee_instance.show()
        self.edit_employee_instance.raise_()

    def clicked_yes(self):
        editingEmployee(self.find_employee_id_line_edit.text(),
                        self.user_name_output.text(),
                        self.first_name_output.text(),
                        self.last_name_output.text(),
                        self.email_address_output.text())
        self.AddEmployeeSucess()


    def clicked_no(self):
        self.pop_up_instance.close()

    def close_pop_ups(self):
        self.edit_employee_instance.close()
        self.pop_up_instance.close()

    def find_employee_by_id(self):
        with sqlite3.connect("ProductDatabase.db") as db:
            employee_id = self.find_employee_id_line_edit.text()
            cursor = db.cursor()
            cursor.execute("SELECT * FROM Employee WHERE EmployeeID = ?",(employee_id,))
            employee_info = cursor.fetchall()
            db.commit()
            if employee_info:
                self.main_widget.setEnabled(True)
                self.first_name.setText(employee_info[0][2])
                self.last_name.setText(employee_info[0][3])
                self.email_address.setText(employee_info[0][4])
                self.user_name_output.setText(employee_info[0][1])
                self.first_name_output.setText(self.first_name.text())
                self.last_name_output.setText(self.last_name.text())
                self.email_address_output.setText(self.email_address.text())
                                       
            if not employee_info:
                print("NOT IN DATABASE")
                self.main_widget.setDisabled(True)
                self.first_name.setText("")
                self.last_name.setTex("")
                self.email_address.setText("")
                self.username_output.setText("")
                self.first_name_output.setText("")
                self.last_name_ouput.setText("")
                self.email_address_output("")
