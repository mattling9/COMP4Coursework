import sys, random, datetime, sqlite3, re

from PyQt4.QtSql import *
from PyQt4.QtGui import *
from PyQt4.QtCore import *
from matplotlib.backends.backend_qt4agg import FigureCanvasQTAgg as FigureCanvas
from matplotlib import pyplot as plt
from matplotlib.dates import date2num


class manageStockClass(QWidget):
    """A representation of managing stock"""
    def __init__(self):
        super().__init__()
        self.product_id_layout = QHBoxLayout()
        self.product_id_widget = QWidget()
        self.product_id_label = QLabel("Product ID: ")
        self.product_id = QLineEdit()
        self.find_button = QPushButton("Find..")
        self.find_button.clicked.connect(self.find_product_by_id)
        self.product_id_layout.addWidget(self.product_id_label)
        self.product_id_layout.addWidget(self.product_id)
        self.product_id_layout.addWidget(self.find_button)
        self.product_id_widget.setLayout(self.product_id_layout)

        self.buttonBox = QDialogButtonBox()
        self.buttonBox.setOrientation(Qt.Horizontal)
        self.buttonBox.setStandardButtons(QDialogButtonBox.Save |QDialogButtonBox.Cancel)

        self.path = (".\images\Default.png")
        self.image = QLabel()
        self.image_pixmap = QPixmap(self.path)
        self.scaled_image = self.image_pixmap.scaled(180, 180, Qt.IgnoreAspectRatio, Qt.FastTransformation)
        self.image.setPixmap(self.scaled_image)

        font = QFont()
        font.setPointSize(14)
        font.setBold(True)
        self.product_name = QLabel("Product Name")
        self.product_name.setFont(font)
        self.stock1_label = QLabel("Stock in Shop: ")
        self.stock2_label = QLabel("Stock in Storage Room: ")
        self.stock1 = QSpinBox()
        self.stock2 = QSpinBox()

        self.current_stock_groupbox = QGroupBox("Current Stock: ")
        self.current_stock_layout = QHBoxLayout()
        self.product_info_layout = QVBoxLayout() 
        self.product_info_widget = QWidget()
        self.stock_layout = QGridLayout()
        self.stock_widget = QWidget()

        self.stock_layout.addWidget(self.stock1_label, 0,0)
        self.stock_layout.addWidget(self.stock1, 0,1)
        self.stock_layout.addWidget(self.stock2_label, 1,0)
        self.stock_layout.addWidget(self.stock2, 1,1)
        self.stock_widget.setLayout(self.stock_layout)
        
        self.product_info_layout.addWidget(self.product_name)
        self.product_info_layout.addWidget(self.stock_widget)
        self.product_info_widget.setLayout(self.product_info_layout)

        self.current_stock_layout.addWidget(self.image)
        self.current_stock_layout.addWidget(self.product_info_widget)
        self.current_stock_groupbox.setLayout(self.current_stock_layout)

        self.stock_prediction_groupbox = QGroupBox("Change Stock")
        self.stock_prediction_layout = QHBoxLayout()

        #ADDING THE GRAPH TO THE WINDOW
        self.figure = plt.figure()
        self.canvas = FigureCanvas(self.figure)
        self.plot()
        #ADDING THE GRAPH TO THE WINDOW
        self.graph = QLabel("Heres ya graph")
        self.prediction_label = QLabel("Estimated Restock: ")
        self.prediction = QLineEdit()

        self.prediction_layout = QHBoxLayout()
        self.prediction_widget = QWidget()
        self.prediction_layout.addWidget(self.prediction_label)
        self.prediction_layout.addWidget(self.prediction)
        self.prediction_widget.setLayout(self.prediction_layout)

        self.stock_prediction_layout.addWidget(self.canvas)
        self.stock_prediction_layout.addWidget(self.prediction_widget)
        self.stock_prediction_groupbox.setLayout(self.stock_prediction_layout)

        self.current_stock_groupbox.setDisabled(True)
        self.stock_prediction_groupbox.setDisabled(True)

        self.main_layout = QVBoxLayout()

        self.main_layout.addWidget(self.product_id_widget)
        self.main_layout.addWidget(self.current_stock_groupbox)
        self.main_layout.addWidget(self.stock_prediction_groupbox)
        self.main_layout.addWidget(self.buttonBox)
        self.setLayout(self.main_layout)

    def plot(self):

        data = [(datetime.datetime.strptime('01-02-2015', "%d-%m-%Y"), 11),
                (datetime.datetime.strptime('08-02-2015', "%d-%m-%Y"), 1),
                (datetime.datetime.strptime('15-02-2015', "%d-%m-%Y"), 5),
                (datetime.datetime.strptime('22-02-2015', "%d-%m-%Y"), 3)]


        x = [date2num(date) for (date, value) in data]
        y = [value for (date, value) in data]

        graph = self.figure.add_subplot(111)
        
        # plot data
        graph.plot(x,y, 'r-o',
        linestyle=("-"),
        color=('#7CFC00'),
        marker="o",
        markeredgecolor="#1919FF",
        markerfacecolor="#1919FF",
        linewidth=3.0)
        plt.xlabel("Date")
        plt.ylabel("Weekly Sales")


        graph.set_xticks(x)
        graph.set_xticklabels([date.strftime("%d-%m-%Y") for (date, value) in data])

        #refresh canvas

    def find_product_by_id(self):
        with sqlite3.connect("ProductDatabase.db") as db:
            product_id = self.product_id.text()
            cursor = db.cursor()
            cursor.execute("SELECT ProductName, Location1, Location2, ImagePath FROM Product WHERE ProductID = ?",(product_id,))
            self.product_info = cursor.fetchall()
            db.commit()
            if self.product_info:
                self.current_stock_groupbox.setEnabled(True)
                self.stock_prediction_groupbox.setEnabled(True)
                self.product_name.setText(self.product_info[0][0])
                self.stock1.setValue(self.product_info[0][1])
                self.stock2.setValue(self.product_info[0][2])
                self.path = self.product_info[0][3]
                self.pixmap = QPixmap(self.path)
                self.scaled_image = self.pixmap.scaled(180, 180, Qt.IgnoreAspectRatio, Qt.FastTransformation)
                self.image.setPixmap(self.scaled_image)

                self.canvas.draw()
            if not self.product_info:
                print("NOT IN DATABASE")
                self.current_stock_groupbox.setDisabled(True)
                self.stock_prediction_groupbox.setDisabled(True)
