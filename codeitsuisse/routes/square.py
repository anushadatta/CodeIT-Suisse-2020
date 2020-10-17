import logging
import json

from flask import request, jsonify;

from codeitsuisse import app;

logger = logging.getLogger(__name__)

@app.route('/square', methods=['POST'])
def evaluateSquare():
    '''
    API endpoint for squaring a number
    '''
    data = request.get_json()
    logging.info("data sent for evaluation {}".format(data))
    inputValue = data.get("input")
    result = inputValue * inputValue +100
    logging.info("My result :{}".format(result))
    return json.dumps(result)



