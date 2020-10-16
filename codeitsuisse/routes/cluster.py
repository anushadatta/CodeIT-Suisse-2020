import logging
import json
from queue import Queue
from flask import request, jsonify;

from codeitsuisse import app

logger = logging.getLogger(__name__)


def get_neighbors(i,j,max_rows,max_cols):
    '''
    given a cell in a grid, get a list of all its neighbours
    '''
    result = []
    for _i in range(-1,2):
        for _j in range(-1,2):
            if 0<=i+_i<max_rows and 0<=j+_j<max_cols:
                result.append([i+_i,j+_j])
    return result



def find_cycles(map_arr):
    '''
    function which implements DFS to find the number of cycles in a grid graph
    '''
    visited = [[False for j in i] for i in map_arr]
    count = 0
    for i in range(len(map_arr)):
        for j in range(len(map_arr[i])):
            if(not visited[i][j]):
                is_cluster = False  
                curr_queue = Queue()
                curr_queue.put([i,j])
                while(not curr_queue.empty()):
                    curr_node = curr_queue.get()
                    if visited[curr_node[0]][curr_node[1]]:
                        continue
                    visited[curr_node[0]][curr_node[1]] = True

                    curr_node_val = map_arr[curr_node[0]][curr_node[1]]
                    if curr_node_val =="*":
                        continue
                    if curr_node_val == "1":
                        if not is_cluster:
                            count += 1
                            is_cluster = True
                    curr_neighbors = get_neighbors(curr_node[0],curr_node[1],len(map_arr),len(map_arr[i]))
                    for neighbor in curr_neighbors:
                        curr_queue.put(neighbor)
    return count


@app.route('/cluster', methods=['POST'])
def cluster():
    '''
    API endpoint used to calculate the scores required by credit suisse
    '''
    data = request.get_json()
    cycles = find_cycles(data)
    response = {
        "answer":cycles
    }

    return json.dumps(response)



