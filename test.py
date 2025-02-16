from app import app
from models.db import db
from sqlalchemy import text

with app.app_context():
    db.session.execute(text("DROP TABLE alembic_version;"))  # Deletes Alembic's tracking table
    db.session.commit()
    print("Alembic versioning reset.")
