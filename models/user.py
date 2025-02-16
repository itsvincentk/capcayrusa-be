import uuid
from models.db import db
from sqlalchemy.dialects.postgresql import UUID

class User(db.Model):
    id = db.Column(UUID(as_uuid=True), primary_key=True, default=uuid.uuid4, unique=True, nullable=False)
    username = db.Column(db.String(50), unique=True, nullable=False)
    password = db.Column(db.String(100), nullable=False)
    role_access = db.Column(db.String(20), nullable=False, default="user")

    def __repr__(self):
        return f"<User {self.username}, Role: {self.role_access}>"
