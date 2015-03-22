import shutil, re

from PyQt4.QtGui import *
from PyQt4.QtCore import *
from PopUpMenuClass import *
from AddingRemovingData import *
from ErrorMessageClass import *
class deleteProductClass(QWidget):
    """ A representation of the Adding Product Interface"""
    def __init__(self):
        super().__init__()
        #Adding group box
        self.product_info_group_box = QGroupBox()
        self.product_info_group_box.setTitle("Enter Product Information:")
        
        

        #creating the buttons
        self.find_product_id_layout = QHBoxLayout()
        self.find_product_id_widget = QWidget()
        self.find_product_id_label = QLabel("ProductID")
        self.find_product_id_line_edit = QLineEdit()
        self.find_product_id_button = QPushButton("Find...")
        self.find_product_id_button.setFixedSize(84,27)
        self.find_product_id_button.clicked.connect(self.find_product_by_id)

                                        
        self.find_product_id_layout.addWidget(self.find_product_id_label)
        self.find_product_id_layout.addWidget(self.find_product_id_line_edit)
        self.find_product_id_layout.addWidget(self.find_product_id_button)
        self.find_product_id_widget.setLayout(self.find_product_id_layout)
        
        #Price
        self.pound = QLabel("Price: £")
        self.price_button = QLineEdit("")
        self.price_button.setReadOnly(True)
        self.validator = QDoubleValidator()
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
        self.size_integer.setReadOnly(True)
        self.size_integer.setPlaceholderText("Size: (750)")
        self.size_integer.setFixedWidth(180)
        self.size_button = QComboBox()
        self.size_button.setDisabled(True)
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
        self.category1_button.setFixedHeight(30)
        self.category1_button.setDisabled(True)
        self.category2_button = QComboBox()
        self.category2_button.setFixedHeight(30)
        self.category2_button.setDisabled(True)
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
        self.location1.setDisabled(True)


        #Location 2
        self.location2 = QLineEdit()
        self.location2.setPlaceholderText("Stock In Location 2...")
        self.location2.setDisabled(True)


        #Done
        self.done = QPushButton("Delete Product")
        self.done.clicked.connect(self.CreatePopUpWindow)
        self.done.setShortcut(QKeySequence("CTRL+S"))
        self.done.setFixedSize(110, 27)

        #Product Name
        self.product_name = QLineEdit()
        self.product_name.setReadOnly(True)
        product_name_info = self.product_name.text()
        self.product_name.setPlaceholderText("Product Name...")
        self.product_name.setFixedWidth(260)

        #Image
        self.image = QLabel()
        self.image_pixmap = QPixmap(".\ProductImages\Default.jpg")
        self.scaled_image = self.image_pixmap.scaled(300, 300, Qt.IgnoreAspectRatio, Qt.FastTransformation)
        self.image.setPixmap(self.scaled_image)
        

        #Browse
        path = "./ProductImages/Default.jpg"
        
        self.browse_layout = QHBoxLayout()
        self.browse_widget = QWidget()
        self.browse = QPushButton("Browse...")
        self.browse.setDisabled(True)
        self.browse.clicked.connect(self.get_image_path)
        self.browse.setFixedSize(84, 27)
        self.browse.setObjectName('browse')
        
        self.upload = QPushButton("Upload")
        self.upload.setDisabled(True)
        self.upload.setFixedSize(78,27)
        self.upload.setObjectName('upload')
        
        self.path = QLineEdit("")
        self.path.setReadOnly(True)
        self.path.setText(path)
        self.browse_layout.addWidget(self.path)
        self.browse_layout.addWidget(self.browse)
        self.browse_layout.addWidget(self.upload)
        self.browse_widget.setLayout(self.browse_layout)
        
        
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
        self.leftright_widget.setDisabled(True)

        self.add_product_layout = QHBoxLayout()
        self.add_product_widget = QWidget()
        self.spacer = QLabel()
        self.spacer.setFixedWidth(600)
        self.add_product_layout.addWidget(self.spacer)
        self.add_product_layout.addWidget(self.done)
        self.add_product_widget.setLayout(self.add_product_layout)

        self.main_layout = QVBoxLayout()
        self.main_layout.addWidget(self.find_product_id_widget)
        self.main_layout.addWidget(self.leftright_widget)
        self.main_layout.addWidget(self.add_product_widget)
        self.main_widget = QWidget()
        self.main_widget.setLayout(self.main_layout)

        self.total_layout = QVBoxLayout()
        self.total_layout.addWidget(self.main_widget)
        self.setLayout(self.total_layout)
        
    def CreatePopUpWindow(self):
        self.pop_up_instance = PopUpWindow("Are you sure you want to Delete The Product?", QDialogButtonBox.Yes, QDialogButtonBox.No)
        self.pop_up_instance.buttonBox.button(
            QDialogButtonBox.Yes).clicked.connect(self.clicked_yes)
        self.pop_up_instance.buttonBox.button(
            QDialogButtonBox.No).clicked.connect(self.clicked_no)

    def AddProductSucess(self):
        self.add_product_instance = PopUpWindow("Product Sucessfully Deleted!", QDialogButtonBox.Ok, QDialogButtonBox.Cancel)
        self.add_product_instance.buttonBox.button(
            QDialogButtonBox.Ok).clicked.connect(self.close_pop_ups)
        self.add_product_instance.buttonBox.button(
            QDialogButtonBox.Cancel).clicked.connect(self.close_pop_ups)

    def get_image_path(self):
        path =  QFileDialog.getOpenFileName()
        self.path.setText(path)

    def update_image(self):
        self.pixmap = QPixmap(self.path.text())
        self.scaled_image = self.pixmap.scaled(300, 300, Qt.IgnoreAspectRatio, Qt.FastTransformation)
        self.image.setPixmap(self.scaled_image)

    def clicked_yes(self):
        self.size_list = [self.size_integer.text(), self.size_button.currentText()]
        self.temp = ""
        self.category_string = str((self.category1_button.currentText() + " " + self.category2_button.currentText()))
        self.size_string = self.temp.join(self.size_list)
        deletingProduct(self.find_product_id_line_edit.text())
        self.AddProductSucess()
        
    def find_product_by_id(self):
        with sqlite3.connect("ProductDatabase.db") as db:
            product_id = self.find_product_id_line_edit.text()
            cursor = db.cursor()
            cursor.execute("SELECT * FROM Product WHERE ProductID = ?",(product_id,))
            self.product_info = cursor.fetchall()
            db.commit()
            if self.product_info:
                self.leftright_widget.setEnabled(True)
                self.product_name.setText(self.product_info[0][1])
                self.size_integer.setText(self.product_info[0][2])
                self.price_button.setText(str(self.product_info[0][3]))
                self.path.setText(self.product_info[0][7])
                self.pixmap = QPixmap(self.path.text())
                self.scaled_image = self.pixmap.scaled(300, 300, Qt.IgnoreAspectRatio, Qt.FastTransformation)
                self.image.setPixmap(self.scaled_image)
                
                
                
            if not self.product_info:
                self.error = ErrorMessageClass("No product found with Product ID: {0}".format(self.find_product_id_line_edit.text()))
                self.error.setFixedSize(400,150)
                self.clear_fields()
        


    def clear_fields(self):
        self.find_product_id_line_edit.setText("")
        self.product_name.setText("")
        self.size_integer.setText("")
        self.price_button.setText("")
        self.path.setText(".\ProductImages\Default.jpg")
        self.image_pixmap = QPixmap(".\ProductImages\Default.jpg")
        self.scaled_image = self.image_pixmap.scaled(300, 300, Qt.IgnoreAspectRatio, Qt.FastTransformation)
        self.image.setPixmap(self.scaled_image)
        
    def clicked_no(self):
        self.pop_up_instance.close()

    def close_pop_ups(self):
        self.add_product_instance.close()
        self.pop_up_instance.close()
        self.clear_fields()
     
    
    
