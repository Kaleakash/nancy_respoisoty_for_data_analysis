from sqlalchemy import Column,Integer,String,Float,create_engine
from sqlalchemy.orm import declarative_base,sessionmaker
# create teh Alchemy Base 
Base = declarative_base();

# create teh ORM model in python side 
class Employee(Base):
    __tablename__= "employee"

    id=Column(Integer,primary_key=True)
    name=Column(String(20))
    salary=Column(Float)
    
    def __repr__(self):
        return f"<Employee (id={self.id} name {self.name} Salary {self.salary})>"
    
# create the engine and session factory 
def get_engine():
    engine = create_engine("mysql+pymysql://root:root123@localhost:3306/nancy_db")
    return engine;

def get_session():
    try:
        engine = get_engine();
        Session = sessionmaker(bind=engine)
        print("Database connected successfully")
        return Session();
    except:
        print("Error generated")
        return None;

def create_tables():
    engine = get_engine();
    Base.metadata.create_all(engine)
    print("Table created successfully")

def insert_employee():
    eid = int(input("Enter the emp id"))
    ename = input("Enter the name")
    esalary = float(input("Enter the salary"))
    session = get_session();
    try:
        emp = Employee(id=eid,name=ename,salary=esalary); # converted each individual value to object. 
        session.add(emp);               # internally it convert to insert query 
        session.commit();
        print("Employee records stored")
    except Exception as e:
        session.rollback();
        print(e)
    finally:
        session.close();

def get_all_employee():
    session = get_session();
    try:
        employees = session.query(Employee).all();  # select * from employee 
        print("All Employee records")
        for emp in employees:
            print(emp)
    except Exception as error:
        print(error)
    finally:
        session.close();

def update_employee():
    eid = int(input("Enter the emp id"))
    emp_new_salary = float(input("Enter the new salary to update"))
    session = get_session();
    try:
       emp = session.query(Employee).filter(Employee.id==eid).first();
       if emp:
        emp.salary=emp_new_salary;      # replace with new salary 
        session.commit();
        print("Employee salary updated successfully")
       else:
        print("Employee record not present")
    except Exception as e:
        session.rollback();
        print(e)
    finally:
        session.close();

def delete_employee():
    eid = int(input("Enter the emp id"))
    session = get_session();
    try:
        emp = session.query(Employee).filter(Employee.id==eid).first();
        if emp:
            session.delete(emp);
            session.commit();
            print("Employee details deleted successfully")
        else:
            print("Employee record not present")
    except Exception as e:
        session.rollback();
        print(e)
    finally:
        session.close();

# main function to start the code 
if __name__=="__main__":
    #get_session();
    #create_tables();
    #insert_employee();
    # get_all_employee();
    # update_employee();
    # get_all_employee();
    delete_employee();