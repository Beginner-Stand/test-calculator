from app import app
from flask import request
from vari import var_dict as var_dict

@app.route('/calc', methods=['POST'])
def calc():
	save = False
	if 'save_to' in request.json:
		save = True
	left,op,right = request.json['expression'].split()
	if left in var_dict:
		left = str(var_dict[left])
	if right in var_dict:
		right = str(var_dict[right])
	expr = "".join([left,op,right])
	ans = str(eval(expr))
	if save:
		savet = request.json['save_to']
		var_dict[savet] =  ans
	return {"result" : ans}
