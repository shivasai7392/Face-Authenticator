"""
    _summary_

_extended_summary_

Returns:
    _type_: _description_
"""
from flask import Flask
from flask import render_template
from forms import RegistrationForm
from forms import LoginForm
# from flask import request
# from flask import redirect

app = Flask(__name__)
app.config["SECRET_KEY"] = "dbb4576b2349b9da3759800a4c88e793"

@app.route('/register')
def signup():
    """
    signup _summary_

    _extended_summary_

    Returns:
        _type_: _description_
    """
    form = RegistrationForm()
    return render_template("register.html", title = "Register", form = form)

@app.route('/login')
def login():
    """
    login _summary_

    _extended_summary_

    Returns:
        _type_: _description_
    """
    form = LoginForm()
    return render_template("login.html", title = "Login", form = form)

@app.route('/')
@app.route('/home')
def index():
    """
    index _summary_

    _extended_summary_

    Returns:
        _type_: _description_
    """
    return render_template("index.html", title = "Welcome!")

if __name__ == "__main__":
    app.run(debug=True)
