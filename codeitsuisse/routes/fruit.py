import logging
import json
import sympy
import random
from flask import request, jsonify;

from codeitsuisse import app;

logger = logging.getLogger(__name__)

@app.route('/fruitbasket', methods=['POST'])
def fruit():
    data = request.get_data()
    print(data)
    data = json.loads(data)
    fruits_count = []
    result = 0

    for fruit in data:

        weight = random.randint(1,100)
        print("{}:{}".format(weight,fruit))
        result += (weight * data[fruit])

    return str(result)