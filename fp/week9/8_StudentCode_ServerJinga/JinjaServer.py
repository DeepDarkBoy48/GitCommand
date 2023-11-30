import os
from flask import Flask, redirect, request,render_template, jsonify

app = Flask(__name__)

ALLOWED_EXTENSIONS = set(['txt', 'pdf', 'png', 'jpg', 'jpeg', 'gif'])
directory = {'Ian':'0000','Chris':'1111','Wendy':'2222'}

app = Flask(__name__)


@app.route("/Basic", methods=['GET'])
def returnFirst():
    if request.method == 'GET':
        return render_template('0_Basic.html', data = 'Hello World')

# Quick Exercise complete the return route to include a message.
@app.route("/Basic2", methods=['GET'])
def returnSecond():
    if request.method == 'GET':
        return render_template('0-2_Basic.html', data = 'Hello World', msg="ian")

@app.route("/Json", methods=['GET'])
def returnjson():
    if request.method == 'GET':
        messages = {'title':'HelloWorld', 'name':'Ian', 'message':'this is a json string, the same format as a dictionary'}
        return render_template('1_json.html', data = messages)

@app.route("/Loops", methods=['GET'])
def returnLoops():
    if request.method == 'GET':
        vals = [1,2,3,4,5,6,7]
        days = ['mon','tues','wed','thurs','fri']
        return render_template('2_loops.html', nums = vals, days = days)

@app.route("/Dict", methods=['GET'])
def returnDict():
    if request.method == 'GET':
        data = {'title':'HelloWorld',
                'name':'Ian',
                'message':'hi!',
                'days': ['mon','tues','wed','thurs','fri']
                }
        return render_template('3_dictionary.html', data = data)

@app.route("/InheritanceBase", methods=['GET'])
def returnInheritanceBase():
    if request.method == 'GET':
        return render_template('4_inheritance.html')

@app.route("/Inheritance", methods=['GET'])
def returnInheritance():
    if request.method == 'GET':
        return render_template('5_inheritance.html')

# @app.route("/EX_1", methods=['GET'])
# def returnex1():
    # Exercise 1: un-comment this route and put the route code in here

# @app.route("/EX_2", methods=['GET'])
# def returnDir():
    #Exercise2: At the top of this server file there is
    # a dictionary; the directory
    #Create a page, using templates, to display
    #this in a tabular format.

if __name__ == "__main__":
    app.run(debug=True)
