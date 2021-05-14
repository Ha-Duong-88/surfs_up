{
 "cells": [],
 "metadata": {},
 "nbformat": 4,
 "nbformat_minor": 4
}


# Import dependencies
from flask import Flask
import datetime as dt
import numpy as np
import pandas as pd
import sqlalchemy
from sqlalchemy.ext.automap import automap_base
from sqlalchemy.orm import Session
from sqlalchemy import create_engine, func
from flask import Flask, jsonify





####################################################################
# Create a new Flask app instance
####################################################################
# Set up routes
# Add the routing information for each of the other routes
# For this, first we'll create a function and our return statement will have f-strings as a reference to all of the other routes
# Next, add the precipitation, stations, tobs, and temp routes that we'll need for this module into our return statement. 
#def welcome():
    #return(
    #'''
    #Welcome to the Climate Analysis API!
    #Available Routes:
    #/api/v1.0/precipitation
    #/api/v1.0/stations
    #/api/v1.0/tobs
    #/api/v1.0/temp/start/end
    #''')


# Create a Flask application
# Set up Flask
# The __name__ variable denotes the name of the current function
app = Flask(__name__)

# Create Flask routes
# First define the starting point (root)
# The forward slash denotes that we want to put our data at the root of our routes; commonly known as highest level of hierarchy
# This defines the welcome route
# When you make a route in Flask, you put the code you want in the specific route
@app.route('/')

# Create a function called hello_world()
def hello_world():
    return 'Hello world'

# Environment variable
# Modify the path that will run app.py
#export FLASK_APP=app.py

# Add the other routes
@app.route("/api/v1.0/precipitation")

# Create the precipitation() function
# Then, write a query to get the date and precipitation for the previous year
# the .\ in the first line of our query? This is used to signify that we want our query to 
# continue on the next line. 
# Finally, create a dictionary with the date as the key and the precipitation as the value
# We'll use the jasonify() to format our results into a JSON file
def precipitation():
    prev_year = dt.date(2017, 8, 23) - dt.timedelta(days=365)
    precipitation = session.query(Measurement.date, Measurement.prcp).\
      filter(Measurement.date >= prev_year).all()
    precip = {date: prcp for date, prcp in precipitation}
    return jsonify(precip)


# Run a Flask app
# To run Flask app, you have to run in command line 
# First set the Flask_APP env variable:  export FLASK_APP=app.py
# flask run

# Environment variable
# Modify the path that will run app.py
#export FLASK_APP=app.py

##################### Do I need to add this to app.py? #################
# Set up database
# create_engine() function allows us to access and query SQLite database file
engine = create_engine("sqlite:///hawaii.sqlite")

# Reflect the database into our classes
Base = automap_base()

# Reflect tables
Base.prepare(engine, reflect=True)

# With database reflected, we can save our references to each table
# Reuse the same references that we created in ipynb earlier in module
Measurement = Base.classes.measurement
Station = Base.classes.station

# Create a session link from Python to our database
session = Session(engine)

