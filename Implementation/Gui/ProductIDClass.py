import sqlite3

from PyQt4.QtGui import *
from PyQt4.QtCore import *
from PyQt4.QtSql import *

class ProductIDClass(QWidget):
    """A representation of A Push Button Widget"""
    def __init__(self, Label, index):
        super().__init__()
        self.layout = QHBoxLayout()
        self.widget = QWidget()
        self.find_product_id_label = QLabel(Label)
        self.find_product_id_line_edit = QLineEdit()
        self.find_product_id_button = QPushButton("Find...")
   
        self.layout.addWidget(self.find_product_id_label)
        self.layout.addWidget(self.find_product_id_line_edit)
        self.layout.addWidget(self.find_product_id_button)
        self.setLayout(self.layout)

    def find_product_by_id(self):
        with sqlite3.connect("ProductDatabase.db") as db:
            product_id = self.line_edit.text()
            cursor = db.cursor()
            cursor.execute("SELECT * FROM Product WHERE ProductID = ?",(product_id,))
            self.product_info = cursor.fetchall()
            db.commit()
            if self.product_info:
                print(self.product_info)
                
            if not self.product_info:
                print("NOT IN DATABASE")
        

    def find_member_by_id(self):
        with sqlite3.connect("ProductDatabase.db") as db:
            product_id = self.line_edit.text()
            cursor = db.cursor()
            cursor.execute("SELECT * FROM Member WHERE MemberID = ?",(product_id,))
            product_info = cursor.fetchall()
            db.commit()
            if product_info != "":
                print(product_info)
                self.self.visible = True
                print(self.visible)
            if not product_info:
                print("NOT IN DATABASE")

    def find_employee_by_id(self):
        with sqlite3.connect("ProductDatabase.db") as db:
            product_id = self.line_edit.text()
            cursor = db.cursor()
            cursor.execute("SELECT * FROM Employee WHERE EmployeeID = ?",(product_id,))
            product_info = cursor.fetchall()
            db.commit()
            if product_info != "":
                print(product_info)
                self.visible = True
                print(self.visible)
            if not product_info:
                print("NOT IN DATABASE")
