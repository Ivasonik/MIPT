#!/usr/bin/env python3
from flask import Flask

app = Flask(__name__)

@app.route('/')
def main_page():
	return '<b>Hello</b>, <u>World!</u>\n'

if __name__=='__main__':
	app.run('0.0.0.0', debug=True)
