import os
from flask import Flask

app = Flask(__name__)

app_dir = os.path.abspath(os.path.dirname(__file__))
db_file = os.path.join(app_dir, "db/tog.db")

@app.route("/")
def hello_world():
    return "<p>Hello, World!</p>"