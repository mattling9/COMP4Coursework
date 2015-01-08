import shutil, time

from PyQt4.QtGui import *
from PyQt4.QtCore import *
from SQLConnection import *
from CreatingTable import *
from PopUpMenuClass import *

class DatabaseClass(QWidget):
    """Representation of Preferences Menu"""
    def __init__(self):
        super().__init__()

        #Group Box
        self.group_box = QGroupBox("Preferences:")

        #Creating Buttons
        self.current_database_label = QLabel("Current Database:")
        self.open_database = QPushButton("Open Database")
        self.new_database = QPushButton("Create New Database")
        self.database_path = QLineEdit("database.db")
        self.database_path.setReadOnly(True)
        self.open_database.clicked.connect(self.get_database)

        self.database_layout = QGridLayout()
        self.database_widget = QWidget()
        self.database_layout.addWidget(self.current_database_label, 0,0)
        self.database_layout.addWidget(self.database_path, 0,1)
        self.database_layout.addWidget(self.open_database, 1,0)
        #self.database_layout.addWidget(self.new_database, 1,0)
        self.database_widget.setLayout(self.database_layout)

        self.main_layout = QVBoxLayout()
        self.main_layout.addWidget(self.database_widget)
        
        self.setLayout(self.main_layout)

    def get_database(self):
        path = QFileDialog.getOpenFileName()
        self.database_path.setText(path)
        self.connection = SQLConnection(path)
        self.open_database
        database = self.connection.open_database()
        time.sleep(0.5)
        self.CreatePopUpWindow()
        

    def CreatePopUpWindow(self):
        self.pop_up_instance = PopUpWindow("Beacon Vets Stock Control", 300, 100)
        self.icon = QIcon(QPixmap("./images/Logo.jpg"))
        self.pop_up_instance.setWindowIcon(self.icon)
        self.label = QLabel("Database Sucessfully Opened!")
        self.label.setAlignment(Qt.AlignCenter)
        self.buttonBox = QDialogButtonBox()
        self.buttonBox.setOrientation(Qt.Horizontal)
        self.buttonBox.setStandardButtons(QDialogButtonBox.Ok | QDialogButtonBox.Cancel)
        self.buttonBox.button(QDialogButtonBox.Ok).clicked.connect(self.clicked_ok)
        self.buttonBox.button(QDialogButtonBox.Cancel).clicked.connect(self.clicked_cancel)
        self.pop_up_layout = QVBoxLayout()
        self.pop_up_widget = QWidget()
        self.pop_up_layout.addWidget(self.label)
        self.pop_up_layout.addWidget(self.buttonBox)
        self.pop_up_widget.setLayout(self.pop_up_layout)
        self.pop_up_instance.setCentralWidget(self.pop_up_widget)
        self.pop_up_instance.move(750,500)
        self.pop_up_instance.show()
        self.pop_up_instance.raise_()        

    def clicked_ok(self):
        self.pop_up_instance.close()


    def clicked_cancel(self):
        self.pop_up_instance.close()
        
