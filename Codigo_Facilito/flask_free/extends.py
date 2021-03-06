#!/usr/bin/env python3
from flask import Flask
from flask import render_template

app = Flask(__name__)  # Change default folder 'template_folder'


@app.route('/')
def index():
    name = 'Juan David'
    return render_template('index.html', name=name)

if __name__ == "__main__":
    app.run(debug=True, port=8000)
