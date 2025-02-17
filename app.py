from flask import Flask
from flask_migrate import Migrate
from models.db import db
from models.user import User  # Import the User model
from routes.main import main
from config.config import Config

app = Flask(__name__)
app.config.from_object(Config)

# Initialize database
db.init_app(app)

# Initialize Flask-Migrate
migrate = Migrate(app, db)

# Register routes
app.register_blueprint(main)

if __name__ == "__main__":
    app.run(debug=True)
