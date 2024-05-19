#!/usr/bin/python3
"""
A Flask web application with various routes.
"""

from flask import Flask, render_template

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


@app.route('/number_template/<int:n>', strict_slashes=False)
def number_template(n):
    """
    Route that returns an HTML page with 'Number: n' in H1 tag,
    only if n is an integer.
    """
    return render_template('6-number.html', number=n)


@app.route('/number_odd_or_even/<int:n>', strict_slashes=False)
def number_odd_or_even(n):
    """
    Route that returns an HTML page with 'Number: n is even|odd' in H1 tag,
    only if n is an integer.
    """
    even_or_odd = "even" if n % 2 == 0 else "odd"
    values = {
        "number": n,
        "even_or_odd": even_or_odd
    }
    return render_template('6-number_odd_or_even.html', values=values)


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
