import sys
from PyQt4.QtCore import *
from PyQt4.QtGui import *
from PushButtonClass import *

class MainWindow(QMainWindow):
    
    def __init__(self):
        super().__init__()
        self.setWindowTitle('Menu Button Test')
        self.resize(200, 200)
        self.menuButton()
        

    def menuButton(self):
        #create a menu
        self.layout = QHBoxLayout()
        #create button group
        self.widget_group_box = QGroupBox("Please Enter Size of Product:")
        #add button
        self.MenuButton = QComboBox()
        self.MenuButton.setMinimumWidth(100)
        self.MenuButton.addItem("Kg")
        self.MenuButton.addItem("g")
        self.MenuButton.addItem("L")
        self.MenuButton.addItem("ml")
        #add Line Edit
        self.size = QLineEdit("100")
        self.size.setMinimumWidth(120)
        




        
        self.layout.addWidget(self.size)
        self.layout.addWidget(self.MenuButton)
        self.widget_group_box.setLayout(self.layout)

        self.main_layout = QVBoxLayout()
        self.main_layout.addWidget(self.widget_group_box)
        self.setLayout(self.main_layout)

        self.ButtonWidget = QWidget()
        self.ButtonWidget.setLayout(self.main_layout)
        self.setCentralWidget(self.ButtonWidget)

    def kilogram_function(self):
        print("Kg")


    def gram_function(self):
        print("g")


    def litre_function(self):
        print("L")


    def millilitre_function(self):
        print("ml")

    
        
        
        
        
def main():
    app = QApplication(sys.argv)
    main_window = MainWindow()
    main_window.show()
    main_window.raise_()
    sys.exit(app.exec_())


if __name__ == '__main__':
    main()
