import sys

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

class MainWindow(QMainWindow):
    """This class creates the Main window"""

    def __init__(self):
        super().__init__()
        self.setWindowTitle("Beacon Vets Stock Control")
        self.setFixedSize(700, 600)
        self.icon = QIcon(QPixmap("./images/Logo.jpg"))
        self.setWindowIcon(self.icon)
        self.statusBar().showMessage('Status: Idle')
        self.Settings()
        self.stacked_layout = QStackedLayout()
        self.add_product()
        self.edit_product()
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
        self.options()
        self.widget = QWidget()
        self.widget.setLayout(self.stacked_layout)
        self.setCentralWidget(self.widget)
        #creating titles for each window


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
        self.product_id = ProductIDClass()
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
        self.product_id = ProductIDClass()
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
        self.product_id = ProductIDClass()
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
        self.product_id = ProductIDClass()
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
        self.product_id = ProductIDClass()
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
        self.product_id = ProductIDClass()
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
        self.product_id = ProductIDClass()
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

    def options(self):
        self.title = self.create_title()
        self.title.setText("Options")

        self.options_layout = QVBoxLayout()
        self.options_widget = QWidget()
        self.options_layout.addWidget(self.title)
        self.options_widget.setLayout(self.options_layout)
        self.setCentralWidget(self.options_widget)
        self.stacked_layout.addWidget(self.options_widget)

        
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
        self.options_action = QAction("Options", self)
        #Creating MenuBar
        self.menu = QMenuBar()

        #Creating ToolBar
        self.toolbar = QToolBar()
        self.addToolBar(Qt.RightToolBarArea, self.toolbar)
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
        self.optionsmenu.addAction(self.options_action)
        #self.menu.setCornerWidget(self.databasemenu, Qt.TopRightCorner)
        

        #Add tools to Toolbar
        self.addToolBar(self.toolbar)
        
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
        self.optionsmenu.triggered.connect(self.options_function)

        #Set Menu Bar
        self.setMenuBar(self.menu)

        

    #Connecting Button Clicks to Doing Something   

    def add_product_function(self):
        self.stacked_layout.setCurrentIndex(0)

    def edit_product_function(self):
        self.stacked_layout.setCurrentIndex(1)
        
    def delete_product_function(self):
        self.stacked_layout.setCurrentIndex(2)

    def find_product_function(self):
        self.stacked_layout.setCurrentIndex(3)

    def manage_stock_function(self):
        self.stacked_layout.setCurrentIndex(4)

    def product_restock_function(self):
        self.stacked_layout.setCurrentIndex(0)

    def create_new_order_function(self):
        self.stacked_layout.setCurrentIndex(5)

    def add_new_member_function(self):
        self.stacked_layout.setCurrentIndex(6)

    def edit_member_function(self):
        self.stacked_layout.setCurrentIndex(7)


    def remove_a_member_function(self):
        self.stacked_layout.setCurrentIndex(8)

    def add_an_employee_function(self):
        self.stacked_layout.setCurrentIndex(9)

    def edit_employee_function(self):
        self.stacked_layout.setCurrentIndex(10)
    

    def remove_an_employee_function(self):
        self.stacked_layout.setCurrentIndex(11)

    def options_function(self):
        self.stacked_layout.setCurrentIndex(12)

    def set(self):
        path = QFileDialog.getOpenFileName()
        self.connection = SQLConnection(path)
        ok = self.connection.open_database()
        print(ok)

    def close_database_function(self):
        if self.connection:
            self.connection.close_database()
        else:
            print("no db to close")










def main():
    stock_control = QApplication(sys.argv) #creates new application
    main_window = MainWindow() #Creates a New instance of main window
    main_window.show()
    main_window.raise_()
    stock_control.exec_() 


if __name__ == '__main__':
    main()
