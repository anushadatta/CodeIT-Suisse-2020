import logging
import json
import sympy
import random
from flask import request, jsonify;

from codeitsuisse import app;

logger = logging.getLogger(__name__)

def difference(g1, g2): 
    '''
    function to calculate difference between gene1 and 2
    '''
        difference = 0
        for i in range(len(g1)):
            if g1[i] != g2[i]:
                difference += 1
        return difference 

def check_for_nonsilent(g1, g2):
    '''
    function to determine if strings are non silent
    '''
        g1 = g1.split('-')
        g2 = g2.split('-')
        for i in range(len(g1)):
            if g1[i][0] != g2[i][0]:
                return True
        return False

@app.route('/contact_trace', methods=['POST'])
def contact_tracing(): 
    '''
    API endpoint used for the contact trace problem
    '''
    result = []
    genome_differences = float('inf')

    data = request.get_json()

    infected_name = data['infected']['name']
    infected_genome = data['infected']['genome']

    origin_name = data['origin']['name']
    origin_genome = data['origin']['genome']

    cluster = data['cluster']
    cluster_name = []
    cluster_genome = []
    for i in cluster:
        cluster_name.append(i['name'])
        cluster_genome.append(i['genome'])

    if infected_genome != origin_genome:
        for i in range(len(cluster_name)):
            path = ''
            if difference(infected_genome, cluster_genome[i]) <= genome_differences:
                genome_differences = difference(infected_genome, cluster_genome[i])
                if check_for_nonsilent(infected_genome, cluster_genome[i]):
                    path = infected_name + "* ->" + cluster_name[i]
                else:
                    path = infected_name + "->" + cluster_name[i]
            
            if difference(cluster_genome[i], origin_genome) <= genome_differences and cluster_genome[i] != origin_genome:
                if check_for_nonsilent(cluster_genome[i], origin_genome):
                    path += "* ->" + origin_name
                else:
                    path += "->" + origin_name
            if path != '':
                result.append((path, genome_differences))
            
        if difference(infected_genome, origin_genome) <= genome_differences: 
            path = ''
            genome_differences = difference(infected_genome, origin_genome)
            if check_for_nonsilent(infected_genome, origin_genome):
                path = infected_name + "* ->" + origin_name
            else:
                path = infected_name + "->" + origin_name
            result.append((path, genome_differences))
    else:
        path = infected_name + "->" + origin_name
        result.append((path, 0))
        genome_differences = 0

        for i in range(len(cluster_name)):
            if cluster_genome[i] == infected_genome:
                path = infected_name + "->" + cluster_name[i]
                result.append((path, 0))   
                genome_differences = 0
    
    answer = []
    for path, difference in result:
        if difference <= genome_differences:
            answer.append(path)
    
    return jsonify(answer)

