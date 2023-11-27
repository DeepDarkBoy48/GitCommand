import os
from flask import Flask, redirect, request

app = Flask(__name__)

ALLOWED_EXTENSIONS = set(['txt', 'pdf', 'png', 'jpg', 'jpeg', 'gif'])

app = Flask(__name__)

communityData = {}

@app.route("/AddCommunityData", methods=['POST'])
def form():
    global communityData

    print("Processing form")
    email = request.form['email']
    worst = request.form['worst']
    best = request.form['best']
    habbit = request.form['habbit']
    communityData[email] = [worst,best,habbit]

    print(communityData )
    return "Thankyou"

@app.route("/GetData", methods=['GET'])
def getData():
    global communityData
    return communityData

@app.route("/DeleteData", methods=['POST'])
def deleteData():
    global communityData
    email = request.form['email']
    print(email)
    del communityData[email]
    return communityData

if __name__ == "__main__":
    app.run(debug=True)
