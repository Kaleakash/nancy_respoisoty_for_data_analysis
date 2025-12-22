from pymongo import MongoClient

def get_connection():
    client = MongoClient("mongodb://localhost:27017")
    db = client["nancy_db"]
    return db["employee"]

#create a function to store document in employee collection 
def create_document(e_id,e_name,e_salary):
    connection = get_connection();
    emp = {
        "_id":e_id,
        "name":e_name,
        "salary":e_salary
    }
    try:
        connection.insert_one(emp);
        print("Record inserted")
    except Exception as e:
        print("error generated ",e)

#create_document(102,"Lex",42000)

#create a function to store document in employee collection 
def find_all():
    connection = get_connection();
    try:
        print("All employee details are")
        employees = connection.find();
        for emp in employees:
            print(emp)
    except Exception as e:
        print("error generated ",e)
#find_all();


#delete document from a collection  
def delete_document(e_id):
    connection = get_connection();
    try:
        result = connection.delete_one({"_id":e_id})
        if result.deleted_count >0 :
            print("document deleted successfully")
        else:
            print("document not present")
    except Exception as e:
        print("error generated ",e)

#delete_document(100)

#update document from a collection  
def update_document(e_id,new_salary):
    connection = get_connection();
    
    try:
        result = connection.update_one({"_id":e_id},{"$set":{"salary":new_salary}})
        if result.modified_count >0:
            print("document updated successfully")
        else:
            print("document is not present")
    except Exception as e:
        print("error generated ",e)

update_document(101,35000)

