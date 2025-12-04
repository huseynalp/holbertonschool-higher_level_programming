#!/usr/bin/python3
"""
A Flask API with Basic and JWT-based authentication.
Implements role-based access control for admin routes.
"""
from flask import Flask, jsonify, request
from flask_httpauth import HTTPBasicAuth
from flask_jwt_extended import (
    JWTManager, create_access_token, jwt_required, get_jwt_identity, get_jwt
)
from werkzeug.security import generate_password_hash, check_password_hash

app = Flask(__name__)

# JWT Configuration
app.config['JWT_SECRET_KEY'] = 'your-secret-key-change-this-in-production'
jwt = JWTManager(app)
auth = HTTPBasicAuth()

# In-memory user storage with hashed passwords and roles
users = {
    "user1": {
        "username": "user1",
        "password": generate_password_hash("password"),
        "role": "user"
    },
    "admin1": {
        "username": "admin1",
        "password": generate_password_hash("password"),
        "role": "admin"
    }
}


# Basic Authentication verification
@auth.verify_password
def verify_password(username, password):
    """Verify username and password for basic auth."""
    if username in users and check_password_hash(users[username]["password"], password):
        return username
    return None


# JWT Error Handlers - All return 401
@jwt.unauthorized_loader
def handle_unauthorized_error(err):
    """Handle missing or invalid token."""
    return jsonify({"error": "Missing or invalid token"}), 401


@jwt.invalid_token_loader
def handle_invalid_token_error(err):
    """Handle invalid token."""
    return jsonify({"error": "Invalid token"}), 401


@jwt.expired_token_loader
def handle_expired_token_error(jwt_header, jwt_payload):
    """Handle expired token."""
    return jsonify({"error": "Token has expired"}), 401


@jwt.revoked_token_loader
def handle_revoked_token_error(jwt_header, jwt_payload):
    """Handle revoked token."""
    return jsonify({"error": "Token has been revoked"}), 401


@jwt.needs_fresh_token_loader
def handle_needs_fresh_token_error(jwt_header, jwt_payload):
    """Handle needs fresh token."""
    return jsonify({"error": "Fresh token required"}), 401


# Routes
@app.route("/basic-protected")
@auth.login_required
def basic_protected():
    """Basic authentication protected route."""
    return "Basic Auth: Access Granted"


@app.route("/login", methods=["POST"])
def login():
    """
    Login endpoint to get JWT token.
    
    Expected JSON:
        {
            "username": "user1",
            "password": "password"
        }
    
    Returns:
        JWT access token or 401 if credentials are invalid
    """
    data = request.get_json()
    
    if not data:
        return jsonify({"error": "Missing JSON in request"}), 400
    
    username = data.get("username")
    password = data.get("password")
    
    if not username or not password:
        return jsonify({"error": "Missing username or password"}), 400
    
    # Verify credentials
    if username in users and check_password_hash(users[username]["password"], password):
        # Create token with user role in additional claims
        additional_claims = {"role": users[username]["role"]}
        access_token = create_access_token(identity=username, additional_claims=additional_claims)
        return jsonify({"access_token": access_token}), 200
    
    return jsonify({"error": "Invalid credentials"}), 401


@app.route("/jwt-protected")
@jwt_required()
def jwt_protected():
    """JWT authentication protected route."""
    return "JWT Auth: Access Granted"


@app.route("/admin-only")
@jwt_required()
def admin_only():
    """
    Admin-only route with role-based access control.
    
    Returns:
        Success message if user is admin, 403 error otherwise
    """
    # Get the JWT claims
    claims = get_jwt()
    user_role = claims.get("role")
    
    # Check if user has admin role
    if user_role != "admin":
        return jsonify({"error": "Admin access required"}), 403
    
    return "Admin Access: Granted"


if __name__ == "__main__":
    app.run()
