from flask import Flask, request, jsonify

app = Flask(__name__)
# Sample data array of users
users = [
    {
        "id": 1, 
        "name": "Alon Rotem",
        "gender": "M",
        "birth_year": 1973,
        "role": "Software engineer"
    }
]

# General method to get a user's property by ID
def get_property(user_id, property_name):
    user = next((user for user in users if user['id'] == user_id), None)
    if user:
        return jsonify({ "id": user_id, property_name: user[property_name] })
    return jsonify({"message": "User not found"}), 404

# GET a specific user's name 
@app.route('/user/name<int:user_id>', methods=['GET'])
def get_user_name(user_id):
    return get_property(user_id, "name")

# GET a specific user's gender 
@app.route('/user/gender<int:user_id>', methods=['GET'])
def get_user_name(user_id):
    return get_property(user_id, "gender")

# GET a specific user's birth year 
@app.route('/user/birth_year<int:user_id>', methods=['GET'])
def get_user_name(user_id):
    return get_property(user_id, "birth_year")

# GET a specific user's birth year 
@app.route('/user/birth_year<int:user_id>', methods=['GET'])
def get_user_name(user_id):
    return get_property(user_id, "birth_year")

# GET a specific user's role
@app.route('/user/role/<int:user_id>', methods=['GET'])
def get_user_name(user_id):
    return get_property(user_id, "role")

# ... more profile property fetching API functions here

if __name__ == '__main__':
    app.run(debug=True)
