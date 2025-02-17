import jwt
import datetime
from flask import Blueprint, request, jsonify
from models.user import User

main = Blueprint("main", __name__)

# Secret key for JWT encoding/decoding
secret_key = "lavanya"  # Replace this with your actual secret key

@main.route("/login", methods=["POST"])
def login():
    # Get the password from the request
    data = request.get_json()
    password = data.get("password")

    users = User.query.all()
    for user in users:
        if user and user.check_password(password):
            # Set expiration to 15 minutes from now using timezone-aware datetime
            expiration_time = datetime.datetime.now(datetime.timezone.utc) + datetime.timedelta(minutes=15)

            # Create JWT token with only the user.id and expiration time
            token = jwt.encode({
                'user_id': str(user.id),  # Only encode user.id
                'exp': expiration_time  # Add expiration to the token
            }, secret_key, algorithm='HS256')

            return jsonify({
                "message": "Login successful!",
                "role_access": user.role_access,
                "token": token  # Return JWT token
            }), 200

    return jsonify({"message": "Invalid password"}), 401


@main.route("/verifyjwt", methods=["POST"])
def verify_jwt():
    # Get the token from the request
    data = request.get_json()
    token = data.get("token")

    if not token:
        return jsonify({"message": "Token is missing"}), 400

    try:
        # Decode the token and verify its validity
        decoded_token = jwt.decode(token, secret_key, algorithms=["HS256"])

        # If decoding is successful, return the decoded data
        return jsonify({
            "message": "Token is valid",
            "user_id": decoded_token["user_id"]
        }), 200

    except jwt.ExpiredSignatureError:
        return jsonify({"message": "Token has expired"}), 401

    except jwt.InvalidTokenError:
        return jsonify({"message": "Invalid token"}), 401
