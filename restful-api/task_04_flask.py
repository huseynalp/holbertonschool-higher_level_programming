#!/usr/bin/python3
"""
A simple Flask RESTful API for managing users.
This API provides endpoints to view, add, and manage user data.
"""
from flask import Flask, jsonify, request

app = Flask(__name__)

# In-memory storage for users (username as key)
users = {}


@app.route("/")
def home():
    """Root endpoint - returns welcome message."""
    return "Welcome to the Flask API!"


@app.route("/data")
def get_data():
    """Returns a list of all usernames."""
    return jsonify(list(users.keys()))


@app.route("/status")
def get_status():
    """Returns the API status."""
    return "OK"


@app.route("/users/<username>")
def get_user(username):
    """
    Returns the full user object for the given username.
    
    Args:
        username: The username to look up
        
    Returns:
        JSON object with user data or 404 error if not found
    """
    user = users.get(username)
    if user is None:
        return jsonify({"error": "User not found"}), 404
    return jsonify(user)


@app.route("/add_user", methods=["POST"])
def add_user():
    """
    Add a new user to the API.
    
    Expected JSON body:
        {
            "username": "john",
            "name": "John",
            "age": 30,
            "city": "New York"
        }
    
    Returns:
        201: User added successfully
        400: Invalid JSON or missing username
        409: Username already exists
    """
    # Check if request contains valid JSON
    try:
        data = request.get_json()
    except Exception:
        return jsonify({"error": "Invalid JSON"}), 400
    
    # Check if data is None (invalid JSON)
    if data is None:
        return jsonify({"error": "Invalid JSON"}), 400
    
    # Check if username is provided
    username = data.get("username")
    if not username:
        return jsonify({"error": "Username is required"}), 400
    
    # Check if username already exists
    if username in users:
        return jsonify({"error": "Username already exists"}), 409
    
    # Add user to the dictionary
    users[username] = data
    
    # Return success message with user data
    return jsonify({
        "message": "User added",
        "user": data
    }), 201


if __name__ == "__main__":
    app.run()
