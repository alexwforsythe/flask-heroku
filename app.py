"""
Flask Documentation:     http://flask.pocoo.org/docs/
Jinja2 Documentation:    http://jinja.pocoo.org/2/documentation/
Werkzeug Documentation:  http://werkzeug.pocoo.org/documentation/

See more at: https://github.com/zachwill/flask_heroku
"""

import os
from flask import Flask


# Settings
app = Flask(__name__)


# Routing
@app.route('/')
def hello():
    return 'Hello World!'


if __name__ == '__main__':
    app.run()
