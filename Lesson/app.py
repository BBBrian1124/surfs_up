### IMPORT DEPENDENCIES ###
# To import the Flask dependency, add the following to your code
from flask import Flask
# Import other dependencies
import datetime as dt
import numpy as np
import pandas as pd
# Import SQLAlchemy dependencies 
import sqlalchemy
from sqlalchemy.ext.automap import automap_base
from sqlalchemy.orm import Session
from sqlalchemy import create_engine, func
# Import Flask dependenceies 
from flask import Flask, jsonify

### SET UP THE DATABASE ###
# prepare the database using create_engine by passing the location of the SQLite database as the paramater 
engine = create_engine("sqlite:///hawaii.sqlite")
# Automap Base creates a base class for an automap schema in SQLAlchemy, essentially helps the rest of the code run
Base = automap_base()
# this creates classes that help keep our code separate so we can interact with them individually in classes rather than tables
Base.prepare(engine, reflect=True)
# Save references to each table by storing the classes into variables 
Measurement = Base.classes.measurement
Station = Base.classes.station
# Create the link from python to our database
session = Session(engine)

### CREATE A NEW FLASK INSTANCE ### 
# By using the double underline this is a magic method which calls the function when the class is called
app = Flask(__name__)

# Notice the __name__ variable in this code. 
# This is a special type of variable in Python. Its value depends on where and how the code is run. 
    # For example, if we wanted to import our app.py file into another Python file named example.py, 
    # the variable __name__ would be set to example. Here's an example of what that might look like:
# However, when we run the script with python app.py, the __name__ variable will be set to __main__. 
# This indicates that we are not using any other file to run this code.
#import app
#print("example __name__ = %s", __name__)
#if __name__ == "__main__":
#    print("example is being run directly.")
#else:
#    print("example is being imported")

### ROUTE CREATION ### 
# Create Flask route by using this function
# The backslash indicates we will put the data at the root of the route (i.e. the first directory or homepage)
@app.route('/')
# When creating routes, we follow the naming convention /api/v1.0/ followed by the name of the route. 
# This convention signifies that this is version 1 of our application. 
# This line can be updated to support future versions of the app as well.
def welcome():
    # We will return the names of our other routes on the homepage
    return(
    '''
    Welcome to the Climate Analysis API!
    Available Routes:
    /api/v1.0/precipitation
    /api/v1.0/stations
    /api/v1.0/tobs
    /api/v1.0/temp/start/end
    ''')

# To add more routes you need to call @app.route again then specify the route 
@app.route("/api/v1.0/precipitation")
def precipitation():
    # We will query to find date and percepitation on the days greater than the previous year
    # Use .\ to continue lines of code on the next line
    prev_year = dt.date(2017, 8, 23) - dt.timedelta(days=365)
    precipitation = session.query(Measurement.date, Measurement.prcp).\
    filter(Measurement.date >= prev_year).all()
    # Json files store values in key-attribute pairs
    # We will store it with date as the key and percipation as the value in a dictionary first 
    precip = {date: prcp for date, prcp in precipitation}
    # Use jsonify to convert the dictionary to a json file  
    return jsonify(precip)

# Create another route 
@app.route("/api/v1.0/stations")
def stations():
    # query that will allow us to get all of the stations in our database
    results = session.query(Station.station).all()
    # unraveling our results into a one-dimensional array using np.ravel 
    # then use list to convert that array into a list
    stations = list(np.ravel(results))
    # then convert it to a json file
    return jsonify(stations=stations)

# For this route, the goal is to return the temperature observations for the previous year
@app.route("/api/v1.0/tobs")
def temp_monthly():
    # Create the function to find tempature filtered for a specific station after the specified date 
    prev_year = dt.date(2017, 8, 23) - dt.timedelta(days=365)
    results = session.query(Measurement.tobs).\
      filter(Measurement.station == 'USC00519281').\
      filter(Measurement.date >= prev_year).all()
    # Unrevel the results into a list 
    temps = list(np.ravel(results))
    # then convert it to a json file 
    return jsonify(temps=temps)

# This route is different from the previous ones in that we will have to provide both a starting and ending date
@app.route("/api/v1.0/temp/<start>")
@app.route("/api/v1.0/temp/<start>/<end>")
# Create the function that takes 2 paramaters 'start' and 'end' and set them as none for the time being 
def stats(start=None, end=None):
    # Store the min/avg/max in a list name sel
    sel = [func.min(Measurement.tobs), func.avg(Measurement.tobs), func.max(Measurement.tobs)]
    # If not end then query based on our filters 
    # the * indicates that there will be multiple results for that query of min/avg/max
    if not end:
        results = session.query(*sel).\
            filter(Measurement.date >= start).\
            filter(Measurement.date <= end).all()
        # Again unravel into a list and convert to json
        temps = list(np.ravel(results))
        return jsonify(temps)

    results = session.query(*sel).\
        filter(Measurement.date >= start).\
        filter(Measurement.date <= end).all()
    temps = list(np.ravel(results))
    return jsonify(temps=temps)
# ensure a start and end date is specified otherwise there will be no results
start = '2017-06-01'
end = '2017-06-30'
# similarily we just need to add the route to the end of our link to find it 
# http://127.0.0.1:5000/api/v1.0/temp/2017-06-01/2017-06-30