import sqlite3, sys, datetime, calendar
from PyQt4.QtCore import *
from PyQt4.QtGui import *
from PyQt4.QtSql import *
#-----------------------------------------Product-----------------------------------------

def addingProduct(name, size, price, category, location1, location2, image_path, weekly_sales):
    Product = (name, size, price, category, location1, location2, image_path, weekly_sales)
    with sqlite3.connect("ProductDatabase.db") as db:
        cursor = db.cursor()
        sql = "insert into Product (ProductName, Size, Price, Category, Location1, Location2, ImagePath, WeeklySales) values(?,?,?,?,?,?,?,?)"
        cursor.execute(sql,Product)
        db.commit()

def editProduct(product_id, name, size, price, category, path):
    Product = (name, size, price, category, path, product_id)
    with sqlite3.connect("ProductDatabase.db") as db:
        cursor = db.cursor()
        sql = "UPDATE Product SET ProductName= ?,  Size = ?,  Price = ?, Category= ?, ImagePath= ? WHERE ProductID = ?"
        cursor.execute(sql,Product)
        db.commit()

def edit_stock(product_id, location1, location2):
    with sqlite3.connect("ProductDatabase.db") as db:
        Product = (location1, location2, product_id)
        cursor = db.cursor()
        sql = "UPDATE Product SET Location1 = ?, Location2 = ? WHERE ProductID = ?"
        cursor.execute(sql, Product)
        db.commit()


def deletingProduct(product_id):
    data = (product_id,)
    with sqlite3.connect("ProductDatabase.db") as db:
        cursor = db.cursor()
        sql = "delete from Product where ProductID = ?"
        cursor.execute(sql,data)
        db.commit()

#-----------------------------------------Member-----------------------------------------


def addingMember(Title,MemberFirstName,MemberLastName,HouseNo,Street,Town,City,County,Postcode,TelephoneNo, MemberEmail):
    Member = (Title,MemberFirstName,MemberLastName,HouseNo,Street,Town,City,County,Postcode,TelephoneNo, MemberEmail)
    with sqlite3.connect("ProductDatabase.db") as db:
        cursor = db.cursor()
        sql = "insert into Member (Title, MemberFirstName, MemberLastName, HouseNo, Street, Town, City, County, Postcode, TelephoneNo, MemberEmail) values(?,?,?,?,?,?,?,?,?,?,?)"
        cursor.execute(sql,Member)
        db.commit()

def editMember(Title,MemberFirstName,MemberLastName,HouseNo,Street,Town,City,County,Postcode,TelephoneNo, MemberEmail, MemberID):
    Member = (Title,MemberFirstName,MemberLastName,HouseNo,Street,Town,City,County,Postcode,TelephoneNo, MemberEmail, MemberID)
    with sqlite3.connect("ProductDatabase.db") as db:
        cursor = db.cursor()
        sql = """UPDATE Member SET Title = ?,
                                   MemberFirstName = ?,
                                   MemberLastName = ?,
                                   HouseNo = ?,
                                   Street = ?,
                                   Town = ?,
                                   City = ?,
                                   County = ?,
                                   Postcode = ?,
                                   TelephoneNo = ?,
                                   MemberEmail = ?
                                   WHERE MemberID = ?"""
        cursor.execute(sql,Member)
        db.commit()

def deletingMember(MemberID):
    data = (MemberID,)
    with sqlite3.connect("ProductDatabase.db") as db:
        cursor = db.cursor()
        sql = "delete from Member where MemberID = ?"
        cursor.execute(sql,data)
        db.commit()


#-----------------------------------------Employee-----------------------------------------

def addingEmployee(EmployeeUserName,EmployeeFirstName,EmployeeLastName,EmployeeEmail,EmployeePassword):
    Employee = (EmployeeUserName,EmployeeFirstName,EmployeeLastName,EmployeeEmail,EmployeePassword)
    with sqlite3.connect("ProductDatabase.db") as db:
        cursor = db.cursor()
        sql = "insert into Employee (EmployeeUserName, EmployeeFirstName, EmployeeLastName, EmployeeEmail, EmployeePassword) values(?,?,?,?,?)"
        cursor.execute(sql,Employee)
        db.commit()

