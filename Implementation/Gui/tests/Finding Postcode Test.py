import sys
from PyQt4.QtCore import *
from PyQt4.QtGui import *


class MainWindow(QMainWindow):
    
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Adding Member Test")
        self.resize(400, 300)
        self.addMember()

    

    def addMember(self):



            
            #Postcode Tickbox
            self.postcode_tickbox = QCheckBox("Do You Live in Cumbria?")

            #Find Button
            self.find_button = QPushButton("Find...")
            self.find_button.setEnabled(False)

            
            self.postcode_tickbox.stateChanged.connect(self.change_button)
            

            #Postcode
            self.postcode_layout = QHBoxLayout()
            self.postcode_widget = QWidget()
            self.postcode_label = QLabel("Postcode: ")
            self.postcode = QLineEdit()
            self.postcode.setPlaceholderText("Postcode: i.e(CB7 5LQ) ")
            self.postcode_layout.addWidget(self.postcode_label)
            self.postcode_layout.addWidget(self.postcode)
            self.postcode_layout.addWidget(self.find_button)
            self.postcode_widget.setLayout(self.postcode_layout)


            #Add Member Button
            self.add_member = QPushButton("Add Member")

            #Group Box
            self.group_box = QGroupBox("Enter Member Information")
            self.group_box_layout = QVBoxLayout()


            self.main_layout = QVBoxLayout()
            self.main_widget = QWidget()
            self.group_box_layout.addWidget(self.postcode_tickbox)
            self.group_box_layout.addWidget(self.postcode_widget)
            self.group_box.setLayout(self.group_box_layout)
            self.main_layout.addWidget(self.group_box)
            self.main_layout.addWidget(self.add_member)
            self.main_widget.setLayout(self.main_layout)

            self.setCentralWidget(self.main_widget)

    def change_button(self):
        if self.postcode_tickbox.checkState() == False:
            self.find_button.setEnabled(False)
        else:
            self.find_button.setEnabled(True)
        
        
        
        
def main():
    app = QApplication(sys.argv)
    main_window = MainWindow()
    main_window.show()
    main_window.raise_()
    sys.exit(app.exec_())


if __name__ == '__main__':
    main()


