from mongoengine import connect,Document,IntField,StringField,FloatField

def db_connection():
    connect(
        db="nancy_db",
        host="localhost",
        port=27017
    )

class Product(Document):
    pid=IntField(primary_key=True)
    pname=StringField(require=True)
    price = FloatField(require=True)

    def __str__(self):
        return f"Employee id is {self.pid} Name is {self.pname} and price is {self.price}"

# insert the document in Product collection 
def insert_document(p_pid,p_name,p_price):
    db_connection();
    try:
        product = Product(pid=p_pid,pname=p_name,price=p_price) # convert to product object
        product.save();     # directly insert the document with help of save functions. 
        print("document inserted successfully")
    except Exception as error:
        print("error generated ",error)

#insert_document(102,"Pen Drive",1800)

# find all documents from a collection 
def find_all():
    db_connection();
    try:
        products = Product.objects();           # equal to find query 
        print("All product details are ")
        for product in products:
            print(product);
    except Exception as error:
        print("error generated ",error)

#find_all();


# insert the document in Product collection 
def update_document(p_pid,new_price):
    db_connection();
    try:
        db_product = Product.objects(pid=p_pid).first();
        if db_product:
            db_product.price = new_price;
            db_product.save();      # equal to update function 
            print("document updated successfully")
        else:
            print("document not present")
    except Exception as error:
        print("error generated ",error)
#update_document(100,58000);

# insert the document in Product collection 
def delete_document(p_pid):
    db_connection();
    try:
        db_product = Product.objects(pid=p_pid).first();
        if db_product:
            db_product.delete(); 
            print("document deleted successfully")
        else:
            print("document not present")
    except Exception as error:
        print("error generated ",error)

delete_document(101)