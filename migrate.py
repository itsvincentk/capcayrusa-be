from flask_migrate import upgrade, migrate, init
from app import app, db  # Import your app and database

# Ensure the app context is pushed
with app.app_context():
    try:
        init()  # Run only once if it's the first time
    except:
        pass  # Ignore if already initialized
    
    migrate(message="fix")
    upgrade()

print("Database migration completed successfully.")
