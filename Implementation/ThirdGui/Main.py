import sys

from PyQt4.QtCore import *
from PyQt4.QtGui import *
from ProductSearchClass import *
from AddingProductClass import *
from AddingMemberClass import *
from AddingEmployeeClass import *
from StockManagementClass import *

class MainWindow(QMainWindow):
    """This class creates the Main window"""

    def __init__(self):
        super().__init__()
        self.setWindowTitle("Beacon Vets Stock Control")
        self.resize(900, 800)
        self.icon = QIcon(QPixmap("./images/Logo.jpg"))
        self.setWindowIcon(self.icon)
        self.statusBar().showMessage('Status: Idle')
        self.Settings()
        self.stacked_layout = QStackedLayout()
        self.search_product()
        self.add_product()
        self.add_member()
        self.add_employee()
        self.manage_stock()
        self.product_id = QLineEdit()
        self.product_id.setPlaceholderText("ProductID: 02")
        self.widget = QWidget()
        self.widget.setLayout(self.stacked_layout)
        self.setCentralWidget(self.widget)

    def search_product(self):
        self.search_product_instance = searchProductClass()
        #create layout to hold widgets
        self.search_product_layout = QVBoxLayout()
        self.search_product_layout.addWidget(self.search_product_instance)                                     
        self.select_animal_widget = QWidget()
        self.select_animal_widget.setLayout(self.search_product_layout)
        self.setCentralWidget(self.select_animal_widget)
        self.stacked_layout.addWidget(self.select_animal_widget)

        
    def add_product(self):
        self.add_product_instance = addProductClass()
        
        self.add_product_layout = QVBoxLayout()
        self.add_product_layout.addWidget(self.add_product_instance)
        self.add_product_widget = QWidget()
        self.add_product_widget.setLayout(self.add_product_layout)
        self.setCentralWidget(self.add_product_widget)
        self.stacked_layout.addWidget(self.add_product_widget)
        


    def add_member(self):
        self.add_member_instance = addMemberClass()

        self.add_member_layout = QVBoxLayout()
        self.add_member_widget = QWidget()
        self.add_member_layout.addWidget(self.add_member_instance)
        self.add_member_widget.setLayout(self.add_member_layout)
        self.setCentralWidget(self.add_member_widget)
        self.stacked_layout.addWidget(self.add_member_widget)
        


    def add_employee(self):
        self.add_employee_instance = addEmployeeClass("Adding New Empoyee", "Add New Employee")

        self.add_employee_layout = QVBoxLayout()
        self.add_employee_widget = QWidget()
        self.add_employee_layout.addWidget(self.add_employee_instance)
        self.add_employee_widget.setLayout(self.add_employee_layout)
        self.setCentralWidget(self.add_employee_widget)
        self.stacked_layout.addWidget(self.add_employee_widget)

    def manage_stock(self):
        self.manage_stock_instance = manageStockClass()
        self.product_id = QLineEdit()
        self.product_id.setPlaceholderText("ProductID: 02")
        self.manage_stock_layout = QVBoxLayout()
        self.manage_stock_widget = QWidget()
        self.manage_stock_layout.addWidget(self.product_id)
        self.manage_stock_layout.addWidget(self.manage_stock_instance)
        self.manage_stock_widget.setLayout(self.manage_stock_layout)
        self.setCentralWidget(self.manage_stock_widget)
        self.stacked_layout.addWidget(self.manage_stock_widget)
        
        

        
    def Settings(self):
        #Adding Actions
        self.add_new_product = QAction("Add a New Product", self)
        self.delete_a_product = QAction("Delete a Product", self)
        self.find_a_product = QAction("Find a Product", self)
        self.manage_current_stock = QAction("Manage Stock", self)
        self.product_restock = QAction("Product Restock", self)
        self.create_order = QAction("Create New Order", self)
        self.add_new_member = QAction("Add New Member", self)
        self.remove_a_member = QAction("Delete a Member", self)
        self.add_an_employee = QAction("Add Employee", self)
        self.remove_an_employee = QAction("Remove Employee", self)
        #Creating MenuBar
        self.menu = QMenuBar()

        #Creating ToolBar
        self.toolbar = QToolBar()
        self.addToolBar(Qt.RightToolBarArea, self.toolbar)
        #self.toolbar.setMovable(False)


        #Adding Menu to MenuBar
        
        self.productsmenu = self.menu.addMenu("Product")
        self.productsmenu.addAction(self.add_new_product)
        self.productsmenu.addAction(self.delete_a_product)
        self.productsmenu.addAction(self.find_a_product)
        self.stockmenu = self.menu.addMenu("Stock")
        self.stockmenu.addAction(self.manage_current_stock)
        self.stockmenu.addAction(self.product_restock)
        self.ordermenu = self.menu.addMenu("Order")
        self.ordermenu.addAction(self.create_order)
        self.membersmenu = self.menu.addMenu("Member")
        self.membersmenu.addAction(self.add_new_member)
        self.membersmenu.addAction(self.remove_a_member)
        self.employeemenu = self.menu.addMenu("Employee")
        self.employeemenu.addAction(self.add_an_employee)
        self.employeemenu.addAction(self.remove_an_employee)
        self.databasemenu = self.menu.addMenu("Options")
        #self.menu.setCornerWidget(self.databasemenu, Qt.TopRightCorner)
        

        #Add tools to Toolbar
        self.addToolBar(self.toolbar)
        
         #Add connections to buttons
        self.add_new_product.triggered.connect(self.add_product_function)
        self.delete_a_product.triggered.connect(self.delete_product_function)
        self.find_a_product.triggered.connect(self.find_product_function)
        self.manage_current_stock.triggered.connect(self.manage_stock_function)
        self.product_restock.triggered.connect(self.product_restock_function)
        self.create_order.triggered.connect(self.create_new_order_function)
        self.add_new_member.triggered.connect(self.add_new_member_function)
        self.remove_a_member.triggered.connect(self.remove_a_member_function)
        self.add_an_employee.triggered.connect(self.add_an_employee_function)
        self.remove_an_employee.triggered.connect(self.remove_an_employee_function)

        #Set Menu Bar
        self.setMenuBar(self.menu)

        

    #Connecting Button Clicks to Doing Something   

    def add_product_function(self):
        self.stacked_layout.setCurrentIndex(1)
        
    def delete_product_function(self):
        print("2")

    def find_product_function(self):
        self.stacked_layout.setCurrentIndex(0)

    def manage_stock_function(self):
        self.stacked_layout.setCurrentIndex(4)

    def product_restock_function(self):
        print("5")

    def create_new_order_function(self):
        print("6")

    def add_new_member_function(self):
        self.stacked_layout.setCurrentIndex(2)

    def remove_a_member_function(self):
        print("8")

    def add_an_employee_function(self):
        self.stacked_layout.setCurrentIndex(3)

    def remove_an_employee_function(self):
        print("10")

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
