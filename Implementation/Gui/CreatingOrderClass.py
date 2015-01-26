import sqlite3, sys, random, smtplib, datetime
from PyQt4.QtSql import *
from PyQt4.QtGui import *
from PyQt4.QtCore import *
from PopUpMenuClass import *
from AddingRemovingData import *
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart

class createOrderClass(QWidget):
    """A representation of creating an order"""
    def __init__(self):
        super().__init__()
        ProductID_list = []
        self.category_layout = QHBoxLayout()
        self.category_label = QLabel("Find Product:")
        self.category_label.setFixedWidth(70)
        self.category_search = QLineEdit()
        self.category_search.textChanged.connect(self.find_product)
        self.category_layout.addWidget(self.category_label)
        self.category_layout.addWidget(self.category_search)
        self.category_widget = QWidget()
        self.category_widget.setLayout(self.category_layout)
        self.subtotal_price = 0.00
        ProductList = [""]

      #Product Display Table
        self.display_table = QTableView()
        self.display_table.setFixedHeight(150)
        self.display_table_layout = QVBoxLayout()
        self.display_table_layout.addWidget(self.display_table)
        self.display_table.setSelectionBehavior(QAbstractItemView.SelectRows)
        self.display_table.setAlternatingRowColors(True)
        self.display_table_widget = QWidget()
        self.display_table_widget.setLayout(self.display_table_layout)
        self.model = None
        if not self.model or not isinstance(self.model, QSqlTableModel):
            self.model = QSqlTableModel()
        
        self.model.setTable("Product")
        self.model.select()
        self.display_table.setModel(self.model)
        self.display_table.hideColumn(5)
        self.display_table.hideColumn(6)
        self.display_table.hideColumn(7)
        column_width_list = [80, 300, 90, 75]
        counter = 0
        for item in column_width_list:
            self.display_table.setColumnWidth(counter, item)
            counter += 1

        

        self.display_table.horizontalHeader().setStretchLastSection(True)
        self.display_table.setEditTriggers(QAbstractItemView.NoEditTriggers)
        self.display_table.doubleClicked.connect(self.clicked)
        self.display_table.show()

        self.table_layout = QVBoxLayout()

        self.add_product = QPushButton("Add Product")
        self.add_product.setFixedWidth(100)
        self.add_product.clicked.connect(self.clicked, 0)
        self.table_layout.addWidget(self.display_table)
        self.table_layout.addWidget(self.add_product)
        self.table_widget = QWidget()
        self.table_layout.setAlignment(Qt.AlignCenter)
        self.table_widget.setLayout(self.table_layout)
        self.find_product_box = QGroupBox("Finding Product")
        self.find_product_layout = QVBoxLayout()
        self.find_product_layout.addWidget(self.category_widget)
        self.find_product_layout.addWidget(self.table_widget)
        self.find_product_box.setLayout(self.find_product_layout)

        self.member_label = QLabel("Member ID:")
        self.member_line_edit = QLineEdit()
        self.member_button = QPushButton("Enter")
        self.member_button.clicked.connect(self.find_member_by_id)
        self.member_layout = QHBoxLayout()
        self.member_widget = QWidget()
        self.member_layout.addWidget(self.member_label)
        self.member_layout.addWidget(self.member_line_edit)
        self.member_widget.setLayout(self.member_layout)
        self.subtotal_label = QLabel("Subtotal: £")
        self.subtotal_label.setAlignment(Qt.AlignRight)
        self.total_label = QLabel("Total: £")
        self.total_label.setAlignment(Qt.AlignRight)
        self.tax_label = QLabel("Discount: £")
        self.tax_label.setAlignment(Qt.AlignRight)
        self.subtotal = QLineEdit("0.0")
        self.subtotal.setReadOnly(True)
        self.subtotal.setFixedWidth(65)
        self.discount_line_edit = QLineEdit("0.0")
        self.discount_line_edit.setReadOnly(True)
        self.discount_line_edit.setFixedWidth(65)
        self.total = QLineEdit("0.0")
        self.total.setReadOnly(True)
        self.total.setFixedWidth(65)

        #Subtotal, Tax and Total Prices
        self.price_layout = QGridLayout()
        self.price_layout.addWidget(self.member_widget, 0,0)
        self.price_layout.addWidget(self.member_button, 0,1)
        self.price_layout.addWidget(self.subtotal_label, 1,0)
        self.price_layout.addWidget(self.tax_label, 2,0)
        self.price_layout.addWidget(self.total_label, 3,0)
        self.price_layout.addWidget(self.subtotal, 1,1)
        self.price_layout.addWidget(self.discount_line_edit, 2,1)
        self.price_layout.addWidget(self.total, 3,1)
        self.price_widget = QWidget()
        self.price_widget.setLayout(self.price_layout)

        #Create Invoice Button
        self.preview_button = QPushButton("Preview")
        self.preview_button.setFixedWidth(200)
        self.preview_button.clicked.connect(self.preview_invoice_clicked)
        self.print_checkbox = QCheckBox("Print Invoice")
        self.email_invoice = QCheckBox("Send Invoice To Email")
        self.email_invoice.stateChanged.connect(self.enable_email)
        self.email_invoice_address = QLineEdit()
        self.email_invoice_address.setPlaceholderText("Email Address")
        self.email_invoice_address.setEnabled(False)

        self.buttonBox = QDialogButtonBox()
        self.buttonBox.setOrientation(Qt.Horizontal)
        self.buttonBox.setStandardButtons(QDialogButtonBox.Save |QDialogButtonBox.Cancel)
        self.buttonBox.button(QDialogButtonBox.Save).clicked.connect(self.invoice_saved)
        
        self.invoice_layout = QVBoxLayout()
        self.invoice_layout.addWidget(self.preview_button)
        self.invoice_layout.addWidget(self.print_checkbox)
        self.invoice_layout.addWidget(self.email_invoice)
        self.invoice_layout.addWidget(self.email_invoice_address)
        self.invoice_widget = QWidget()
        self.invoice_widget.setLayout(self.invoice_layout)
    

        #order_group_box
        self.order_box = QGroupBox("Current Order")
        self.order_layout = QVBoxLayout()
        self.current_order = QTableWidget(0,5)
        self.current_order.setAlternatingRowColors(True)
        self.column_headers = ["ProductID","Product Name","Size","Price","Quantity"]
        self.current_order.setHorizontalHeaderLabels(self.column_headers)
        column_width_list = [100, 300, 90, 75]
        counter = 0
        for item in column_width_list:
            self.current_order.setColumnWidth(counter, item)
            counter += 1
            
        self.current_order.horizontalHeader().setStretchLastSection(True)
        self.current_order.setSelectionBehavior(QAbstractItemView.SelectRows)
        self.order_layout.addWidget(self.current_order)
        self.order_layout.addWidget(self.price_widget)
        self.order_box.setLayout(self.order_layout)



        self.main_layout = QVBoxLayout()
        self.main_layout.addWidget(self.find_product_box)
        self.main_layout.addWidget(self.order_box)
        self.main_layout.addWidget(self.invoice_widget)
        self.main_layout.addWidget(self.buttonBox)
        self.setLayout(self.main_layout)
        self.discount = 0

    def invoice_saved(self):
        if self.print_checkbox.isChecked() and self.email_invoice.isChecked():
            self.print_document()
            self.email_document()
        elif self.print_checkbox.isChecked():
            self.print_document()
        elif self.email_invoice.isChecked():
            self.email_document()

    def preview_invoice_clicked(self):
        self.printer = QPrinter()
        html = self.createHtml()
        document = QTextDocument()
        document.setHtml(html)
        PrintPreview = QPrintPreviewDialog(self.printer, self)
        PrintPreview.paintRequested.connect(document.print_)
        PrintPreview.showFullScreen()
        PrintPreview.exec()
        PrintPreview.showFullScreen()

    def createHtml(self):
        date = datetime.datetime.today()
        date_time = date.strftime("%d-%m-%Y %H:%M")
        
        company_address = ["21-23 Station Road","Silloth","Cumbria","CA7 4AE"]
        company_contact = ["Phone: 016973 20242","Email: beaconvets@gmail.com"]
        invoice_to = self.email_invoice_address.text()
        invoice_number = "4"
        invoice_date = datetime.date.today().strftime("%d-%m-%Y")
        product_order = []
        for row in range(0, self.current_order.rowCount()):
            product = str(self.current_order.item(row, 0).text()), str(self.current_order.item(row, 1).text()), str(self.current_order.item(row, 2).text()), str(self.current_order.item(row, 3).text()), str(self.current_order.item(row, 4).text())
            product_order.append(product)
            
        subtotal = self.subtotal.text()
        discount = self.discount_line_edit.text()
        total = self.total.text()
        invoice_history = [[date ,"Invoice Sent"],[date,"Invoice Created"]]
        
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
                <img src="./images/Logo.jpg" alt="Beacon Veterinary Centre Logo" width="109" height="109">
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
                   <td bgcolor="#94FF70"><b>Size</b></td>
                   <td bgcolor="#94FF70"><b>Quantity</b></td>
                   <td bgcolor="#94FF70"><b>Price</b></td>
                   <td bgcolor="#94FF70"><b>Total Price</b></td>			
                   </tr>"""
        for product in product_order:
            total_price = float(product[3]) * float(product[4])
            rounded_total = round(total_price,4)
            html += """<tr>"""
            html += """<td bgcolor="#F8F8F8">{0}</td>""".format(product[1])
            html += """<td bgcolor="#F8F8F8">{0}</td>""".format(product[2])
            html += """<td bgcolor="#F8F8F8">{0}</td>""".format(product[4])
            html += """<td bgcolor="#F8F8F8">{0}</td>""".format(product[3])
            html += """<td bgcolor="#F8F8F8">{0}</td>""".format(rounded_total)
            html +=   """</tr>"""
        html += "<tr>"
        for count in range(0,5):        
            html += """<td bgcolor="#F8F8F8"></td>"""
        html += """</tr>
                   <tr>
                   <td bgcolor="#F8F8F8"></td>
                   <td bgcolor="#F8F8F8"></td>
                   <td bgcolor="#F8F8F8"></td>
                   <td bgcolor="#94FF70"><b>Subtotal:</b></td>"""
        html += """<td bgcolor="#F8F8F8">{0}</td>		
                   </tr>
                   <tr>
                   <td bgcolor="#F8F8F8"></td>
                   <td bgcolor="#F8F8F8"></td>
                   <td bgcolor="#F8F8F8"></td>
                   <td bgcolor="#94FF70"><b>Discount:</b></td>""".format(subtotal)
        html += """<td bgcolor="#F8F8F8">{0}</td>		
                   </tr>
                   <tr>
                   <td bgcolor="#F8F8F8"></td>
                   <td bgcolor="#F8F8F8"></td>
                   <td bgcolor="#F8F8F8"></td>
                   <td bgcolor="#94FF70"><b>Total:</b></td>""".format(discount)
        html += """<td bgcolor="#94FF70"><b>{0}</b></td>		
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
                   <tr>""".format(total)
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

        

    def print_document(self):
        self.printer = QPrinter()
        html = self.createHtml()
        document = QTextDocument()
        document.setHtml(html)

        dialog = QPrintDialog(self.printer, self)
        if dialog.exec_():
            document = QTextDocument()
            document.setHtml(html)
            document.print_(self.printer)
        print("document printed")


    def email_document(self):
        date = datetime.date.today()
        date = date.strftime("%d-%m-%Y")
        subject = ("Beacon Vets Invoice from {0}".format(date))
        html = self.createHtml()
        text = ("Hello, Here is the Invoice from the order you made on: {0}".format(date))
        message = MIMEText(html, 'html')
        msg = MIMEMultipart('alternative')
        msg['Subject'] = subject
        msg['From'] = "beaconvets@gmail.com"
        msg['To'] = self.email_invoice_address.text()

        part1 = MIMEText(text, 'plain')
        part2 = MIMEText(html, 'html')
        msg.attach(part1)
        msg.attach(part2)
        
        mail = smtplib.SMTP('smtp.gmail.com','587')
        mail.ehlo()
        mail.starttls()
        mail.login('mattling147@gmail.com','alienware')
        mail.sendmail('mattling147@gmail.com', self.email_invoice_address.text(), msg.as_string())
        mail.close()
        print("email sent")

    def enable_email(self):
        if self.email_invoice.isChecked():
            self.email_invoice_address.setEnabled(True)
        else:
            self.email_invoice_address.setEnabled(False)

    def clicked_Ok(self):
        self.pop_up_instance.close()

    def clicked(self):
        self.indexes = self.display_table.selectionModel().selection().indexes()
        rows = []
        for selected_row in self.indexes:
            row_number = selected_row.row()
            if row_number not in rows:
                rows.append(row_number)      
        no_of_rows_selected = len(rows)
        if no_of_rows_selected == 1:
            self.selected_product_id = self.model.record(rows[0]).field(0).value()
            product_info = self.find_product_by_id(self.selected_product_id)
        if self.indexes:
            for index in self.indexes:
                row = index.row()
                row += 1

                
        inTable = False
        if self.current_order.rowCount() != 0:
            for row in range(0, self.current_order.rowCount()):
                if product_info[0][0] == int(self.current_order.item(row,0).text()):
                    new_quantity = int(self.current_order.item(row,4).text()) + 1
                    self.current_order.setItem(row,4, (QTableWidgetItem(str(new_quantity))))
                    self.subtotal_price = float(self.current_order.item(row,3).text()) * float(self.current_order.item(row,4).text())
                    inTable  = True

        if inTable == False:
            new_row = (self.current_order.rowCount())
            self.current_order.insertRow(new_row)
            count = 0
            for item in product_info[0]:
                self.current_order.setItem(new_row, count, (QTableWidgetItem(str(item))))
                count += 1
            self.current_order.setItem(new_row, 4, (QTableWidgetItem(str(1))))
            self.subtotal_price += float(self.current_order.item(new_row,3).text())

        
        self.subtotal_price = round(self.subtotal_price, 4)
        self.discount_multiplier = (1 - self.discount)
        self.total_price = (self.discount_multiplier * self.subtotal_price)
        self.total_price = round(self.total_price, 4)
        self.money_off = (self.subtotal_price - self.total_price)
        self.money_off = round(self.money_off, 4)
        
        self.subtotal.setText(str(self.subtotal_price))
        self.discount_line_edit.setText(str(self.money_off))

        self.total.setText(str(self.total_price))
        
    def change_price(self):
        self.subtotal_price
        self.discount_multiplier = (1 - self.discount)
        
        self.total_price = (self.discount_multiplier * self.subtotal_price)

        
        self.money_off = (self.subtotal_price - self.total_price)

            
        if len(str(self.subtotal_price)) == 5:
            self.subtotal.setText(str(self.subtotal_price)[:5])
            self.discount_line_edit.setText(str(self.money_off)[:5])
            self.total.setText(str(self.total_price)[:5])

        elif len(str(self.subtotal_price)) == 6:
            self.subtotal.setText(str(self.subtotal_price)[:6])
            self.discount_line_edit.setText(str(self.money_off)[:6])
            self.total.setText(str(self.total_price)[:6])

        else:
            self.subtotal.setText(str(self.subtotal_price)[:4])
            self.discount_line_edit.setText(str(self.money_off)[:4])
            self.total.setText(str(self.total_price)[:4])

    def find_product(self):
        ProductName = self.category_search.text()
        filter_query = "ProductID like '%{0}%' or ProductName like '%{0}%' or Size like '%{0}%' or Price like '%{0}%' or Category like '%{0}%'".format(ProductName)
        self.model.setFilter(filter_query)
        self.model.select()

    def find_product_by_id(self, product_id):
        with sqlite3.connect("ProductDatabase.db") as db:
            cursor = db.cursor()
            cursor.execute("SELECT ProductID, ProductName, Size, Price FROM Product WHERE ProductID = ?",(product_id,))
            product_info = cursor.fetchall()
            db.commit()
            return product_info
            
                
            


    def find_member_by_id(self):
        with sqlite3.connect("ProductDatabase.db") as db:
            member_id = self.member_line_edit.text()
            cursor = db.cursor()
            cursor.execute("SELECT * FROM Member WHERE MemberID = ?",(member_id,))
            product_info = cursor.fetchall()
            db.commit()
            if product_info:
                self.discount = 0.1
                self.change_price()
                self.email_invoice_address.setText(product_info[0][11])
            if not product_info:
                self.discount = 0.0
                self.change_price()
                self.display_message()

    def display_message(self):
        self.member_id_error_instance = PopUpWindow("Beacon Vets Stock Control",300,100)
        self.icon = QIcon(QPixmap("./images/Logo.jpg"))
        self.member_id_error_instance.setWindowIcon(self.icon)
        self.label = QLabel("Sorry, that MemberID is not valid.")
        self.label.setAlignment(Qt.AlignCenter)
        self.buttonBox = QDialogButtonBox()
        self.buttonBox.setOrientation(Qt.Horizontal)
        self.buttonBox.setStandardButtons(QDialogButtonBox.Ok | QDialogButtonBox.Cancel)
        self.buttonBox.button(QDialogButtonBox.Ok).clicked.connect(self.close_pop_up)
        self.buttonBox.button(QDialogButtonBox.Cancel).clicked.connect(self.close_pop_up)
        self.pop_up_layout = QVBoxLayout()
        self.pop_up_widget = QWidget()
        self.pop_up_layout.addWidget(self.label)
        self.pop_up_layout.addWidget(self.buttonBox)
        self.pop_up_widget.setLayout(self.pop_up_layout)
        self.member_id_error_instance.setCentralWidget(self.pop_up_widget)
        self.member_id_error_instance.move(800,450)
        self.member_id_error_instance.show()
        self.member_id_error_instance.raise_()

    def close_pop_up(self):
        self.member_id_error_instance.close()

    def save_invoice(self):
        createCustomerOrder(self)

    def save_sucess(self):
        self.add_product_instance = PopUpWindow("Beacon Vets Adding Product", 300, 100)
        self.icon = QIcon(QPixmap("./images/Logo.jpg"))
        self.add_order_instance.setWindowIcon(self.icon)
        self.label = QLabel("Order Sucessfully Saved")
        self.label.setAlignment(Qt.AlignCenter)
        self.buttonBox = QDialogButtonBox()
        self.buttonBox.setOrientation(Qt.Horizontal)
        self.buttonBox.setStandardButtons(QDialogButtonBox.Ok | QDialogButtonBox.Cancel)
        self.buttonBox.button(QDialogButtonBox.Ok).clicked.connect(self.close_pop_ups)
        self.buttonBox.button(QDialogButtonBox.Cancel).clicked.connect(self.close_pop_ups)
        self.pop_up_layout = QVBoxLayout()
        self.pop_up_widget = QWidget()
        self.pop_up_layout.addWidget(self.label)
        self.pop_up_layout.addWidget(self.buttonBox)
        self.pop_up_widget.setLayout(self.pop_up_layout)
        self.add_order_instance.setCentralWidget(self.pop_up_widget)
        self.add_order_instance.move(800,450)
        self.add_order_instance.show()
        self.add_order_instance.raise_()
        
       
