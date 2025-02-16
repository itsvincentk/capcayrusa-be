from flask import Flask
from models.db import db
from routes.main import main
from config.config import Config

app = Flask(__name__)
app.config.from_object(Config)

# Initialize the database
db.init_app(app)

# Register routes
app.register_blueprint(main)

# Only run locally
if __name__ == "__main__":
    app.run(debug=True)
