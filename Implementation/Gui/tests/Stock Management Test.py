import sys
from PyQt4.QtCore import *
from PyQt4.QtGui import *


class MainWindow(QMainWindow):
    
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Stock Management Test")
        self.resize(600, 400)
        self.stockManagement()

    def stockManagement(self):
        #Title
        self.title = QLabel("Stock Management")
        self.title.setAlignment(Qt.AlignCenter)
        self.title_font = QFont()
        self.title_font.setPointSize(18)
        self.title_font.setBold(True)
        self.title.setFont(self.title_font)

        #Image
        self.image = QLabel()
        self.image_pixmap = QPixmap(".\images\dance.gif")
        self.scaled_image = self.image_pixmap.scaled(180, 180, Qt.IgnoreAspectRatio, Qt.FastTransformation)
        self.image.setPixmap(self.scaled_image)
        
        
        #Product Name
        self.product_name = QLineEdit("Pedigree Chum")
        self.product_name.setReadOnly(True)
        self.product_name.setFixedHeight(50)
        self.product_name.setAlignment(Qt.AlignRight)
        self.product_font = QFont()
        self.product_font.setPointSize(12)
        self.product_name.setFont(self.product_font)
        self.product_name.setAlignment(Qt.AlignCenter)


        #Location 1
        self.location1_label = QLineEdit("Stock in Location 1:")
        self.location1_label.setAlignment(Qt.AlignCenter)
        self.location1_label.setReadOnly(True)
        self.location1 = QSpinBox()
        self.location1.setRange(0, 100)
        self.location1.setMinimumWidth(100)

        #Location 2
        self.location2_label = QLineEdit("Stock in Location 2:")
        self.location2_label.setAlignment(Qt.AlignCenter)
        self.location2_label.setReadOnly(True)
        self.location2 = QSpinBox()
        self.location2.setRange(0, 100)
        self.location2.setMinimumWidth(100)

        #Stock Required
        self.stock_required_label = QLineEdit("Stock Required")
        self.stock_required_label.setAlignment(Qt.AlignCenter)
        self.stock_required_label.setReadOnly(True)
        self.stock_required = QLineEdit("12")
        self.stock_required.setAlignment(Qt.AlignCenter)
        self.stock_required.setReadOnly(True)

        #Done
        self.done_button = QPushButton("Done")


        # Adding Layouts 
        self.image_layout = QHBoxLayout()
        self.image_widget = QWidget()
        self.image_layout.addWidget(self.image)
        self.image_layout.addWidget(self.product_name)
        self.image_widget.setLayout(self.image_layout)

        self.location1_layout = QHBoxLayout()
        self.location1_widget = QWidget()
        self.location1_layout.addWidget(self.location1_label)
        self.location1_layout.addWidget(self.location1)
        self.location1_widget.setLayout(self.location1_layout)

        self.location2_layout = QHBoxLayout()
        self.location2_widget = QWidget()
        self.location2_layout.addWidget(self.location2_label)
        self.location2_layout.addWidget(self.location2)
        self.location2_widget.setLayout(self.location2_layout)

        self.stock_layout = QHBoxLayout()
        self.stock_widget = QWidget()
        self.stock_layout.addWidget(self.stock_required_label)
        self.stock_layout.addWidget(self.stock_required)
        self.stock_widget.setLayout(self.stock_layout)

        #Group Box
        self.group_box_layout = QVBoxLayout()
        self.group_box = QGroupBox("Current Stock")
        self.group_box_layout.addWidget(self.location1_widget)
        self.group_box_layout.addWidget(self.location2_widget)
        self.group_box.setLayout(self.group_box_layout)



        self.main_layout = QVBoxLayout()
        self.main_widget = QWidget()
        self.main_layout.addWidget(self.title)
        self.main_layout.addWidget(self.image_widget)
        self.main_layout.addWidget(self.group_box)
        self.main_layout.addWidget(self.stock_widget)
        self.main_layout.addWidget(self.done_button)
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


