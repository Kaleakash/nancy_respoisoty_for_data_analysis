from flask import Flask,jsonify, request

app = Flask(__name__)

# in memory data store for Users 
usersData =[
    {"id": 1, "name": "Alice", "age": 30},
    {"id": 2, "name": "Bob", "age": 25},    
    {"id": 3, "name": "Charlie", "age": 35}
]

#http://localhost:5000/

@app.route('/', methods=['GET'])
def home():
    return "Welcome to the Simple REST API!"

#http://localhost:5000/jsonData
@app.route('/jsonData', methods=['GET'])
def get_json_data():
    return jsonify({"message": "This is a JSON response", "status": "success"})

#http://localhost:5000/users
# this end point returns the list of users in json format 
@app.route('/users', methods=['GET'])
def users():
    return jsonify(usersData)

#http://localhost:5000/user/<int:id>
# this end point returns a user by id
# http://localhost:5000/user/1
@app.route('/user/<int:u_id>', methods=['GET'])
def get_user_by_id(u_id):
    user = next((u for u in usersData if u["id"] == u_id), None)
    if user:
        return jsonify(user)
    return jsonify({"error": "User not found"}), 404

# http://localhost:5000/createUser
# this end point creates a new user
# need id must be unique 
@app.route('/createUser', methods=['POST'])
def create_user():
    new_user = request.get_json()  # data pass through post man client or rest client 
    # check if id is unique
    if any(u["id"] == new_user["id"] for u in usersData):
        return jsonify({"error": "User with this ID already exists"}), 400
    usersData.append(new_user)
    return jsonify({"message": "User created successfully", "user": new_user}), 201


# http://localhost:5000/updateUser/1
# this end point update existing user age or name
@app.route('/updateUser/<int:u_id>', methods=['PUT'])
def update_user(u_id):
    updated_user = request.get_json()  # data pass through post man client or rest client 
    # check if id present then only you need to update
    for user in usersData:              
        if user["id"] == u_id:
            user["name"] = updated_user.get("name", user["name"])
            user["age"] = updated_user.get("age", user["age"])
            return jsonify({"message": "User updated successfully", "user": user}), 200 
        return jsonify({"error": "User with this ID does not exist"}), 400

# http://localhost:5000/deleteUser/5
# this end point delete existing user by id 
@app.route('/deleteUser/<int:u_id>', methods=['DELETE'])
def delete_user(u_id):
    global usersData        # to modify the global usersData list
    # check if id present then only you need to delete
    for user in usersData:              
        if user["id"] == u_id:
            usersData = [user for user in usersData if user["id"] != u_id]
            return jsonify({"message": "User deleted successfully"}), 200
    return jsonify({"error": "User with this ID does not exist"}), 400
  
if __name__ == '__main__':
    app.run(debug=True)