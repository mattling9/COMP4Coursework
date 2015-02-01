import shutil

from PyQt4.QtGui import *
from PyQt4.QtCore import *
from PopUpMenuClass import *
from AddingRemovingData import *

class preferencesClass(QWidget):
    """ A representation of the Adding Product Interface"""
    def __init__(self):
        super().__init__()
        settings = getSettings()
        self.main_layout = QVBoxLayout()
        self.main_widget = QWidget()
        ##
        self.company_info = QGroupBox("Company Info:")
        self.company_info_layout = QVBoxLayout()
        self.buttonBox = QDialogButtonBox()
        self.buttonBox.setOrientation(Qt.Horizontal)
        self.buttonBox.setStandardButtons(QDialogButtonBox.Save |QDialogButtonBox.Cancel)
        self.buttonBox.button(QDialogButtonBox.Save).clicked.connect(self.save_clicked)


        self.image_layout = QVBoxLayout()
        self.image_widget = QWidget()
        ##
        if not settings:
            path = ""
        else:
            path = settings[0][1]
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
        self.path.setText(path)
        self.browse_button = QPushButton("Browse...")
        self.browse_button.clicked.connect(self.get_path)
        self.path_layout.addWidget(self.path)
        self.path_layout.addWidget(self.browse_button)
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

        self.invoice_email_label = QLabel("Email: ")
        self.invoice_password_label = QLabel("Password: ")
        self.invoice_email = QLineEdit()
        self.invoice_password = QLineEdit()
        self.invoice_password.setEchoMode(QLineEdit.Password)

        self.new_path_line_edit = QLineEdit()

        #INSERT THE DATA FROM FILE HERE
        if settings:
            self.company_name.setText(settings[0][2])
            self.street.setText(settings[0][3])
            self.town.setText(settings[0][4])
            self.city.setText(settings[0][5])
            self.county.setText(settings[0][6])
            self.postcode.setText(settings[0][7])
            self.phone.setText(settings[0][8])
            self.email.setText(settings[0][9])
            self.invoice_email.setText(settings[0][10])
            self.invoice_password.setText(settings[0][11])
            #INSERT THE DATA FROM FILE HERE

        self.gmail_groupbox = QGroupBox("Email Account:")
        self.gmail_layout = QGridLayout()
        self.gmail_layout.addWidget(self.invoice_email_label, 0,0)
        self.gmail_layout.addWidget(self.invoice_email, 0,1)
        self.gmail_layout.addWidget(self.invoice_password_label, 1,0)
        self.gmail_layout.addWidget(self.invoice_password, 1,1)
        self.gmail_groupbox.setLayout(self.gmail_layout)
        self.gmail_groupbox.setFixedHeight(250)
        
        
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
        self.main_widget.setLayout(self.main_layout)

        self.leftright_layout = QHBoxLayout()
        self.leftright_layout.addWidget(self.main_widget)
        self.leftright_layout.addWidget(self.gmail_groupbox)
        self.leftright_widget = QWidget()
        self.leftright_widget.setLayout(self.leftright_layout)
        
        self.main_layout2 = QVBoxLayout()
        self.main_layout2.addWidget(self.leftright_widget)
        self.main_layout2.addWidget(self.buttonBox)
        self.setLayout(self.main_layout2)
            
                
        

    def get_path(self):
        self.path_text =  QFileDialog.getOpenFileName()
        self.path.setText(self.path_text)
        self.file_name = "SystemLogo.jpg"
        self.new_path = ("./ProductImages/{0}".format(self.file_name))
        shutil.copy(self.path.text(), self.new_path)
        self.pixmap = QPixmap(self.path.text())
        self.new_path_line_edit.setText(self.new_path)
        self.scaled_image = self.pixmap.scaled(230, 230, Qt.IgnoreAspectRatio, Qt.FastTransformation)
        self.image_label.setPixmap(self.scaled_image)


    def save_clicked(self):
        encrypted_password = change_password(self.invoice_password.text(), 3)
        
        updateSettings("./ProductImages/SystemLogo.jpg",
                       self.company_name.text(),
                       self.street.text(),
                       self.town.text(),
                       self.city.text(),
                       self.county.text(),
                       self.postcode.text(),
                       self.phone.text(),
                       self.email.text(),
                       self.invoice_email.text(),
                       encrypted_password)
        print("updated")

        
        self.setWindowTitle("{0} Stock Control".format(self.company_name.text()))
        self.icon = QIcon("./ProductImages/SystemLogo.jpg")
        self.setWindowIcon(self.icon)
     


    
        
        
        
        


        
        
    
    
