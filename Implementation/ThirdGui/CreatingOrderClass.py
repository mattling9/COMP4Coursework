from PyQt4.QtGui import *
from PyQt4.QtCore import *
from PopUpMenuClass import *

class createOrderClass(QWidget):
    """A representation of creating an order"""
    def __init__(self):
        super().__init__()
        self.category_layout = QHBoxLayout()
        self.category_label = QLabel("Category")
        self.category_label.setFixedWidth(70)
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

        #Product Display Table
        self.display_table = QTableWidget()
        self.display_table.setRowCount(7)
        self.display_table.setColumnCount(5)
        self.table_widget = QTableWidget()
        self.table_widget.setRowCount(3)
        self.table_widget.setColumnCount(5)        

        #display table
        title_list = ["Product ID","Product Name","Price","Size","Category"]
        self.display_table.setHorizontalHeaderLabels(title_list)

        #Finding product group box
        find_product_box = QGroupBox("Finding Product")
        find_product_layout = QVBoxLayout()
        find_product_layout.addWidget(self.category_widget)
        find_product_layout.addWidget(self.display_table)
        find_product_box.setLayout(find_product_layout)

        self.subtotal_label = QLabel("Subtotal:")
        self.subtotal_label.setAlignment(Qt.AlignRight)
        self.total_label = QLabel("Total:")
        self.total_label.setAlignment(Qt.AlignRight)
        self.tax_label = QLabel("Tax:")
        self.tax_label.setAlignment(Qt.AlignRight)
        self.subtotal = QLineEdit("£12.99")
        self.subtotal.setReadOnly(True)
        self.subtotal.setFixedWidth(50)
        self.tax = QLineEdit("£0.50")
        self.tax.setReadOnly(True)
        self.tax.setFixedWidth(50)
        self.total = QLineEdit("£13.49")
        self.total.setReadOnly(True)
        self.total.setFixedWidth(50)

        #Subtotal, Tax and Total Prices
        self.price_layout = QGridLayout()
        self.price_layout.addWidget(self.subtotal_label, 0,0)
        self.price_layout.addWidget(self.tax_label, 1,0)
        self.price_layout.addWidget(self.total_label, 2,0)
        self.price_layout.addWidget(self.subtotal, 0,1)
        self.price_layout.addWidget(self.tax, 1,1)
        self.price_layout.addWidget(self.total, 2,1)
        self.price_widget = QWidget()
        self.price_widget.setLayout(self.price_layout)

        #Create Invoice Button
        self.preview_button = QPushButton("Preview Invoice")
        self.preview_button.clicked.connect(self.preview_invoice_clicked)
        self.invoice_button = QPushButton("Create Invoice")
        self.invoice_button.clicked.connect(self.create_invoice_clicked)
        self.invoice_layout = QHBoxLayout()
        self.invoice_layout.addWidget(self.preview_button)
        self.invoice_layout.addWidget(self.invoice_button)
        self.invoice_widget = QWidget()
        self.invoice_widget.setLayout(self.invoice_layout)
    

        #order_group_box
        self.order_box = QGroupBox("Current Order")
        self.order_layout = QVBoxLayout()
        self.order_layout.addWidget(self.table_widget)
        self.order_layout.addWidget(self.price_widget)
        self.order_box.setLayout(self.order_layout)

        

        self.table_layout = QVBoxLayout()
        self.table_layout.addWidget(find_product_box)
        self.table_layout.addWidget(self.order_box)
        self.table_layout.addWidget(self.invoice_widget)
        self.table_widget = QWidget()
        self.table_widget.setFixedSize(580,500)
        self.setLayout(self.table_layout)

    def preview_invoice_clicked(self):
        self.pop_up_instance = PopUpWindow("Beacon Vets Invoice Preview", 900, 900)
        self.icon = QIcon(QPixmap("./images/Logo.jpg"))
        self.pop_up_instance.setWindowIcon(self.icon)
        self.print_preview = QPrintPreviewDialog()
        self.pop_up_instance.setCentralWidget(self.print_preview)

    def create_invoice_clicked(self):
        self.pop_up_instance = PopUpWindow("Beacon Vets Invoice Preview", 900, 900)
        self.icon = QIcon(QPixmap("./images/Logo.jpg"))
        self.pop_up_instance.setWindowIcon(self.icon)
        self.label = QLabel()
        self.image = QPixmap("./images/Logo.jpg")
        self.label.setPixmap(self.image)
        self.label.setAlignment(Qt.AlignCenter)
        self.buttonBox = QDialogButtonBox()
        self.buttonBox.setOrientation(Qt.Horizontal)
        self.buttonBox.setStandardButtons(QDialogButtonBox.Ok)
        self.buttonBox.button(QDialogButtonBox.Ok).clicked.connect(self.clicked_Ok)
        self.buttons = self.buttonBox.buttons()
        self.pop_up_layout = QVBoxLayout()
        self.pop_up_widget = QWidget()
        self.pop_up_layout.addWidget(self.label)
        self.pop_up_layout.addWidget(self.buttonBox)
        self.pop_up_widget.setLayout(self.pop_up_layout)
        self.pop_up_instance.setCentralWidget(self.pop_up_widget)
        self.pop_up_instance.showMaximized()
        self.pop_up_instance.raise_()

    

    def clicked_Ok(self):
        self.pop_up_instance.close()
        


        