def editingEmployee(EmployeeID, EmployeeUserName, EmployeeFirstName,EmployeeLastName,EmployeeEmail):
    Employee = (EmployeeUserName,EmployeeFirstName,EmployeeLastName, EmployeeEmail, EmployeeID)
    with sqlite3.connect("ProductDatabase.db") as db:
        cursor = db.cursor()
        sql = """Update Employee SET EmployeeUserName = ?,
                                     EmployeeFirstName = ?,
                                     EmployeeLastName = ?,
                                     EmployeeEmail = ?
                                     WHERE EmployeeID= ?"""
        cursor.execute(sql, Employee)
        db.commit()

def deletingEmployee():
    EmployeeID = input("Enter EmployeeID To Delete")
    data = (EmployeeID,)
    with sqlite3.connect("ProductDatabase.db") as db:
        cursor = db.cursor()
        sql = "delete from Employee where EmployeeID = ?"
        cursor.execute(sql,data)
        db.commit()
#-----------------------------------------Location-----------------------------------------


def addingLocation():
    LocationName = input("Enter Location Name")
    Location = (LocationName,)
    with sqlite3.connect("ProductDatabase.db") as db:
        cursor = db.cursor()
        sql = "insert into Location (LocationName) values(?)"
        cursor.execute(sql,Location)
        db.commit()



def deletingLocation():
    LocationID = input("Enter LocationID To Delete")
    data = (LocationID,)
    with sqlite3.connect("ProductDatabase.db") as db:
        cursor = db.cursor()
        sql = "delete from Location where LocationID = ?"
        cursor.execute(sql,data)
        db.commit()

#------------------------------------------------------------------------------------------
def addingCustomerOrder(member_id, employee_id, date_time):
    CustomerDetails = (member_id, employee_id, date_time)
    with sqlite3.connect("ProductDatabase.db") as db:
        cursor = db.cursor()
        sql = "insert into CustomerOrder (MemberID, EmployeeID, DateTime) values(?,?,?)"
        cursor.execute(sql, CustomerDetails)
        db.commit()

def removingCustomerOrder():
    Order_ID = "1"
    with sqlite3.connect("ProductDatabase.db") as db:
        cursor = db.cursor()
        sql = "delete FROM CustomerOrder WHERE OrderID = ?"
        cursor.execute(sql, Order_ID)
        db.commit()


        
def addingOrder(order_id, ProductID, name, size, price, quantity):
    order_info = (order_id, ProductID, name, size, price, quantity)
    with sqlite3.connect("ProductDatabase.db") as db:
        cursor = db.cursor()
        sql = "insert into ProductOrder (OrderID, ProductID, ProductName, Size, Price, Quantity) values(?,?,?,?,?,?)"
        cursor.execute(sql, order_info)
        db.commit()

def IncrementQuantity(ProductID, quantity):
    with sqlite3.connect("ProductDatabase.db") as db:
        cursor = db.cursor()
        quantity += 1
        product_info = [quantity, ProductID]
        sql = "Update ProductOrder Set Quantity= ? where ProductID = ?"
        cursor.execute(sql, product_info)
        db.commit()

def FindProductByName(self, ProductName):
        with sqlite3.connect("ProductDatabase.db") as db:
            find_product_cursor = db.cursor()
            find_product_cursor.execute("SELECT * FROM Product where 1=1")
            db.commit()
            ProductsFound = find_product_cursor.fetchall()
            ProductList = []
            MatchedProducts = []
            MatchedProductsTuple = tuple(MatchedProducts)
            for item in ProductsFound:
                ProductList.append(item)
            for count in range(0, len(ProductList)):
                if ProductName in ProductList[count][1]:
                    MatchedProducts.append(ProductList[count][0])
                else:
                    pass
            MatchedProductsTuple = tuple(MatchedProducts)
            if len(MatchedProducts) > 0:
                query = QSqlQuery("SELECT * FROM Product where ProductID IN (:id)")
                query.bindValue(":id", MatchedProductsTuple)
                self.query_model.setQuery(query)
                self.query_table.setModel(self.query_model)
                self.query_table.show()
                
            
            else:
                no_match_cursor = db.cursor()
                no_match_cursor.execute("SELECT * FROM Product where ProductID = -1")


