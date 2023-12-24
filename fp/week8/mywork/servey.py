from flask import Flask
app = Flask(__name__)

# @app.route("/")
# def myHello():
#     print("hello requested")
#     return "Hello World! - from Flask server 2"

# @app.route("/redirect")
# def redirectToStatic():
#     print("do something in the redirect route")
#     return redirect("/static/hello.html")

# @app.route("/pathVars/<name>")
# @app.route("/pathVars/<name>/<surname>")
# def pathVars(name, surname="Doe"):
#     print(name)
#     print(surname)
#     msg = "Hello "+name+" "+surname
#     return msg

# =================================
# Exercises

# 1) complete the route to give a goodbye message
# @app.route("/goodbye")
#    def goodbye():

# 2) Add a route: /goodbye/<name>
# Return “goodbye Ian”     where Ian is the name in the url.

# 3) complete the route to return the time
# @app.route("/time")


# 4) create a route that returns a hit counter with a message

# 5) create a route to returrn the IP ADDRESS of the client



if __name__ == "__main__":

    # this line will let the server serve to the local machine
    # to serve to other machines on the network
    # change this line (see slides)
    app.run(debug=True)