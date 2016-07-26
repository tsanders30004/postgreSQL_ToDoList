import traceback

import pg
db=pg.DB(dbname='tasklist')

from flask import Flask, render_template, request, redirect, session

app = Flask('MyApp')

@app.route('/')
def home():
    query = db.query("select id, task, complete from tasks order by task;")
    return render_template('list.html', title='Task List', tasks_from_database=query.namedresult())

@app.route('/add', methods=['POST'])
def add():
    newtask = request.form['newtask']
    sql_str = "insert into tasks (task) values ('" + newtask + "');"
    print sql_str
    db.query(sql_str)
    return redirect('/')

@app.route('/complete', methods=['POST'])
def complete():
    my_tasks = request.form
    print "tasks"
    print my_tasks

    # need to find out if it is complete or delete

    for t in my_tasks:
        if t == "complete":
            mode = "complete"
        elif t == "delete":
            mode = "delete"

    print mode

    if mode == "complete":
        for t in my_tasks:
            # print "task"
            # print t
            sql = "update tasks set complete=true where id=" + t
            # print "sql"
            # print sql
            if t != "complete":
                db.query(sql)

    if mode == "delete":
        for t in my_tasks:
            print "task"
            print t
            sql = "delete from tasks where id=" + t
            print "sql"
            print sql
            if t != "delete":
                db.query(sql)

    return redirect('/')


    # for t in my_tasks:
    #     print "task"
    #     print t
    #
    #     sql = "update tasks set complete=true where id=" + t
    #     print "sql"
    #     print sql
    #     if t != "complete":
    #         db.query(sql)
    # return redirect('/')



# @app.route('/complete', methods=['POST'])
# def complete():
#     my_tasks = request.form
#     print "tasks"
#     print my_tasks
#     for t in my_tasks:
#         print "task"
#         print t
#         # sql = "delete from tasks where id=" + t + ";"
#         sql = "update tasks set complete=true where id=" + t
#         print "sql"
#         print sql
#         if t != "complete":
#             db.query(sql)
#     return redirect('/')


app.debug = True

if __name__ == '__main__':
     app.run(debug=True)
