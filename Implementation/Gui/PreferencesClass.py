import shutil

from PyQt4.QtGui import *
from PyQt4.QtCore import *
from PopUpMenuClass import *
from AddingRemovingData import *

class preferencesClass(QWidget):
    """ A representation of the Adding Product Interface"""
    def __init__(self):
        super().__init__()
        self.main_layout = QVBoxLayout()
        self.main_widget = QWidget()
        ##
        self.company_info = QGroupBox("Company Info:")
        self.company_info_layout = QVBoxLayout()


        self.image_layout = QVBoxLayout()
        self.image_widget = QWidget()
        ##
        path = "./images/Logo.jpg"
        self.unscaled_pixmap = QPixmap(path)
        self.pixmap = self.unscaled_pixmap.scaled(230, 230, Qt.IgnoreAspectRatio, Qt.FastTransformation)
        self.image_label = QLabel()
        self.image_label.setPixmap(self.pixmap)
        self.logo = QGroupBox("Logo:")


        self.path_layout = QHBoxLayout()
        self.path_widget = QWidget()
        #
        self.path = QLineEdit()
        self.path.setReadOnly(True)
        self.path.setText("Input Path From File")
        self.browse_button = QPushButton("Browse...")
        self.browse_button.clicked.connect(self.get_path)
        self.upload_button = QPushButton("Upload")
        self.upload_button.clicked.connect(self.set_image)
        self.path_layout.addWidget(self.path)
        self.path_layout.addWidget(self.browse_button)
        self.path_layout.addWidget(self.upload_button)
        self.path_widget.setLayout(self.path_layout)
        self.path_widget.setFixedWidth(300)
        
        self.details_layout = QGridLayout()
        self.details_widget = QWidget()
        self.company_name_label = QLabel("Company Name: ")
        self.street_label = QLabel("Street: ")
        self.town_label = QLabel("Town: ")
        self.city_label = QLabel("City: ")
        self.county_label = QLabel("County: ")
        self.postcode_label = QLabel("Postcode: ")
        self.phone_label = QLabel("Phone Number: ")
        self.email_label = QLabel("Email Address: ")
        self.company_name = QLineEdit()
        self.street = QLineEdit()
        self.town = QLineEdit()
        self.city = QLineEdit()
        self.county = QLineEdit()
        self.postcode = QLineEdit()
        self.phone = QLineEdit()
        self.email = QLineEdit()

        #INSERT THE DATA FROM FILE HERE
        self.company_name.setText("")
        self.street.setText("")
        self.town.setText("")
        self.city.setText("")
        self.county.setText("")
        self.postcode.setText("")
        self.phone.setText("")
        self.email.setText("")
        #INSERT THE DATA FROM FILE HERE
        self.invoice_email_label = QLabel("Email: ")
        self.invoice_password_label = QLabel("Password: ")
        self.invoice_email = QLineEdit()
        self.invoice_password = QLineEdit()
        self.invoice_password.setEchoMode(QLineEdit.Password)
        
        label_list = [self.company_name_label, self.street_label, self.town_label, self.city_label, self.county_label, self.postcode_label, self.phone_label, self.email_label]
        line_edit_list = [self.company_name, self.street, self.town, self.city, self.county, self.postcode, self.phone, self.email]
        
        row = 0
        for item in label_list:
            self.details_layout.addWidget(item, row,0)
            row +=1
        row = 0
        for item in line_edit_list:
            self.details_layout.addWidget(item, row,1)
            row += 1
        self.details_widget.setLayout(self.details_layout)
        self.details_widget.setFixedWidth(300)

        self.image_layout.addWidget(self.image_label)
        self.image_layout.addWidget(self.path_widget)
        self.logo.setLayout(self.image_layout)
        self.logo.setFixedWidth(310)


        self.company_info_layout.addWidget(self.logo)
        self.company_info_layout.addWidget(self.details_widget)
        self.company_info.setLayout(self.company_info_layout)
        self.company_info.setFixedWidth(330)

        self.main_layout.addWidget(self.company_info)
        self.setLayout(self.main_layout)
            
                
        

    def get_path(self):
        self.path_text =  QFileDialog.getOpenFileName()
        self.path.setText(self.path_text)

    def set_image(self):
        self.file_name = "Logo.jpg"
        self.new_path = ("./ProductImages/{0}.jpg".format(self.file_name))
        shutil.copy(self.path.text(), self.new_path)
        self.pixmap = QPixmap(self.path.text())
        self.scaled_image = self.pixmap.scaled(230, 230, Qt.IgnoreAspectRatio, Qt.FastTransformation)
        self.image_label.setPixmap(self.scaled_image)
    
    
        
        
        
        


        
        
    
    
