import sqlite3

#-----------------------------------------Product-----------------------------------------

def addingProduct(name,size,price,location1,location2):
    Product = (name,size,price,location1,location2)
    insert_product_data(Product)
def insert_product_data(values):
    with sqlite3.connect("ProductDatabase.db") as db:
        cursor = db.cursor()
        sql = "insert into Product (ProductName, Size, Price, Location1, Location2) values(?,?,?,?,?)"
        cursor.execute(sql,values)
        db.commit()


def deletingProduct(ProductID):
    data = (ProductID,)
    delete_product(data)
def delete_product(data):
    with sqlite3.connect("ProductDatabase.db") as db:
        cursor = db.cursor()
        sql = "delete from Product where ProductID = ?"
        cursor.execute(sql,data)
        db.commit()

#-----------------------------------------Member-----------------------------------------


def addingMember(Title,MemberFirstName,MemberLastName,HouseNo,Street,Town,City,County,Postcode,TelephoneNo, MemberEmail):
    Member = (Title,MemberFirstName,MemberLastName,HouseNo,Street,Town,City,County,Postcode,TelephoneNo, MemberEmail)
    insert_member_data(Member)
def insert_member_data(values):
    with sqlite3.connect("ProductDatabase.db") as db:
        cursor = db.cursor()
        sql = "insert into Member (Title, MemberFirstName, MemberLastName, HouseNo, Street, Town, City, County, Postcode, TelephoneNo, MemberEmail) values(?,?,?,?,?,?,?,?,?,?,?)"
        cursor.execute(sql,values)
        db.commit()

def deletingMember(MemberID):
    data = (MemberID,)
    delete_member(data)
def delete_member(data):
    with sqlite3.connect("ProductDatabase.db") as db:
        cursor = db.cursor()
        sql = "delete from Member where MemberID = ?"
        cursor.execute(sql,data)
        db.commit()


#-----------------------------------------Employee-----------------------------------------

def addingEmployee(EmployeeUsername,EmployeeFirstName,EmployeeLastName,EmployeeEmail):
    Employee = (EmployeeUsername,EmployeeFirstName,EmployeeLastName,EmployeeEmail)
    insert_employee_data(Employee)
def insert_employee_data(values):
    with sqlite3.connect("ProductDatabase.db") as db:
        cursor = db.cursor()
        sql = "insert into Employee ( EmployeeUserName, EmployeeFirstName, EmployeeLastName, EmployeeEmail) values(?,?,?,?)"
        cursor.execute(sql,values)
        db.commit()

def deletingEmployee(EmployeeID):
    data = (EmployeeID,)
    delete_employee(data)
def delete_employee(data):
    with sqlite3.connect("ProductDatabase.db") as db:
        cursor = db.cursor()
        sql = "delete from Employee where EmployeeID = ?"
        cursor.execute(sql,data)
        db.commit()
#-----------------------------------------Location-----------------------------------------


def addingLocation(LocationName):
    Location = (LocationName,)
    insert_location_data(Location)
def insert_location_data(values):
    with sqlite3.connect("ProductDatabase.db") as db:
        cursor = db.cursor()
        sql = "insert into Location (LocationName) values(?)"
        cursor.execute(sql,values)
        db.commit()



def deletingLocation(LocationID):
    data = (LocationID,)
    delete_location(data)
def delete_location(data):
    with sqlite3.connect("ProductDatabase.db") as db:
        cursor = db.cursor()
        sql = "delete from Location where LocationID = ?"
        cursor.execute(sql,data)
        db.commit()

#------------------------------------------------------------------------------------------

