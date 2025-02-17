from app import app
from models.db import db
from models.user import User

# Create a new Flask application context
with app.app_context():
    # Create a new user instance
    new_user = User(username="rusa", password="123123", role_access="user")

    # Add and commit the new user to the database
    db.session.add(new_user)
    db.session.commit()

    print("User added successfully!")
