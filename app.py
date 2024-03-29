### flask page admin 
### gurugeek started 19/9/2019

from flask import Flask, render_template, redirect
from flask_mysqldb import MySQL

import yaml

app = Flask(__name__, static_url_path='') #hload /public inside the static folder without having the /static prefix

db = yaml.load(open('db.yaml'))
app.config['MYSQL_HOST'] = db['mysql_host']
app.config['MYSQL_USER'] = db['mysql_user']
app.config['MYSQL_PASSWORD'] = db['mysql_password']
app.config['MYSQL_DB'] = db['mysql_db']
app.config['MYSQL_CURSORCLASS'] = 'DictCursor'
mysql = MySQL(app)


    
# general 404
@app.errorhandler(404)
def page_not_found(e):
    return '======== 404 Page Not Found ========'
    
@app.route('/')
def index():
    return redirect('/index')
    
        
@app.route('/<page>')
def page(page):
    cur = mysql.connection.cursor()
#   debug
    print(("SELECT * FROM pages WHERE page = '{}'".format(page)))
    resultValue = cur.execute("SELECT * FROM pages WHERE page = '{}'".format(page))
    if resultValue > 0:
        page = cur.fetchone()
        return render_template('page.html', page=page)
    cur.close()    
    return '======== 404 Page Not Found ========'


if __name__ == '__main__':
    app.run(debug=True, port=5001)
