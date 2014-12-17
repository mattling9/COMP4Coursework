import sys
from PyQt4.QtGui import *

class MainWindow(QWidget):
    
    def __init__(self):
        super().__init__()
        self.setWindowTitle('Menu Button Program')
        self.resize(200, 200)
        self.menuButton()
        

    def menuButton(self):
        #create a menu
        self.add_new_product = QAction("Add a New Product", self)
        self.delete_a_product = QAction("Delete a Product", self)
        self.find_a_product = QAction("Find a Product", self)
        self.menu = QMenuBar()

        self.productsmenu = self.menu.addMenu("Product")
        self.productsmenu.addAction(self.add_new_product)
        self.productsmenu.addAction(self.delete_a_product)
        self.productsmenu.addAction(self.find_a_product)
        self.setMenuBar(self.menu)

        self.layout = QVBoxLayout()
        self.MenuButton = QPushButton("HI")
        #self.MenuButton.setMenu(self.menu)
        self.layout.addWidget(self.MenuButton)
        self.setLayout(self.layout)
        
        
        
        
def main():
    app = QApplication(sys.argv)
    main_window = MainWindow()
    main_window.show()
    main_window.raise_()
    sys.exit(app.exec_())


if __name__ == '__main__':
    main()
