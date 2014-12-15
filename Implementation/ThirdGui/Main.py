import sys

from PyQt4.QtCore import *
from PyQt4.QtGui import *
from PyQt4 import QtGui

class MainWindow(QMainWindow):
    """This class creates the Main window"""

    def __init__(self):
        super().__init__()
        self.setWindowTitle("Beacon Vets Stock Control")
        self.resize(800, 800)
        self.icon = QIcon(QPixmap("./Logo.jpg"))
        self.setWindowIcon(self.icon)
        self.statusBar().showMessage('Status: Idle')
        self.Settings()

    def Settings(self):
        #Adding Actions
        self.add_new_product = QAction("Add a New Product", self)
        self.delete_a_product = QAction("Delete a Product", self)
        self.find_a_product = QAction("Find a Product", self)
        self.manage_stock = QAction("Manage Stock", self)
        self.product_restock = QAction("Product Restock", self)
        self.create_order = QAction("Create New Order", self)
        self.add_new_member = QAction("Add New Member", self)
        self.remove_a_member = QAction("Delete a Member", self)
        self.add_an_employee = QAction("Add Employee", self)
        self.remove_an_employee = QAction("Remove Employee", self)
        self.open_a_database = QAction("Open Database", self)
        self.close_a_database = QAction("Close Database", self)

        #Creating MenuBar
        self.menu = QMenuBar()

        #Creating ToolBar
        #self.toolbar = QToolBar()       #No Toolbar needed


        #Adding Menu to MenuBar
        
        self.productsmenu = self.menu.addMenu("Product")
        self.productsmenu.addAction(self.add_new_product)
        self.productsmenu.addAction(self.delete_a_product)
        self.productsmenu.addAction(self.find_a_product)
        self.stockmenu = self.menu.addMenu("Stock")
        self.stockmenu.addAction(self.manage_stock)
        self.stockmenu.addAction(self.product_restock)
        self.ordermenu = self.menu.addMenu("Order")
        self.ordermenu.addAction(self.create_order)
        self.membersmenu = self.menu.addMenu("Member")
        self.membersmenu.addAction(self.add_new_member)
        self.membersmenu.addAction(self.remove_a_member)
        self.employeemenu = self.menu.addMenu("Employee")
        self.employeemenu.addAction(self.add_an_employee)
        self.employeemenu.addAction(self.remove_an_employee)
        self.databasemenu = self.menu.addMenu("Database")
        self.databasemenu.addAction(self.open_a_database)
        self.databasemenu.addAction(self.close_a_database)
        #self.menu.setCornerWidget(self.databasemenu, Qt.TopRightCorner)
        

        #Add tools to Toolbar
        #self.addToolBar(self.toolbar)
        
         #Add connections to buttons
        self.add_new_product.triggered.connect(self.add_product_function)
        self.delete_a_product.triggered.connect(self.delete_product_function)
        self.find_a_product.triggered.connect(self.find_product_function)
        self.manage_stock.triggered.connect(self.manage_stock_function)
        self.product_restock.triggered.connect(self.product_restock_function)
        self.create_order.triggered.connect(self.create_new_order_function)
        self.add_new_member.triggered.connect(self.add_new_member_function)
        self.remove_a_member.triggered.connect(self.remove_a_member_function)
        self.add_an_employee.triggered.connect(self.add_an_employee_function)
        self.remove_an_employee.triggered.connect(self.remove_an_employee_function)
        self.open_a_database.triggered.connect(self.open_database_function)
        self.close_a_database.triggered.connect(self.close_database_function)

        #Set Menu Bar
        self.setMenuBar(self.menu)


    #Connecting Button Clicks to Doing Something   

    def add_product_function(self):
        print("1")
        
    def delete_product_function(self):
        print("2")

    def find_product_function(self):
        print("3")

    def manage_stock_function(self):
        print("4")

    def product_restock_function(self):
        print("5")

    def create_new_order_function(self):
        print("6")

    def add_new_member_function(self):
        print("7")

    def remove_a_member_function(self):
        print("8")

    def add_an_employee_function(self):
        print("9")

    def remove_an_employee_function(self):
        print("10")

    def open_database_function(self):
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
