#import dependencies
import datetime as dt
import numpy as np
import pandas as pd

#SQLalchemy dependencies
import sqlalchemy
from sqlalchemy.ext.automap import automap_base
from sqlalchemy.orm import Session
from sqlalchemy import create_engine, func

#Flask denpendencies
from flask import Flask, jsonify

#SET UP THE DATABASE
#Access database
engine = create_engine("sqlite:///hawaii.sqlite")

#reflect database into classes
Base = automap_base()

#reflect database
Base.prepare(engine, reflect=True)

#create variables for each class
Measurement = Base.classes.measurement
Station = Base.classes.station

#create session link
session = Session(engine)

#SET UP FLASK
#define flask app
app = Flask(__name__)

#define welcome route
@app.route("/")

#function for routing information
def welcome():
    return(
    '''
    Welcome to the Climate Analysis API!<br/>
    Available Routes:<br/>
    /api/v1.0/precipitation<br/>
    /api/v1.0/stations<br/>
    /api/v1.0/tobs<br/>
    /api/v1.0/temp/start/end
    ''')

#route to precipitation analysis
@app.route("/api/v1.0/precipitation")

#create precipitation function
def precipitation():
    #calculate the date one year ago from the most recent date in the database
    prev_year = dt.date(2017, 8, 23) - dt.timedelta(days=365)
    #query to get date and prcp for the previous year
    precipitation = session.query(Measurement.date, Measurement.prcp).\
      filter(Measurement.date >= prev_year).all()
    #jsonify to format results in JSON structured file
    precip = {date: prcp for date, prcp in precipitation}
    return jsonify(precip)

#route to stations 
@app.route("/api/v1.0/stations")

#create stations function
def stations():
    #query to get all of the stations in database
    results = session.query(Station.station).all()
    #unravel results into list and jsonify
    stations = list(np.ravel(results))
    return jsonify(stations=stations)

#route to tobs
@app.route("/api/v1.0/tobs")

#create temps_monthly function
def temp_monthly():
    #calculate date one year ago from the last daye in the database
    prev_year = dt.date(2017, 8, 23) - dt.timedelta(days=365)
    #query the primary station for all the temp observations from previou year
    results = session.query(Measurement.tobs).\
      filter(Measurement.station == 'USC00519281').\
      filter(Measurement.date >= prev_year).all()
    #unravel results and convert to list then jsonify and return
    temps = list(np.ravel(results))
    return jsonify(temps=temps)

#route to report min, max, avg temps
@app.route("/api/v1.0/temp/<start>")
@app.route("/api/v1.0/temp/<start>/<end>")

#create stats function
def stats(start=None, end=None):
    #query to select min, max, avg temps
    sel = [func.min(Measurement.tobs), func.avg(Measurement.tobs), func.max(Measurement.tobs)]

    #determine the start and end date
    if not end:
        results = session.query(*sel).\
            filter(Measurement.date >= start).all()
        temps = list(np.ravel(results))
        return jsonify(temps)

    #calculate temp min, max, avg with start and end dates
    results = session.query(*sel).\
        filter(Measurement.date >= start).\
        filter(Measurement.date <= end).all()
    temps = list(np.ravel(results))
    return jsonify(temps)