from app import app
from flask import request
import json 
var_dict = {}

@app.route('/variable/<vari>', methods=['PUT'])
def put_var(vari):
    status = 201
    if vari in var_dict:
        status = 204
    var_dict[vari] = request.json['value']
    return "", status

@app.route('/variable/<vari>', methods=['GET'])
def get_var(vari):
    if vari in var_dict:
        return {"value": var_dict[vari]}, 200
    else:
        return "", 404

@app.route('/variable', methods=['GET'])
def dump():
        result = json.dumps(var_dict)
        return {"data": result}, 200

@app.route('/variable', methods=['POST'])
def load():
        body = request.json
        data = body['data']
        if 'overwrite' in body:
            sover = body['overwrite']
            if sover == 'true':
                over = True
            else:
                over = False
        else:
            over = False
        ndict = json.loads(data)
        for vari in ndict:
            if over or vari not in var_dict:
                var_dict[vari] = ndict[vari]

        return "",204
