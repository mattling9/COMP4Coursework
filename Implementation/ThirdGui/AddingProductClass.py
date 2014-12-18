from PyQt4.QtGui import *
from PyQt4.QtCore import *

class AddingProductLayout(QWidget):
    """ A representation of the Adding Product Interface"""
    def __init__(self):
        super().__init__()
        self.product_info_group_box = QGroupBox("Enter Product Info: ")
        self.product_info_group = QButtonGroup()

        #creating the buttons

        #Price
        self.price_button = QLineEdit()
        self.price_button.setPlaceholderText("Price: £0.00")

        #Size
        self.size_button = QComboBox()
        self.size_button.addItem("Kg.")
        self.size_button.addItem("g.")
        self.size_button.addItem("L.")
        self.size_button.addItem("ml.")

        #Category
        self.category_layout = QHBoxLayout()
        self.category_label = QLabel("Category")
        self.category_button = QToolButton()
        self.category_layout.addWidget(self.category_label)
        self.category_layout.addWidget(self.category_button)

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
        
        
        
        
        
        
        
        
        
    
    
