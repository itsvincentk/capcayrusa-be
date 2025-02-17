import uuid
from models.db import db
from sqlalchemy.dialects.postgresql import UUID
from werkzeug.security import generate_password_hash, check_password_hash

class User(db.Model):
    id = db.Column(UUID(as_uuid=True), primary_key=True, default=uuid.uuid4, unique=True, nullable=False)
    username = db.Column(db.String(10), unique=True, nullable=False)
    password = db.Column(db.String(256), nullable=False)  # Store hashed password
    role_access = db.Column(db.String(10), nullable=False, default="user")
    
    def __init__(self, username, password, role_access):
        self.username = username
        self.password = generate_password_hash(password)  # Hash the password before storing
        self.role_access = role_access

    def set_password(self, password):
        """Hashes the password before storing it"""
        self.password = generate_password_hash(password)

    def check_password(self, password):
        """Verifies the hashed password"""
        return check_password_hash(self.password, password)

    def __repr__(self):
        return f"<User {self.username}, Role: {self.role_access}>"