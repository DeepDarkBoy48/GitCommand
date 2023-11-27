import os
from flask import Flask

app = Flask(__name__)

if __name__ == "__main__":

    # this line will let the server serve to the local machine
    # to serve to other machines on the network
    # change this line (see slides)
    app.run(debug=True)
