import traceback

import pg
db=pg.DB(dbname='tasklist')

from flask import Flask, render_template, request, redirect, session

app = Flask('MyApp')

@app.route('/')
def home():
    query = db.query("select id, task, complete from tasks;")
    return render_template('list.html', title='Task List', tasks_from_database=query.namedresult())

@app.route('/add', methods=['POST'])
def add():
    newtask = request.form['newtask']
    sql_str = "insert into tasks (task) values ('" + newtask + "');"
    print sql_str
    db.query(sql_str)
    return redirect('/')



#   Degug Settings
app.debug = True

if __name__ == '__main__':
     app.run(debug=True)
