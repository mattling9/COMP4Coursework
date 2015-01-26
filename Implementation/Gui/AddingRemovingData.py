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

def editProduct(product_id, name, size, price, category):
    Product = (name, size, price, category, product_id)
    with sqlite3.connect("ProductDatabase.db") as db:
        cursor = db.cursor()
        sql = "UPDATE Product SET ProductName= ?,  Size = ?,  Price = ?, Category= ? WHERE ProductID = ?"
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


        
def addingOrder(ProductID, name, size, price, quantity):
    ProductOrderID = get_product_order_id()
    order_info = (ProductID, name, size, price, quantity)
    with sqlite3.connect("ProductDatabase.db") as db:
        cursor = db.cursor()
        sql = "insert into ProductOrder (ProductID, ProductName, Size, Price, Quantity) values(?,?,?,?,?)"
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

def addingProductToOrder(self, ProductID):
    with sqlite3.connect("ProductDatabase.db") as db:
        cursor = db.cursor()
        find_cursor = db.cursor()
        cursor.execute(" SELECT * FROM Product WHERE ProductID = ?",(ProductID,))
        find_cursor.execute(" SELECT ProductID, Quantity FROM ProductOrder WHERE ProductID = ?",(ProductID,))
        product = cursor.fetchall()
        returned_product = find_cursor.fetchall()
        db.commit()
        MatchingProductID = returned_product
        quantity = 1
        if not MatchingProductID:
            quantity = 1
            ProductID = product[0][0]
            name = product[0][1]
            size = product[0][2]
            price = product[0][3]
            addingOrder(ProductID, name, size, price, quantity)
            return price
        elif ProductID == MatchingProductID[0][0]:
            price = product[0][3]
            quantity = MatchingProductID[0][1]
            IncrementQuantity(ProductID, quantity)
            return price

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
                    print(ProductList[count][0])
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


def get_product_order_id():
    with sqlite3.connect("ProductDatabase.db") as db:
            cursor = db.cursor()
            cursor.execute("SELECT * FROM ProductOrder")
            items = cursor.fetchall()
    return items

def createCustomerOrder(self):
    date = datetime.datetime.today()
    date_time = date.strftime("%d-%m-%Y %H:%M")
    self.member_id = self.member_line_edit.text()
    #NEED TO GET EMPLOYEE ID FROM THE EMPLOYEE WHO IS CURRENTLY LOGGED IN!!
    self.employee_id = 2
    #NEED TO GET EMPLOYEE ID FROM THE EMPLOYEE WHO IS CURRENTLY LOGGED IN!!
    addingCustomerOrder(self.member_id, self.employee_id, date_time)
    with sqlite3.connect("ProductDatabase.db") as db:
        cursor = db.cursor()
        cursor.execute("SELECT * FROM CustomerOrder")
        customer_order_list = cursor.fetchall()
        date = datetime.datetime.today()
        date_time = date.strftime("%d-%m-%Y %H:%M")
    

                
                

        
