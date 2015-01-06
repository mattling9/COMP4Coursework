import sys, shutil

from PyQt4.QtCore import *
from PyQt4.QtGui import *


class MainWindow(QMainWindow):
    
    def __init__(self):
        super().__init__()
        self.setWindowTitle('Opening an Image Test')
        self.resize(400, 400)

        path = "./images/Default.png"
        
        self.browse_button = QPushButton("Browse...")
        self.upload_button = QPushButton("Upload")
        self.path_line_edit = QLineEdit()
        self.path_line_edit.setReadOnly(True)
        self.image_label = QLabel()
        self.path_line_edit.setText(path)
        self.image = QPixmap(path)
        self.image_label.setPixmap(self.image)
        self.main_layout = QGridLayout()
        self.main_layout.addWidget(self.image_label, 0,0)
        self.main_layout.addWidget(self.path_line_edit, 1,0)
        self.main_layout.addWidget(self.browse_button, 1,1)
        self.main_layout.addWidget(self.upload_button, 1,2)
        self.main_widget = QWidget()
        self.main_widget.setLayout(self.main_layout)
        self.setCentralWidget(self.main_widget)
        self.browse_button.clicked.connect(self.get_image_path)
        self.upload_button.clicked.connect(self.update_image)

    def get_image_path(self):
        path =  QFileDialog.getOpenFileName()
        self.path_line_edit.setText(path)
        

    def update_image(self):
        path = self.path_line_edit.text()
        new_path = "./ProductImage.jpg"
        shutil.copy(path, new_path)
        self.image = QPixmap(path)
        self.image_label.setPixmap(self.image)
        
def main():
    app = QApplication(sys.argv)
    main_window = MainWindow()
    main_window.show()
    main_window.raise_()
    sys.exit(app.exec_())


if __name__ == '__main__':
    main()
