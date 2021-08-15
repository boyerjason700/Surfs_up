# from flask import Flask
# app = Flask(__name__)

# @app.route('/')
# def hello_world():
#     return 'Hello world'

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
    