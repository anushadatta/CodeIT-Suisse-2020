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
        dirty_floor = value["floor"]
        moves_count = 0

        # Counting moves for dirty floor
        for i in range(len(dirty_floor)):
            
            # Current spot
            current_spot = dirty_floor[i]
            
            # Next spot
            if i < (len(dirty_floor)-1):
                next_spot = dirty_floor[i+1]
            else:
                moves_count += current_spot
                break
            
            # Count
            if current_spot == 0:
                continue 
            # eg. 5, 5
            if current_spot == next_spot:
                moves_count += current_spot + next_spot
                if (i+1) == (len(dirty_floor)-1): # Last index, whole floor is now clean
                    break
                else:
                    dirty_floor[i+1] = 1
            # eg. 1,3
            if current_spot < next_spot:
                difference = abs(current_spot-next_spot)
                if(difference%2==0): # Even
                    moves_count += max(current_spot, next_spot) + 1
                    if (i+1) == (len(dirty_floor)-1): # Last index, whole floor is now clean
                        break
                    else:
                        dirty_floor[i+1] = 1
                else: # Odd
                    moves_count += ((current_spot + next_spot)*2) + 1
                    if (i+1) == (len(dirty_floor)-1): # Last index, whole floor is now clean
                        break
                    else:
                        dirty_floor[i+1] = 1
                
            if current_spot > next_spot:
                difference = abs(current_spot-next_spot)
                if(difference%2==0): # Even
                    moves_count += (max(current_spot, next_spot)*2) + 1
                    if (i+1) == (len(dirty_floor)-1): # Last index, whole floor is now clean
                        break
                    else:
                        dirty_floor[i+1] = 1
                else: # Odd
                    moves_count += (max(current_spot, next_spot)*2) + 1
                    if (i+1) == (len(dirty_floor)-1): # Last index, whole floor is now clean
                        break
                    else:
                        dirty_floor[i+1] = 0

        moves_answer[key] = moves_count
    
    final_answer = {}
    final_answer["answers"] = moves_answer

    return jsonify(final_answer)