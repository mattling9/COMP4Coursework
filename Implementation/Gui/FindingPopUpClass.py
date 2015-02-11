from PyQt4.QtSql import *
from PyQt4.QtGui import *
from PyQt4.QtCore import *
from PopUpMenuClass import *
from CustomToolbarClass import *

class SearchClass(QDialog):
    def __init__(self):
        super().__init__()
        style_sheet = """QDialog#main_window{
                                 background-color: white;
                                 border-style: solid;
                                 border-width: 2px;
                                 border-color: rgb(180,180,180);}
                         QLabel{
                                 font-family: Segoe UI;
                                 font-size: 12pt;
                                 color: rgb(70,70,70)}

                        QPushButton{
                                 font-family: Segoe UI;
                                 font-size: 11pt;
                                 font-weight: bold;
                                 color: white;
                                 background-color: rgb(0,240,0);
                                 border: 0px;} 
                   
                        QTableView{
                                 font-family: Segoe UI;
                                 font-size: 12pt;
                                 color: rgb(70,70,70);
                                 border-style: solid;
                                 border-width: 1px;
                                 border-color: rgb(200,200,200);
                                 selection-background-color: rgb(0,240,0);
                                 selection-color: rgb(255,255,255);}
                                   
                        QHeaderView:section{
                                 background: white;
                                 font-family: Segoe UI;
                                 font-size: 12pt;
                                 border-style: solid;
                                 border-width: 1px;
                                 border-color: rgb(200,200,200);
                                 color: rgb(70,70,70);
                                 height: 30px;}
                                 
                        QLineEdit{
                                 font-family: Segoe UI;
                                 font-size: 12pt;}
                                 
                        QComboBox{
                                 font-family: Segoe UI;
                                 font-size: 12pt;
                                 background: white;
                                 border-style: solid;
                                 border-width: 1px;
                                 border-color: rgb(210,210,210);
                                 color: rgb(70,70,70);}

                      """
        self.setObjectName("main_window")
        self.setWindowFlags(Qt.FramelessWindowHint)
        self.title_bar = TitleBar()
        self.title_bar.minimise.clicked.connect(self.minimise_window)
        self.title_bar.close.clicked.connect(self.close_window)

        self.buttonBox = QDialogButtonBox()
        self.buttonBox.setOrientation(Qt.Horizontal)
        self.buttonBox.setStandardButtons(QDialogButtonBox.Close)
        self.buttonBox.button(QDialogButtonBox.Close).setFixedSize(84,27)
        self.buttonBox.button(QDialogButtonBox.Close).clicked.connect(self.close_window)


        
        self.setFixedSize(800,500)
        self.setWindowTitle("Find Something in The Database")
        self.icon = QIcon(QPixmap("./images/Logo.jpg"))
        self.setWindowIcon(self.icon)
        self.label = QLabel()
        self.pixmap = QPixmap("./images/search_icon.png")
        self.scaled_pixmap = self.pixmap.scaled(27,27, Qt.IgnoreAspectRatio, Qt.FastTransformation)
        self.label.setPixmap(self.scaled_pixmap)

        self.main_layout = QVBoxLayout()
        self.group_box = QWidget()
        
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

        self.product_right_click_menu = QMenu()
        self.member_right_click_menu = QMenu()
        self.employee_right_click_menu = QMenu()

        self.display_table = QTableView()
        
        self.display_table.clicked.connect(self.clicked)
        
        self.display_table.setEditTriggers(QAbstractItemView.NoEditTriggers)
        self.display_table.setSelectionBehavior(QAbstractItemView.SelectRows)
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

        

        self.display_table.horizontalHeader().setStretchLastSection(True)
        self.display_table_layout.addWidget(self.display_table)
        self.display_table_widget.setLayout(self.display_table_layout)
        self.display_table.horizontalHeader().setObjectName("header")
        self.display_table.hideColumn(5)
        self.display_table.hideColumn(6)
        self.display_table.hideColumn(7)
        self.display_table.hideColumn(8)
        self.display_table.hideColumn(9)


        self.main_layout.addWidget(self.title_bar)
        self.main_layout.addWidget(self.search_widget)
        self.main_layout.addWidget(self.display_table_widget)
        self.main_layout.addWidget(self.buttonBox)
        self.group_box.setLayout(self.main_layout)
        self.group_box_layout = QVBoxLayout()
        self.group_box_layout.addWidget(self.group_box)
        self.setLayout(self.group_box_layout)
        self.setStyleSheet(style_sheet)

    def clicked(self):
        self.indexes = self.display_table.selectionModel().selection().indexes()
        if self.indexes:
            self.customContextMenuRequested.connect(self.show_menu)
    def show_menu(self, position):

        if self.table_combo_box.currentIndex() == 0:
            self.product_right_click_menu.exec_(self.mapToGlobal(position))
        elif self.table_combo_box.currentIndex() == 1:
            self.member_right_click_menu.exec_(self.mapToGlobal(position))
        elif self.table_combo_box.currentIndex() == 2:
            self.employee_right_click_menu.exec_(self.mapToGlobal(position))

    def change_table(self):
        if self.table_combo_box.currentIndex() == 0:
            self.model.setTable("Product")
            self.model.select()
            self.display_table.setModel(self.model)
            self.display_table.hideColumn(5)
            self.display_table.hideColumn(6)
            self.display_table.hideColumn(7)
            self.display_table.hideColumn(8)
            self.display_table.hideColumn(9)
            self.display_table.update()
        elif self.table_combo_box.currentIndex() == 1:
            self.model.setTable("Member")
            self.model.select()
            self.display_table.showColumn(5)
            self.display_table.showColumn(6)
            self.display_table.showColumn(7)
            self.display_table.showColumn(8)
            self.display_table.showColumn(9)
            self.display_table.setModel(self.model)
            self.display_table.update()
        elif self.table_combo_box.currentIndex() == 2:
            self.model.setTable("Employee")
            self.model.select()
            self.display_table.setModel(self.model)
            self.display_table.hideColumn(5)
            self.display_table.showColumn(6)
            self.display_table.showColumn(7)
            self.display_table.showColumn(8)
            self.display_table.showColumn(9)
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
        filter_query = "ProductID like '%{0}%' or ProductName like '%{0}%' or Size like '%{0}%' or Price like '%{0}%' or Category like '%{0}%'".format(product)
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

    def minimise_window(self):
        self.showMinimized()

    def close_window(self):
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


    
        
