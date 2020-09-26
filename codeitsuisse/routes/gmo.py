import logging
import json
from collections import Counter
from flask import request, jsonify;

from codeitsuisse import app;

logger = logging.getLogger(__name__)

@app.route('/intelligent-farming', methods=['POST'])
def sort():
    data = request.get_json()
    genes_list = data['list']
    for id,gene in genes_list:
        count_dict = dict(Counter(gene))
        print(count_dict)
        



    return json.dumps(data)