def get_order_id():
    with sqlite3.connect("ProductDatabase.db") as db:
            cursor = db.cursor()
            cursor.execute("SELECT * FROM ProductOrder")
            items = cursor.fetchall()
    return items

def updateSettings(logo, company_name, street, town, city, county, postcode, phone, email_address, gmail_address, gmail_password):
    with sqlite3.connect("ProductDatabase.db") as db:
        cursor = db.cursor()
        settings_id = 1
        search_cursor = db.cursor()
        settings_data = (logo, company_name, street, town, city, county, postcode, phone, email_address, gmail_address, gmail_password)
        settings_data_with_id = (settings_id, logo, company_name, street, town, city, county, postcode, phone, email_address, gmail_address, gmail_password)
        cursor.execute("SELECT * FROM Settings where 1=1")
        item_in_list = cursor.fetchall()
        if not item_in_list:
            sql = "insert into Settings (SettingsID, Logo,  CompanyName,  Street, Town , City, County, Postcode, Phone, EmailAddress, GmailAddress, GmailPassword) values(?,?,?,?,?,?,?,?,?,?,?,?)"
            search_cursor.execute(sql, settings_data_with_id)
            db.commit()
        else:
            sql = "UPDATE Settings Set Logo = ?,  CompanyName = ?,  Street = ?, Town= ?, City = ?, County = ?, Postcode = ?, Phone = ?, EmailAddress = ?, GmailAddress = ?, GmailPassword = ? where SettingsID = 1"
            search_cursor.execute(sql, settings_data)
            db.commit()

def getSettings():
    with sqlite3.connect("ProductDatabase.db") as db:
        cursor = db.cursor()
        cursor.execute("SELECT * FROM Settings where SettingsID = 1")
        settings = cursor.fetchall()
    return settings

############################################################ MUST SAY WHERE I GOT THIS CODE FROM... #####################################################
def change_password(password, shift):
	password = password.lower()
	encrypted_password = ""
	for c in password:
		if c in "abcdefghijklmnopqrstuvwxyz":
			num = ord(c)
			num += shift
			if num > ord("z"):
				num -= 26
			elif num < ord("a"):
				num += 26
			encrypted_password += chr(num)
		else:
			encrypted_password += c
	return encrypted_password
#########################################################################################################################################################

def getStock(product_id):
    product_info = (product_id,)
    with sqlite3.connect("ProductDatabase.db") as db:
            cursor = db.cursor()
            sql = ("SELECT Location1 FROM Product WHERE ProductID = ?")
            cursor.execute(sql, product_info)
            current_stock = cursor.fetchall()
    return current_stock

def editStock(new_stock, product_id):
    with sqlite3.connect("ProductDatabase.db") as db:
        product_info = (new_stock, product_id,)
        cursor = db.cursor()
        sql = "UPDATE Product SET Location1= ? WHERE ProductID = ?"
        cursor.execute(sql, product_info)
        db.commit()


def update_weekly_sales(product_id, sales):
    with sqlite3.connect("ProductDatabase.db") as db:
        find_cursor = db.cursor()
        find_info = (product_id)
        find_sql = "SELECT WeeklySales from Product WHERE ProductID = ?"
        find_cursor.execute(find_sql, find_info)
        returned_sales = find_cursor.fetchall()
        if not returned_sales:
            current_weekly_sales = 0
        else:
            current_weekly_sales = returned_sales[0][0]
        new_weekly_sales = current_weekly_sales + int(sales)
        
        
        
        update_cursor = db.cursor()
        update_info = (new_weekly_sales, product_id,)
        update_sql = "UPDATE Product SET WeeklySales= ? WHERE ProductID = ?"
        update_cursor.execute(update_sql, update_info)
        db.commit()

def reset_weekly_sales(product_id):
    with sqlite3.connect("ProductDatabase.db") as db:
        cursor = db.cursor()
        product_info = (str(product_id))
        sql = "UPDATE Product SET WeeklySales = 0  WHERE ProductID = ?"
        cursor.execute(sql, product_info)
        
