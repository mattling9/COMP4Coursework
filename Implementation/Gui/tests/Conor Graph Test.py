import sys, random, datetime, sqlite3, re, numpy

from pylab import *

from PyQt4.QtGui import *
from PyQt4.QtCore import *
from matplotlib.backends.backend_qt4agg import FigureCanvasQTAgg as FigureCanvas
from matplotlib import pyplot as plt
from matplotlib.dates import date2num
from matplotlib.legend_handler import HandlerLine2D

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.figure = plt.figure()
        self.canvas = FigureCanvas(self.figure)
        plt.clf()
        
        self.ax.plot(targetWeight)
        self.ax.set_xlim(1,10)
        self.ax.set_ylim(0,300)
        self.ax.set_xticks(np.arange(len(targetWeight)))        #Adds length to x-axis
        self.fig.autofmt_xdate()                                #Formats font
        self.ax.set_title("Target Weight Data readings")        #Creates title
        self.ax.set_xlabel("Product")                           #Creates x-axis label
        self.ax.set_ylabel("Weight (kg)")                       #Creates y-axis label
        self.figure.canvas.draw()                                  #Draws the diagram
        self.setCentralWidget(self.canvas)


def main():
    app = QApplication(sys.argv) #creates new application
    mainWindow = MainWindow()#Creates a New instance of main window
    mainWindow.show()
    mainWindow.raise_()
    app.exec_()
    
if __name__ == '__main__':
    main()
