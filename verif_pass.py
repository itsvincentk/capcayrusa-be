from app import app
from models.db import db
from models.user import User  # Import your User model

# Query all users in the table
with app.app_context():
    user = User.query.filter_by(username="bebek").first()
    # Verify the password
    if user and user.check_password("142556"):
        print("Login successful")
    else:
        print("Invalid credentials")
