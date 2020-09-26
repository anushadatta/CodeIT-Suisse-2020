import logging
import json
import sympy
from flask import request, jsonify;

from codeitsuisse import app;

logger = logging.getLogger(__name__)

@app.route('/revisitgeometry', methods=['POST'])
def geometry():
    data = request.get_json()

    points_arr_shape = []
    for i in data['shapeCoordinates']:
        points_arr_shape.append(sympy.Point(i["x"], i["y"]))
    line_array_shape = []

    for i in range(len(points_arr_shape)-1):
        line_array_shape.append(sympy.Segment(points_arr_shape[i],points_arr_shape[i+1]))
    line_array_shape.append(sympy.Segment(points_arr_shape[0],points_arr_shape[-1]))

    line_points = []
    for i in data['lineCoordinates']:
        line_points.append(sympy.Point(i["x"], i["y"]))
    
    main_line = sympy.Line(line_points[0],line_points[1])

    intersections = []

    output = []
    for i in line_array_shape:
        res = sympy.geometry.intersection(i,main_line)
        if(len(res)):
            res = list(res[0])
            output.append({
                "x":round(float(res[0]),2),
                "y":round(float(res[1]),2),
            })

    return jsonify(output)



