from PyQt4.QtGui import *
from PyQt4.QtCore import *

class ErrorMessageClass(QMainWindow):
    """a representation of the Error Window"""
    def __init__(self, LabelText):
        super().__init__()
        self.setWindowTitle("Beacon Vets Stock Control")
        self.icon = QIcon(QPixmap("./images/Logo.jpg"))
        self.setWindowIcon(self.icon)
        self.label = QLabel(LabelText)
        self.label.setAlignment(Qt.AlignCenter)
        self.buttonBox = QDialogButtonBox()
        self.buttonBox.setOrientation(Qt.Horizontal)
        self.buttonBox.setStandardButtons(QDialogButtonBox.Ok )
        self.buttonBox.button(QDialogButtonBox.Ok).clicked.connect(self.close_window)
        self.pop_up_layout = QVBoxLayout()
        self.pop_up_widget = QWidget()
        self.pop_up_layout.addWidget(self.label)
        self.pop_up_layout.addWidget(self.buttonBox)
        self.pop_up_widget.setLayout(self.pop_up_layout)
        self.setCentralWidget(self.pop_up_widget)
        self.move(700,430)
        self.show()
        self.raise_()

    def close_window(self):
        self.close()
