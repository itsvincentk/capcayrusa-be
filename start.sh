#!/bin/sh
pip install -r requirements.txt  # Manually install dependencies
gunicorn -w 1 -b 0.0.0.0:5000 app:app  # Start the Flask app
