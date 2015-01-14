import sys, shutil

from PyQt4.QtCore import *
from PyQt4.QtGui import *
from ProductSearchClass import *
from AddingProductClass import *
from AddingMemberClass import *
from AddingEmployeeClass import *
from StockManagementClass import *
from ProductIDClass import *
from CreatingOrderClass import *
from PopUpMenuClass import *
from DatabaseClass import *
from SQLConnection import *
from CreatingTable import *

class MainWindow(QMainWindow):
    """This class creates the Main window"""

    def __init__(self):
        super().__init__()
        self.setWindowTitle("Beacon Vets Stock Control")
        self.setFixedSize(700, 600)
        self.icon = QIcon(QPixmap("./images/Logo.jpg"))
        self.setWindowIcon(self.icon)
        self.statusBar().showMessage('Status: Idle')
        self.connection = SQLConnection("ProductDatabase.db")
        open_db = self.connection.open_database()
        self.Settings()
        self.stacked_layout = QStackedLayout()
        self.add_product()
        product_name_info = self.edit_product()
        self.delete_product()
        self.search_product()
        self.manage_stock()
        self.create_order()
        self.add_member()
        self.edit_member()
        self.delete_member()
        self.add_employee()
        self.edit_employee()
        self.delete_employee()
        self.widget = QWidget()
        self.widget.setLayout(self.stacked_layout)
        self.setCentralWidget(self.widget)
        self.create_new_order_function()
        
        
        


    def create_title(self):
        self.title = QLabel("Default Text")
        self.title.setAlignment(Qt.AlignCenter)
        font = QFont()
        font.setPointSize(18)
        font.setBold(True)
        self.title.setFont(font)
        self.title.setFixedHeight(30)
        return self.title


    def search_product(self):
        self.title = self.create_title()
        self.title.setText("Search For Product")
        
        self.search_product_instance = searchProductClass()
        #create layout to hold widgets
        self.search_product_layout = QVBoxLayout()
        self.search_product_layout.addWidget(self.search_product_instance)                                     
        self.select_animal_widget = QWidget()
        self.select_animal_widget.setLayout(self.search_product_layout)
        self.setCentralWidget(self.select_animal_widget)
        self.stacked_layout.addWidget(self.select_animal_widget)

        
    def add_product(self):
        self.title = self.create_title()
        self.title.setText("Add Product ")
        self.add_product_instance = addProductClass("Add Product")
        product_name_info = self.add_product_instance.product_name.text()
        
        self.add_product_layout = QVBoxLayout()
        self.add_product_layout.addWidget(self.title)
        self.add_product_layout.addWidget(self.add_product_instance)
        self.add_product_widget = QWidget()
        self.add_product_widget.setLayout(self.add_product_layout)
        self.setCentralWidget(self.add_product_widget)
        self.stacked_layout.addWidget(self.add_product_widget)

    def edit_product(self):
        self.product_found = False
        self.title = self.create_title()
        self.title.setText("Edit Product ")
        self.edit_product_instance = addProductClass("Edit Product")
        self.edit_product_layout = QVBoxLayout()
        if self.product_found == False:
            self.edit_product_instance.setEnabled(False)
        elif self.product_found == True:
            self.edit_product_instance.setEnabled(True)
        self.product_id = ProductIDClass("Product ID")
        self.product_id.setFixedHeight(40)
        self.edit_product_layout.addWidget(self.title)
        self.edit_product_layout.addWidget(self.product_id)
        self.edit_product_layout.addWidget(self.edit_product_instance)
        self.edit_product_widget = QWidget()
        self.edit_product_widget.setLayout(self.edit_product_layout)
        self.setCentralWidget(self.edit_product_widget)
        self.stacked_layout.addWidget(self.edit_product_widget)

    def delete_product(self):
        self.product_found = False
        self.title = self.create_title()
        self.title.setText("Delete Product ")
        self.delete_product_instance = addProductClass("Delete Product")
        self.delete_product_layout = QVBoxLayout()
        if self.product_found == False:
            self.delete_product_instance.setEnabled(False)
        elif self.product_found == True:
            self.delete_product_instance.setEnabled(True)
        self.product_id = ProductIDClass("Product ID")
        self.product_id.setFixedHeight(40)
        self.delete_product_layout.addWidget(self.title)
        self.delete_product_layout.addWidget(self.product_id)
        self.delete_product_layout.addWidget(self.delete_product_instance)
        self.delete_product_widget = QWidget()
        self.delete_product_widget.setLayout(self.delete_product_layout)
        self.setCentralWidget(self.delete_product_widget)
        self.stacked_layout.addWidget(self.delete_product_widget)
        


    def add_member(self):
        self.title = self.create_title()
        self.title.setText("Add Member")
        
        self.add_member_instance = addMemberClass("Add New Member")
        self.add_member_layout = QVBoxLayout()
        self.add_member_widget = QWidget()
        self.add_member_layout.addWidget(self.title)
        self.add_member_layout.addWidget(self.add_member_instance)
        self.add_member_widget.setLayout(self.add_member_layout)
        self.setCentralWidget(self.add_member_widget)
        self.stacked_layout.addWidget(self.add_member_widget)

    def edit_member(self):
        self.title = self.create_title()
        self.title.setText("Edit Member")

        
        self.edit_member_instance = addMemberClass("Edit Member")        
        self.product_id = ProductIDClass("Member ID")
        self.product_id.setFixedHeight(40)
        self.edit_member_layout = QVBoxLayout()
        self.edit_member_widget = QWidget()
        if self.product_found == False:
            self.edit_member_instance.setEnabled(False)
        elif self.product_found == True:
            self.edit_member_instanceset.Enabled(True)
        self.edit_member_layout.addWidget(self.title)
        self.edit_member_layout.addWidget(self.product_id)
        self.edit_member_layout.addWidget(self.edit_member_instance)
        self.edit_member_widget.setLayout(self.edit_member_layout)
        self.setCentralWidget(self.edit_member_widget)
        self.stacked_layout.addWidget(self.edit_member_widget)

    def delete_member(self):
        self.title = self.create_title()
        self.title.setText("Delete Member")

        
        self.delete_member_instance = addMemberClass("Delete Member")
        self.product_id = ProductIDClass("Member ID")
        self.product_id.setFixedHeight(40)
        self.delete_member_layout = QVBoxLayout()
        self.delete_member_widget = QWidget()
        if self.product_found == False:
            self.delete_member_instance.setEnabled(False)
        elif self.product_found == True:
            self.delete_member_instance.setEnabled(True)
        self.delete_member_layout.addWidget(self.title)
        self.delete_member_layout.addWidget(self.product_id)
        self.delete_member_layout.addWidget(self.delete_member_instance)
        self.delete_member_widget.setLayout(self.delete_member_layout)
        self.setCentralWidget(self.delete_member_widget)
        self.stacked_layout.addWidget(self.delete_member_widget)
        


    def add_employee(self):
        self.title = self.create_title()
        self.title.setText("Add Employee")

        
        self.add_employee_instance = addEmployeeClass("Add New Employee")

        self.add_employee_layout = QVBoxLayout()
        self.add_employee_widget = QWidget()
        self.add_employee_layout.addWidget(self.title)
        self.add_employee_layout.addWidget(self.add_employee_instance)
        self.add_employee_widget.setLayout(self.add_employee_layout)
        self.setCentralWidget(self.add_employee_widget)
        self.stacked_layout.addWidget(self.add_employee_widget)

    def edit_employee(self):
        self.title = self.create_title()
        self.title.setText("Edit Employee")

        
        self.edit_employee_instance = addEmployeeClass("Edit Employee")
        self.product_id = ProductIDClass("Employee ID")
        self.product_id.setFixedHeight(40)
        self.edit_employee_layout = QVBoxLayout()
        self.edit_employee_widget = QWidget()
        if self.product_found == False:
            self.edit_employee_instance.setEnabled(False)
        elif self.product_found == True:
            self.edit_employee_instance.setEnabled(True)
        self.edit_employee_layout.addWidget(self.title)
        self.edit_employee_layout.addWidget(self.product_id)
        self.edit_employee_layout.addWidget(self.edit_employee_instance)
        self.edit_employee_widget.setLayout(self.edit_employee_layout)
        self.setCentralWidget(self.edit_employee_widget)
        self.stacked_layout.addWidget(self.edit_employee_widget)

    def delete_employee(self):
        self.title = self.create_title()
        self.title.setText("Delete Employee")

        
        self.delete_employee_instance = addEmployeeClass("Delete Employee")
        self.product_id = ProductIDClass("Employee ID")
        self.product_id.setFixedHeight(40)
        self.delete_employee_layout = QVBoxLayout()
        self.delete_employee_widget = QWidget()
        if self.product_found == False:
            self.delete_employee_instance.setEnabled(False)
        elif self.product_found == True:
            self.delete_employee_instance.setEnabled(True)
        self.delete_employee_layout.addWidget(self.title)
        self.delete_employee_layout.addWidget(self.product_id)
        self.delete_employee_layout.addWidget(self.delete_employee_instance)
        self.delete_employee_widget.setLayout(self.delete_employee_layout)
        self.setCentralWidget(self.delete_employee_widget)
        self.stacked_layout.addWidget(self.delete_employee_widget)

    def manage_stock(self):
        self.title = self.create_title()
        self.title.setText("Manage Stock")
        self.product_id = ProductIDClass("Product ID")
        self.product_id.setFixedHeight(40)
        self.manage_stock_instance = manageStockClass()
        
        self.manage_stock_layout = QVBoxLayout()
        self.manage_stock_widget = QWidget()
        if self.product_found == False:
            self.manage_stock_instance.setEnabled(False)
        elif self.product_found == True:
            self.manage_stock_instance.setEnabled(True)
        self.manage_stock_layout.addWidget(self.title)
        self.manage_stock_layout.addWidget(self.product_id)
        self.manage_stock_layout.addWidget(self.manage_stock_instance)
        self.manage_stock_widget.setLayout(self.manage_stock_layout)
        self.setCentralWidget(self.manage_stock_widget)
        self.stacked_layout.addWidget(self.manage_stock_widget)

    def create_order(self):
        self.title = self.create_title()
        self.title.setText("Create Order")
        self.create_order_instance = createOrderClass()
        
        self.create_order_layout = QVBoxLayout()
        self.create_order_layout.addWidget(self.title)
        self.create_order_layout.addWidget(self.create_order_instance)
        self.create_order_widget = QWidget()
        self.create_order_widget.setLayout(self.create_order_layout)
        self.setCentralWidget(self.create_order_widget)
        self.stacked_layout.addWidget(self.create_order_widget)


        
    def Settings(self):
        #Adding Actions
        self.add_product_action = QAction("Add a New Product", self)
        self.edit_product_action = QAction("Edit a Product", self)
        self.delete_a_product_action = QAction("Delete a Product", self)
        self.find_a_product_action = QAction("Find a Product", self)
        self.manage_current_stock_action = QAction("Manage Stock", self)
        self.product_restock_action = QAction("Product Restock", self)
        self.create_order_action = QAction("Create New Order", self)
        self.add_new_member_action = QAction("Add New Member", self)
        self.edit_member_action  = QAction("Edit a Member", self)
        self.remove_a_member_action = QAction("Delete a Member", self)
        self.add_an_employee_action = QAction("Add Employee", self)
        self.edit_employee_action = QAction("Edit an Employee", self)
        self.remove_an_employee_action = QAction("Remove Employee", self)
        self.search_product_action = QAction("Product Search Window", self)
        self.search_product_action.setShortcut("Ctrl+F")
        #Creating MenuBar
        self.menu = QMenuBar()

        #Creating ToolBar
        #self.toolbar = QToolBar()
        #self.addToolBar(Qt.RightToolBarArea, self.toolbar)
        #self.toolbar.setMovable(False)


        #Adding Menu to MenuBar
        
        self.productsmenu = self.menu.addMenu("Product")
        self.productsmenu.addAction(self.add_product_action)
        self.productsmenu.addAction(self.edit_product_action)
        self.productsmenu.addAction(self.delete_a_product_action)
        self.productsmenu.addAction(self.find_a_product_action)
        self.stockmenu = self.menu.addMenu("Stock")
        self.stockmenu.addAction(self.manage_current_stock_action)
        self.stockmenu.addAction(self.product_restock_action)
        self.ordermenu = self.menu.addMenu("Order")
        self.ordermenu.addAction(self.create_order_action)
        self.membersmenu = self.menu.addMenu("Member")
        self.membersmenu.addAction(self.add_new_member_action)
        self.membersmenu.addAction(self.edit_member_action)
        self.membersmenu.addAction(self.remove_a_member_action)
        self.employeemenu = self.menu.addMenu("Employee")
        self.employeemenu.addAction(self.add_an_employee_action)
        self.employeemenu.addAction(self.edit_employee_action)
        self.employeemenu.addAction(self.remove_an_employee_action)
        self.optionsmenu = self.menu.addMenu("Options")
        self.optionsmenu.addAction(self.search_product_action)
        #self.menu.setCornerWidget(self.databasemenu, Qt.TopRightCorner)
        

        #Add tools to Toolbar
        #self.addToolBar(self.toolbar)
        
         #Add connections to buttons
        self.add_product_action.triggered.connect(self.add_product_function)
        self.edit_product_action.triggered.connect(self.edit_product_function)
        self.delete_a_product_action.triggered.connect(self.delete_product_function)
        self.find_a_product_action.triggered.connect(self.find_product_function)
        self.manage_current_stock_action.triggered.connect(self.manage_stock_function)
        self.product_restock_action.triggered.connect(self.product_restock_function)
        self.create_order_action.triggered.connect(self.create_new_order_function)
        self.add_new_member_action.triggered.connect(self.add_new_member_function)
        self.edit_member_action.triggered.connect(self.edit_member_function)
        self.remove_a_member_action.triggered.connect(self.remove_a_member_function)
        self.add_an_employee_action.triggered.connect(self.add_an_employee_function)
        self.edit_employee_action.triggered.connect(self.edit_employee_function)
        self.remove_an_employee_action.triggered.connect(self.remove_an_employee_function)
        self.search_product_action.triggered.connect(self.search_product_function)

        #Set Menu Bar
        self.setMenuBar(self.menu)
        

        

    #Connecting Button Clicks to Doing Something   

    def add_product_function(self, product_name_info):
        self.stacked_layout.setCurrentIndex(0)
        self.setFixedSize(700, 600)

    def edit_product_function(self):
        self.stacked_layout.setCurrentIndex(1)
        self.setFixedSize(700, 600)

    def delete_product_function(self):
        self.stacked_layout.setCurrentIndex(2)
        self.setFixedSize(700, 600)

    def find_product_function(self):
        self.stacked_layout.setCurrentIndex(3)
        self.setFixedSize(700, 600)

    def manage_stock_function(self):
        self.stacked_layout.setCurrentIndex(4)
        self.setFixedSize(700, 600)

    def product_restock_function(self):
        self.stacked_layout.setCurrentIndex(0)
        self.setFixedSize(700, 600)

    def create_new_order_function(self):
        self.stacked_layout.setCurrentIndex(5)
        self.setFixedSize(700, 900)

    def add_new_member_function(self):
        self.stacked_layout.setCurrentIndex(6)
        self.setFixedSize(700, 600)

    def edit_member_function(self):
        self.stacked_layout.setCurrentIndex(7)
        self.setFixedSize(700, 600)


    def remove_a_member_function(self):
        self.stacked_layout.setCurrentIndex(8)
        self.setFixedSize(700, 600)

    def add_an_employee_function(self):
        self.stacked_layout.setCurrentIndex(9)
        self.setFixedSize(700, 600)

    def edit_employee_function(self):
        self.stacked_layout.setCurrentIndex(10)
        self.setFixedSize(700, 600)
    

    def remove_an_employee_function(self):
        self.stacked_layout.setCurrentIndex(11)
        self.setFixedSize(700, 600)

    def search_product_function(self):
        self.FShortcut_instance = PopUpWindow("Find A Specific Product", 500, 200)
        self.icon = QIcon(QPixmap("./images/Logo.jpg"))
        self.FShortcut_instance.setWindowIcon(self.icon)
        self.label = QLabel()
        self.pixmap = QPixmap("./images/search_icon.png")
        self.scaled_pixmap = self.pixmap.scaled(15,15, Qt.IgnoreAspectRatio, Qt.FastTransformation)
        self.label.setPixmap(self.scaled_pixmap)

        self.line_edit = QLineEdit()
        self.line_edit.setPlaceholderText("Product Name, Member Name, Employee Name")
        self.search_layout = QHBoxLayout()
        self.search_widget = QWidget()
        self.search_layout.addWidget(self.label)
        self.search_layout.addWidget(self.line_edit)
        self.search_widget.setLayout(self.search_layout)
        self.list = QListWidget()
        self.list.insertItem(0, "Dog Food")
        self.list.insertItem(1, "Mark, Reed")
        self.list.insertItem(2, "Cat Brush")
        self.list.insertItem(3, "John, Smith")
        self.main_layout = QVBoxLayout()
        self.main_layout.addWidget(self.search_widget)
        self.main_layout.addWidget(self.list)
        self.main_widget = QWidget()
        self.main_widget.setLayout(self.main_layout)
        self.FShortcut_instance.setCentralWidget(self.main_widget)
        self.FShortcut_instance.move(750,200)
        self.FShortcut_instance.show()
        self.FShortcut_instance.raise_()

def main():
    stock_control = QApplication(sys.argv) #creates new application
    main_window = MainWindow() #Creates a New instance of main window
    main_window.show()
    main_window.raise_()
    stock_control.exec_() 


if __name__ == '__main__':
    main()
