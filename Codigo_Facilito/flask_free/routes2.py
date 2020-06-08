#!/usr/bin/env python3
from flask import Flask
from flask import request

app = Flask(__name__)


@app.route('/')
def index():
    return "Hello World "


@app.route('/params/')
@app.route('/params/<name>/')
@app.route('/params/<name>/<last_name>/')
@app.route('/params/<name>/<last_name>/<int:num>')
def params(name='default value', last_name="default value 2", num="empty"):
    return "El parametro es : {} {} {}".format(name, last_name, num)

if __name__ == "__main__":
    app.run(debug=True, port=8000)
