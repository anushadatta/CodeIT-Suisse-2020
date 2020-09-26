# import logging
# import json
import numpy as np
# from flask import request, jsonify;

# from codeitsuisse import app;

# logger = logging.getLogger(__name__)

def editDistDP(str1, str2, m, n): 
    dp = [[0 for x in range(n + 1)] for x in range(m + 1)] 
    for i in range(m + 1): 
        for j in range(n + 1): 
            if i == 0: 
                dp[i][j] = j    
            elif j == 0: 
                dp[i][j] = i    
            elif str1[i-1] == str2[j-1]: 
                dp[i][j] = dp[i-1][j-1] 
            else: 
                dp[i][j] = 1 + min(dp[i][j-1],        # Insert 
                                   dp[i-1][j],        # Remove 
                                   dp[i-1][j-1])    # Replace 
  
    return dp[m][n] 
  
str1 = "sunday"
str2 = "saturday"
  
print(editDistDP(str1, str2)) 


# @app.route('/inventory-management', methods=['POST'])
# def edits_min():
#     data = request.get_json()
#     data.sort()

#     return json.dumps(data)



