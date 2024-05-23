import os
from flask import Flask, render_template
import sqlite3

import logging 

logging.basicConfig(level=logging.DEBUG,
                    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
                    handlers=[logging.FileHandler("my_logger.log"),
                              logging.StreamHandler()])

logger = logging.getLogger('my_logger')


app = Flask(__name__)

app_dir = os.path.abspath(os.path.dirname(__file__))


def get_db_connection():
    conn = sqlite3.connect('database.db')
    conn.row_factory = sqlite3.Row
    return conn

@app.route("/")
def index():
    conn = get_db_connection()
    res = conn.execute("select * from books").fetchall()
    conn.close()
    for i in res:
        logger.debug(i[0])
    return render_template("index.html")