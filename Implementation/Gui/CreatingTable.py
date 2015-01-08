import sqlite3

def create_table(db_name,table_name, sql):
    with sqlite3.connect(db_name) as db:
        cursor = db.cursor()
        cursor.execute("select name from sqlite_master where name=?",(table_name,))
        result = cursor.fetchall()
        keep_table = True
        if len(result) == 1:
            response = input("The table {0} already exists, do you wish to re-create it (y/n):".format(table_name))
            if response == 'y':
                keep_table = False
                print("The {0} table will be recreated - all existing data will be deleted".format(table_name))
                cursor.execute("drop table if exists {0}".format(table_name))
                db.commit()
            else:
                print("The existing table was kept")
        else:
            keep_table = False
        if not keep_table:
            cursor.execute(sql)
            db.commit()

def create_product_table():
    sql = """create table Product
              (ProductID integer,
              ProductName text,
              Size string,
              Price real,
              Location1 integer,
              Location2 integer,
              Primary Key(ProductID))"""
    create_table(db_name, "Product", sql)


def create_employee_table():
    sql = """create table Employee
              (EmployeeID integer,
              EmployeeFirstName text,
              EmployeeLastName text,
              EmployeeEmail float,
              Primary Key(EmployeeID))"""
    create_table(db_name, "Employee", sql)

def create_member_table():
    sql = """create table Member
              (MemberID integer,
              Title string,
              MemberFirstName text,
              MemberLastName text,
              HouseNo interger,
              Street text,
              Town text,
              City text,
              County text,
              Postcode text,
              TelephoneNo integer,
              MemberEmail text,
              Primary Key(MemberID))"""
    create_table(db_name, "Member", sql)

def create_order_table():
    sql = """create table CustomerOrder
            (OrderID integer,
            MemberID integer,
            EmployeeID integer,
            DateTime text,
            Primary Key(OrderID),
            foreign key(MemberID) references Member(MemberID),
            foreign key(EmployeeID) references Employee(EmployeeID))"""        
    create_table(db_name,"CustomerOrder", sql)

def create_product_order_table():
    sql = """create table ProductOrder
            (ProductOrderID integer,
            ProductID interger,
            OrderID integer,
            Quantity integer,
            Primary Key(ProductOrderID),
            foreign key(ProductID) references Product(ProductID),
            foreign key(OrderID) references CustomerOrder(OrderID))"""        
    create_table(db_name,"ProductOrder", sql)

def create_location_table():
    sql = """create table Location
            (LocationID integer,
            LocationName string,
            Primary Key(LocationID))"""        
    create_table(db_name,"Location", sql)

def create_product_location_table():
    sql = """create table ProductLocation
            (ProductID integer,
            LocationID integer,
            Primary Key(ProductID),
            Foreign Key(LocationID) references Location(LocationID))"""        
    create_table(db_name,"ProductLocation", sql)

if __name__ == "__main__":
    db_name = "ProductDatabase.db"
    create_product_table()
    create_product_order_table()
    create_location_table()
    create_product_location_table()
    create_employee_table()
    create_member_table()
    create_order_table()
