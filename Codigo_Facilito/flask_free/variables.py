#!/usr/bin/env python3
from flask import Flask
from flask import render_template

app = Flask(__name__)  # Change default folder 'template_folder'


@app.route('/user/')
@app.route('/')
def name():
    return render_template('index.html')


@app.route('/user/<name>')
def user(name='Juan'):
    age = 17
    my_list = [1, 2, 3, 4]
    return render_template('user.html', name=name, age=age, list=my_list)

if __name__ == "__main__":
    app.run(debug=True, port=8000)
