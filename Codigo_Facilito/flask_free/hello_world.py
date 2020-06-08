from flask import Flask
# Basic Elements in flask 

app = Flask(__name__) #New instance

@app.route('/') #wrap or decoratore
def index(): # Function
    return "Hello World from Code" #Return string
app.run() #execute server for default in port 5000
