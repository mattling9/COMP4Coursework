import sys
from PyQt4.QtCore import *
from PyQt4.QtGui import *


class MainWindow(QMainWindow):
    
    def __init__(self):
        super().__init__()
        self.setWindowTitle('Image Label Test')
        self.resize(200, 200)
        self.display_image()

    def display_image(self):
        
        #creating the label and the image
        self.label = QLabel()
        self.image = QPixmap('./images/logo.jpg')
        self.scaled_image = self.image.scaledToWidth(500, Qt.FastTransformation)


        #scaling the image #The image will change to the size of the label

        #setting to image to the label

        self.label.setPixmap(self.scaled_image)




        
        self.layout = QVBoxLayout()
        self.layout.addWidget(self.label)
        self.main_widget =  QWidget()
        self.main_widget.setLayout(self.layout)
        self.setCentralWidget(self.main_widget)
        
        
        
        
def main():
    app = QApplication(sys.argv)
    main_window = MainWindow()
    main_window.show()
    main_window.raise_()
    sys.exit(app.exec_())


if __name__ == '__main__':
    main()
