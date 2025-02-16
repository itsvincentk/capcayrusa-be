#!/bin/sh
export PATH="/usr/local/bin:/usr/bin:/bin"

# Ensure pip is installed
python3 -m ensurepip --default-pip
python3 -m pip install --upgrade pip setuptools wheel

# Install dependencies from requirements.txt
python3 -m pip install -r requirements.txt

# Start the Flask app with Gunicorn
gunicorn -w 1 -b 0.0.0.0:5000 app:app
