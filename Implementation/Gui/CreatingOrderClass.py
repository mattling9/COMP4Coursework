import sqlite3, sys
from PyQt4.QtSql import *
from PyQt4.QtGui import *
from PyQt4.QtCore import *
from PopUpMenuClass import *
from AddingRemovingData import *

class createOrderClass(QWidget):
    """A representation of creating an order"""
    def __init__(self):
        super().__init__()
        ProductID_list = []
        self.category_layout = QHBoxLayout()
        self.category_label = QLabel("Find Product:")
        self.category_label.setFixedWidth(70)
        self.category_search = QLineEdit()
        self.category_search.textChanged.connect(self.find_product)
        self.category_layout.addWidget(self.category_label)
        self.category_layout.addWidget(self.category_search)
        self.category_widget = QWidget()
        self.category_widget.setLayout(self.category_layout)
        self.subtotal_price = 0.00
        ProductList = [""]

      #Product Display Table
        self.display_table = QTableView()
        self.display_table.setFixedHeight(150)
        self.display_table_layout = QVBoxLayout()
        self.display_table_layout.addWidget(self.display_table)
        self.display_table.setSelectionBehavior(QAbstractItemView.SelectRows)
        self.display_table.setAlternatingRowColors(True)
        self.display_table_widget = QWidget()
        self.display_table_widget.setLayout(self.display_table_layout)
        self.model = None
        if not self.model or not isinstance(self.model, QSqlTableModel):
            self.model = QSqlTableModel()
        
        self.model.setTable("Product")
        self.model.select()
        self.display_table.setModel(self.model)
        self.display_table.hideColumn(4)
        self.display_table.hideColumn(5)
        column_width_list = [80, 300, 90, 75]
        counter = 0
        for item in column_width_list:
            self.display_table.setColumnWidth(counter, item)
            counter += 1

        

        self.display_table.horizontalHeader().setStretchLastSection(True)
        self.display_table.verticalHeader().setStretchLastSection(True)
        self.display_table.setEditTriggers(QAbstractItemView.NoEditTriggers)
        self.display_table.doubleClicked.connect(self.clicked)
        self.display_table.show()

        self.table_layout = QVBoxLayout()

        self.add_product = QPushButton("Add Product")
        self.add_product.setFixedWidth(100)
        self.add_product.clicked.connect(self.clicked, 0)
        self.table_layout.addWidget(self.display_table)
        self.table_layout.addWidget(self.add_product)
        self.table_widget = QWidget()
        self.table_layout.setAlignment(Qt.AlignCenter)
        self.table_widget.setLayout(self.table_layout)
        self.find_product_box = QGroupBox("Finding Product")
        self.find_product_layout = QVBoxLayout()
        self.find_product_layout.addWidget(self.category_widget)
        self.find_product_layout.addWidget(self.table_widget)
        self.find_product_box.setLayout(self.find_product_layout)

        self.member_label = QLabel("Member ID:")
        self.member_line_edit = QLineEdit()
        self.member_button = QPushButton("Enter")
        self.member_button.clicked.connect(self.find_member_by_id)
        self.member_layout = QHBoxLayout()
        self.member_widget = QWidget()
        self.member_layout.addWidget(self.member_label)
        self.member_layout.addWidget(self.member_line_edit)
        self.member_widget.setLayout(self.member_layout)
        self.subtotal_label = QLabel("Subtotal: £")
        self.subtotal_label.setAlignment(Qt.AlignRight)
        self.total_label = QLabel("Total: £")
        self.total_label.setAlignment(Qt.AlignRight)
        self.tax_label = QLabel("Discount: £")
        self.tax_label.setAlignment(Qt.AlignRight)
        self.subtotal = QLineEdit("0.0")
        self.subtotal.setReadOnly(True)
        self.subtotal.setFixedWidth(65)
        self.discount_line_edit = QLineEdit("0.0")
        self.discount_line_edit.setReadOnly(True)
        self.discount_line_edit.setFixedWidth(65)
        self.total = QLineEdit("0.0")
        self.total.setReadOnly(True)
        self.total.setFixedWidth(65)

        #Subtotal, Tax and Total Prices
        self.price_layout = QGridLayout()
        self.price_layout.addWidget(self.member_widget, 0,0)
        self.price_layout.addWidget(self.member_button, 0,1)
        self.price_layout.addWidget(self.subtotal_label, 1,0)
        self.price_layout.addWidget(self.tax_label, 2,0)
        self.price_layout.addWidget(self.total_label, 3,0)
        self.price_layout.addWidget(self.subtotal, 1,1)
        self.price_layout.addWidget(self.discount_line_edit, 2,1)
        self.price_layout.addWidget(self.total, 3,1)
        self.price_widget = QWidget()
        self.price_widget.setLayout(self.price_layout)

        #Create Invoice Button
        self.save_button = QPushButton("Save")
        self.save_button.clicked.connect(self.save_invoice)
        self.preview_button = QPushButton("Preview Invoice")
        self.preview_button.clicked.connect(self.preview_invoice_clicked)
        self.invoice_button = QPushButton("Create Invoice")
        self.invoice_button.clicked.connect(self.create_invoice_clicked)
        self.invoice_layout = QHBoxLayout()
        self.invoice_layout.addWidget(self.save_button)
        self.invoice_layout.addWidget(self.preview_button)
        self.invoice_layout.addWidget(self.invoice_button)
        self.invoice_widget = QWidget()
        self.invoice_widget.setLayout(self.invoice_layout)
    

        #order_group_box
        self.order_box = QGroupBox("Current Order")
        self.order_layout = QVBoxLayout()
        self.current_order = QTableView()
        self.order_model = None
        if not self.order_model or not isinstance(self.order_model, QSqlTableModel):
            self.order_model = QSqlTableModel()

        self.order_model.setTable("ProductOrder")
        self.order_model.select()
        self.current_order.setModel(self.order_model)
        self.current_order.setAlternatingRowColors(True)
        self.current_order.hideColumn(0)
        self.current_order.hideColumn(1)
        self.current_order.horizontalHeader().setStretchLastSection(True)
        self.current_order.setSelectionBehavior(QAbstractItemView.SelectRows)
        self.order_layout.addWidget(self.current_order)
        self.order_layout.addWidget(self.price_widget)
        self.order_box.setLayout(self.order_layout)



        self.main_layout = QVBoxLayout()
        self.main_layout.addWidget(self.find_product_box)
        self.main_layout.addWidget(self.order_box)
        self.main_layout.addWidget(self.invoice_widget)
        self.setLayout(self.main_layout)
        self.discount = 0

        ##
        ##


    def preview_invoice_clicked(self):
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

    def create_invoice_clicked(self):
        self.pop_up_instance = PopUpWindow("Beacon Vets Stock Control", 900, 900)
        self.icon = QIcon(QPixmap("./images/Logo.jpg"))
        self.pop_up_instance.setWindowIcon(self.icon)
        
        self.label = QLabel()
        self.image = QPixmap("./images/Logo.jpg")
        self.buttonBox = QDialogButtonBox()
        self.buttonBox.setOrientation(Qt.Horizontal)
        self.buttonBox.setStandardButtons(QDialogButtonBox.Ok)
        self.buttonBox.button(QDialogButtonBox.Ok).clicked.connect(self.clicked_Ok)
        self.buttons = self.buttonBox.buttons()
        self.pop_up_layout = QVBoxLayout()
        self.pop_up_widget = QWidget()
        self.pop_up_layout.addWidget(self.buttonBox)
        self.pop_up_widget.setLayout(self.pop_up_layout)
        self.pop_up_instance.setCentralWidget(self.pop_up_widget)
        self.pop_up_instance.show()
        self.pop_up_instance.raise_()

    

    def clicked_Ok(self):
        self.pop_up_instance.close()

    def clicked(self):
        self.indexes = self.display_table.selectionModel().selectedRows()
        if self.indexes:
            for index in self.indexes:
                row = index.row()
                row += 1

            price = addingProductToOrder(self, row)
            self.subtotal_price = self.subtotal_price + price
            self.subtotal_price = round(self.subtotal_price, 4)
            self.discount_multiplier = (1 - self.discount)
            self.total_price = (self.discount_multiplier * self.subtotal_price)
            self.total_price = round(self.total_price, 4)
            self.money_off = (self.subtotal_price - self.total_price)
            self.money_off = round(self.money_off, 4)
            
            self.subtotal.setText(str(self.subtotal_price))
            self.discount_line_edit.setText(str(self.money_off))

            self.total.setText(str(self.total_price))
                
            self.order_model.select()
        else:
            pass
        
    def change_price(self):
        self.subtotal_price
        self.discount_multiplier = (1 - self.discount)
        
        self.total_price = (self.discount_multiplier * self.subtotal_price)

        
        self.money_off = (self.subtotal_price - self.total_price)

            
        if len(str(self.subtotal_price)) == 5:
            self.subtotal.setText(str(self.subtotal_price)[:5])
            self.discount_line_edit.setText(str(self.money_off)[:5])
            self.total.setText(str(self.total_price)[:5])

        elif len(str(self.subtotal_price)) == 6:
            self.subtotal.setText(str(self.subtotal_price)[:6])
            self.discount_line_edit.setText(str(self.money_off)[:6])
            self.total.setText(str(self.total_price)[:6])

        else:
            self.subtotal.setText(str(self.subtotal_price)[:4])
            self.discount_line_edit.setText(str(self.money_off)[:4])
            self.total.setText(str(self.total_price)[:4])

    def find_product(self):
        ProductName = self.category_search.text()
        filter_query = "ProductID like '%{0}%' or ProductName like '%{0}%' or Size like '%{0}%' or Price like '%{0}%'".format(ProductName)
        self.model.setFilter(filter_query)
        self.model.select()

    def find_member_by_id(self):
        with sqlite3.connect("ProductDatabase.db") as db:
            member_id = self.member_line_edit.text()
            cursor = db.cursor()
            cursor.execute("SELECT * FROM Member WHERE MemberID = ?",(member_id,))
            product_info = cursor.fetchall()
            db.commit()
            if product_info:
                self.discount = 0.1
                self.change_price()
            if not product_info:
                self.discount = 0.0
                self.change_price()
                self.display_message()

    def display_message(self):
        self.member_id_error_instance = PopUpWindow("Fucking Buy Membership Now",300,100)
        self.icon = QIcon(QPixmap("./images/Logo.jpg"))
        self.member_id_error_instance.setWindowIcon(self.icon)
        self.label = QLabel("Oi bitch, your Member ID aint valid ya cunt")
        self.label.setAlignment(Qt.AlignCenter)
        self.buttonBox = QDialogButtonBox()
        self.buttonBox.setOrientation(Qt.Horizontal)
        self.buttonBox.setStandardButtons(QDialogButtonBox.Ok | QDialogButtonBox.Cancel)
        self.buttonBox.button(QDialogButtonBox.Ok).clicked.connect(self.close_pop_up)
        self.buttonBox.button(QDialogButtonBox.Cancel).clicked.connect(self.close_pop_up)
        self.pop_up_layout = QVBoxLayout()
        self.pop_up_widget = QWidget()
        self.pop_up_layout.addWidget(self.label)
        self.pop_up_layout.addWidget(self.buttonBox)
        self.pop_up_widget.setLayout(self.pop_up_layout)
        self.member_id_error_instance.setCentralWidget(self.pop_up_widget)
        self.member_id_error_instance.move(800,450)
        self.member_id_error_instance.show()
        self.member_id_error_instance.raise_()

    def close_pop_up(self):
        self.member_id_error_instance.close()

    def save_invoice(self):
        print("saved")
        createCustomerOrder()

    def save_sucess(self):
        self.add_product_instance = PopUpWindow("Beacon Vets Adding Product", 300, 100)
        self.icon = QIcon(QPixmap("./images/Logo.jpg"))
        self.add_order_instance.setWindowIcon(self.icon)
        self.label = QLabel("Order Sucessfully Saved")
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
        self.add_order_instance.setCentralWidget(self.pop_up_widget)
        self.add_order_instance.move(800,450)
        self.add_order_instance.show()
        self.add_order_instance.raise_()
        
       
