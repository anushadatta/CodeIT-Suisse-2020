import logging
import json

from flask import request, jsonify;

from codeitsuisse import app;

logger = logging.getLogger(__name__)

@app.route('/sort', methods=['POST'])
def sort():
    '''
    API endpoint for sorting
    '''
    data = request.get_json()
    data.sort()
    return json.dumps(data)



