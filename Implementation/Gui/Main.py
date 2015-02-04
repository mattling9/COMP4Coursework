import sys, shutil, sqlite3, smtplib, datetime

from PyQt4.QtCore import *
from PyQt4.QtGui import *
from PyQt4.QtSql import *
from ProductSearchClass import *

from AddingProductClass import *
from EditProductClass import *
from DeleteProductClass import *
from PopUpMenuClass import *
from AddingMemberClass import *
from AddingEmployeeClass import *
from StockManagementClass import *
from ProductIDClass import *
from CreatingOrderClass import *
from PopUpMenuClass import *
from DatabaseClass import *
from FindingPopUpClass import *
from SQLConnection import *
from CreatingTable import *
from AddingRemovingData import *
from PreferencesClass import *
from LogInClass import *
from PasswordResetClass import *
from ErrorMessageClass import *

class MainWindow(QMainWindow):
    """This class creates the Main window"""

    def __init__(self):
        super().__init__()
        check_date()
        add_admin_employee()
        settings = getSettings()
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
        self.preferences()
        self.log_in()
        self.password_reset()
        self.widget = QWidget()
        self.widget.setLayout(self.stacked_layout)
        self.setCentralWidget(self.widget)
        self.log_in_function()
        if settings:
            self.setWindowTitle("{0} Stock Control".format(settings[0][2]))
            self.icon = QIcon("{0}".format(str(settings[0][1])))
        else:
            self.setWindowTitle(" No Current Company Name")
            self.icon = QIcon("")

        self.setWindowIcon(self.icon)
        
        


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
        self.title = self.create_title()
        self.title.setText("Edit Product ")
        self.edit_product_instance = editProductClass()
        self.edit_product_layout = QVBoxLayout()
        self.edit_product_layout.addWidget(self.title)
        self.edit_product_layout.addWidget(self.edit_product_instance)
        self.edit_product_widget = QWidget()
        self.edit_product_widget.setLayout(self.edit_product_layout)
        self.setCentralWidget(self.edit_product_widget)
        self.stacked_layout.addWidget(self.edit_product_widget)

    def change_view(self):
        if not self.edit_product_instance.isEnabled():
            self.edit_product_instance.setEnabled(True)

    def delete_product(self):
        self.title = self.create_title()
        self.title.setText("Delete Product ")
        self.delete_product_instance = deleteProductClass()
        self.delete_product_layout = QVBoxLayout()
        self.delete_product_layout.addWidget(self.title)
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
        self.edit_member_layout = QVBoxLayout()
        self.edit_member_widget = QWidget()
        self.edit_member_layout.addWidget(self.title)
        self.edit_member_layout.addWidget(self.edit_member_instance)
        self.edit_member_widget.setLayout(self.edit_member_layout)
        self.setCentralWidget(self.edit_member_widget)
        self.stacked_layout.addWidget(self.edit_member_widget)

    def delete_member(self):
        self.title = self.create_title()
        self.title.setText("Delete Member")

        
        self.delete_member_instance = addMemberClass("Delete Member")
        self.delete_member_layout = QVBoxLayout()
        self.delete_member_widget = QWidget()
        self.delete_member_layout.addWidget(self.title)
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
        self.edit_employee_layout = QVBoxLayout()
        self.edit_employee_widget = QWidget()
        self.edit_employee_layout.addWidget(self.title)
        self.edit_employee_layout.addWidget(self.edit_employee_instance)
        self.edit_employee_widget.setLayout(self.edit_employee_layout)
        self.setCentralWidget(self.edit_employee_widget)
        self.stacked_layout.addWidget(self.edit_employee_widget)

    def delete_employee(self):
        self.title = self.create_title()
        self.title.setText("Delete Employee")
        self.delete_employee_instance = addEmployeeClass("Delete Employee")
        self.delete_employee_layout = QVBoxLayout()
        self.delete_employee_widget = QWidget()
        self.delete_employee_layout.addWidget(self.title)
        self.delete_employee_layout.addWidget(self.delete_employee_instance)
        self.delete_employee_widget.setLayout(self.delete_employee_layout)
        self.setCentralWidget(self.delete_employee_widget)
        self.stacked_layout.addWidget(self.delete_employee_widget)

    def manage_stock(self):
        self.title = self.create_title()
        self.title.setText("Manage Stock")
        self.manage_stock_instance = manageStockClass()
        self.manage_stock_layout = QVBoxLayout()
        self.manage_stock_widget = QWidget()
        self.manage_stock_layout.addWidget(self.title)
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
        self.create_order_instance.display_table.update()
        self.create_order_instance.current_order.update()

    def search(self):
        self.search_instance = SearchClass()
        self.search_instance.move(750,300)
        self.search_instance.show()
        self.search_instance.raise_()

    def preferences(self):
        self.preferences_instance = preferencesClass()
        self.stacked_layout.addWidget(self.preferences_instance)

    def log_in(self):
        self.log_in_instance = logInClass()
        self.log_in_instance.enter_button.clicked.connect(self.find_account)
        self.log_in_instance.connect(self.log_in_instance.forgot_password, SIGNAL('clicked()'), self.reset_password)
        self.stacked_layout.addWidget(self.log_in_instance)

    def password_reset(self):
        self.password_reset_instance = PasswordResetClass()
        self.password_reset_instance.button.clicked.connect(self.display_message)
        self.stacked_layout.addWidget(self.password_reset_instance)
        
    def Settings(self):
        #Adding Actions
        self.add_product_action = QAction("Add a New Product", self)
        self.edit_product_action = QAction("Edit a Product", self)
        self.delete_a_product_action = QAction("Delete a Product", self)
        self.find_a_product_action = QAction("Find a Product", self)
        self.manage_current_stock_action = QAction("Manage Stock", self)
        self.create_order_action = QAction("Create New Order", self)
        self.add_new_member_action = QAction("Add New Member", self)
        self.edit_member_action  = QAction("Edit a Member", self)
        self.remove_a_member_action = QAction("Delete a Member", self)
        self.add_an_employee_action = QAction("Add Employee", self)
        self.edit_employee_action = QAction("Edit an Employee", self)
        self.remove_an_employee_action = QAction("Remove Employee", self)
        self.preferences_action = QAction("Preferences", self)
        self.search_product_action = QAction("Search Window", self)
        self.search_product_action.setShortcut("Ctrl+F")
        self.log_off_action = QAction("Log off", self)
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
        self.optionsmenu.addAction(self.preferences_action)
        self.optionsmenu.addAction(self.search_product_action)
        self.optionsmenu.addAction(self.log_off_action)
        #self.menu.setCornerWidget(self.databasemenu, Qt.TopRightCorner)
        

        #Add tools to Toolbar
        #self.addToolBar(self.toolbar)
        
         #Add connections to buttons
        self.add_product_action.triggered.connect(self.add_product_function)
        self.edit_product_action.triggered.connect(self.edit_product_function)
        self.delete_a_product_action.triggered.connect(self.delete_product_function)
        self.find_a_product_action.triggered.connect(self.find_product_function)
        self.manage_current_stock_action.triggered.connect(self.manage_stock_function)
        self.create_order_action.triggered.connect(self.create_new_order_function)
        self.add_new_member_action.triggered.connect(self.add_new_member_function)
        self.edit_member_action.triggered.connect(self.edit_member_function)
        self.remove_a_member_action.triggered.connect(self.remove_a_member_function)
        self.add_an_employee_action.triggered.connect(self.add_an_employee_function)
        self.edit_employee_action.triggered.connect(self.edit_employee_function)
        self.remove_an_employee_action.triggered.connect(self.remove_an_employee_function)
        self.search_product_action.triggered.connect(self.search_product_function)
        self.preferences_action.triggered.connect(self.preferences_function)
        self.log_off_action.triggered.connect(self.log_in_function)

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
        self.setFixedSize(900, 800)

    def create_new_order_function(self):
        self.create_order_instance.current_order.clearContents()
        for line in range(0, self.create_order_instance.current_order.rowCount()):
            self.create_order_instance.current_order.removeRow(line)
        self.create_order_instance.current_order.removeRow(0)
        self.create_order_instance.subtotal.setText("0.0")
        self.create_order_instance.total.setText("0.0")
        self.create_order_instance.discount_line_edit.setText("0.0")
        self.stacked_layout.setCurrentIndex(5)
        self.setFixedSize(900, 850)
        self.create_order_instance.model.select()
        self.move(300,1)

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
        self.search()

    def preferences_function(self):
        self.stacked_layout.setCurrentIndex(12)
        self.setFixedSize(900, 850)

    def log_in_function(self):
        self.stacked_layout.setCurrentIndex(13)
        self.setFixedSize(600,400)
        self.menu.hide()
        self.log_in_instance.username.setText("")
        self.log_in_instance.password.setText("")

    def password_reset_function(self):
        self.stacked_layout.setCurrentIndex(14)
        self.setFixedSize(600,400)
        self.password_reset_instance.email_address.setText("")
        
    def find_account(self):
        encrypted_password_entered = change_password(self.log_in_instance.password.text(), 3)
        self.return_signal = find_username_and_password(self.log_in_instance.username.text(), encrypted_password_entered)
        if self.return_signal == 1:
            self.error_message_instance = ErrorMessageClass("Sorry the Password you entered is incorrect")
            self.error_message_instance.move(750,500)
            self.error_message_instance.show()
            self.error_message_instance.raise_()
        elif self.return_signal == 2:
            self.error_message_instance = ErrorMessageClass("Sorry the Username and Password you entered are incorrect")
            self.error_message_instance.move(750,500)
            self.error_message_instance.show()
            self.error_message_instance.raise_()
        elif self.return_signal == 3:
            print("Log In Sucessful")
            self.create_new_order_function()
            self.menu.show()



    def reset_password(self):
        self.password_reset_function()

    def display_message(self):
        self.valid = find_employee_by_email(self.password_reset_instance.email_address.text())
        if self.valid:
            username = get_employee_username(self.password_reset_instance.email_address.text())
            password = get_employee_password(self.password_reset_instance.email_address.text())
            first_name = get_employee_first_name(self.password_reset_instance.email_address.text())
            self.send_password_reset_email(self.password_reset_instance.email_address.text(), username, password, first_name)
            self.log_in_function()
            self.error_message_instance = ErrorMessageClass("Your Username and Password have been sent to your email address.")
            self.error_message_instance.move(750,500)
            self.error_message_instance.show()
            self.error_message_instance.raise_()

        else:
            self.error_message_instance = ErrorMessageClass("Sorry the Email address does not match any of the Accounts.")

    def send_password_reset_email(self, email_address, username, password, first_name):
        print(username)
        print(password)
        settings = getSettings()
        subject = ("Your Beacon Vet Account Details")

        send_from = '{0}'.format(settings[0][10])
        decrypted_password = change_password(settings[0][11], -3)

        msg = "\r\n".join([
              "From: BeaconVets@Admin.com",
                "To: {0}".format(email_address),
                "Subject: Beacon Vets Account Details",
              "",
              ("Hello {0}, Here are your account details: \n \n Username:   {1} \n  Password:   {2}".format(first_name, username, password))])

        mail = smtplib.SMTP('smtp.gmail.com','587')
        mail.ehlo()
        mail.starttls()
        mail.login(send_from, decrypted_password)
        mail.sendmail(send_from, email_address, msg)
        mail.close()
        print("email sent")    

def main():
    stock_control = QApplication(sys.argv) #creates new application
    main_window = MainWindow() #Creates a New instance of main window
    main_window.show()
    main_window.raise_()
    stock_control.exec_() 


if __name__ == '__main__':
    main()
