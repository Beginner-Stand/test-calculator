from flask import Flask
app = Flask(__name__)

import calc, vari

@app.route('/')
def index():
	return 'Hi'
