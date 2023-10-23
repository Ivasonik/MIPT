#!/usr/bin/env python3

import sqlite3

from flask import Flask, render_template

DB_PATH = '/home/ivasonik/MIPT/DBSM/test.db'

app = Flask(__name__)

def db_query(query_text):
	with sqlite3.connect(DB_PATH) as conn:
		cur = conn.cursor()
		cur.execute(query_text)
		data=cur.fetchall()
		#columns = []
		#for descr in cur.description:
		#	columns.append(descr[0])
		#or instead of upper 3 strings:
		columns = [descr[0] for descr in cur.description]
		return columns, data
@app.route('/')
def main_page():
	columns, data = db_query('SELECT * FROM t1')
	return render_template('main_page.html', rows=data, column_names = columns)

if __name__=='__main__':
	app.run('0.0.0.0', debug=True)

