from PyQt4.QtGui import *
from PyQt4.QtCore import *



class Image_Buttons(QWidget):
    """A representation of a grid layout"""
    def __init__(self):
        self.layout = self.image_button_layout()
        self.setLayout(self.layout)
        self.model = None
        self.image_button_layout()

    def image_button_layout(self):
        self.grid_layout = QGridLayout()
        grid.setspacing(10)
        #create buttons
        self.dog_button = QPushButton("Dog")
        self.cat_button = QPushButton("Cat")
        self.fish_button = QPushButton("Fish")
        self.small_pets_button = QPushButton("Small Pets")
        self.bird_button = QPushButton("Bird")
        self.reptile_button = QPushButton("Reptile")
        self.equine_button = QPushButton("Equine")
        #add widget to layout
        self.grid_layout.addWidget(self.dog_button, 1,0)
        self.grid_layout.addWidget(self.cat_button, 1,1)
        self.grid_layout.addWidget(self.fish_button, 1,2)
        self.grid_layout.addWidget(self.small_pets_button, 2,0)
        self.grid_layout.addWidget(self.bird_button, 2,1)
        self.grid_layout.addWidget(self.reptile_button, 2,2)
        self.grid_layout.addWidget(self.equine_button, 3,0)

        self.grid_widget = QWidget()
        self.grid_widget.setLayout(grid_layout)


        return image_button_layout
        
        
        

