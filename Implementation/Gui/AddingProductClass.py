import shutil, re

from PyQt4.QtGui import *
from PyQt4.QtCore import *
from PopUpMenuClass import *
from AddingRemovingData import *

class addProductClass(QWidget):
    """ A representation of the Adding Product Interface"""
    def __init__(self, ButtonText):
        super().__init__()
        self.resize(10,20)
        #Adding group box
        self.product_info_group_box = QGroupBox()
        self.product_info_group_box.setTitle("Enter Product Information:")
        
        

        #creating the buttons
    
        
        #Price
        self.pound = QLabel("Price: £")
        self.price_button = QLineEdit("")
        self.validator = QDoubleValidator()
        self.price_button.setValidator(self.validator)
        self.price_button.textChanged.connect(self.validate_price)
        self.price_button.setPlaceholderText("Price: £0.00")
        self.price_widget = QWidget()
        self.price_layout = QHBoxLayout()
        self.price_layout.addWidget(self.pound)
        self.price_layout.addWidget(self.price_button)
        self.price_widget.setLayout(self.price_layout)
        

        #Size
        self.size_layout = QHBoxLayout()
        self.size_widget = QWidget()
        self.size_integer = QLineEdit()
        self.validator = QIntValidator()
        self.size_integer.setValidator(self.validator)
        self.size_integer.textChanged.connect(self.validate_size)
        self.size_integer.setPlaceholderText("Size: (750)")
        self.size_button = QComboBox()
        self.size_button.addItem("Kg.")
        self.size_button.addItem("g.")
        self.size_button.addItem("L.")
        self.size_button.addItem("ml.")
        self.size_layout.addWidget(self.size_integer)
        self.size_layout.addWidget(self.size_button)
        self.size_widget.setLayout(self.size_layout)

        #Category
        self.category_layout = QHBoxLayout()
        self.category_label = QLabel("Category")
        self.category1_button = QComboBox()
        self.category2_button = QComboBox()
        self.category1_button.addItem("Dog")
        self.category1_button.addItem("Cat")
        self.category1_button.addItem("Fish")
        self.category1_button.addItem("Small Pet")
        self.category1_button.addItem("Bird")
        self.category1_button.addItem("Reptile")
        self.category1_button.addItem("Equine")
        self.category2_button.addItem("Food")
        self.category2_button.addItem("Health Care")
        self.category_layout.addWidget(self.category_label)
        self.category_layout.addWidget(self.category1_button)
        self.category_layout.addWidget(self.category2_button)
        self.category_widget = QWidget()
        self.category_widget.setLayout(self.category_layout)

        #Location 1
        self.location1 = QLineEdit()
        self.location1.setPlaceholderText("Stock In Location 1...")
        self.validator = QIntValidator()
        self.location1.setValidator(self.validator)
        self.location1.textChanged.connect(self.validate_stock1)

        #Location 2
        self.location2 = QLineEdit()
        self.location2.setPlaceholderText("Stock In Location 2...")
        self.validator = QIntValidator()
        self.location2.setValidator(self.validator)
        self.location2.textChanged.connect(self.validate_stock2)

        #Done
        self.done = QPushButton(ButtonText)
        self.done.clicked.connect(self.CreatePopUpWindow)

        #Product Name
        self.product_name = QLineEdit()
        self.product_name.textChanged.connect(self.validate_name)
        product_name_info = self.product_name.text()
        self.product_name.setPlaceholderText("Product Name...")
        self.product_name.setFixedWidth(300)

        #Image
        self.image = QLabel()
        self.image_pixmap = QPixmap(".\images\Default.png")
        self.scaled_image = self.image_pixmap.scaled(300, 300, Qt.IgnoreAspectRatio, Qt.FastTransformation)
        self.image.setPixmap(self.scaled_image)
        

        #Browse
        path = "./images/Default.png"
        
        self.browse_layout = QHBoxLayout()
        self.browse_widget = QWidget()
        self.browse = QPushButton("Browse...")
        self.browse.clicked.connect(self.get_image_path)
        
        self.upload = QPushButton("Upload")
        self.upload.clicked.connect(self.update_image)
        
        self.path = QLineEdit("")
        self.path.setReadOnly(True)
        self.browse_layout.addWidget(self.path)
        self.browse_layout.addWidget(self.browse)
        self.browse_layout.addWidget(self.upload)
        self.browse_widget.setLayout(self.browse_layout)
        self.browse_widget.setFixedWidth(300)
        
        
        #Creating Layouts and Adding Widgets

        self.input_layout = QVBoxLayout()
        self.input_widget = QWidget()
        self.input_layout.addWidget(self.price_widget)
        self.input_layout.addWidget(self.size_widget)
        self.input_layout.addWidget(self.category_widget)
        self.input_layout.addWidget(self.location1)
        self.input_layout.addWidget(self.location2)
        self.input_widget.setLayout(self.input_layout)
        self.product_info_group_box.setLayout(self.input_layout)
        self.left_widget = QWidget()
        self.left_layout = QVBoxLayout()
        self.left_layout.addWidget(self.product_info_group_box)
        self.left_widget.setLayout(self.left_layout)

        self.image_layout = QVBoxLayout()
        self.image_widget = QWidget()
        self.image_layout.addWidget(self.product_name)
        self.image_layout.addWidget(self.image)
        self.image_widget.setLayout(self.image_layout)

        self.right_layout = QVBoxLayout()
        self.right_widget = QWidget()
        self.right_layout.addWidget(self.image_widget)
        self.right_layout.addWidget(self.browse_widget)
        self.right_widget.setLayout(self.right_layout)

        #main layout

        self.leftright_layout = QHBoxLayout()
        self.leftright_layout.addWidget(self.left_widget)
        self.leftright_layout.addWidget(self.right_widget)

        self.leftright_widget = QWidget()
        self.leftright_widget.setLayout(self.leftright_layout)

        self.main_layout = QVBoxLayout()
        self.main_layout.addWidget(self.leftright_widget)
        self.main_layout.addWidget(self.done)
        self.main_widget = QWidget()
        self.main_widget.setLayout(self.main_layout)

        self.total_layout = QVBoxLayout()
        self.total_layout.addWidget(self.main_widget)
        self.setLayout(self.total_layout)
        
    def CreatePopUpWindow(self):
        self.pop_up_instance = PopUpWindow("Beacon Vets Adding Product", 300, 100)
        self.icon = QIcon(QPixmap("./images/Logo.jpg"))
        self.pop_up_instance.setWindowIcon(self.icon)
        self.label = QLabel("Are you sure you want to Add The Product?")
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

    def AddProductSucess(self):
        self.add_product_instance = PopUpWindow("Beacon Vets Adding Product", 300, 100)
        self.icon = QIcon(QPixmap("./images/Logo.jpg"))
        self.add_product_instance.setWindowIcon(self.icon)
        self.label = QLabel("Product Sucessfully Added!")
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
        self.add_product_instance.setCentralWidget(self.pop_up_widget)
        self.add_product_instance.move(800,450)
        self.add_product_instance.show()
        self.add_product_instance.raise_()

    def get_image_path(self):
        path =  QFileDialog.getOpenFileName()
        self.path.setText(path)
        

    def update_image(self):
        path = self.path.text()
        new_path = "./ProductImages/01.jpg"
        shutil.copy(path, new_path)
        self.pixmap = QPixmap(path)
        self.scaled_image = self.pixmap.scaled(300, 300, Qt.IgnoreAspectRatio, Qt.FastTransformation)
        self.image.setPixmap(self.scaled_image)

    def clicked_yes(self):
        self.size_list = [self.size_integer.text(), self.size_button.currentText()]
        self.temp = ""
        self.size_string = self.temp.join(self.size_list)
        addingProduct(self.product_name.text(), self.size_string, self.price_button.text(), self.location1.text(), self.location2.text())
        self.AddProductSucess()
        
        


    def clicked_no(self):
        self.pop_up_instance.close()

    def close_pop_ups(self):
        self.add_product_instance.close()
        self.pop_up_instance.close()


    #VALIDATION
    def validate_name(self):
        valid = False
        self.name = self.product_name.text()
        self.product_name.setText(self.name.capitalize())
        if len(self.name) > 3 and len(self.name) < 32:
            valid = True
        
        if valid:
            self.product_name.setStyleSheet("QLineEdit { background-color : rgb(166,251,153);}")
        else:
            self.product_name.setStyleSheet("QLineEdit { background-color : rgb(255,255,255);}")


    def validate_price(self):
        valid = False
        self.pattern = re.compile("[0-9]{1,3}.[0-9]{2}")
        self.price = self.price_button.text()
        self.price_button.setText(self.price)
        valid =  self.pattern.match(self.price)
        if valid:
                self.price_button.setStyleSheet("QLineEdit { background-color : rgb(166,251,153);}")
        else:
                self.price_button.setStyleSheet("QLineEdit { background-color : rgb(255,255,255);}")
        
    
    def validate_size(self):
        self.pattern = re.compile("[0-9]")
        self.size = self.size_integer.text()
        valid =  self.pattern.match(self.size)
        if len(self.size) > 0 and len(self.size) <= 5:
            if valid:
                self.size_integer.setStyleSheet("QLineEdit { background-color : rgb(166,251,153);}")
        else:
            self.size_integer.setStyleSheet("QLineEdit { background-color : rgb(255,255,255);}")
        
    def validate_stock1(self):
        self.pattern = re.compile("[0-9]")
        self.stock = self.location1.text()
        valid =  self.pattern.match(self.stock)
        if len(self.stock) > 0 and len(self.stock) <= 2:
            if valid:
                self.location1.setStyleSheet("QLineEdit { background-color : rgb(166,251,153);}")
        else:
            self.location1.setStyleSheet("QLineEdit { background-color : rgb(255,255,255);}")

    def validate_stock2(self):
        self.pattern = re.compile("[0-9]")
        self.stock = self.location2.text()
        valid =  self.pattern.match(self.stock)
        if len(self.stock) > 0 and len(self.stock) <= 2:
            if valid:
                self.location2.setStyleSheet("QLineEdit { background-color : rgb(166,251,153);}")
        else:
            self.location2.setStyleSheet("QLineEdit { background-color : rgb(255,255,255);}")

        
        
        
        
        
        
        
    
    
