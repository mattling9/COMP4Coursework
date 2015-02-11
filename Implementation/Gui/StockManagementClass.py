import sys, random, datetime, sqlite3, re, numpy

from pylab import *
from PyQt4.QtSql import *
from PyQt4.QtGui import *
from PyQt4.QtCore import *
from matplotlib.backends.backend_qt4agg import FigureCanvasQTAgg as FigureCanvas
from matplotlib import pyplot as plt
from matplotlib.dates import date2num
from matplotlib.legend_handler import HandlerLine2D
from AddingRemovingData import *
from ErrorMessageClass import *


class manageStockClass(QWidget):
    """A representation of managing stock"""
    def __init__(self):
        super().__init__()
        self.product_id_layout = QHBoxLayout()
        self.product_id_widget = QWidget()
        self.product_id_label = QLabel("Product ID: ")
        self.product_id = QLineEdit()
        self.find_button = QPushButton("Find..")
        self.find_button.setFixedSize(84,27)
        self.find_button.clicked.connect(self.find_product_by_id)
        self.product_id_layout.addWidget(self.product_id_label)
        self.product_id_layout.addWidget(self.product_id)
        self.product_id_layout.addWidget(self.find_button)
        self.product_id_widget.setLayout(self.product_id_layout)

        self.buttonBox = QDialogButtonBox()
        self.buttonBox.setOrientation(Qt.Horizontal)
        self.buttonBox.setStandardButtons(QDialogButtonBox.Save)
        self.buttonBox.button(QDialogButtonBox.Save).setFixedSize(84,27)
        self.buttonBox.button(QDialogButtonBox.Save).setShortcut(QKeySequence("CTRL+S"))
        self.buttonBox.button(QDialogButtonBox.Save).clicked.connect(self.save)

        self.path = (".\images\Default.png")
        self.image = QLabel()
        self.image_pixmap = QPixmap(self.path)
        self.scaled_image = self.image_pixmap.scaled(180, 180, Qt.IgnoreAspectRatio, Qt.FastTransformation)
        self.image.setPixmap(self.scaled_image)

        self.product_name = QLabel("Product Name")
        self.product_name.setObjectName("product_name")
        self.stock1_label = QLabel("Stock in Shop: ")
        self.stock2_label = QLabel("Stock in Storage Room: ")
        self.stock1 = QSpinBox()
        self.stock1.setFixedWidth(50)
        self.stock2 = QSpinBox()
        self.stock2.setFixedWidth(50)

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
        #ADDING THE GRAPH TO THE WINDOW
        self.prediction_label = QLabel("Predicted  Sales Next Week: ")
        self.prediction = QLabel()

        self.prediction_layout = QHBoxLayout()
        self.prediction_widget = QWidget()
        self.prediction_layout.addWidget(self.prediction_label)
        self.prediction_layout.addWidget(self.prediction)
        self.prediction_widget.setLayout(self.prediction_layout)

        self.change_sales_layout = QHBoxLayout()
        self.change_sales_widget = QWidget()
        self.change_sales_label = QLabel("View Sales Per:")
        self.change_sales_box = QComboBox()
        self.change_sales_box.setFixedHeight(30)
        self.change_sales_box.addItem("Day")
        self.change_sales_box.addItem("Week")
        self.change_sales_box.currentIndexChanged.connect(self.change_graph)
        self.change_sales_layout.addWidget(self.change_sales_label)
        self.change_sales_layout.addWidget(self.change_sales_box)
        self.change_sales_widget.setLayout(self.change_sales_layout)

        self.sales_layout = QVBoxLayout()
        self.sales_widget = QWidget()
        self.sales_layout.addWidget(self.change_sales_widget)
        self.sales_layout.addWidget(self.prediction_widget)
        self.sales_widget.setLayout(self.sales_layout)

        self.stock_prediction_layout.addWidget(self.canvas)
        self.stock_prediction_layout.addWidget(self.sales_widget)
        self.stock_prediction_groupbox.setLayout(self.stock_prediction_layout)

        self.current_stock_groupbox.setDisabled(True)
        self.stock_prediction_groupbox.setDisabled(True)

        self.main_layout = QVBoxLayout()

        self.main_layout.addWidget(self.product_id_widget)
        self.main_layout.addWidget(self.current_stock_groupbox)
        self.main_layout.addWidget(self.stock_prediction_groupbox)
        self.main_layout.addWidget(self.buttonBox)
        self.setLayout(self.main_layout)

    def plot(self, sales_by):
        plt.clf()
        product_id = self.product_id.text()
        if sales_by == "day":
            sales = get_daily_sales(product_id)
            dates = get_daily_sales_date(product_id)
            plt.ylabel("Daily Sales")
        elif sales_by == "week":
            sales = get_weekly_sales(product_id)
            dates = get_weekly_sales_date(product_id)
            plt.ylabel("Weekly Sales")
        data = []
        graph = self.figure.add_subplot(111)
        if dates:
            for count in range(0, len(dates)):
                value = (datetime.datetime.strptime(dates[count][0], "%d-%m-%Y"), sales[count][0])
                data.append(value)
                x = [date2num(date) for (date, value) in data]
                y = [value for (date, value) in data]
                
            # plot data
            line, = graph.plot(x,y, 'r-o',
            linestyle=("-"),
            color=('#7CFC00'),
            marker="o",
            markeredgecolor="#1919FF",
            markerfacecolor="#1919FF",
            linewidth=3.0,
            label = ("No. of Sales made"))
            plt.xlabel("Date")
            graph.set_xticks(x)
            graph.set_xticklabels([date.strftime("%d-%m-%Y") for (date, value) in data])

            if len(dates) > 1:
                #plotting the average
                #the line below gets the gradient and y intercept from the line of best fit where
                # m = gradient, c = y intercept. (c is not right because dates have been used!)
                (m,c) = polyfit(x,y,1)
                yp = polyval([m,c],x)
                difference = yp[1] - yp[0]
                rounded_difference = round(difference, 2)
                length_of_list = len(yp)
                last_sale = yp[length_of_list - 1]
                predicted_sale = last_sale + rounded_difference
                rounded_predicted_sale = int(round(predicted_sale, 0))
                self.prediction.setText(str(rounded_predicted_sale))
                average, = graph.plot(x,yp,
                linestyle=("--"),
                color=('#FF1919'),
                label = ("Average Sales made"),
                linewidth=1.0)
                
            plt.legend(loc='upper left')
            graph.grid(b=True, which='major')
            

        elif dates == None:
            graph.plot(0,0)
            plt.xlabel("Date")
            plt.ylabel("Weekly Sales")
        
        self.canvas.draw()

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
                self.plot("week")
                self.change_sales_box.setCurrentIndex(1)
            if not self.product_info:
                self.error = ErrorMessageClass("No product with Product ID: {0}".format(self.product_id.text()))
                self.error.setFixedSize(400,150)
                plt.clf()
                self.current_stock_groupbox.setDisabled(True)
                self.stock_prediction_groupbox.setDisabled(True)
                self.product_name.setText("Product Name")
                self.path = (".\images\Default.png")
                self.image_pixmap = QPixmap(self.path)
                self.scaled_image = self.image_pixmap.scaled(180, 180, Qt.IgnoreAspectRatio, Qt.FastTransformation)
                self.image.setPixmap(self.scaled_image)
                self.stock1.setValue(0)
                self.stock2.setValue(0)

    def save(self):
        edit_stock(self.product_id.text(), int(self.stock1.value()), int(self.stock2.value()))
        self.error = ErrorMessageClass("Stock Successfully saved!")
        self.error.setFixedSize(400,150)

    def change_graph(self):
        if self.change_sales_box.currentIndex() == 0:
            self.plot("day")

        elif self.change_sales_box.currentIndex() == 1:
            self.plot("week")
