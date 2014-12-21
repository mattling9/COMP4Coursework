from PyQt4.QtGui import *
from PyQt4.QtCore import *

class addProduct(QWidget):
    """ A representation of the Adding Product Interface"""
    def __init__(self):
        super().__init__()
        self.resize(400,300)
        addProduct()

    def addProduct(self):
        #Adding group box
        self.product_info_group_box = QGroupBox()
        self.product_info_group_box.setTitle("Enter Product Information:")
        
        

        #creating the buttons

        #Title
        self.title = QLabel("Adding New Product")
        self.title.setAlignment(Qt.AlignCenter)
        font = QFont()
        font.setPointSize(18)
        font.setBold(True)
        self.title.setFont(font)
    
        
        #Price
        self.price_button = QLineEdit()
        self.price_button.setPlaceholderText("Price: £0.00")

        #Size
        self.size_layout = QHBoxLayout()
        self.size_widget = QWidget()
        self.size_integer = QLineEdit()
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

        #Location 2
        self.location2 = QLineEdit()
        self.location2.setPlaceholderText("Stock In Location 2...")

        #Done
        self.done = QPushButton("Done")

        #Product Name
        self.product_name = QLineEdit()
        self.product_name.setPlaceholderText("Product Name...")

        #Image
        self.image = QLabel()
        self.image_pixmap = QPixmap(".\images\Logo.jpg")
        self.scaled_image = self.image_pixmap.scaled(300, 300, Qt.IgnoreAspectRatio, Qt.FastTransformation)
        self.image.setPixmap(self.scaled_image)
        

        #Browse
        self.browse_layout = QHBoxLayout()
        self.browse_widget = QWidget()
        self.browse = QPushButton("Browse...")
        self.upload = QPushButton("Upload")
        self.path = QLineEdit("/images/example.png")
        self.browse_layout.addWidget(self.path)
        self.browse_layout.addWidget(self.browse)
        self.browse_layout.addWidget(self.upload)
        self.browse_widget.setLayout(self.browse_layout)
        
        
        #Creating Layouts and Adding Widgets

        self.input_layout = QVBoxLayout()
        self.input_widget = QWidget()
        self.input_layout.addWidget(self.price_button)
        self.input_layout.addWidget(self.size_widget)
        self.input_layout.addWidget(self.category_widget)
        self.input_layout.addWidget(self.location1)
        self.input_layout.addWidget(self.location2)
        self.input_widget.setLayout(self.input_layout)
        self.product_info_group_box.setLayout(self.input_layout)
        self.left_widget = QWidget()
        self.left_layout = QVBoxLayout()
        self.left_layout.addWidget(self.product_info_group_box)
        self.left_layout.addWidget(self.done)
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

        self.main_layout = QHBoxLayout()
        self.main_layout.addWidget(self.left_widget)
        self.main_layout.addWidget(self.right_widget)
        self.main_widget = QWidget()
        self.main_widget.setLayout(self.main_layout)

        self.total_layout = QVBoxLayout()
        self.total_widget = QWidget()
        self.total_layout.addWidget(self.title)
        self.total_layout.addWidget(self.main_widget)
        self.total_widget.setLayout(self.total_layout)
        self.setCentralWidget(self.total_widget)
        

    

        
        
        
        
        
        
        
        
        
        
    
    
