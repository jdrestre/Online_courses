from flask import Flask
from flask import request

app = Flask(__name__)


@app.route('/')
def index():
    return "Hello World "

# http://127.0.0.1:8000/params?params1=Juan_David_Restrepo
# http://127.0.0.1:8000/params?params1=Juan_David_Restrepo&params2=otro_parametro


@app.route('/params')
def params():
    param = request.args.get('params1', 'no contiene este parametro')
    param_dos = request.args.get('params2', 'no contiene este parametro')
    return "Los parametros son : {} y {}".format(param, param_dos)

if __name__ == "__main__":
    app.run(debug=True, port=8000)
