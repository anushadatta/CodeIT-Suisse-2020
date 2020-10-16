import logging
import json
import sympy
import random
from flask import request, jsonify;

from codeitsuisse import app;

logger = logging.getLogger(__name__)

@app.route('/clean_floor', methods=['POST'])
def clean():
    '''
    API endpoint
    main function used for the clean the floor problem
    '''
    data = request.get_json()

    tests = data['tests']
    cleaning_moves = {}
    
    # Iterate through all floors
    for key in tests.keys():
        minimum_moves = 0
        floor = tests[key]['floor']
        n = len(floor)

        # Calculating moves for one floor
        for i in range(n - 1):
            minimum_moves += floor[i]*2

            # Special Case: Check for second last spot
            if (i != n-2):
                if floor[i+1] > 0:
                    floor[i+1] = floor[i+1] - 1
                else:
                    floor[i+1] = floor[i+1] + 1
                minimum_moves += 1 

            # CASE 1: dirt level (current spot > next spot)
            if floor[i] > floor[i+1]:
                difference = abs(floor[i] - floor[i+1])
                if difference % 2 != 0:
                    floor[i+1] = 1
                else:
                    floor[i+1] = 0
            else:
                # CASE 2: dirt level (current spot <= next spot)
                floor[i+1] = abs(floor[i+1] - floor[i])

        # Check last spot!!!
        if (floor[n-1] != 0):
            floor[n-1] -= 1
            minimum_moves += 1

            if floor[n-1] % 2 != 0:
                minimum_moves += 1

        minimum_moves += 2 * floor[n-1]
        cleaning_moves[key] = minimum_moves
        
    result = {}
    result["answers"] = cleaning_moves

    return jsonify(result)
