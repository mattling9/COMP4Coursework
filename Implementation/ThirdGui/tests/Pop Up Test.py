import sys, random
from PyQt4.QtCore import *
from PyQt4.QtGui import *

                
class MainWindow(QMainWindow):
    
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Adding Member Test")
        self.resize(300, 300)
        self.button = QPushButton("Get Free Steam Credits")
        self.button.clicked.connect(self.create_new_window)
        self.main_layout = QVBoxLayout()
        self.main_widget = QWidget()
        self.main_layout.addWidget(self.button)
        self.main_widget.setLayout(self.main_layout)
        self.setCentralWidget(self.main_widget)
    def create_new_window(self):
            self.new_window = PopUpWindow()
            self.new_window.show()
            self.new_window.raise_()

class PopUpWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Pop-Up Window")
        self.resize(400,300)
        self.label = QLabel("You Mad")
        self.main_layout = QVBoxLayout()
        self.main_widget = QWidget()
        self.main_layout.addWidget(self.label)
        self.main_widget.setLayout(self.main_layout)
        self.setCentralWidget(self.main_widget)

        




        
        
        
def main():
    app = QApplication(sys.argv)
    main_window = MainWindow()
    main_window.show()
    main_window.raise_()
    sys.exit(app.exec_())


if __name__ == '__main__':
    main()

