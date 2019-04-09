import os
import json
import datetime
from flask import Flask

# mongoDB imports
from bson.objectid import ObjectId
from flask_pymongo import PyMongo


class JSONEncoder(json.JSONEncoder):
  ''' extend the encoder class for flexible json '''

  def default(self, o):
    if isinstance(o, ObjectId):
      return str(o)
    
    if isinstance(o, datetime.datetime):
      return str(o)

    return json.JSONEncoder.default(self, o)

# create the Flask app
app = Flask(__name__)

# Add the mongo url to flask config so that we can make connection to mongoDb
app.config['MONGO_URI'] = os.environ.get('DB')
mongo = PyMongo(app)

app.json_encoder = JSONEncoder

from app.controllers import *