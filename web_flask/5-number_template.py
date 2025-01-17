s module uses Flask and starts a web application"""


from flask import Flask, render_template
app = Flask(__name__)


@app.route('/', strict_slashes=False)
def hello_hbnb():
    """Hello world for flask"""
    return "Hello HBNB!"


@app.route('/hbnb', strict_slashes=False)
def hbnb():
    """display HBNB for /hbnb"""
    return "HBNB"


@app.route('/c/<string:text>', strict_slashes=False)
def c_route(text):
    """display `C` followed by value of text variable
    replace underscores with a space"""
    return "C {:s}".format(text.replace("_", " "))


@app.route('/python', strict_slashes=False)
@app.route('/python/<string:text>', strict_slashes=False)
def py_route(text="is cool"):
    """display `Python` followed by value of text variable
    replace underscores with a space"""
    return "Python {:s}".format(text.replace("_", " "))


@app.route('/number/<int:num>', strict_slashes=False)
def number_route(num):
    """display `n is a number` only if `n` is an int"""
    return "{:d} is a number".format(num)


@app.route('/number_template/<int:num>', strict_slashes=False)
def number_template(num):
    """displays a HTML page if `num` is an integer"""
    return render_template('5-number.html', num=num)

if __name__ == "__main__":
    app.run(host="0.0.0.0", port="5000")
