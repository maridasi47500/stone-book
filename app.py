from flask import Flask
from . import db


app = Flask(__name__)
db.init_app(app)

@app.route("/")
def hello_world():
    return "<p><form><div>add a note to your notebook<textarea></textarea></div><div>choose bullet style <select><option>&#128142; &#x1F48E;</option><option>&#127963;</option><option>&#127756;</option></select></div></form></p>"

@app.route("/cafeteria")
def hello_world():
    return "cafeteria menu"

@app.route("/souvenirshop")
def hello_world():
    return "souvenir shop items"