def get_date_stored():
        with sqlite3.connect("ProductDatabase.db") as db:
            cursor = db.cursor()
            sql = "SELECT SalesDate from Settings"
            cursor.execute(sql)
            date_stored = cursor.fetchall()
        return date_stored

def update_date(input_date):
        with sqlite3.connect("ProductDatabase.db") as db:
            product_info = (input_date,)
            cursor = db.cursor()
            sql = "UPDATE Settings SET SalesDate = ?"
            cursor.execute(sql, product_info)

def get_current_week_sales(product_id):
    with sqlite3.connect("ProductDatabase.db") as db:
        product_info = (product_id,)
        weekly_sales = []
        cursor = db.cursor()
        sql =("SELECT WeeklySales From Product WHERE ProductID =?")
        cursor.execute(sql, product_info)
        returned_sales = cursor.fetchall()
        if returned_sales:
            for item in returned_sales[0]:
                weekly_sales.append(item)
    return weekly_sales

def get_all_product_id():
    with sqlite3.connect("ProductDatabase.db") as db:
        product_id_list = []
        cursor = db.cursor()
        cursor.execute("SELECT * From Product")
        products = cursor.fetchall()
        for product in products:
            product_id_list.append(product[0])
    return product_id_list


def check_date():

    
    #get date stored as SalesDate
    date_stored = get_date_stored()
    
    current_date = datetime.date.today()
    current_year = current_date.year
    current_month = current_date.month
    current_day = current_date.day
    
    if current_day < 8:
        current_month = current_date.month
        last_month = current_month - 1
        next_month = current_month + 1
        no_days_last_month = calendar.monthrange(current_date.year, last_month)[1]
        days_to_minus = 7 - current_day
        previous_month = datetime.date(current_year, last_month, no_days_last_month)
        new_day = previous_month.day - days_to_minus
        new_date = datetime.date(current_year, last_month, new_day)

    else:
        new_date = datetime.date(current_year, current_month, (current_day - 7))

    new_date = new_date.strftime("%d-%m-%Y")
    
    if not date_stored:
        print("date updated")
        update_date(current_date.strftime("%d-%m-%Y"))

    elif date_stored[0][0] == "":
        print("date updated")
        update_date(current_date.strftime("%d-%m-%Y"))

    elif date_stored == new_date:
        #IF A WEEK HAS PASSED ADD WEEKLY SALES TO TOTAL SALES AND CHANGE WEEKLY SALES TO 0. STORE CURRENT DATE AS SALES DATE
        product_id_list = get_all_product_id()
        for product_id in product_id_list:
            total_sales_list = []
            total_sales = get_total_sales(str(product_id))
            for item in total_sales:
                total_sales_list.append(item)
            weekly_sales = get_current_week_sales(str(product_id))
            total_sales_list.append(weekly_sales)
            reset_weekly_sales(product_id)
        print("updated")

def update_product_sales(product_id, sales):
    with sqlite3.connect("ProductDatabase.db") as db:
        #date = datetime.date.today().strftime("%d-%m-%Y")
        #date = datetime.date(2015,2,9).strftime("%d-%m-%Y")
        #date = datetime.date(2015,2,16).strftime("%d-%m-%Y")
        #date = datetime.date(2015,2,23).strftime("%d-%m-%Y")
        date = datetime.date(2015,3,2).strftime("%d-%m-%Y")
        product_info = (product_id, date, sales,)
        cursor = db.cursor()
        sql = "Insert into ProductSales (ProductID, Date, Sales) values(?,?,?)"
        cursor.execute(sql, product_info)

def get_product_sales_date(product_id):
    with sqlite3.connect("ProductDatabase.db") as db:
        product_info = (product_id,)
        cursor = db.cursor()
        sql = "Select Date From ProductSales Where ProductID = ?"
        cursor.execute(sql, product_info)
        date_list = cursor.fetchall()
        if date_list:
            return date_list

