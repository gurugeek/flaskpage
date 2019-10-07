### bottlepage gurugeek 11 September 2019 

import bottle
import bottle_mysql
from urllib.error import HTTPError
from bottle import route, run, template, static_file, redirect

app = bottle.Bottle()
# dbhost is optional, default is localhost
plugin = bottle_mysql.Plugin(dbuser='washnotes', dbpass='2q2XsZQTV2RFYsOQ',  dbhost='sql.fyi', dbname='washnotes')
app.install(plugin)


@app.route('/hello')
def hello():
    return "Hello World!"
    
@app.route('/')
def index():
    return redirect('/index')    
    
@app.route('/public/<filepath:path>')
def server_static(filepath):
    return static_file(filepath, root='./public')    
    
    
@app.route('/<page>')
def show(page, db):
    print ('WTF')
    print ('SELECT * from pages where page="%s"', (page,))
    #db.execute('SELECT * from pages where page="index"')
    db.execute("SELECT * FROM pages WHERE page = '{}'".format(page))

    row = db.fetchone()
    if row:
        return template('page.tpl', page=row)
    return HTTPError(404, "Page not found")
    
run(app, host='localhost', port=8080, debug=True)    
    
    
    