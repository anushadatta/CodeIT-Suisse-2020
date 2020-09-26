import logging
import json
import sympy
import random
from flask import request, jsonify;

from codeitsuisse import app;

logger = logging.getLogger(__name__)

@app.route('/clean_floor', methods=['POST'])
def clean():
    data = request.get_json()
    data = data["tests"]

    moves_answer = {}

    for key, value in data.items():
        print(key, value)
        dirty_floor = value["floor"]
        moves_count = 0

        # Counting moves for dirty floor
        for i in range(len(dirty_floor)):
            
            # Current spot
            current_spot = dirty_floor[i]
            
            # # Previous Spot
            # if i>0:
            #     prev_spot = dirty_floor[i-1]
            # else:
            #     prev_spot = -1
            
            # Next spot
            if i < (len(dirty_floor)-1):
                next_spot = dirty_floor[i+1]
            else:
                moves_count += current_spot
                break
            
            # Count
            if current_spot == 0:
                continue 
            if current_spot <= next_spot:
                moves_count += (current_spot * 2)
                dirty_floor[i+1] = next_spot - current_spot

            if current_spot > next_spot:
                moves_count += (current_spot * 2)
                dirty_floor[i+1] = current_spot - next_spot 
        
        moves_answer[key] = moves_count
    
    print(moves_answer)
    final_answer = {}
    final_answer["answers"] = moves_answer

    print(final_answer)

    return jsonify(final_answer)