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

if __name__ == '__main__':
    app.run(debug=True)