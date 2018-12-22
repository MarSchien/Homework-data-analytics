import numpy as np
import pandas as pd

import sqlalchemy
from sqlalchemy.ext.automap import automap_base
from sqlalchemy.orm import Session
from sqlalchemy import create_engine, func

from flask import Flask, jsonify


#################################################
# Database Setup
#################################################
engine = create_engine("sqlite:///hawaii.sqlite")

# reflect an existing database into a new model
Base = automap_base()
# reflect the tables
Base.prepare(engine, reflect=True)

# Save reference to the table
Measurement = Base.classes.measurement
Station = Base.classes.station

# Create our session (link) from Python to the DB
session = Session(engine)

#################################################
# Flask Setup
#################################################
app = Flask(__name__)


#################################################
# Flask Routes
#################################################

# conduct SQL query, bind to session and put query info into pandas DF, then into dictionary and jsonify
@app.route('/api/v1.0/precipitation')
def precipitation():
    query = '''SELECT date, tobs
                FROM measurement
                WHERE date >= '2016-8-23'
                GROUP BY date
                ORDER BY date DESC '''
    df = pd.read_sql_query(query, session.bind)
    results = df.to_dict(orient='records')

    return jsonify(results)

@app.route('/api/v1.0/stations')
def stations():
    query = '''SELECT station.name, station.station
                FROM station
                INNER JOIN measurement
                ON station.station=measurement.station
                WHERE date >= '2016-8-23'
                GROUP BY station.station
                ORDER BY station.station DESC '''
    df = pd.read_sql_query(query, session.bind)
    results = df.to_dict(orient='records')

    return jsonify(results)

@app.route('/api/v1.0/tobs')
def tobs():

    # Query all passengers
    results = session.query(Measurement.tobs).\
    filter(Measurement.date >= 2016-8-23).all()

    # Convert list of tuples into normal list
    all_stations = list(np.ravel(results))

    return jsonify(all_stations)

# Must talk to instructor about this.  He did not go over this in class
@app.route('/api/v1.0/<start>')
def start(start):
    query = '''SELECT tobs
                FROM measurement
                WHERE date >= '2016-8-23'
                GROUP BY date DESC '''
    df = pd.read_sql_query(query, session.bind)
    results = df.to_dict(orient='records')

    return jsonify(results)


#     canonicalized = superhero.replace(" ", "").lower()
#     for character in measurement.tobs:
#         search_term = character["superhero"].replace(" ", "").lower()

#         if search_term == canonicalized:
#             return jsonify(character)

#     return jsonify({"error": "Character not found."}), 404

# @app.route('/api/v1.0/<start>/<end>')
#     def start(start)

#     canonicalized = superhero.replace(" ", "").lower()
#     for character in justice_league_members:
#         search_term = character["superhero"].replace(" ", "").lower()

#         if search_term == canonicalized:
#             return jsonify(character)

#     return jsonify({"error": "Character not found."}), 404


if __name__ == '__main__':
    app.run(debug=True)