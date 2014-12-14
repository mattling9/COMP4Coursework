from PyQt4.QtGui import *
from PyQt4.QtCore import *
from PyQt4.QtSql import *


class DisplayWidget(QWidget):
    """A representation of the Display Widget"""
    def __init__(self):
        super().__init__()
        self.stacked_layout = QStackedLayout()
        self.setLayout(self.stacked_layout)
        self.model = None
        self.display_results_layout()

    def display_results_layout(self):
        self.results_table = QTableView()



        #create the main results layout       
        self.results_layout = QVBoxLayout()
        self.results_layout.addWidget(self.results_table)

        #create the main results widget
        self.results_widget = QWidget()
        self.results_widget.setLayout(self.results_layout)


        #add the results widget to the stacked layout
        self.stacked_layout.addWidget(self.results_widget)

        
    def show_results(self,query):
        self.model = QSqlQueryModel()
        self.model.setQuery(query)
        self.results_table.setModel(self.model)
        self.results_table.show()
        print("working")
    


    def show_results(self, query):
        self.model = QSqlQueryModel()
         #set query model
        self.model.setQuery(query)
        self.results_table.setModel(self.model)
        self.results_table.show()            

    
    
