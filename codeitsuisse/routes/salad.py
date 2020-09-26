import logging
import json
import sympy
from flask import request, jsonify;

from codeitsuisse import app;

logger = logging.getLogger(__name__)

# def rolling_window(prices_array, start_index, n):
#     rolling_window = 0
#     price_count = 0

#     for i in range(start_index, len(prices_array)-n+1):
#         current_price = prices_array[i]

#         if price_count == n:
#             return rolling_window

#         if current_price == 'X':
#             rolling_window = 0
#             price_count = 0
#         else:
#             rolling_window += current_price
#             price_count += 1

@app.route('/salad-spree', methods=['POST'])
def salad():
    data = request.get_json()

    number_of_salads = data["number_of_salads"]
    salad_shop_prices = data["salad_prices_street_map"]
    min_price = float('inf')

    for shops_list in salad_shop_prices:
        price = 0

        for i in range(len(shops_list)-number_of_salads+1):
            
            sub_array = shops_list[i:i+number_of_salads]

            if 'X' not in sub_array:
                price = sum(list(map(int, sub_array)))
                min_price = min(min_price, price)

    if min_price == float('inf'):
        min_price = 0

    result = {}
    result["result"] = min_price

    return jsonify(result)


