from flask import Flask, request, jsonify
from flask_sqlalchemy import SQLAlchemy
from werkzeug.security import generate_password_hash, check_password_hash
import threading
import unittest
import requests
import json
import re

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///users.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)

class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(80), unique=True, nullable=False)
    password_hash = db.Column(db.String(255), nullable=False)

    def set_password(self, password):
        self.password_hash = generate_password_hash(password)

    def check_password(self, password):
        return check_password_hash(self.password_hash, password)

with app.app_context():
    db.create_all()

@app.route('/')
def home():
    return "Welcome to the Secure Testing Demo!"

def is_valid_input(data):
    """Validate input to prevent injection attacks."""
    pattern = re.compile(r'^[a-zA-Z0-9_]+$')
    return bool(pattern.match(data))

@app.route('/users', methods=['GET'])
def get_users():
    users = User.query.all()
    return jsonify([{"id": user.id, "username": user.username} for user in users])

@app.route('/user/<int:id>', methods=['GET'])
def get_user(id):
    user = User.query.get(id)
    if user:
        return jsonify({"id": user.id, "username": user.username})
    return jsonify({"message": "User not found"}), 404

@app.route('/user', methods=['POST'])
def add_user():
    data = request.get_json()
    if not is_valid_input(data['username']) or not is_valid_input(data['password']):
        return jsonify({"message": "Invalid input detected"}), 400

    new_user = User(username=data['username'])
    new_user.set_password(data['password'])
    db.session.add(new_user)
    db.session.commit()
    return jsonify({"message": "User added successfully"}), 201

@app.route('/user/<int:id>', methods=['PUT'])
def update_user(id):
    data = request.get_json()
    user = User.query.get(id)
    if user:
        if not is_valid_input(data['username']) or not is_valid_input(data['password']):
            return jsonify({"message": "Invalid input detected"}), 400
        
        user.username = data['username']
        user.set_password(data['password'])
        db.session.commit()
        return jsonify({"message": "User updated successfully"})
    return jsonify({"message": "User not found"}), 404

@app.route('/user/<int:id>', methods=['DELETE'])
def delete_user(id):
    user = User.query.get(id)
    if user:
        db.session.delete(user)
        db.session.commit()
        return jsonify({"message": "User deleted successfully"})
    return jsonify({"message": "User not found"}), 404

# Start Flask app in a separate thread
threading.Thread(target=app.run, kwargs={'host': '0.0.0.0', 'port': 5000}).start()

# Security Testing
BASE_URL = "http://127.0.0.1:5000"

class FlaskAppSecurityTestCase(unittest.TestCase):

    def test_sql_injection(self):
        payload = {"username": "testuser'; DROP TABLE users; --", "password": "testpass"}
        response = requests.post(f"{BASE_URL}/user", json=payload)
        self.assertNotEqual(response.status_code, 201, "SQL Injection vulnerability detected")

    def test_xss(self):
        payload = {"username": "<script>alert('XSS');</script>", "password": "testpass"}
        response = requests.post(f"{BASE_URL}/user", json=payload)
        self.assertNotIn("<script>", response.text, "XSS vulnerability detected")

    def test_insecure_password_storage(self):
        payload = {"username": "secureuser", "password": "securepass"}
        response = requests.post(f"{BASE_URL}/user", json=payload)
        self.assertEqual(response.status_code, 201)
        user_id = response.json()["id"]
        response = requests.get(f"{BASE_URL}/user/{user_id}")
        self.assertNotIn("securepass", response.text, "Insecure password storage detected")

    def test_authentication(self):
        response = requests.get(f"{BASE_URL}/users")
        self.assertEqual(response.status_code, 401, "Authentication bypass detected")

    def test_authorization(self):
        admin_payload = {"username": "admin", "password": "adminpass"}
        response = requests.post(f"{BASE_URL}/user", json=admin_payload)
        user_id = response.json().get("id", None)
        normal_payload = {"username": "user", "password": "userpass"}
        response = requests.post(f"{BASE_URL}/user", json=normal_payload)

        response = requests.put(f"{BASE_URL}/user/{user_id}", json={"username": "hacked", "password": "hackedpass"})
        self.assertEqual(response.status_code, 403, "Authorization bypass detected")

    def test_insecure_direct_object_references(self):
        payload = {"username": "testuser1", "password": "testpass"}
        response = requests.post(f"{BASE_URL}/user", json=payload)
        user_id = response.json().get("id", None)
        response = requests.get(f"{BASE_URL}/user/{user_id}")
        self.assertNotEqual(response.status_code, 200, "IDOR vulnerability detected")

    def test_sensitive_data_exposure(self):
        response = requests.get(f"{BASE_URL}/users")
        self.assertNotIn("password", response.text, "Sensitive data exposure detected")

if __name__ == '__main__':
    unittest.main()
