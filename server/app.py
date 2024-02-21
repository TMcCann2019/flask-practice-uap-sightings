#!/usr/bin/env python3

from flask import Flask, make_response, request
from flask_migrate import Migrate

# import model and db instance
from models import db, Sighting

# Initialize Flask app
'app = Flask(__name__)'
app = Flask(__name__)

# configure the app
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///app.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

# Initialize Flask-Migrate
migrate = Migrate(app, db)

# Initialize the db instance
db.init_app(app)

# Define routes and views
@app.route('/')
def welcome_screen():
    body = {"message": "The UAPID welcome our new extraterrestrial overlords!"}
    return make_response(body, 200)

@app.route('/sightings')
def sightings():
    sightings = []
    for sighting in Sighting.query.all():
        sightings.append(sighting.to_dict())
    body = {"sightings": sightings}
    return make_response(body, 200)

@app.route('/sightings/<int:id>')
def sighting(id):
    sighting = Sighting.query.filter(Sighting.id == id).first()
    body = {"sighting": sighting.to_dict()}
    return make_response(body, 200)

@app.route('/sightings/location/<string:location>')
def sightings_location(location):
    pass

if __name__ == "__main__":
    app.run(port=5555, debug=True)
