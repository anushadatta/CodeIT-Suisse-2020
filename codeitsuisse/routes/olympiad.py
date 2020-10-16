import logging
import json
import sympy
import random
from flask import request, jsonify;

from codeitsuisse import app;

logger = logging.getLogger(__name__)

@app.route('/olympiad-of-babylon', methods=['POST'])
def olympiad():
    '''
    API endpoint used for olympiad of babylon
    '''
    data = request.get_json()
    
    books_time = data["books"]
    days_time = data["days"]

    total_time = sum(days_time)
    books_time.sort()
    books_count = 0
    first_book = books_time[0]

    while total_time >= first_book:
        b_time = books_time.pop(0)
        total_time = total_time - b_time
        books_count +=1

        if len(books_time)>0:
            first_book = books_time[0]
        else: 
            break

    print(books_time)
    print(days_time)

    answer = {}
    answer["optimalNumberOfBooks"] = books_count

    return jsonify(answer)