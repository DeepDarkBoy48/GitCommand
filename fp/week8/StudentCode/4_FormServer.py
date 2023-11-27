import os
from flask import Flask, redirect, request

app = Flask(__name__)

ALLOWED_EXTENSIONS = set(['txt', 'pdf', 'png', 'jpg', 'jpeg', 'gif'])

app = Flask(__name__)

names = []

@app.route("/HomeForm", methods=['POST', "GET"])
def form():
    global names
    global surnames
    print("Processing form")
    if request.method == 'POST':
        name = request.form['firstname']
        names.append(name)
    if request.method =='GET':   # shouldn't use get for adding data
        name = request.args.get('firstname')
        names.append(name)
    print(names )
    return "Hello World!"





if __name__ == "__main__":
    app.run(debug=True)
