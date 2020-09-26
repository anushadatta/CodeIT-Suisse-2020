import logging
import json
import sympy
import random
from flask import request, jsonify;

from codeitsuisse import app;

logger = logging.getLogger(__name__)

@app.route('/social-distancing', methods=['POST'])
def socialdistancing():
    data = request.get_json()
    print(data)
    tests_dict = data["tests"]
    print(tests_dict)
    combinations= {}

    for key,dict_data in tests_dict.items():
        seats = dict_data["seats"]
        people = dict_data["people"]
        spaces = dict_data["spaces"]

        number_of_ways = 0

        combinations[key] = number_of_ways

    result = {}
    result["answers"] = combinations

    return jsonify(result)
    