def get_product_sales(product_id):
    with sqlite3.connect("ProductDatabase.db") as db:
        product_info = (product_id,)
        cursor = db.cursor()
        sql = "Select Sales From ProductSales Where ProductID = ?"
        cursor.execute(sql, product_info)
        sales_list = cursor.fetchall()
        if sales_list:
            return sales_list
        
def get_new_employee_id():
    with sqlite3.connect("ProductDatabase.db") as db:
        employee_id_list = []
        cursor = db.cursor()
        cursor.execute("Select EmployeeID From Employee")
        employee_ids = cursor.fetchall()
        if employee_ids:
            for employee_id in employee_ids:
                for individual_id in employee_id:
                    employee_id_list.append(individual_id)
                counter = len(employee_id_list)
                greatest_employee_id = (employee_id_list[counter - 1])
                new_employee_id = greatest_employee_id + 1
        else:
            new_employee_id = 1
    return new_employee_id
                
def find_username_and_password(username, password):
    with sqlite3.connect("ProductDatabase.db") as db:
        cursor = db.cursor()
        sql = "Select * From Employee Where EmployeePassword = ? AND EmployeeUsername = ?"
        cursor.execute(sql, (password, username,))
        password_list = cursor.fetchone()
        if not password_list:
            return_signal = 1
        else:
            return_signal = 2
            
        return return_signal
        
def find_employee_by_email(email):
    with sqlite3.connect("ProductDatabase.db") as db:
        in_database = False
        cursor = db.cursor()
        sql = ("Select * From Employee Where EmployeeEmail = ?")
        cursor.execute(sql, (email,))
        employee_list = cursor.fetchall()
        if employee_list:
            in_database = True
        return in_database
        
def get_employee_username(email):
    with sqlite3.connect("ProductDatabase.db") as db:
        cursor = db.cursor()
        sql = ("Select EmployeeUsername From Employee Where EmployeeEmail = ?")
        cursor.execute(sql, (email,))
        employee_list = cursor.fetchall()
        employee_username = employee_list[0][0]
        return employee_username
        
def get_employee_password(email):
    with sqlite3.connect("ProductDatabase.db") as db:
        cursor = db.cursor()
        sql = ("Select EmployeePassword From Employee Where EmployeeEmail = ?")
        cursor.execute(sql, (email,))
        employee_list = cursor.fetchall()
        encrypted_password = str(employee_list[0][0])
        decrypted_password = change_password(encrypted_password, -3)
        return decrypted_password

def get_employee_first_name(email):
    with sqlite3.connect("ProductDatabase.db") as db:
        cursor = db.cursor()
        sql = ("Select EmployeeFirstName From Employee Where EmployeeEmail = ?")
        cursor.execute(sql, (email,))
        employee_list = cursor.fetchall()
        first_name = employee_list[0][0]
        return first_name

def add_admin_employee():
    with sqlite3.connect("ProductDatabase.db") as db:
        cursor = db.cursor()
        cursor.execute("Select * From Employee")
        employees = cursor.fetchall()
        if not employees:
            values = ('1', 'THenderson1', 'Tom', 'Henderson', 'thenderson11@gmail.com', 'sdvvzrug',)
            admin_cursor = db.cursor()
            sql = ("Insert Into Employee (EmployeeID, EmployeeUserName, EmployeeFirstName, EmployeeLastName, EmployeeEmail, EmployeePassword) values(?,?,?,?,?,?)")
            admin_cursor.execute(sql, values)

def change_employee_password(employee_id, password):
    with sqlite3.connect("ProductDatabase.db") as db:
        data = (password, employee_id,)
        cursor = db.cursor()
        sql = "UPDATE Employee SET EmployeePassword = ? WHERE EmployeeUserName = ?"
        cursor.execute(sql, data)

def find_employee_by_username(username):
    with sqlite3.connect("ProductDatabase.db") as db:
        in_database = False
        cursor = db.cursor()
        sql = ("Select EmployeeFirstName, EmployeePassword, EmployeeEmail, EmployeeID From Employee Where EmployeeUserName = ?")
        cursor.execute(sql, (username,))
        employee_list = cursor.fetchall()
        return employee_list[0]
    
    
