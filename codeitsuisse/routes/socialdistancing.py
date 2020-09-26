import logging
import json
import sympy
import random
import math
from flask import request, jsonify;

from codeitsuisse import app;

logger = logging.getLogger(__name__)

def choose(n, r):
    return int(math.factorial(n) / (math.factorial(r) * math.factorial(n-r)))

@app.route('/social-distancing', methods=['POST'])
def socialdistancing():
    data = request.get_json()
    # print(data)
    tests_dict = data["tests"]
    # print(tests_dict)
    combinations= {}

    for key,dict_data in tests_dict.items():
        seats = dict_data["seats"]
        people = dict_data["people"]
        spaces = dict_data["spaces"]

        # number_of_ways = choose(seats - (people-1)*spaces, people)
        a = seats - spaces * (people-1) - people
        b = people+1
        number_of_ways = choose(a+b-1,a)

        combinations[key] = number_of_ways

    result = {}
    result["answers"] = combinations
    
    return jsonify(result)
    
