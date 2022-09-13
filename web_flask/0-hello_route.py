#!/usr/bin/python3
"""
    Script that starts a Flask Web application that prints Hello HBNB
"""


from flask import Flask
app = Flask(__name__)


@app.route('/', strict_slashes=False)
def hello_hbnb():
    """
        function triggered by URL
    """
    return 'Hello HBNB!'

if __name__ == '__main__':
    """
        make web page accessible
    """
    app.run(host="0.0.0.0")
