# Import the dependencies.
import numpy as np

import sqlalchemy
from sqlalchemy.ext.automap import automap_base
from sqlalchemy.orm import Session 
from sqlalchemy  import create_engine, func

from flask import Flask, jsonify


#################################################
# Database Setup
#################################################
engine = create_engine("sqlite:///Resources/hawaii.sqlite")

# reflect an existing database into a new model
Base = automap_base()
# reflect the tables
Base.prepare(autoload_with=engine)

# Save references to each table
station = Base.classes.station
measurement = Base.classes.measurement

# Create our session (link) from Python to the DB
session = Session(engine)

#################################################
# Flask Setup
#################################################
app = Flask(__name__)



#################################################
# Flask Routes
#################################################
@app.route("/")
def welcome():
    """List of all available api routes."""
    return (
        f"Available Routes:<br/>"
        f"/api/v1.0/precipitation<br/>"
        f"/api/v1.0/stations<br/>"
        f"/api/v1.0/tobs<br/>"
        f"/api/v1.0/<start>"
    )

@app.route("/api/v1.0/precipitation")
def precipitation():
    last_year_data = session.query(measurement.date,measurement.prcp).filter(measurement.date >= '2016-08 23').order_by(measurement.date).all()
    precipitation = [measurement[3] for prcp in last_year_data]
    
    return jsonify(precipitation)
    
    
    session.close()

    
@app.route("/api/v1.0/stations")
def stations():
    #Query
    
    """Return a list of stations from the dataset"""
    station_list = session.query(station.station).all()
    stations = [station[0] for station in station_list]
    
    return jsonify(stations)

    session.close()


@app.route("/api/v1.0/tobs")
def tobs():

    
    
    session.close()


if __name__ == '__main__':
    app.run(debug=True)

