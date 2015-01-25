from PyQt4.QtGui import *
from PyQt4.QtCore import *
import sys, datetime


class MainWindow(QMainWindow):
    """ This is a test for the printing function """

    def __init__(self):
        super().__init__()


        self.setWindowTitle("Printing Test")
        self.printer = QPrinter()
        self.printer.setPageSize(QPrinter.A4)
        self.mainLayout()

        
    def mainLayout(self):

        self.layout = QHBoxLayout()
        self.print_button = QPushButton("Print")
        self.preview_button = QPushButton("Print Preview")

        self.layout.addWidget(self.preview_button)
        self.layout.addWidget(self.print_button)
                

        self.mainWidget = QWidget()
        self.mainWidget.setLayout(self.layout)

        self.setCentralWidget(self.mainWidget)
        
        self.preview_button.clicked.connect(self.print_preview)
        self.print_button.clicked.connect(self.printViaHtml)


    def createHtml(self):
        date = datetime.datetime.today()
        date_time = date.strftime("%d-%m-%Y %H:%M")
        company_address = ["21-23 Station Road","Silloth","Cumbria","CA7 4AE"]
        company_contact = ["Phone: 016973 20242","Email: beaconvets@gmail.com"]
        invoice_to = "mattling9@hotmail.co.uk"
        invoice_number = "4"
        invoice_date = "21-1-2015"
        product_order = [["Pedigree Chum","2","3.99","7.98"]]
        subtotal = "7.98"
        discount = "0.80"
        total = "7.18"
        invoice_history = [["22-1-2015 14:19","Invoice Sent"],["22-1-2015 14:18","Invoice Created"]]
        
        html = u""
        html += """<html>

                <head>
                <style>
                table, th, td {border: 1px solid white; border-collapse: collapse}
                th, td {padding: 5px; text-align: left}
                body{padding:10px; background-color:white; width:21cm; height:28cm; margin: 10px; box-shadow: 0px 0px 30px rgba(50, 50, 50, 0.75);} 
                </style>
                </head>
                <body style="font-family:'Verdana'; font-size:13px">
                <br>
                <img src="C:/Users/Matt/Desktop/GitHub/COMP4Coursework/Implementation/Gui/images/Logo.jpg" alt="HTML5 Icon" width="109" height="109">
                <br>
                <b>Beacon Veterinary Centre </b> 
                <br>"""

        for item in company_address:
            html += """{0} <br> """.format(item)
        html += "<br>"

        for line in company_contact:
            html += """{0} <br> """.format(line)
        html += """ <br>
                    <div align="right"> 

                    <table style="width:45%">
                    <tr>
                    <td bgcolor= "#94FF70"><b>Invoice Number<bb/></td>"""
                 
        html += """<td bgcolor="#F8F8F8">{0}</td>
                   </tr>
                   <tr>""".format(invoice_number)
        html += """<td bgcolor="#94FF70"><b>Invoice Date<b/></td>"""
        html += """<td bgcolor="#F8F8F8">{0}</td>""".format(invoice_date)
        html += """  </tr>
                     </table>
                     </div>
                     <b>Invoice To:</b> <br>"""
        html += "{0} <br><br><br><br>".format(invoice_to)
        html += """<div> 

                   <table width="100%">
                   <tr>
                   <td bgcolor="#94FF70"><b>Description<bb/></td>
                   <td bgcolor="#94FF70"><b>Quantity</b></td>
                   <td bgcolor="#94FF70"><b>Price</b></td>
                   <td bgcolor="#94FF70"><b>Total Price</b></td>			
                   </tr>
                   <tr>"""
        for line in product_order:
            html += """<td bgcolor="#F8F8F8">{0}</td>
                       <td bgcolor="#F8F8F8">{1}</td>
                       <td bgcolor="#F8F8F8">{2}</td>
                       <td bgcolor="#F8F8F8">{3}</td>""".format(line[0],line[1],line[2],line[3])
        html +=   """</tr>
                     <tr>"""
        for count in range(0,4):
            html += """<td bgcolor="#F8F8F8"></td>"""
        html += """</tr>
                   <tr>
                   <td bgcolor="#F8F8F8"></td>
                   <td bgcolor="#F8F8F8"></td>
                   <td bgcolor="#94FF70"><b>Subtotal:</b></td>"""
        html += """<td bgcolor="#F8F8F8">{0}</td>		
                   </tr>
                   <tr>
                   <td bgcolor="#F8F8F8"></td>
                   <td bgcolor="#F8F8F8"></td>
                   <td bgcolor="#94FF70"><b>Discount:</b></td>""".format(subtotal)
        html += """<td bgcolor="#F8F8F8">{0}</td>		
                   </tr>
                   <tr>
                   <td bgcolor="#F8F8F8"></td>
                   <td bgcolor="#F8F8F8"></td>
                   <td bgcolor="#94FF70"><b>Total:</b></td>""".format(discount)
        html += """<td bgcolor="#94FF70"><b>7.18</b></td>		
                   </tr>
                   </table>
                   <br><br><br><br><br>

                   </div>
                   <div > 
    
                   <table width:45%;>
                   <tr>
                   <th bgcolor= "#E0E0E0"><b>Date and Time</b>
                   <th bgcolor= "#E0E0E0"><b>Invoice History</b>
                   </tr>
                   <tr>"""
        html += """<td bgcolor= "#F8F8F8">{0}</td>
                   <td bgcolor="#F8F8F8">Invoice Sent</td>		
                   </tr>
                   <tr>""".format(date_time)
        html += """<td bgcolor="#F8F8F8">{0}</td>
                   <td bgcolor="#F8F8F8">Invoice Created</td>		
                   </tr>
                   </table>
                   </div>

                  <br>
                  <br>
                  </body>
                  </html>""".format(date_time)
        return html

        

    def printViaHtml(self):

        html = self.createHtml()
        document = QTextDocument()
        document.setHtml(html)

        dialog = QPrintDialog(self.printer, self)
        if dialog.exec_():
            document = QTextDocument()
            document.setHtml(html)
            document.print_(self.printer)
            print("Print Successful")
        else:
            print("The print process has failed!")

    def print_preview(self):
        html = self.createHtml()
        document = QTextDocument()
        document.setHtml(html)
        PrintPreview = QPrintPreviewDialog(self.printer, self)
        PrintPreview.paintRequested.connect(document.print_)
        PrintPreview.showFullScreen()
        PrintPreview.exec()
        PrintPreview.showFullScreen()
        


if __name__ == "__main__":

    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    window.raise_()
    app.exec_()
