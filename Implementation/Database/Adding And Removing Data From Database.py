import sqlite3



def mainWindow():
    Done = False
    while not Done:
        print("")
        print("-----Product-----")
        print("1. Add a New Product")
        print("2. Delete a Product")
        print("3. Edit a Product")
        print("")
        print("-----Member-----")
        print("4. Add a New Member")
        print("5. Delete an Existing Member")
        print("6. Edit a Member")
        print("")
        print("-----Employee-----")
        print("7. Add a New Employee")
        print("8. Delete an Existing Employee")
        print("9. Edit an Employee")
        print("")
        print("-----Location-----")
        print("10. Add a New Location")
        print("11. Delete a New Location")
        print("12. Edit a Location")
        print("")
        print("-----Other-----")
        print("0. Exit")
        print("")
        print("---------------")
        print("")
        print("")
        choice = int(input("Enter Choice Here: "))
        print("---------------")
        print("")
        if choice == 1:
            addingProduct()
            print("")
            print("")
            print("**********************Prouct Sucessfully Added**********************")
        elif choice == 2:
            deletingProduct()
            print("")
            print("")
            print("**********************Prouct Sucessfully Removed**********************")
        elif choice == 3:
            addingMember()
            print("")
            print("")
            print("**********************Product Sucessfully Edited**********************")
        elif choice == 4:
            addingMember()
            print("")
            print("")
            print("**********************Member Sucessfully Added**********************")
        elif choice == 5:
            deletingMember()
            print("")
            print("")
            print("**********************Member Sucessfully Removed**********************")
        elif choice == 6:
            editingMember()
            print("")
            print("")
            print("**********************Member Sucessfully Edited**********************")
        elif choice == 7:
            addingEmployee()
            print("")
            print("")
            print("**********************Employee Sucessfully Added**********************")
        elif choice == 8:
            deletingEmployee()
            print("")
            print("")
            print("**********************Employee Sucessfully Removed**********************")
        elif choice == 9:
            editingEmployee()
            print("")
            print("")
            print("**********************Employee Sucessfully Edited**********************")
        elif choice == 10:
            addingLocation()
            print("")
            print("")
            print("**********************Location Sucessfully Added**********************")
        elif choice == 11:
            deletingLocation()
            print("")
            print("")
            print("**********************Location Sucessfully Removed**********************")
        elif choice == 12:
            editingLocation()
            print("")
            print("")
            print("**********************Location Sucessfully Edited**********************")
        elif choice == 0:
            Done = True


#-----------------------------------------Product-----------------------------------------

def addingProduct():
    name = input("Enter Product Name To Add: ")
    size = input("Enter Product Size To Add: ")
    price = input("Enter Product Price To Add (0.00): ")
    location1 = input("Enter Stock in location 1")
    location2 = input("Enter Stock in location 2")
    Product = (name,size,price,location1,location2)
    insert_product_data(Product)
def insert_product_data(values):
    with sqlite3.connect("ProductDatabase.db") as db:
        cursor = db.cursor()
        sql = "insert into Product (ProductName, Size, Price, Location1, Location2) values(?,?,?,?,?)"
        cursor.execute(sql,values)
        db.commit()


def deletingProduct():
    ProductID = input("Enter ProductID To Delete")
    data = (ProductID,)
    delete_product(data)
def delete_product(data):
    with sqlite3.connect("ProductDatabase.db") as db:
        cursor = db.cursor()
        sql = "delete from Product where ProductID = ?"
        cursor.execute(sql,data)
        db.commit()

#-----------------------------------------Member-----------------------------------------


def addingMember():
    Title = input("Enter Member Title (Mr./Mrs.): ")
    MemberFirstName = input("Enter Member First Name")
    MemberLastName = input("Enter Member Last Name")
    HouseNo = int(input("Enter House No."))
    Street = input("Enter Street Name")
    Town = input("Enter Town: ")
    City = input("Enter City: ")
    County = input("Enter County: ")
    Postcode = input("Enter Postcode: ")
    TelephoneNo = input("Enter Telephone Number: ")
    MemberEmail = input("Enter Member Email: ")
    Member = (Title,MemberFirstName,MemberLastName,HouseNo,Street,Town,City,County,Postcode,TelephoneNo, MemberEmail)
    insert_member_data(Member)
def insert_member_data(values):
    with sqlite3.connect("ProductDatabase.db") as db:
        cursor = db.cursor()
        sql = "insert into Member (Title, MemberFirstName, MemberLastName, HouseNo, Street, Town, City, County, Postcode, TelephoneNo, MemberEmail) values(?,?,?,?,?,?,?,?,?,?,?)"
        cursor.execute(sql,values)
        db.commit()

def deletingMember():
    MemberID = input("Enter MemberID To Delete")
    data = (MemberID,)
    delete_member(data)
def delete_member(data):
    with sqlite3.connect("ProductDatabase.db") as db:
        cursor = db.cursor()
        sql = "delete from Member where MemberID = ?"
        cursor.execute(sql,data)
        db.commit()


#-----------------------------------------Employee-----------------------------------------

def addingEmployee():
    EmployeeFirstName = input("Enter Employee First Name")
    EmployeeLastName = input("Enter Employee Last Name")
    EmployeeEmail = input("Enter Employee Email")
    Employee = (EmployeeFirstName,EmployeeLastName,EmployeeEmail)
    insert_employee_data(Employee)
def insert_employee_data(values):
    with sqlite3.connect("ProductDatabase.db") as db:
        cursor = db.cursor()
        sql = "insert into Employee (EmployeeFirstName, EmployeeLastName, EmployeeEmail) values(?,?,?)"
        cursor.execute(sql,values)
        db.commit()

def deletingEmployee():
    EmployeeID = input("Enter EmployeeID To Delete")
    data = (EmployeeID,)
    delete_employee(data)
def delete_employee(data):
    with sqlite3.connect("ProductDatabase.db") as db:
        cursor = db.cursor()
        sql = "delete from Employee where EmployeeID = ?"
        cursor.execute(sql,data)
        db.commit()
#-----------------------------------------Location-----------------------------------------


def addingLocation():
    LocationName = input("Enter Location Name")
    Location = (LocationName,)
    insert_location_data(Location)
def insert_location_data(values):
    with sqlite3.connect("ProductDatabase.db") as db:
        cursor = db.cursor()
        sql = "insert into Location (LocationName) values(?)"
        cursor.execute(sql,values)
        db.commit()



def deletingLocation():
    LocationID = input("Enter LocationID To Delete")
    data = (LocationID,)
    delete_location(data)
def delete_location(data):
    with sqlite3.connect("ProductDatabase.db") as db:
        cursor = db.cursor()
        sql = "delete from Location where LocationID = ?"
        cursor.execute(sql,data)
        db.commit()

#------------------------------------------------------------------------------------------
        
if __name__ =='__main__':
        mainWindow()
