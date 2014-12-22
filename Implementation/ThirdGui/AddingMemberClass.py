from PyQt4.QtGui import *
from PyQt4.QtCore import *

class addMemberClass(QWidget):
        """a representation of Adding an Member"""
        def __init__(self):
                super().__init__()
                self.resize(400,300)
                self.addMember()

        def addMember(self):

                #Title
                self.title = QLabel("Adding New Member")
                self.title.setAlignment(Qt.AlignCenter)
                font = QFont()
                font.setPointSize(18)
                font.setBold(True)
                self.title.setFont(font)
                self.title.setFixedHeight(30)

                #Name_title
                self.name_title = QComboBox()
                self.name_title.addItem("Mr.")
                self.name_title.addItem("Mrs.")
                self.name_title.addItem("Ms.")
                self.name_title.addItem("Miss.")
                self.name_title.addItem("Dr.")
                self.name_title.addItem("Prof.")
                self.name_title.addItem("Sgt.")

                #First name
                self.first_name = QLineEdit()
                self.first_name.setPlaceholderText("First Name: ")
                    
                #Last Name
                self.last_name = QLineEdit()
                self.last_name.setPlaceholderText("Last Name: ")
                    
                #Postcode Tickbox
                self.postcode_tickbox = QCheckBox("Do You Live in Cumbria?")

                #Find Button
                self.find_button = QPushButton("Find...")
                self.find_button.setEnabled(False)

                    
                self.postcode_tickbox.stateChanged.connect(self.change_button)
                    

                #Postcode
                self.postcode_layout = QHBoxLayout()
                self.postcode_widget = QWidget()
                self.postcode_label = QLabel("Postcode: ")
                self.postcode = QLineEdit()
                self.postcode.setPlaceholderText("Postcode: i.e(CB7 5LQ) ")
                self.postcode_layout.addWidget(self.postcode_label)
                self.postcode_layout.addWidget(self.postcode)
                self.postcode_layout.addWidget(self.find_button)
                self.postcode_widget.setLayout(self.postcode_layout)

                #County
                self.county_layout = QHBoxLayout()
                self.county_widget = QWidget()
                self.county_label = QLabel("County: ")
                self.county = QLineEdit()
                self.county.setPlaceholderText("County: ")
                self.county_layout.addWidget(self.county_label)
                self.county_layout.addWidget(self.county)
                self.county_widget.setLayout(self.county_layout)

                #City
                self.city_layout = QHBoxLayout()
                self.city_widget = QWidget()
                self.city_label = QLabel("City: ")
                self.city = QLineEdit()
                self.city.setPlaceholderText("City: ")
                self.city_layout.addWidget(self.city_label)
                self.city_layout.addWidget(self.city)
                self.city_widget.setLayout(self.city_layout)

                    #Town
                self.town_layout = QHBoxLayout()
                self.town_widget = QWidget()
                self.town_label = QLabel("Town: ")
                self.town = QLineEdit()
                self.town.setPlaceholderText("Town: ")
                self.town_layout.addWidget(self.town_label)
                self.town_layout.addWidget(self.town)
                self.town_widget.setLayout(self.town_layout)

                #Street
                self.street_layout = QHBoxLayout()
                self.street_widget = QWidget()
                self.street_label = QLabel("Street: ")
                self.street = QLineEdit()
                self.street.setPlaceholderText("Street: ")
                self.street_layout.addWidget(self.street_label)
                self.street_layout.addWidget(self.street)
                self.street_widget.setLayout(self.street_layout)

                    #House No
                self.houseno_layout = QHBoxLayout()
                self.houseno_widget = QWidget()
                self.houseno_label = QLabel("House No:")
                self.houseno = QSpinBox()
                self.houseno.setRange(1,200)
                self.houseno_layout.addWidget(self.houseno_label)
                self.houseno_layout.addWidget(self.houseno)
                self.houseno_widget.setLayout(self.houseno_layout)

                    #Telephone Number
                self.telephone_number_layout = QHBoxLayout()
                self.telephone_number_widget = QWidget()
                self.telephone_number_label = QLabel("Telephone Number: ")
                self.telephone_number = QLineEdit()
                self.telephone_number.setPlaceholderText("Telephone Number:")
                self.telephone_number_layout.addWidget(self.telephone_number_label)
                self.telephone_number_layout.addWidget(self.telephone_number)
                self.telephone_number_widget.setLayout(self.telephone_number_layout)

                    #Email
                self.email_layout = QHBoxLayout()
                self.email_widget = QWidget()
                self.email_label = QLabel("Email: ")
                self.email = QLineEdit()
                self.email.setPlaceholderText("Email: ")
                self.email_layout.addWidget(self.email_label)
                self.email_layout.addWidget(self.email)
                self.email_widget.setLayout(self.email_layout)

                    #Add Member Button
                self.add_member = QPushButton("Add Member")

                    #Group Box
                self.group_box = QGroupBox("Enter Member Information")
                self.group_box_layout = QVBoxLayout()



                    #Creating Layouts
                self.name_layout = QHBoxLayout()
                self.name_widget = QWidget()
                self.name_layout.addWidget(self.name_title)
                self.name_layout.addWidget(self.first_name)
                self.name_layout.addWidget(self.last_name)
                self.name_widget.setLayout(self.name_layout)


                self.main_layout = QVBoxLayout()
                self.main_widget = QWidget()
                self.main_layout.addWidget(self.title)
                self.group_box_layout.addWidget(self.name_widget)
                self.group_box_layout.addWidget(self.postcode_tickbox)
                self.group_box_layout.addWidget(self.postcode_widget)
                self.group_box_layout.addWidget(self.county_widget)
                self.group_box_layout.addWidget(self.city_widget)
                self.group_box_layout.addWidget(self.town_widget)
                self.group_box_layout.addWidget(self.street_widget)
                self.group_box_layout.addWidget(self.houseno_widget)
                self.group_box_layout.addWidget(self.telephone_number_widget)
                self.group_box_layout.addWidget(self.email_widget)
                self.group_box.setLayout(self.group_box_layout)
                self.main_layout.addWidget(self.group_box)
                self.main_layout.addWidget(self.add_member)
                self.setLayout(self.main_layout)


        def change_button(self):
                if self.postcode_tickbox.checkState() == False:
                        self.find_button.setEnabled(False)
                else:
                        self.find_button.setEnabled(True)


    
