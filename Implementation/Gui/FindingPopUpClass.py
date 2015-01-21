from PyQt4.QtSql import *
from PyQt4.QtGui import *
from PyQt4.QtCore import *
from PopUpMenuClass import *

class SearchClass(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setFixedSize(800,400)
        self.setWindowTitle("Find Something in The Database")
        self.icon = QIcon(QPixmap("./images/Logo.jpg"))
        self.setWindowIcon(self.icon)
        self.label = QLabel()
        self.pixmap = QPixmap("./images/search_icon.png")
        self.scaled_pixmap = self.pixmap.scaled(15,15, Qt.IgnoreAspectRatio, Qt.FastTransformation)
        self.label.setPixmap(self.scaled_pixmap)

        self.main_layout = QVBoxLayout()
        self.group_box = QGroupBox()
        
        self.table_selection_layout = QHBoxLayout()
        self.table_selection_label = QLabel("Search For: ")
        self.table_combo_box = QComboBox()
        self.table_combo_box.setFixedWidth(100)
        self.item_list = ["Product","Member","Employee"]
        for item in self.item_list:
            self.table_combo_box.addItem(item)
        self.table_selection_layout.addWidget(self.table_selection_label)
        self.table_selection_layout.addWidget(self.table_combo_box)
        self.table_selection_widget = QWidget()
        self.table_selection_widget.setLayout(self.table_selection_layout)
        self.table_combo_box.currentIndexChanged.connect(self.change_table)
        
        self.search_layout = QHBoxLayout()
        self.search_layout.addWidget(self.label)
        self.line_edit = QLineEdit()
        self.line_edit.textChanged.connect(self.decide_search)
        self.line_edit.setPlaceholderText("Product Name, Member Name, Employee Name")
        self.search_layout.addWidget(self.label)
        self.search_layout.addWidget(self.line_edit)
        self.search_layout.addWidget(self.table_combo_box)
        self.search_widget = QWidget()
        self.search_widget.setLayout(self.search_layout)


        self.display_table = QTableView()
        self.display_table.setFixedHeight(300)
        self.display_table_layout = QVBoxLayout()
        self.display_table_widget = QWidget()
        self.model = None
        if not self.model or not isinstance(self.model, QSqlTableModel):
            self.model = QSqlTableModel()
        self.model.setTable("Product")
        self.model.select()
        self.display_table.setModel(self.model)
        column_width_list = [80, 300, 90, 75]
        counter = 0
        for item in column_width_list:
            self.display_table.setColumnWidth(counter, item)
            counter += 1
        self.display_table.hideColumn(4)
        self.display_table.hideColumn(5)

        

        self.display_table.horizontalHeader().setStretchLastSection(True)
        self.display_table_layout.addWidget(self.display_table)
        self.display_table_widget.setLayout(self.display_table_layout)



        
        self.main_layout.addWidget(self.search_widget)
        self.main_layout.addWidget(self.display_table_widget)
        self.group_box.setLayout(self.main_layout)
        self.group_box_layout = QVBoxLayout()
        self.group_box_layout.addWidget(self.group_box)
        self.setCentralWidget(self.group_box)

    def change_table(self):
        if self.table_combo_box.currentIndex() == 0:
            self.model.setTable("Product")
            self.model.select()
            self.display_table.setModel(self.model)
            self.display_table.hideColumn(4)
            self.display_table.hideColumn(5)
            self.display_table.update()
        elif self.table_combo_box.currentIndex() == 1:
            self.model.setTable("Member")
            self.model.select()
            self.display_table.setModel(self.model)
            self.display_table.update()
        elif self.table_combo_box.currentIndex() == 2:
            self.model.setTable("Employee")
            self.model.select()
            self.display_table.setModel(self.model)
            self.display_table.update()

    def decide_search(self):
        if self.table_combo_box.currentIndex() == 0:
            self.find_product()
        elif self.table_combo_box.currentIndex() == 1:
            self.find_member()
        elif self.table_combo_box.currentIndex() == 2:
            self.find_employee()
            

    def find_product(self):
        product = self.line_edit.text()
        filter_query = "ProductID like '%{0}%' or ProductName like '%{0}%' or Size like '%{0}%' or Price like '%{0}%'".format(product)
        self.model.setFilter(filter_query)
        self.model.select()
    
    def find_member(self):
        member = self.line_edit.text()
        filter_query = """MemberID like '%{0}%' or Title like '%{0}%' or MemberFirstName like '%{0}%' or MemberLastName like '%{0}%'
                          or Town like '%{0}%' or City like '%{0}%' or County like '%{0}%' or Postcode like '%{0}%' or TelephoneNo like '%{0}%' or MemberEmail like '%{0}%'""".format(member)
        self.model.setFilter(filter_query)
        self.model.select()
    
    def find_employee(self):
        employee = self.line_edit.text()
        filter_query = "EmployeeID like '%{0}%' or EmployeeFirstName like '%{0}%' or EmployeeLastName like '%{0}%' or EmployeeFirstName like '%{0}%'".format(employee)
        self.model.setFilter(filter_query)
        self.model.select()


    
        
