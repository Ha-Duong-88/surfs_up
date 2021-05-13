{
 "cells": [],
 "metadata": {},
 "nbformat": 4,
 "nbformat_minor": 4
}

from flask import Flask

# Create a Flask application
# The __name__ variable denotes the name of the current function
app = Flask(__name__)

# Create Flask routes
# First define the starting point (root)
# The forward slash denotes that we want to put our data at the root of our routes; commonly known as highest level of hierarchy
@app.route('/')

# Create a function called hello_world()
def hello_world():
    return 'Hello world'

# Run a Flask app
# To run Flask app, you have to run in command line
# First set the Flask_APP env variable:  export FLASK_APP=app.py
# flask run