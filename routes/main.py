import jwt
import datetime
from flask import Blueprint, request, jsonify
from models.user import User

main = Blueprint("main", __name__)

# Secret key for JWT encoding/decoding
secret_key = "lavanya"  # Replace this with your actual secret key


def verify_jwt_token(token):
    """
    Verifies the JWT token and returns the decoded data if valid.
    :param token: The JWT token to verify.
    :return: Decoded token data if valid, or raises an error if invalid or expired.
    """
    try:
        # Decode the token and verify its validity
        decoded_token = jwt.decode(token, secret_key, algorithms=["HS256"])
        return decoded_token
    except jwt.ExpiredSignatureError:
        raise jwt.ExpiredSignatureError("Token has expired")
    except jwt.InvalidTokenError:
        raise jwt.InvalidTokenError("Invalid token")


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
    # Get the token from the Authorization header
    auth_header = request.headers.get("Authorization")

    if not auth_header:
        return jsonify({"message": "Authorization header is missing"}), 400

    # Extract the token from the 'Bearer <token>' format
    try:
        token = auth_header.split(" ")[1]  # Get token after "Bearer"
    except IndexError:
        return jsonify({"message": "Token is missing from the Authorization header"}), 400

    try:
        # Verify the JWT token using the separate method
        decoded_token = verify_jwt_token(token)

        # If decoding is successful, return the decoded data
        return jsonify({
            "message": "Token is valid",
            "user_id": decoded_token["user_id"]
        }), 200

    except jwt.ExpiredSignatureError as e:
        return jsonify({"message": str(e)}), 401

    except jwt.InvalidTokenError as e:
        return jsonify({"message": str(e)}), 401
