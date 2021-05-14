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


######################################################
# Set up database
#######################################################

# Set up database for the Flask app
# create_engine() function allows us to access and query SQLite database file
engine = create_engine("sqlite:///hawaii.sqlite")

# Reflect the database into our classes
Base = automap_base()

# Reflect tables
Base.prepare(engine, reflect=True)

# With database reflected, we can save our references to each table
# Reuse the same references that we created in ipynb earlier in module
# Create a variable for each of the classes so that we can reference them later
Measurement = Base.classes.measurement
Station = Base.classes.station

# Create a session link from Python to our database
session = Session(engine)


####################################################################
# Set up Flask 
# Create a new Flask app instance
# Create a Flask application instance
# Create Flask routes
# Define function and return statement
# Run a Flask app
# To run Flask app, you have to run in command line 
# First set the Flask_APP env variable in command line:  export FLASK_APP=app.py
# Then run command: flask run
# Environment variable sets the path that will run app.py
########################################################################


# Set up Flask application instance
# The __name__ variable denotes the name of the current function
# All code should go after the app=Flask(__name__) code
app = Flask(__name__)

# Create Flask routes
# First define the welcome or starting point (root) --> @app.route('/')
# The forward slash denotes that we want to put our data at the root of our routes; commonly known as highest level of hierarchy
# When you make a route in Flask, you put the code you want in the specific route
@app.route('/')

# Next, add the routing information for each of the other routes
# For this, first we'll create a function and our return statement will have f-strings as a reference to all of the other routes
# Next, add the precipitation, stations, tobs, and temp routes that we'll need for this module into our return statement. 
# Use f-strings to display them
def welcome():
    return(
    '''
    Welcome to the Climate Analysis API!
    Available Routes:
    /api/v1.0/precipitation
    /api/v1.0/stations
    /api/v1.0/tobs
    /api/v1.0/temp/start/end
    ''')

# Add the precipitation route
# This code should occur outside the previous route and have no indentation
# This route will occur separately frm the welcome route
@app.route("/api/v1.0/precipitation")

# Create the precipitation() function
# Then, write a query to get the date and precipitation for the previous year
# the .\ in the first line of our query is used to signify that we want our query to 
# continue on the next line. 
# Finally, create a dictionary with the date as the key and the precipitation as the value
# We'll use the jasonify() to format our results into a JSON file
def precipitation():
    prev_year = dt.date(2017, 8, 23) - dt.timedelta(days=365)
    precipitation = session.query(Measurement.date, Measurement.prcp).\
      filter(Measurement.date >= prev_year).all()
    precip = {date: prcp for date, prcp in precipitation}
    return jsonify(precip)

# Add the stations route
# This code should occur outside the previous route and have no indentation
@app.route("/api/v1.0/stations")

# Define (create) a function called stations() to get a list of all stations
# Then, write query to get all the stations in our database
# We want to unravel results into a one-dimensional array (list) --> use the function np.ravel(), with results as our parameter.
# Then jsonify the  stations list and return it as JSON
# To return our list as JSON, we need to add stations=stations. This formats our list into JSON. 
def stations():
    results = session.query(Station.station).all()
    stations = list(np.ravel(results))
    return jsonify(stations=stations)

#  Add the monthly temperature route
@app.route("/api/v1.0/tobs")

# Define a function called temp_monthly() to return the temperature observations (tobs) for the previous year
# Calculate the date one year ago from the last date in the database
# Write a query statement the primary station for all the temperature observations from the previous year
# Finally, unravel results into a one-dimensional array and convert that array into a list
# Then, jsonify the temps list and return results
def temp_monthly():
    prev_year = dt.date(2017, 8, 23) - dt.timedelta(days=365)
    results = session.query(Measurement.tobs).\
      filter(Measurement.station == 'USC00519281').\
      filter(Measurement.date >= prev_year).all()
    temps = list(np.ravel(results))
    return jsonify(temps=temps)


#  Add the statistics (min/max/avg temps) route
@app.route("/api/v1.0/temp/<start>")
@app.route("/api/v1.0/temp/<start>/<end>")

# Define a function called stats() to return the temperature observations (tobs) for the previous year
# Add parameters to our status() function: a "start" parameter and an "end" parameter, and set both for now to "None"
# Write a query statement to select the min/max/avg temps from our SQLite database
# Start by creating a list called "sel"
# Since we need to determine the starting and end date, add an "if-not" statement to code
# Well use this to query our db using the list that we just made
# Finally, unravel results into a one-dimensional array and convert that array into a list
# Then, jsonify the temps list and return results
# Note the asterik in the query next to the "sel" list
# Now we need to calculate the min/max/avg with the start and date date
# We'll use the "sel" list which is the data points we need to collect
# When copying / pasting the web address provided by Flask into a web server, add 
# entering any date in the dataset as a start and end date. The code will output the minimum, maximum, and average temperatures.
def stats(start=None, end=None):
    sel = [func.min(Measurement.tobs), func.avg(Measurement.tobs), func.max(Measurement.tobs)]

    if not end:
        results = session.query(*sel).\
            filter(Measurement.date >= start).all()
        temps = list(np.ravel(results))
        return jsonify(temps=temps)

    results = session.query(*sel).\
        filter(Measurement.date >= start).\
        filter(Measurement.date <= end).all()
    temps = list(np.ravel(results))
    return jsonify(temps)

#################################################################################
# Additional notes -
# To view the output of your code. copy the web address (http://127.0.0.1:5000/) into our web browser. 
# You will need to navigate to the precipitation route in order to see the output of your code. 
# You can do this by adding api/v1.0/precipitation to the end of the web address.
#################################################################################























