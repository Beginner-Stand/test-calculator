from flask import Flask
app = Flask(__name__)

import calc

@app.route('/')
def index():
	return 'Hi'
