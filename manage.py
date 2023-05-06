from flask import Flask, url_for, redirect, render_template, request
from flask_bootstrap import Bootstrap

import mysql.connector as sql
app = Flask(__name__)
Bootstrap(app)
@app.route('/')
def home():
	return render_template('home.htm')
@app.route('/log')
def log():
	return render_template('log.htm')
@app.route('/addrec',methods = ['POST', 'GET'])
def addrec():
	if request.method == 'POST':
		try:
			
			Time = request.form['Time']
			Date = request.form['Date']
			Out_or_In = request.form['Out_or_In']
			
			with sql.connect(host="localhost", user="flask", password="ubuntu", database="CallLog") as con:
				cur = con.cursor()
				cmd = "INSERT INTO Calls (Time, Date, Out_or_In) VALUES ('{0}','{1}','{2}')".format(Time, Date, Out_or_In)
				cur.execute(cmd)
				con.commit()
				msg = "Call, Logged"
		except:
			con.rollback()
			msg = "Call, Not Logged"
		finally:
			return render_template("result.htm", msg = msg)
			con.close()
@app.route('/calllist')
def list():
	with sql.connect(host="localhost", user="flask", password="ubuntu", database="CallLog") as con:
		cur = con.cursor()
		cur.execute("select * from Calls")
		rows = cur.fetchall();
	return render_template("list.htm",rows = rows)
if __name__ == '__main__':
	app.run(debug = True)
