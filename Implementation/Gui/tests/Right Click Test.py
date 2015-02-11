import sys
from PyQt4.QtCore import *
from PyQt4.QtGui import *
class TestApp(QMainWindow):
    def __init__(self, *args):
        super(TestApp, self).__init__(*args)

        #create contex menu
        self.menu = QMenu()
        self.menu.addAction("Edit Product Data", self.EditShortcut, "CTRL+E")
        self.menu.addAction("Manage Stock", self.ManageShortcut, "CTRL+M")

        self.menu2 = QMenu(self)
        self.menu2.addAction("Edit Product Data2", self.EditShortcut, "CTRL+E")
        self.menu2.addAction("Manage Stock2", self.ManageShortcut, "CTRL+M")

        self.setContextMenuPolicy(Qt.CustomContextMenu)
        self.customContextMenuRequested.connect(self.execContextMenu)

    def execContextMenu(self, point):
        self.menu.exec_(self.mapToGlobal(point))

    def ManageShortcut(self):
        print("2")

    def EditShortcut(self):
        print ('1')
    

app = QApplication(sys.argv)
win = TestApp()
win.show()

app.exec_()
