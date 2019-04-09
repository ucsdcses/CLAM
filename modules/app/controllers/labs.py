''' controller and routes for labs '''
import os
from flask import request, jsonify
from app import app, mongo
import logger

ROOT_PATH = os.environ.get('ROOT_PATH')
LOG = logger.get_root_logger(
    __name__, filename=os.path.join(ROOT_PATH, 'output.log'))


@app.route('/lab', methods=['GET'])
def lab():
  if request.method == 'GET':       # Get the lab from the database
    query = request.args
    lab = mongo.db.labs.find_one(query)
    return jsonify(lab), 200