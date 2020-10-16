import logging
import json

from flask import request, jsonify;

from codeitsuisse import app;

logger = logging.getLogger(__name__)

@app.route('/health', methods=['GET'])
def evaluateHealth():
    '''
    endpoint to check if API service is healthy
    '''
    return json.dumps({"message":'life is good'})



