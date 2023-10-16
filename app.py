#!/usr/bin/env python3

import sqlite3

from flask import Flask

DB_PATH = '/home/ivasonik/MIPT/DBSM/test.db'

app = Flask(__name__)

def db_query(query_text):
	with sqlite3.connect(DB_PATH) as conn:
		cur = conn.cursor()
		cur.execute(query_text)
		return cur.fetchall()
@app.route('/')
def main_page():
	return str(db_query('SELECT * FROM t1'))

if __name__=='__main__':
	app.run('0.0.0.0', debug=True)

