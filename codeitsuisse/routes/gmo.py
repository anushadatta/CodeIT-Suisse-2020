import logging
import json
from collections import Counter
from flask import request, jsonify, Response

from codeitsuisse import app;

logger = logging.getLogger(__name__)

def create_gmo_sequence(gene):
    

    # Count characters in string 
    logger.Debug(gene)
    count_dict = dict(Counter(gene))
    genes = ["A","G","C","T"]
    for i in genes:
        if i not in count_dict:
            count_dict[i]=0


    # Add CC
    c_count = count_dict['C']
    agct_count = 0
    cc_count = 0
    # Add AGCT
    a_count = count_dict['A']
    c_count = count_dict['C']
    g_count = count_dict['G']
    t_count = count_dict['T']
    while a_count >= 2 and c_count >= 2 and g_count >= 2 and t_count >= 2:

        count_dict['A'] = count_dict['A'] - 2
        count_dict['C'] = count_dict['C'] - 2
        count_dict['G'] = count_dict['G'] - 2
        count_dict['T'] = count_dict['T'] - 2
        agct_count+=2
        a_count = count_dict['A']
        c_count = count_dict['C']
        g_count = count_dict['G']
        t_count = count_dict['T']

    while c_count >= 2:

        count_dict['C'] = count_dict['C'] - 2
        cc_count+=1
        c_count = count_dict['C']

    
    while a_count >= 1 and c_count >= 1 and g_count >= 1 and t_count >= 1:

        count_dict['A'] = count_dict['A'] - 1
        count_dict['C'] = count_dict['C'] - 1
        count_dict['G'] = count_dict['G'] - 1
        count_dict['T'] = count_dict['T'] - 1
        agct_count+=1
        a_count = count_dict['A']
        c_count = count_dict['C']
        g_count = count_dict['G']
        t_count = count_dict['T']
    # print(count_dict,agct_count,cc_count)
    # Sprinkle remaining characters without AAA formation
    result = ""

    # print(cc_count)
    # print(agct_count)
    # print(g_count)
    # print(t_count)
    # print(a_count)
    

    # adding ccs to the string
    for i in range(agct_count):
        a_s = min(a_count,1)
        a_count -=a_s
        result+="A"*a_s+"ACGT"

    for i in range(cc_count):
        a_s = min(a_count,2)
        a_count -=a_s
        result+="A"*a_s+"CC"
    for i in range(g_count):
        a_s = min(a_count,2)
        a_count -=a_s
        result+="A"*a_s+"G"
    for i in range(t_count):
        a_s = min(a_count,2)
        a_count -=a_s
        result+="A"*a_s+"T"
    result+=a_count*"A"
    # print(result)
    return result

@app.route('/intelligent-farming', methods=['POST'])
def gmo():
    data = request.get_json()

    for gmo_dict_index in range(len(data["list"])):
        gmo_dict = data["list"][gmo_dict_index]
        gmo_string = gmo_dict["geneSequence"]
        
        answer = create_gmo_sequence(gmo_string)
        # print(gmo_string)
        logger.debug(answer)
        data["list"][gmo_dict_index]["geneSequence"] = answer

    return Response(response = json.dumps(data),status=200,mimetype="application/json")



