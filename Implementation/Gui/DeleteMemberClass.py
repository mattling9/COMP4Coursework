from PyQt4.QtGui import *
from PyQt4.QtCore import *
from PopUpMenuClass import *
from AddingRemovingData import *
from ErrorMessageClass import *
import csv, re

from PyQt4.QtGui import *
from PyQt4.QtCore import *
from PopUpMenuClass import *
from AddingRemovingData import *

class deleteMemberClass(QWidget):
        """a representation of Deleting an Member"""
        def __init__(self, ButtonText):
                super().__init__()

                self.find_member_id_layout = QHBoxLayout()
                self.find_member_id_widget = QWidget()
                self.find_member_id_label = QLabel("MemberID")
                self.find_member_id_line_edit = QLineEdit()
                self.find_member_id_button = QPushButton("Find...")
                self.find_member_id_button.setFixedSize(84,27)
                self.find_member_id_button.clicked.connect(self.find_member_by_id)                                        
                self.find_member_id_layout.addWidget(self.find_member_id_label)
                self.find_member_id_layout.addWidget(self.find_member_id_line_edit)
                self.find_member_id_layout.addWidget(self.find_member_id_button)
                self.find_member_id_widget.setLayout(self.find_member_id_layout)

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
                self.find_button.setFixedSize(84,27)
                self.find_button.setObjectName("find_button")
                self.find_button.clicked.connect(self.FindPostcode)

                    
                self.postcode_tickbox.stateChanged.connect(self.change_button)
                    

                #Postcode
                self.postcode_layout = QHBoxLayout()
                self.postcode_widget = QWidget()
                self.postcode_label = QLabel("Postcode: ")
                self.postcode = QLineEdit()
                #self.postcode.setStyleSheet("QLineEdit { background-color : rgb(166,251,153);}")
                self.postcode.setPlaceholderText("Postcode: i.e(CB7 5LQ) ")
                self.postcode_layout.addWidget(self.postcode_label)
                self.postcode_layout.addWidget(self.postcode)
                self.postcode_layout.addWidget(self.find_button)
                self.postcode_widget.setLayout(self.postcode_layout)                

                #County
                self.county_layout = QHBoxLayout()
                self.county_widget = QWidget()
                self.county_label = QLabel("County: ")
                self.county = QComboBox()
                self.county_list = []
                self.get_counties()
                
                for item in self.county_list:
                        self.county.addItem(item)

                
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
                self.houseno.setFixedWidth(50)
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
                self.add_member = QPushButton(ButtonText)
                self.add_member.clicked.connect(self.CreatePopUpWindow)
                self.add_member.setFixedSize(120,27)

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

                self.spacer = QLabel()
                self.spacer.setFixedWidth(600)
                self.add_member_layout = QHBoxLayout()
                self.add_member_widget = QWidget()
                self.add_member_layout.addWidget(self.spacer)
                self.add_member_layout.addWidget(self.add_member)
                self.add_member_widget.setLayout(self.add_member_layout)


                self.main_layout = QVBoxLayout()
                self.main_widget = QWidget()
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
                self.main_layout.addWidget(self.add_member_widget)
                self.main_widget.setLayout(self.main_layout)
                self.main_widget.setDisabled(True)

                self.display_layout = QVBoxLayout()
                self.display_layout.addWidget(self.find_member_id_widget)
                self.display_layout.addWidget(self.main_widget)
                self.setLayout(self.display_layout)



        def change_button(self):
                if self.postcode_tickbox.checkState() == False:
                        self.find_button.setEnabled(False)
                else:
                        self.find_button.setEnabled(True)

        

        def CreatePopUpWindow(self):
                self.pop_up_instance = PopUpWindow("Are You Sure You Want To Remove The Member?", QDialogButtonBox.Yes, QDialogButtonBox.No)
                self.pop_up_instance.buttonBox.button(QDialogButtonBox.Yes).clicked.connect(self.clicked_yes)
                self.pop_up_instance.buttonBox.button(QDialogButtonBox.No).clicked.connect(self.clicked_no)
                
        def EditMemberSucess(self):
                self.add_member_instance = PopUpWindow("Member Sucessfully Removed!", QDialogButtonBox.Ok, QDialogButtonBox.Cancel)
                self.add_member_instance.buttonBox.button(QDialogButtonBox.Ok).clicked.connect(self.close_pop_ups)
                self.add_member_instance.buttonBox.button(QDialogButtonBox.Cancel).clicked.connect(self.close_pop_ups)

        def clicked_yes(self):
                deletingMember(self.find_member_id_line_edit.text())
                self.EditMemberSucess()


        def clicked_no(self):
                self.pop_up_instance.close()

        def close_pop_ups(self):
                self.add_member_instance.close()
                self.pop_up_instance.close()

        def FindPostcode(self):
                self.address_list = []
                with open("CumbriaPostcodes.csv", "r")as postcode_file:
                        self.postcodes = csv.reader(postcode_file)
                        for item in self.postcodes:
                                self.address_list.append(item)

                        self.postcode_input = self.postcode.text()
                        self.postcode_input = self.postcode_input.upper()
                        for count in range(0, len(self.address_list)):
                                if self.postcode_input in self.address_list[count]:
                                        self.postcode.setText(self.address_list[count][0])
                                        self.index = self.county.findText(self.address_list[count][2])
                                        self.county.setCurrentIndex(self.index)
                                        self.town.setText(self.address_list[count][1])
                                        self.validate_town

        def get_counties(self):
                with open("Counties.txt",mode="r",encoding="utf-8") as myFile:
                    for line in myFile:
                        self.county_list.append(line.rstrip("\n"))

        def find_member_by_id(self):
            with sqlite3.connect("ProductDatabase.db") as db:
                member_id = self.find_member_id_line_edit.text()
                cursor = db.cursor()
                cursor.execute("SELECT * FROM Member WHERE MemberID = ?",(member_id,))
                self.member_info = cursor.fetchall()
                db.commit()
                if self.member_info:
                    self.main_widget.setEnabled(True)
                    title_index = self.name_title.findText(self.member_info[0][1])
                    self.name_title.setCurrentIndex(title_index)
                    self.first_name.setText(self.member_info[0][2])
                    self.first_name.setReadOnly(True)
                    self.last_name.setText(self.member_info[0][3])
                    self.last_name.setReadOnly(True)
                    self.postcode.setText(self.member_info[0][9])
                    self.postcode.setReadOnly(True)
                    county_index = self.county.findText(self.member_info[0][8])
                    self.county.setCurrentIndex(county_index)
                    self.city.setText(self.member_info[0][7])
                    self.city.setReadOnly(True)
                    self.town.setText(self.member_info[0][6])
                    self.town.setReadOnly(True)
                    self.street.setText(self.member_info[0][5])
                    self.street.setReadOnly(True)
                    self.houseno.setValue(int(self.member_info[0][4]))
                    self.houseno.setReadOnly(True)
                    telephone_number = ("0" + str(self.member_info[0][10]))
                    self.telephone_number.setText(telephone_number)
                    self.telephone_number.setReadOnly(True)
                    self.email.setText(self.member_info[0][11])
                    self.email.setReadOnly(True)
                                           
                if not self.member_info:
                    self.error = ErrorMessageClass("No user found with Member ID: {0}".format(self.find_member_id_line_edit.text()))
                    self.error.setFixedSize(400,150)

                    self.main_widget.setEnabled(False)
                    self.name_title.setCurrentIndex(0)
                    self.first_name.setText("")
                    self.last_name.setText("")
                    self.postcode.setText("")
                    self.county.setCurrentIndex(0)
                    self.city.setText("")
                    self.town.setText("")
                    self.street.setText("")
                    self.houseno.setValue(0)
                    self.telephone_number.setText("")
                    self.email.setText("")
