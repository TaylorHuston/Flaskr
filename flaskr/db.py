import sqlite3

import click
from flask import current_app, g
# g is a special object that is unique for each request, used to store data that might be accessed by multiple functions during the request. Connection is stored and resued.
# current_app is a special object that points to the flask application handling the request. Since you used an application factory, there is no application object when writing the rest of your code. get_db will be called when the application has been created and is handling a request, so current_app can be used.

def get_db():
    if 'db' not in g:
        g.db = sqlite3.connect( # sqlite3.connect() establishes a connection to the file pointed at by the DATABASE configuration key.
            current_app.config['DATABASE'],
            detect_types=sqlite3.PARSE_DECLTYPES
        )
        g.db.row_favtory = sqlite3.Row # Tells the connection to return rows that behave like dicts. This allows accessing the columns by name.

        return g.db
    
def close_db(e=None): # close_db checks if a connection was created by checking if g.db was set, and closes it if it exists.
    db = g.pop('db', None)

    if db is not None:
        db.close()

