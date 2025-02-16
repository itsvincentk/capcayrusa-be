from app import app
from models.db import db
from models.user import User

with app.app_context():
    new_user = User(username="bebek", password="142556", role_access="admin")
    db.session.add(new_user)
    db.session.commit()

    print(f"User added successfully! ID: {new_user.id}")
