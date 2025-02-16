from app import app
from models.db import db
from models.user import User  # Import your User model

# Query all users in the table
with app.app_context():
    users = User.query.all()
    for user in users:
        print(f"ID: {user.id}, Username: {user.username}, PIN: {user.password}, ROLE: {user.role_access}")
