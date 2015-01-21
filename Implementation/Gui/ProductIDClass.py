import sqlite3

from PyQt4.QtGui import *
from PyQt4.QtCore import *
from PyQt4.QtSql import *

class ProductIDClass(QWidget):
    """A representation of A Push Button Widget"""
    def __init__(self, Label, index):
        super().__init__()
        self.visible = False
        self.layout = QHBoxLayout()
        self.widget = QWidget()
        self.label = QLabel(Label)
        self.line_edit = QLineEdit()
        self.button = QPushButton("Find...")
        if index == 1:
            self.button.clicked.connect(self.find_product_by_id)
        elif index == 7:
            self.button.clicked.connect(self.find_member_by_id)
        elif index == 10:
            self.button.clicked.connect(self.find_employee_by_id)   
        self.layout.addWidget(self.label)
        self.layout.addWidget(self.line_edit)
        self.layout.addWidget(self.button)
        self.setLayout(self.layout)

    def find_product_by_id(self):
        with sqlite3.connect("ProductDatabase.db") as db:
            product_id = self.line_edit.text()
            cursor = db.cursor()
            cursor.execute("SELECT * FROM Product WHERE ProductID = ?",(product_id,))
            product_info = cursor.fetchall()
            db.commit()
            print(product_info)
            self.visible = True
            print(self.visible)
            if not product_info:
                print("NOT IN DATABASE")
                self.visible = False
        

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
