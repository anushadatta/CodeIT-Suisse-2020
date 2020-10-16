import logging
import json

from flask import request, jsonify;

from codeitsuisse import app;

logger = logging.getLogger(__name__)

def palindromeSubStrs(s): 
    '''
    function to calculate all the required palindromes
    '''
    m = dict() 
    n = len(s) 

    R = [[0 for x in range(n+1)] for x in range(2)] 
  
    s = "@" + s + "#"
  
    for j in range(2): 
        rp = 0
        R[j][0] = 0
  
        i = 1
        while i <= n: 
            while s[i - rp - 1] == s[i + j + rp]: 
                rp += 1 
            R[j][i] = rp 
            k = 1
            while (R[j][i - k] != rp - k) and (k < rp): 
                R[j][i+k] = min(R[j][i-k], rp - k) 
                k += 1
            rp = max(rp - k, 0) 
            i += k 
  
    s = s[1:len(s)-1] 
  
    m[s[0]] = 1
    for i in range(1,n): 
        for j in range(2): 
            for rp in range(R[j][i],0,-1): 
                m[s[i - rp - 1 : i - rp - 1 + 2 * rp + j]] = 1
        m[s[i]] = 1
    res = []
    for i, val in m.items():
        if len(i)>1:
            res.append(i)
    if(len(res)==0):
        return "",0
    maxima = max(res,key=lambda x:len(x))

    return maxima,len(res)

def encrypt(text,s):
    '''
    caesar cypher implementation
    '''
    result = ""
    for i in range(len(text)):
        char = text[i]
        result += chr((ord(char) + s - 97) % 26 + 97)
    return result

def calc_score(inp):
    '''
    function to calculate a score for a word to assess whether its a real word
    '''
    freq_dict = {
        "E":21912,
        "T":16587,
        "A":14810,
        "O":14003,
        "I":13318,
        "N":12666,
        "S":11450,
        "R":10977,
        "H":10795,
        "D":7874,
        "L":7253,
        "U":5246,
        "C":4943,
        "M":4761,
        "F":4200,
        "Y":3853,
        "W":3819,
        "G":3693,
        "P":3316,
        "B":2715,
        "V":2019,
        "K":1257,
        "X":315,
        "Q":205,
        "J":188,
        "Z":128
    }
    score = 0
    for i in inp:
        score+=freq_dict[i.upper()]
    return score

def calc_original_string(encrypted_string):
    '''
    function to calculate original string given a caesar cypher
    '''
    maxi = encrypt(encrypted_string,0)
    for i in range(26):
        cur = (encrypt(encrypted_string,i+1))
        if(calc_score(cur)>calc_score(maxi)):
            maxi = cur

    return maxi

def main(encrypted_string):
    '''
    main function to tackle the entire problem of bored scribe
    '''
    original = calc_original_string(encrypted_string)
    if original == encrypted_string:
        return 0,original
    pal_info =  palindromeSubStrs(original)
    start = original.find(pal_info[0])
    end = start + len(pal_info[0])
    key = sum(map(ord,pal_info[0]))+pal_info[1]
    print(key)
    count = 1
    curr_text = encrypt(original,key)
    for i in range(10):
        if curr_text==encrypted_string:
            break
        key = sum(map(ord,encrypted_string[start:end]))+pal_info[1]
        count += 1
        curr_text = encrypt(curr_text,key)

    return count,original

# main("oxzbzxofpxkbkdifpemxifkaoljb")


@app.route('/bored-scribe', methods=['POST'])
def scribeMoreLikeScrub():
    '''
    API end point used to by credit suisse to calculate the required result
    '''
    data = request.get_json()
    print(data)
    result = []
    for i, val in enumerate(data):
        curr_vals = main(val["encryptedText"])
        curr_res = {
            "id":val["id"],
            "encryptionCount":curr_vals[0],
            "originalText":curr_vals[1],
        }
        result.append(curr_res)


    return jsonify(result)

