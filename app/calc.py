from app import app
from flask import request

@app.route('/calc', methods=['POST'])
def calc():
	expr = request.json['expression']
	return str(eval(expr))
