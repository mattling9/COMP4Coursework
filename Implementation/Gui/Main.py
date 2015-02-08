import sys, shutil, sqlite3, smtplib, datetime

from matplotlib import pyplot as plt
from PyQt4.QtCore import *
from PyQt4.QtGui import *
from PyQt4.QtSql import *
from AddingProductClass import *
from EditProductClass import *
from DeleteProductClass import *
from PopUpMenuClass import *
from AddingMemberClass import *
from EditMemberClass import *
from DeleteMemberClass import *
from AddingEmployeeClass import *
from EditEmployeeClass import *
from DeleteEmployeeClass import *
from StockManagementClass import *
from ProductIDClass import *
from CreatingOrderClass import *
from DatabaseClass import *
from FindingPopUpClass import *
from SQLConnection import *
from CreatingTable import *
from AddingRemovingData import *
from PreferencesClass import *
from LogInClass import *
from PasswordResetClass import *
from ErrorMessageClass import *
from ChangePasswordClass import *
from StyleSheet import *
from CustomToolbarClass import *

class MainWindow(QMainWindow):
    """This class creates the Main window"""

    def __init__(self):
        super().__init__()
        check_date()
        add_admin_employee()
        settings = getSettings()
        self.setStyleSheet(css)
        self.connection = SQLConnection("ProductDatabase.db")
        open_db = self.connection.open_database()
        self.Settings()
        self.stacked_layout = QStackedLayout()
        self.add_product()
        self.edit_product()
        self.delete_product()
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
        self.change_password()
        self.edit_member()
        self.widget = QWidget()
        self.widget.setLayout(self.stacked_layout)

        #Adding The Custom TitleBar
        self.setWindowFlags(Qt.FramelessWindowHint)
        self.title_bar = TitleBar()
        self.title_bar.minimise.clicked.connect(self.minimise_main_window)
        self.title_bar.close.clicked.connect(self.close_main_window)
        self.main_layout = QVBoxLayout()
        self.main_widget = QWidget()
        self.main_layout.addWidget(self.title_bar)
        self.main_layout.addWidget(self.menu)
        self.main_layout.addWidget(self.widget)
        self.main_widget.setLayout(self.main_layout)
        self.setCentralWidget(self.main_widget)
        
        
        self.log_in_function()
        if settings:
            self.setWindowTitle("{0} Stock Control".format(settings[0][2]))
            self.icon = QIcon("{0}".format(str(settings[0][1])))
        else:
            self.setWindowTitle(" No Current Company Name")
            self.icon = QIcon("")

        self.setWindowIcon(self.icon)

    def minimise_main_window(self):
        self.showMinimized()

    def close_main_window(self):
        self.close()

    def mousePressEvent(self,event):

        if event.button() == Qt.LeftButton:
            self.moving = True; self.offset = event.pos()

    def mouseMoveEvent(self,event):
        try:
            if self.moving:
                self.move(event.globalPos()-self.offset)
        except AttributeError:
            pass

        
        


    def create_title(self):
        self.title = QLabel("Default Text")
        self.title.setAlignment(Qt.AlignCenter)
        self.title.setObjectName('title')
        return self.title

        
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
        
        self.add_member_instance = addMemberClass("Add Member")
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

        
        self.edit_member_instance = editMemberClass("Edit Member")        
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

        
        self.delete_member_instance = deleteMemberClass("Delete Member")
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
        self.add_employee_instance = addEmployeeClass("Add Employee")
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
        self.edit_employee_instance = editEmployeeClass("Edit Employee")
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
        self.delete_employee_instance = deleteEmployeeClass("Delete Employee")
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
        self.preferences_instance.connect(self.preferences_instance.question, SIGNAL('clicked()'), self.email_question)
        self.stacked_layout.addWidget(self.preferences_instance)

    def log_in(self):
        self.log_in_instance = logInClass()
        self.log_in_instance.enter_button.clicked.connect(self.find_account)
        self.log_in_instance.connect(self.log_in_instance.forgot_password, SIGNAL('clicked()'), self.reset_password)
        self.stacked_layout.addWidget(self.log_in_instance)

    def password_reset(self):
        self.password_reset_instance = PasswordResetClass()
        self.password_reset_instance.button.clicked.connect(self.display_message)
        self.password_reset_instance.back.clicked.connect(self.log_in_function)
        self.stacked_layout.addWidget(self.password_reset_instance)

    def change_password(self):
        self.change_password_instance = ChangePasswordClass("Please Enter a new password, then re-enter it below.", 0)
        self.change_password_instance.button.clicked.connect(self.match_passwords)
        self.stacked_layout.addWidget(self.change_password_instance)
        self.change_password_instance2 = ChangePasswordClass("Please enter a new password below. The Code has been sent to your email address.", 1)
        self.change_password_instance2.button.clicked.connect(self.match_codes)
        self.stacked_layout.addWidget(self.change_password_instance2)
        
        
        
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
        self.remove_an_employee_action = QAction("Delete Employee", self)
        self.explanation_action = QAction("Why Can't I Access These?", self)
        self.preferences_action = QAction("Preferences", self)
        self.search_product_action = QAction("Search Window", self)
        self.search_product_action.setShortcut("Ctrl+F")
        self.change_password_action = QAction("Change Password", self)
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
        self.employeemenu.addAction(self.explanation_action)
        self.optionsmenu = self.menu.addMenu("Options")
        self.optionsmenu.addAction(self.preferences_action)
        self.optionsmenu.addAction(self.search_product_action)
        self.optionsmenu.addAction(self.change_password_action)
        self.optionsmenu.addAction(self.log_off_action)
        #self.menu.setCornerWidget(self.databasemenu, Qt.TopRightCorner)
        

        #Add tools to Toolbar
        #self.addToolBar(self.toolbar)
        
         #Add connections to buttons
        self.add_product_action.triggered.connect(self.add_product_function)
        self.edit_product_action.triggered.connect(self.edit_product_function)
        self.delete_a_product_action.triggered.connect(self.delete_product_function)
        self.manage_current_stock_action.triggered.connect(self.manage_stock_function)
        self.create_order_action.triggered.connect(self.create_new_order_function)
        self.add_new_member_action.triggered.connect(self.add_new_member_function)
        self.edit_member_action.triggered.connect(self.edit_member_function)
        self.remove_a_member_action.triggered.connect(self.remove_a_member_function)
        self.add_an_employee_action.triggered.connect(self.add_an_employee_function)
        self.edit_employee_action.triggered.connect(self.edit_employee_function)
        self.remove_an_employee_action.triggered.connect(self.remove_an_employee_function)
        self.explanation_action.triggered.connect(self.explanation_function)
        self.search_product_action.triggered.connect(self.search_product_function)
        self.preferences_action.triggered.connect(self.preferences_function)
        self.log_off_action.triggered.connect(self.log_in_function)
        self.change_password_action.triggered.connect(self.change_password_function)

        #Set Menu Bar
        #self.setMenuBar(self.menu)

        

        

    #Connecting Button Clicks to Doing Something   

    def add_product_function(self, product_name_info):
        self.stacked_layout.setCurrentIndex(0)
        self.add_product_instance.price_button.setText("")
        self.add_product_instance.size_integer.setText("")
        self.add_product_instance.size_button.setCurrentIndex(0)
        self.add_product_instance.category1_button.setCurrentIndex(0)
        self.add_product_instance.category2_button.setCurrentIndex(0)
        self.add_product_instance.location1.setText("")
        self.add_product_instance.location2.setText("")
        self.add_product_instance.product_name.setText("")
        self.add_product_instance.image_pixmap = QPixmap(".\ProductImages\Default.jpg")
        self.add_product_instance.scaled_image = self.add_product_instance.image_pixmap.scaled(300, 300, Qt.IgnoreAspectRatio, Qt.FastTransformation)
        self.add_product_instance.image.setPixmap(self.add_product_instance.scaled_image)
        self.edit_product_instance.path.setText(".\ProductImages\Default.jpg")
        
        self.setFixedSize(700, 600)

    def edit_product_function(self):
        self.stacked_layout.setCurrentIndex(1)
        self.edit_product_instance.find_product_id_line_edit.setText("")
        self.edit_product_instance.price_button.setText("")
        self.edit_product_instance.size_integer.setText("")
        self.edit_product_instance.size_button.setCurrentIndex(0)
        self.edit_product_instance.category1_button.setCurrentIndex(0)
        self.edit_product_instance.category2_button.setCurrentIndex(0)
        self.edit_product_instance.location1.setText("")
        self.edit_product_instance.location2.setText("")
        self.edit_product_instance.product_name.setText("")
        self.edit_product_instance.image_pixmap = QPixmap(".\ProductImages\Default.jpg")
        self.edit_product_instance.scaled_image = self.edit_product_instance.image_pixmap.scaled(300, 300, Qt.IgnoreAspectRatio, Qt.FastTransformation)
        self.edit_product_instance.image.setPixmap(self.edit_product_instance.scaled_image)
        self.edit_product_instance.path.setText(".\ProductImages\Default.jpg")
        
        self.setFixedSize(700, 700)
    def delete_product_function(self):
        self.stacked_layout.setCurrentIndex(2)
        self.delete_product_instance.find_product_id_line_edit.setText("")
        self.delete_product_instance.price_button.setText("")
        self.delete_product_instance.size_integer.setText("")
        self.delete_product_instance.size_button.setCurrentIndex(0)
        self.delete_product_instance.category1_button.setCurrentIndex(0)
        self.delete_product_instance.category2_button.setCurrentIndex(0)
        self.delete_product_instance.location1.setText("")
        self.delete_product_instance.location2.setText("")
        self.delete_product_instance.product_name.setText("")
        self.delete_product_instance.image_pixmap = QPixmap(".\ProductImages\Default.jpg")
        self.delete_product_instance.scaled_image = self.delete_product_instance.image_pixmap.scaled(300, 300, Qt.IgnoreAspectRatio, Qt.FastTransformation)
        self.delete_product_instance.image.setPixmap(self.delete_product_instance.scaled_image)
        self.delete_product_instance.path.setText(".\ProductImages\Default.jpg")
        self.setFixedSize(700, 700)

    def manage_stock_function(self):
        self.stacked_layout.setCurrentIndex(3)
        self.manage_stock_instance.product_id.setText("")
        self.manage_stock_instance.stock1.setValue(0)
        self.manage_stock_instance.stock2.setValue(0)
        self.manage_stock_instance.prediction.setText("")
        self.manage_stock_instance.current_stock_groupbox.setDisabled(True)
        self.manage_stock_instance.stock_prediction_groupbox.setDisabled(True)
        self.manage_stock_instance.path = (".\images\Default.png")
        self.manage_stock_instance.image_pixmap = QPixmap(self.manage_stock_instance.path)
        self.manage_stock_instance.scaled_image = self.manage_stock_instance.image_pixmap.scaled(180, 180, Qt.IgnoreAspectRatio, Qt.FastTransformation)
        self.manage_stock_instance.image.setPixmap(self.manage_stock_instance.scaled_image)
        plt.clf()
        self.setFixedSize(900, 850)

    def create_new_order_function(self):
        self.create_order_instance.current_order.clearContents()
        for line in range(0, self.create_order_instance.current_order.rowCount()):
            self.create_order_instance.current_order.removeRow(line)
        self.create_order_instance.current_order.removeRow(0)
        self.create_order_instance.subtotal.setText("0.0")
        self.create_order_instance.total.setText("0.0")
        self.create_order_instance.discount_line_edit.setText("0.0")
        self.stacked_layout.setCurrentIndex(4)
        self.setFixedSize(1200, 770)
        self.create_order_instance.model.select()
        self.move(300,1)

    def add_new_member_function(self):
        self.stacked_layout.setCurrentIndex(5)
        self.add_member_instance.name_title.setCurrentIndex(0)
        self.add_member_instance.first_name.setText("")
        self.add_member_instance.last_name.setText("")
        self.add_member_instance.postcode.setText("")
        self.add_member_instance.county.setCurrentIndex(0)
        self.add_member_instance.city.setText("")
        self.add_member_instance.town.setText("")
        self.add_member_instance.street.setText("")
        self.add_member_instance.houseno.setValue(0)
        self.add_member_instance.telephone_number.setText("")
        self.add_member_instance.email.setText("")
        self.setFixedSize(700, 750)

    def edit_member_function(self):
        self.stacked_layout.setCurrentIndex(6)
        self.edit_member_instance.find_member_id_line_edit.setText("")
        self.edit_member_instance.name_title.setCurrentIndex(0)
        self.edit_member_instance.first_name.setText("")
        self.edit_member_instance.last_name.setText("")
        self.edit_member_instance.postcode.setText("")
        self.edit_member_instance.county.setCurrentIndex(0)
        self.edit_member_instance.city.setText("")
        self.edit_member_instance.town.setText("")
        self.edit_member_instance.street.setText("")
        self.edit_member_instance.houseno.setValue(0)
        self.edit_member_instance.telephone_number.setText("")
        self.edit_member_instance.email.setText("")
        self.setFixedSize(700, 800)
    def remove_a_member_function(self):
        self.stacked_layout.setCurrentIndex(7)
        self.edit_member_instance.find_member_id_line_edit.setText("")
        self.delete_member_instance.name_title.setCurrentIndex(0)
        self.delete_member_instance.first_name.setText("")
        self.delete_member_instance.last_name.setText("")
        self.delete_member_instance.postcode.setText("")
        self.delete_member_instance.county.setCurrentIndex(0)
        self.delete_member_instance.city.setText("")
        self.delete_member_instance.town.setText("")
        self.delete_member_instance.street.setText("")
        self.delete_member_instance.houseno.setValue(0)
        self.delete_member_instance.telephone_number.setText("")
        self.delete_member_instance.email.setText("")
        self.setFixedSize(700, 800)

    def add_an_employee_function(self):
        self.stacked_layout.setCurrentIndex(8)
        self.add_employee_instance.user_name_output.setText("")
        self.add_employee_instance.first_name.setText("")
        self.add_employee_instance.first_name_output.setText("")
        self.add_employee_instance.last_name.setText("")
        self.add_employee_instance.last_name_output.setText("")
        self.add_employee_instance.email_address.setText("")
        self.add_employee_instance.email_address_output.setText("")
        self.setFixedSize(700, 600)

    def edit_employee_function(self):
        self.stacked_layout.setCurrentIndex(9)
        self.edit_employee_instance.find_employee_id_line_edit.setText("")
        self.edit_employee_instance.user_name_output.setText("")
        self.edit_employee_instance.first_name.setText("")
        self.edit_employee_instance.first_name_output.setText("")
        self.edit_employee_instance.last_name.setText("")
        self.edit_employee_instance.last_name_output.setText("")
        self.edit_employee_instance.email_address.setText("")
        self.edit_employee_instance.email_address_output.setText("")
        self.setFixedSize(700, 650)
    

    def remove_an_employee_function(self):
        self.stacked_layout.setCurrentIndex(10)
        self.delete_employee_instance.find_employee_id_line_edit.setText("")
        self.delete_employee_instance.user_name_output.setText("")
        self.delete_employee_instance.first_name.setText("")
        self.delete_employee_instance.first_name_output.setText("")
        self.delete_employee_instance.last_name.setText("")
        self.delete_employee_instance.last_name_output.setText("")
        self.delete_employee_instance.email_address.setText("")
        self.delete_employee_instance.email_address_output.setText("")
        self.setFixedSize(700, 650)

    def explanation_function(self):
        self.error_message_instance = ErrorMessageClass("The Reason you cannot access the above options is because you \n must be logged into the master account to access them.")
        self.error_message_instance.move(750,500)
        self.error_message_instance.show()
        self.error_message_instance.raise_()
    def search_product_function(self):
        self.search()

    def preferences_function(self):
        self.stacked_layout.setCurrentIndex(11)
        self.setFixedSize(900, 850)

    def log_in_function(self):
        self.stacked_layout.setCurrentIndex(12)
        self.setFixedSize(600,460)
        self.menu.hide()
        self.log_in_instance.username.setText("")
        self.log_in_instance.password.setText("")

    def password_reset_function(self):
        self.stacked_layout.setCurrentIndex(13)
        self.setFixedSize(600,400)
        self.password_reset_instance.email_address.setText("")

    def change_password_function(self):
        if self.menu.isHidden():
            self.stacked_layout.setCurrentIndex(14)
            self.setFixedSize(600,400)
            self.change_password_instance.password1.setText("")
            self.change_password_instance.password2.setText("")
        else:
            try:
                self.send_code_to_email(self.log_in_instance.username.text())
                self.stacked_layout.setCurrentIndex(15)
                self.setFixedSize(650,400)
                self.change_password_instance2.password1.setText("")
                self.change_password_instance2.password2.setText("")
                self.change_password_instance2.code.setText("")

            except smtplib.SMTPAuthenticationError:
                self.error_message_instance = ErrorMessageClass("Error: The Gmail account details are not valid.")
                self.error_message_instance.move(750,500)
                self.error_message_instance.show()
                self.error_message_instance.raise_()


        
    def find_account(self):
        settings = getSettings()
        encrypted_password_entered = change_password(self.log_in_instance.password.text(), 3)
        self.return_signal = find_username_and_password(self.log_in_instance.username.text(), encrypted_password_entered)
        if self.return_signal == 1:
            self.error_message_instance = ErrorMessageClass("Sorry the Username and Password you entered are incorrect")
            self.error_message_instance.move(750,500)
            self.error_message_instance.show()
            self.error_message_instance.raise_()
        elif self.return_signal == 2:
            if self.log_in_instance.password.text() == 'password':
                self.change_password_function()
            else:
                self.create_new_order_function()
                self.menu.show()
                username = find_employee_by_username(self.log_in_instance.username.text())
                EmployeeID = username[3]
                if int(EmployeeID) != 1:
                    self.add_an_employee_action.setDisabled(True)
                    self.edit_employee_action.setDisabled(True)
                    self.remove_an_employee_action.setDisabled(True)
                    self.explanation_action.setVisible(True)
                else:
                    self.add_an_employee_action.setEnabled(True)
                    self.edit_employee_action.setEnabled(True)
                    self.remove_an_employee_action.setEnabled(True)
                    self.explanation_action.setVisible(False)



    def reset_password(self):
        self.password_reset_function()

    def email_question(self):
        self.error_message_instance = ErrorMessageClass("This is the email address and password used to send the: \n - Invoice Form \n - Password Reset Code \n - Account Reminder \n  \n This must be a Gmail account.")
        self.error_message_instance.move(750,500)
        self.error_message_instance.show()
        self.error_message_instance.raise_()

    def match_passwords(self):
        if self.change_password_instance.password1.text() == self.change_password_instance.password2.text():
            encrypted_password = change_password(self.change_password_instance.password1.text(), 3)
            change_employee_password(self.log_in_instance.username.text(), encrypted_password)
            self.error_message_instance = ErrorMessageClass("Your Password has Sucessfully been changed!")
            self.error_message_instance.move(750,500)
            self.error_message_instance.show()
            self.error_message_instance.raise_()
            self.create_new_order_function()
            self.menu.show()


        else:
            self.error_message_instance = ErrorMessageClass("Sorry your passwords do not match.")
            self.error_message_instance.move(750,500)
            self.error_message_instance.show()
            self.error_message_instance.raise_()

    def match_codes(self):
        
        if int(self.code) != int(self.change_password_instance2.code.text()):
            self.error_message_instance = ErrorMessageClass("The Code you entered does not match the one emailed to you.")
            self.error_message_instance.move(750,500)
            self.error_message_instance.show()
            self.error_message_instance.raise_()

        elif self.change_password_instance2.password1.text() != self.change_password_instance2.password2.text():
            self.error_message_instance = ErrorMessageClass("The passwords you entered do not match")
            self.error_message_instance.move(750,500)
            self.error_message_instance.show()
            self.error_message_instance.raise_()
        
        elif (self.change_password_instance2.password1.text() == self.change_password_instance2.password2.text() and int(self.code) == int(self.change_password_instance2.code.text())):
            encrypted_password = change_password(self.change_password_instance2.password1.text(), 3)
            change_employee_password(self.log_in_instance.username.text(), encrypted_password)
            self.error_message_instance = ErrorMessageClass("Your Password has Sucessfully been changed!")
            self.error_message_instance.move(750,500)
            self.error_message_instance.show()
            self.error_message_instance.raise_()
            self.create_new_order_function()
            self.menu.show()
            
    

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
        settings = getSettings()
        subject = ("Your Beacon Vet Account Details")

        send_from = '{0}'.format(settings[0][10])
        decrypted_password = change_password(settings[0][11], -3)

        msg = "\r\n".join([
              "From: beaconvets@gmail.com",
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

    def send_code_to_email(self, username):
        settings = getSettings()
        self.code = random.randint(1000,9999)
        print(self.code)
        decrypted_password = change_password(settings[0][11], -3)
        employee_info = find_employee_by_username(username)
        message = "Hello {0}, \n \n Your Reset Password Code is:  ".format(employee_info[0])
        msg = "\r\n".join([
          "From: beaconvets@gmail.com",
          "To: {0}".format(employee_info[2]),
          "Subject: Password Reset Code",
          "",
          ("{0}{1}".format(message ,str(self.code)))])
        mail = smtplib.SMTP('smtp.gmail.com','587')
        mail.ehlo()
        mail.starttls()
        mail.login('{0}'.format(settings[0][10]) , decrypted_password)
        mail.sendmail('{0}'.format(settings[0][10]), str(employee_info[2]) , msg)
        mail.close()
        
def main():
    stock_control = QApplication(sys.argv) #creates new application
    mainWindow = MainWindow()#Creates a New instance of main window
    mainWindow.show()
    mainWindow.raise_()
    stock_control.exec_() 
    
if __name__ == '__main__':
    main() 


