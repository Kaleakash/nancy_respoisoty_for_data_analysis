from flask import Flask,jsonify, request
from mongoengine import connect, Document, StringField, IntField

app = Flask(__name__)

# mongo database information  
connect(db='nancy_db', host='localhost', port=27017)

# Define a User document model
class User(Document):
    name = StringField(required=True)
    age = IntField(required=True)

    def to_json(self):
        return {"id": str(self.id), "name": self.name, "age": self.age}


# http://localhost:5000/createUser
# this end point creates a new user
# need id must be unique 
@app.route('/createUser', methods=['POST'])
def create_user():
    new_user = request.get_json()  # data pass through post man client or rest client 
    new_user_obj = User(name=new_user['name'], age=new_user['age'])
    new_user_obj.save()
    return jsonify({"message": "User created successfully", "user": new_user_obj.to_json()}), 201

#http://localhost:5000/users
# this end point returns the list of users in json format 
@app.route('/users', methods=['GET'])
def users():
    users = User.objects()  # fetch all user documents from MongoDB
    users_list = [user.to_json() for user in users]
    return jsonify(users_list)  # return list of users in json format   to client



#http://localhost:5000/user/<string:id>
# this end point returns a user by id
@app.route('/user/<string:u_id>', methods=['GET'])
def get_user_by_id(u_id):
    user = User.objects(id=u_id).first()  # fetch user document by id from MongoDB
    if user:
        return jsonify(user.to_json()), 200
    else:
        return jsonify({"error": "User with this ID does not exist"}), 400

# http://localhost:5000/updateUser/69594d808a9b102b4c138ceb
# this end point update existing user age or name
@app.route('/updateUser/<string:u_id>', methods=['PUT'])
def update_user(u_id):
    updated_user = request.get_json()  # data pass through post man client or rest client 
    user = User.objects(id=u_id).first()
    if user:
        user.name = updated_user.get("name", user.name)
        user.age = updated_user.get("age", user.age)
        user.save()
        return jsonify({"message": "User updated successfully", "user": user.to_json()}), 200
    else:   
        return jsonify({"error": "User with this ID does not exist"}), 400

# http://localhost:5000/deleteUser/5
# this end point delete existing user by id 
@app.route('/deleteUser/<string:u_id>', methods=['DELETE'])
def delete_user(u_id):
    user = User.objects(id=u_id).first()
    if user:
        user.delete()
        return jsonify({"message": "User deleted successfully"}), 200
    else:
        return jsonify({"error": "User with this ID does not exist"}), 400
  
if __name__ == '__main__':
    app.run(debug=True)