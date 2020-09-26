import logging
import json
import sympy
import random
from flask import request, jsonify;

from codeitsuisse import app;

logger = logging.getLogger(__name__)

@app.route('/fruitbasket', methods=['POST'])
def fruit():
    data = request.get_json()
    fruits_count = []

    for fruit in data:
        fruits_count.append(data[fruit])
    
    result = 0
    for i in range(len(fruits_count)):
        weight = random.randint(1,100)

        result += (weight * fruits_count[i])

    return str(result)