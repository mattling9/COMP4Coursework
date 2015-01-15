from PyQt4.QtSql import *
from PyQt4.QtGui import *
from PyQt4.QtCore import *
from PopUpMenuClass import *

class CTRLF_Class(QWidget):
    def __init__(self):
        super().__intit__()
        self.setWindowSize(600,900)
        self.setWindowTitle("Find Something in The Database")
        self.icon = QIcon(QPixmap("./images/Logo.jpg"))
        self.setWindowIcon(self.icon)
        self.label = QLabel()
        self.pixmap = QPixmap("./images/search_icon.png")
        self.scaled_pixmap = self.pixmap.scaled(15,15, Qt.IgnoreAspectRatio, Qt.FastTransformation)
        self.label.setPixmap(self.scaled_pixmap)

        self.main_layout = QVBoxLayout()

        self.table_selection_layout = QHBoxLayout()
        self.table_selection_label = QLabel("Search For: ")
        self.table_combo_box = QComboBox()
        self.item_list = ["Product","Member","Employee"]
        for item in self.item_list:
            self.table_combo_box.addItem(item)
        self.table_selection_layout.addWidget(self.table_selection_label)
        self.table_selection_layout.addWidget(self.table_combo_box)
        self.table_selection_widget = QWidget()
        self.table_selection_widget.setLayout(self.table_selection_layout)

        
        self.search_layout = QHBoxLayout()
        self.search_layout.addWidget(self.label)
        self.line_edit = QLineEdit()
        self.line_edit.setPlaceholderText("Product Name, Member Name, Employee Name")
        self.search_layout.addWidget(self.label)
        self.search_layout.addWidget(self.line_edit)
        self.search_widget = QWidget()
        self.search_widget.setLayout(self.search_layout)


        self.display_table = QTableView()
        self.display_table.setFixedHeight(150)
        self.display_table_layout = QVBoxLayout()
        self.display_table_layout.addWidget(self.display_table)
        self.display_table_widget = QWidget()
        self.display_table_widget.setLayout(self.display_table_layout)
        self.display_table.selectRow(1)
        self.model = None
        if not self.model or not isinstance(self.model, QSqlTableModel):
            self.model = QSqlTableModel()
        self.model.setTable("Product")

        if self.table_combo_box.currentIndex == 0:
            self.model.setTable("Product")
            self.model.select()
        elif self.table_combo_box.currentIndex == 1:
            self.model.setTable("Member")
            self.model.select()
        elif self.table_combo_box.currentIndex == 2:
            self.model.setTable("Employee")
            self.model.select()
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
        self.display_table.show()

        self.main_layout.addWidget(self.table_selection_widget)
        self.main_layout.addWidget(self.search_widget)
        self.main_layout.addWidget(self.display_table)
        
        self.main_widget = QWidget()
        self.main_widget.setLayout(self.main_layout)
        self.FShortcut_instance.setCentralWidget(self.main_widget)
        self.FShortcut_instance.move(750,200)
        self.FShortcut_instance.show()
        self.FShortcut_instance.raise_()
