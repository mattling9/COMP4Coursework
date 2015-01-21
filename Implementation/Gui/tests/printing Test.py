from PyQt4.QtGui import *
from PyQt4.QtCore import *
import sys


class MainWindow(QMainWindow):
    """ This is a test for the printing function """

    def __init__(self):
        super().__init__()


        self.setWindowTitle("Printing Test")
        self.printer = QPrinter()
        self.printer.setPageSize(QPrinter.Letter)
        self.mainLayout()

        
    def mainLayout(self):

        self.layout = QHBoxLayout()
        self.printButton = QPushButton("Print")

        self.layout.addWidget(self.printButton)

        self.mainWidget = QWidget()
        self.mainWidget.setLayout(self.layout)

        self.setCentralWidget(self.mainWidget)

        self.printButton.clicked.connect(self.printViaHtml)

    def getCurrentDate(self,dateFormat):
        date = QDate.currentDate().toString(dateFormat)
        return date

    def statementHtml(self):

        companyName = "DnA Plastering"
        date = self.getCurrentDate("dd.MM.yyyy")

        jobItems = [["25KG Plaster","30.00","5","150.00"],["Angle Beading 3M","7.00","5","35.00"]]

        invoiceId = "4564"
        amountDue = 0.0
        for each in jobItems:
            price = float(each[3])
            amountDue += price
        amountAfterTax = amountDue * 1.2
        address = ["15 The Glebe","Haverhill","Suffolk","CB9 0DL"]
        
            
            
        
        html = u""
        html += ("<h1 align='center'>{0}</h1>"
                 "<table width='30%' align='left' cellpadding='10px'>").format(companyName)

        for each in address:
            html += ("<tr><td>{0}</td></tr>").format(each)


        html += ("</table>"
                 "<table width='30%' border='1' align='right' cellpadding='10px'>"
                 "<tr><td><b>Invoice</b> #</td><td>{0}</td></tr>"
                 "<tr><td><b>Date</b></td><td>{1}</td></tr>"
                 "<tr><td><b>Amount Due</b></td><td>{2}</td></tr>"
                 "</table>"
                 "<br><hr/>"
                 "<table width='100%' border='1' cellpadding='10px'>"
                 "<tr><td><b>Material/Item</b></td><td><b>Unit Cost</b></td><td><b>Quantity</b></td><td><b>Price</b></td></tr>").format(invoiceId,date,amountDue)

        for item in jobItems:
            html += ("<tr><td>{0}</td><td>{1}</td><td>{2}</td><td>{3}</td></tr>").format(item[0],item[1],item[2],item[3])

        html += ("<tr><td></td><td></td><td><b>Sub Total</b></td><td>{0}</td></tr>"
                 "<tr><td></td><td></td><td><b>Total (20% VAT added)</b></td><td>{1}</td></tr>").format(amountDue,amountAfterTax)

        html += ("</table>"
                 "<br>"
                 "<hr/>"
                 "<p align='center'>{0}</p>").format(companyName)


        return html

        

    def printViaHtml(self):

        html = self.statementHtml()

        dialog = QPrintDialog(self.printer, self)
        if dialog.exec_():
            document = QTextDocument()
            document.setHtml(html)
            document.print_(self.printer)
        else:
            print("The print process has failed!")

        print(html)
        


if __name__ == "__main__":

    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    window.raise_()
    app.exec_()
