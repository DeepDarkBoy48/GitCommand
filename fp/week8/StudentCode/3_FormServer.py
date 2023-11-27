import os
from flask import Flask, redirect, request

app = Flask(__name__)

ALLOWED_EXTENSIONS = set(['txt', 'pdf', 'png', 'jpg', 'jpeg', 'gif'])

app = Flask(__name__)

@app.route("/HomeForm", methods=['GET','POST'])
def form():
    # TODO...
    print("Processing form")
    if request.method =='GET':
        print(request.args.get('firstname'))

    if request.method == 'POST':
        print('Post')
        print(request.form['firstname'])

    return "Hello World!"


if __name__ == "__main__":
    app.run(debug=True)
