#!/usr/bin/python3
"""
A simple Flask web application with multiple routes.
"""

from flask import Flask, abort

app = Flask(__name__)


@app.route('/', strict_slashes=False)
def hello_hbnb():
    """
    Route that returns 'Hello HBNB!'
    """
    return "Hello HBNB!"


@app.route('/hbnb', strict_slashes=False)
def hbnb():
    """
    Route that returns 'HBNB'
    """
    return "HBNB"


@app.route('/c/', strict_slashes=False)
@app.route('/c/<text>', strict_slashes=False)
def c_text(text="is cool"):
    """
    Route that returns 'C ' followed by the value of the text variable,
    with underscores replaced by spaces. Default value: 'is cool'.
    """
    return "C {}".format(text.replace('_', ' '))


@app.route('/python/', strict_slashes=False)
@app.route('/python/<text>', strict_slashes=False)
def python_text(text="is cool"):
    """
    Route that returns 'Python ' followed by the value of the text variable,
    with underscores replaced by spaces. Default value: 'is cool'.
    """
    return "Python {}".format(text.replace('_', ' '))


@app.route('/number/<int:n>', strict_slashes=False)
def number(n):
    """
    Route that returns 'n is a number' only if n is an integer.
    """
    return "{} is a number".format(n)


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
