from PyQt4.QtSql import *
from PyQt4.QtCore import *

class SQLConnection():
    """A representation of an SQL Connection"""
    def __init__(self, path):
        self.path = path
        self.db = None

    def open_database(self):
        if self.db:
            self.close_database()
        self.db = QSqlDatabase.addDatabase("QSQLITE")
        self.db.setDatabaseName(self.path)
        opened_ok = self.db.open()
        return opened_ok

    def close_database(self):
        if self.db:
            if self.db.isOpen() == True:
                self.db.close()
                #conn is the default database name
                QSqlDatabase.removeDatabase("conn")
                closed = self.db.open()
                print("database closed")
            else:
                print("There is no connection")
        else:
            print("No connection to close!")

    def closeEvent(self, event):
        """closes the database when the applicationis closed"""
        self.close_database()

    def show_all_products(self):
        query = QSqlQuery()
        query.prepare(""" SELECT * FROM Product""")
        query.exec_()
        return query

    def find_products_by_number(self, values):
        query = QSqlQuery()
        query.prepare("""select * From Product where ProductID = ?""")
        query.addBindValue(values[0])
        query.exec_()
        return query
