from flask import Flask, jsonify
from flask import request

app = Flask(__name__)

users = [
    {"id": 1, "username": "alice", "email": "alice@email.com"},
    {"id": 2, "username": "bob", "email": "bob@email.com"},
    {"id": 3, "username": "charlie", "email": "charlie@email.com"}
]

# Homepage
@app.route("/")
def hello_world():
    return "<p>Hi!</p>"

# All users
@app.route("/users")
def list_users():
    return jsonify(users)

# User by id
@app.route("/users/<user_id>")
def profile(user_id):
    user = next((user for user in users if str(user["id"]) == user_id), None)

    if user:
        return jsonify(user)
    else:
        return jsonify({"error": "User not found"}), 404


"""http POST http://127.0.0.1:5000/users username="Test" email="test@email.com"""