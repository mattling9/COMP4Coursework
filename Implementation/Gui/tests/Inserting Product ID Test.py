import sys
from PyQt4.QtCore import *
from PyQt4.QtGui import *


class MainWindow(QMainWindow):
    
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Adding Product Test")
        self.resize(400, 300)

        
        self.layout = QHBoxLayout()
        self.widget = QWidget()
        self.label = QLabel("Product ID")
        self.line_edit = QLineEdit()
        self.button = QPushButton("Find")
        self.layout.addWidget(self.label)
        self.layout.addWidget(self.line_edit)
        self.layout.addWidget(self.button)
        self.widget.setLayout(self.layout)
        self.setCentralWidget(self.widget)
        

    
        
        
def main():
    app = QApplication(sys.argv)
    main_window = MainWindow()
    main_window.show()
    main_window.raise_()
    sys.exit(app.exec_())


if __name__ == '__main__':
    main()
