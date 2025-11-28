import mysql.connector 
from mysql.connector import Error

# data connection 
def db_connection():
    try:
        conn = mysql.connector.connect(
            host="localhost",
            port=3306,
            user="root",
            password="root123",
            database="nancy_db"
        )
        if conn.is_connected():
            print("Database connected")
            return conn;
    except Error as e:
        print(e)
    return None

# insert record employee table 
def insert_record(id,name,salary):
    conn = db_connection()
    if conn is None:
        return
    try:
        cursor = conn.cursor();
        query = "insert into employee(id,name,salary) values(%s,%s,%s)";
        data = (id,name,salary)
        cursor.execute(query,data); # 1st parameter query and 2nd parameter record as tuple 
        conn.commit();
        print("Data Stored successfully")
    except Error as e:
        print("Insert Error ",e)
    finally:
        cursor.close();
        conn.close();

# insert record employee table 
def view_record():
    conn = db_connection()
    if conn is None:
        return
    try:
        cursor = conn.cursor();
        query = "select * from employee";
        cursor.execute(query);
        rows = cursor.fetchall();
        print("All records are")
        for row in rows:
            print("id is ",row[0]," Name is ",row[1]," Salary is ",row[2])
    except Error as e:
        print("Insert Error ",e)
    finally:
        cursor.close();
        conn.close();

# insert record employee table 
def search_record_using_id(id):
    conn = db_connection()
    if conn is None:
        return
    try:
        cursor = conn.cursor();
        query = "select * from employee where id = %s"
        data = [id]
        cursor.execute(query,data)
        row = cursor.fetchone()
        if row:
            print("id is ",row[0]," Name is ",row[1]," Salary is ",row[2])
        else:
            print("Record not present")
    except Error as e:
        print("Insert Error ",e)
    finally:
        cursor.close();
        conn.close();

# insert record employee table 
def update_employee_salary(id,newSalary):
    conn = db_connection()
    if conn is None:
        return
    try:
        cursor = conn.cursor();
        query = "update employee set salary = %s where id = %s"
        data = [newSalary,id]
        cursor.execute(query,data)
        conn.commit();

        if cursor.rowcount>0:
            print("Salary updated successfully")
        else:
            print("Record not present")
    except Error as e:
        print("Insert Error ",e)
    finally:
        cursor.close();
        conn.close();

# insert record employee table 
def delete_employee_by_id(id):
    conn = db_connection()
    if conn is None:
        return
    try:
        cursor = conn.cursor();
        query = "delete from employee where id = %s"
        data = [id]
        cursor.execute(query,data)
        conn.commit();

        if cursor.rowcount>0:
            print("Employee record deleted successfully")
        else:
            print("Record not present")
    except Error as e:
        print("Insert Error ",e)
    finally:
        cursor.close();
        conn.close();




print("Employee Crud Operation")
#db_connection()

#insert_record(101,"Steven",13000);

#view_record();


#search_record_using_id(109)

#update_employee_salary(1000,22000)

#delete_employee_by_id(100)
