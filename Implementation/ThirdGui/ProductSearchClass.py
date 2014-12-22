from PyQt4.QtGui import *
from PyQt4.QtCore import *

class searchProductClass(QWidget):
    """A representation of A Push Button Widget"""
    def __init__(self):
        super().__init__()
        #Title
        self.title = QLabel("Product Search")
        self.title.setAlignment(Qt.AlignCenter)
        self.title_font = QFont()
        self.title_font.setPointSize(18)
        self.title_font.setBold(True)
        self.title.setFont(self.title_font)
        self.title.setFixedHeight(30)

        

        self.push_button_group = QButtonGroup()
        self.push_button_group_box = QGroupBox("Please Select a Category")

        self.push_button_list = ["Dog", "Cat", "Fish", "Small pets", "Bird", "Reptile", "Equnie"]

        #create layout for push buttons and add them
        self.push_button_layout = QGridLayout()

        names = ['', '', '',
                 '', '', '',
                '']
        image_list = ['./images/dog.png', './images/cat.png', './images/fish.png', './images/hampster.png', './images/bird.png', './images/reptile.png', './images/horse.png']

        positions = [(NoButtonsY, NoButtonsX) for NoButtonsY in range(3) for NoButtonsX in range(3)]
        count = 0
        for position, name in zip(positions, names):
            button = QPushButton(name)
            button.setIcon(QIcon(image_list[count]))
            button.setIconSize(QSize(220,190))
            button.setMinimumHeight(220)
            button.setMaximumWidth(220)
            self.push_button_layout.addWidget(button, *position)
            count +=1
        

        self.push_button_group_box.setLayout(self.push_button_layout)
        #add layout to group box

        self.main_layout = QVBoxLayout()
        self.main_layout.addWidget(self.title)
        self.main_layout.addWidget(self.push_button_group_box)
        self.main_widget = QWidget()
        self.main_widget.setLayout(self.main_layout)

        #set layout for this widget
        self.setLayout(self.main_layout)
