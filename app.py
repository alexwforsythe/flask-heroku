"""
Flask Documentation:     http://flask.pocoo.org/docs/
Jinja2 Documentation:    http://jinja.pocoo.org/2/documentation/
Werkzeug Documentation:  http://werkzeug.pocoo.org/documentation/

See more at: https://github.com/zachwill/flask_heroku
"""

import os
from flask import Flask
from flask import render_template


# Settings
app = Flask(__name__)


# Routing
@app.route('/')
@app.route('/hello/')
@app.route('/hello/<name>/')
def hello(name=None):
    return render_template('hello.html', name=name)


if __name__ == '__main__':
    app.run(debug=True)
