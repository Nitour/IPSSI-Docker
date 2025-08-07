from flask import Flask, request, jsonify
from pymongo import MongoClient
import os

app = Flask(__name__)

client = MongoClient(f"mongodb://{os.environ['MONGO_USER']}:{os.environ['MONGO_PASS']}@{os.environ['MONGO_HOST']}:{os.environ['MONGO_PORT']}")
db = client[os.environ['MONGO_DB']]
collection = db['users']

@app.route('/')
def home():
    return "Welcome to the Flask-MongoDB API"

@app.route('/users', methods=['GET'])
def get_users():
    users = list(collection.find({}, {'_id': 0}))
    return jsonify(users)

@app.route('/users', methods=['POST'])
def add_user():
    user = request.get_json()
    collection.insert_one(user)
    return jsonify({"message": "User added"}), 201

@app.route('/users/<email>', methods=['GET'])
def get_user(email):
    user = collection.find_one({"email": email}, {'_id': 0})
    if user:
        return jsonify(user)
    return jsonify({"error": "User not found"}), 404

@app.route('/users/<email>', methods=['DELETE'])
def delete_user(email):
    result = collection.delete_one({"email": email})
    if result.deleted_count:
        return jsonify({"message": "User deleted"})
    return jsonify({"error": "User not found"}), 404

if __name__ == '__main__':
    app.run(host='0.0.0.0')
