from flask import Flask
import random

app = Flask(__name__)

print(random.__name__)


@app.route("/")
def hello_world():
    return "<p>Hello, World!</p>"


@app.route("/bye")
def bye():
    return "Good Bye"

@app.route("/username/<name>/<age>")
def url_input(name,age):
    return f"you name is {name}, you age is :{age+'12'}"

@app.route("/<path:currentpath>")
def getpath(currentpath):
    return f"rest of the path{currentpath}"
if __name__ == "__main__":
    app.run(debug=True)
