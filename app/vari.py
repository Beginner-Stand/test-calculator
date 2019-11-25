from app import app
from flask import request
var_dict = {}

@app.route('/variable/<vari>', methods=['PUT'])
def put_var(vari):
    status = 201
    if vari in var_dict:
        status = 204
    var_dict[vari] = request.json['value']
    return status

@app.route('/variable/<vari>', methods=['GET'])
def get_var(vari):
    if vari in var_dict:
        return {"value": var_dict[vari]}, 200
    else:
        return 404