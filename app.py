#!/usr/bin/env python3

import sqlite3

from flask import (
    Flask, 
    abort, redirect, render_template, request, url_for
)

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

def db_modify(query_text, args):
	with sqlite3.connect(DB_PATH) as conn:
		cur = conn.cursor()
		cur.execute(query_text, args)
		conn.commit()

@app.route('/')
def main_page():
	columns, data = db_query('SELECT * FROM t1')
	return render_template('main_page.html', rows=data, column_names = columns)

@app.route('/add', methods=['POST'])
def add_entry():
	try:
		a=int(request.form['a'])
		b=request.form.get('b')
	except (KeyError, ValueError):
		abort(400)
	db_modify('INSERT INTO t1(a,b) VALUES (?,?)', (a,b))
	return redirect(url_for('main_page'))

if __name__=='__main__':
	app.run('0.0.0.0', debug=True)

