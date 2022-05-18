from flask import Flask
import random

app = Flask(__name__)
print(__name__)
number=random.randint(0,9)
@app.route("/")
def add_initial_gif():
    return "<h1>Guess a number between 0 and 9</h1>" \
           "<img src='https://media.giphy.com/media/3o7aCSPqXE5C6T8tBC/giphy.gif'/>"


@app.route("/<int:n>")
def getnumber(n):
    if n<=9 and n>=0:
        if n > number:
            return "<h1 style='color:red'>Too high! Try Again</h1>" \
                   "<img src='https://media.giphy.com/media/3o6ZtaO9BZHcOjmErm/giphy.gif'>"
        elif n < number:
            return "<h1 style='color:red;'>Too Low! Try Again</h1>" \
                   "<img src=' https://media.giphy.com/media/jD4DwBtqPXRXa/giphy.gif'>"
        else:
            return "<h1 style='color:green;'>You Found me!</h1>" \
                   "<img src='https://media.giphy.com/media/4T7e4DmcrP9du/giphy.gif'>"
    else:
        return "<h1>Please enter valid number</h1>"


if __name__ == "__main__":
    app.run(debug=True)