import os
from flask import Flask, redirect, request

app = Flask(__name__)

ALLOWED_EXTENSIONS = set(['txt', 'pdf', 'png', 'jpg', 'jpeg', 'gif'])

app = Flask(__name__)

# create / define your data structure here (a dictionary) to store all the submissions.

# create your Route to addCommunity data here

if __name__ == "__main__":
    app.run(debug=True)
