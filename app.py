import os
from flask import Flask, render_template, jsonify
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

@app.route("/tandem/current_chapter")
def current_chapter():
    section_id = 3

    return jsonify(get_recent_reads(section_id))

def get_recent_reads(id):
    conn = get_db_connection()
    sql = '''
    select b.title, a.color, a.comments, ts.description from tandem_sections ts 
    left join annotations a on ts.id = a.section_id
    left join books b on ts.book_id = b.id
    where ts.id >= ? and ts.id <= ?
    order by ts.id
    '''
    res = conn.execute(sql, (id -1, id+ 1))
    labels = ["prev", "curr", "next"]
    json = {labels[i]: {"title": row[0], "color": row[1], "comments": row[2], "chapters": row[3]} for i, row in enumerate(res)}
    print(json)
    return json

