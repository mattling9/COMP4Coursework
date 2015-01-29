import sqlite3, sys, datetime
from PyQt4.QtCore import *
from PyQt4.QtGui import *
from PyQt4.QtSql import *
#-----------------------------------------Product-----------------------------------------

def addingProduct(name, size, price, category, location1, location2, image_path):
    Product = (name, size, price, category, location1, location2, image_path)
    with sqlite3.connect("ProductDatabase.db") as db:
        cursor = db.cursor()
        sql = "insert into Product (ProductName, Size, Price, Category, Location1, Location2, ImagePath) values(?,?,?,?,?,?,?)"
        cursor.execute(sql,Product)
        db.commit()

def editProduct(product_id, name, size, price, category, path):
    Product = (name, size, price, category, path, product_id)
    with sqlite3.connect("ProductDatabase.db") as db:
        cursor = db.cursor()
        sql = "UPDATE Product SET ProductName= ?,  Size = ?,  Price = ?, Category= ?, ImagePath= ? WHERE ProductID = ?"
        cursor.execute(sql,Product)
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

def deletingMember():
    MemberID = input("Enter MemberID To Delete")
    data = (MemberID,)
    with sqlite3.connect("ProductDatabase.db") as db:
        cursor = db.cursor()
        sql = "delete from Member where MemberID = ?"
        cursor.execute(sql,data)
        db.commit()


#-----------------------------------------Employee-----------------------------------------

def addingEmployee(EmployeeUserName,EmployeeFirstName,EmployeeLastName,EmployeeEmail):
    Employee = (EmployeeUserName,EmployeeFirstName,EmployeeLastName,EmployeeEmail)
    with sqlite3.connect("ProductDatabase.db") as db:
        cursor = db.cursor()
        sql = "insert into Employee (EmployeeUserName, EmployeeFirstName, EmployeeLastName, EmployeeEmail) values(?,?,?,?)"
        cursor.execute(sql,Employee)
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
