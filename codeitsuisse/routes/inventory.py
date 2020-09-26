import logging
import json
import numpy as np
from flask import request, jsonify;

from codeitsuisse import app;

logger = logging.getLogger(__name__)

def editDistDP(str1, str2): 
    m = len(str1)
    n = len(str2)
    dp = [[0 for x in range(n + 1)] for x in range(m + 1)] 
    string_list = [["" for x in range(n + 1)] for x in range(m + 1)] 
    for i in range(m + 1): 
        for j in range(n + 1): 
            if i == 0: 
                dp[i][j] = j
                if j!=0: 
                    string_list[i][j] = str2[j-1]
            elif j == 0: 
                dp[i][j] = i
                if i!=0: 
                    string_list[i][j] = "-" +str1[i-1]
            elif str1[i-1].lower() == str2[j-1].lower(): 
                dp[i][j] = dp[i-1][j-1]
                string_list[i][j] = string_list[i-1][j-1]+str1[i-1]
            else: 
              
                minimum = + min(dp[i][j-1],        # Insert 
                                   dp[i-1][j],        # Remove 
                                   dp[i-1][j-1])    # Replace
                dp[i][j] = 1 + minimum
                if minimum==dp[i][j-1]:
                    sign = "+"+str2[j-1]
                    string_list[i][j] = string_list[i][j-1]
                    
                elif minimum==dp[i-1][j]:
                    sign = "-" +str1[i-1]
                    string_list[i][j] = string_list[i-1][j]
                    
                elif minimum==dp[i-1][j-1]:
                    sign = str2[j-1]
                    string_list[i][j] = string_list[i-1][j-1]
                    

                string_list[i][j] += sign
    # print(np.array(dp))
    # print(np.array(string_list))
    return dp[m][n],string_list[m][n] 
  
str2 = "Amsungh"
str1 = "samsung"
  
print(editDistDP(str1, str2)) 


@app.route('/inventory-management', methods=['POST'])
def edits_min():
    data_list = request.get_json()

    response = []
    for data in data_list:
        search_string = data['searchItemName']
        items = data['items']
        items.sort()
        results = []
        for item in items:
            curr_result = [*editDistDP( search_string,item),item]
            results.append(curr_result)
        results.sort(key=lambda x:x[0])
        # print(*results,sep ="\n")
        results = results[:10]
        for i in results:
            print(i[2])
        results = list(map(lambda x:x[1], results))
        response.append({"searchItemName":search_string,"searchResult":results})

    return jsonify(response)



