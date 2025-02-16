from app import app
from models.db import db
from models.user import User

with app.app_context():
    # Find the user by username
    user_to_delete = User.query.filter_by(username="bebek").first()

    if user_to_delete:
        db.session.delete(user_to_delete)
        db.session.commit()
        print(f"User {user_to_delete.username} deleted successfully!")
    else:
        print("User not found.")
