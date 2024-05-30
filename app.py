import os
from flask import Flask, render_template, jsonify, request
from flask_cors import CORS
import sqlite3
import collections

import logging

logging.basicConfig(
    level=logging.DEBUG,
    format="%(asctime)s - %(name)s - %(levelname)s - %(message)s",
    handlers=[logging.FileHandler("my_logger.log"), logging.StreamHandler()],
)

logger = logging.getLogger("my_logger")

app = Flask(__name__)
CORS(app)

app_dir = os.path.abspath(os.path.dirname(__file__))


def get_db_connection():
    conn = sqlite3.connect("database.db")
    conn.row_factory = sqlite3.Row
    return conn


@app.route("/")
def index():
    conn = get_db_connection()
    res = conn.execute("select * from books").fetchall()

    for i in res:
        logger.debug(i[0])
    return render_template("index.html")


@app.route("/tandem/full-list")
def get_full_list():
    conn = get_db_connection()
    sql = """
    select ts.id, b.title, ts.description, ts.read
    from tandem_sections ts
    left join books b on ts.book_id = b.id"""
    res = conn.execute(sql).fetchall()
    json = []
    for row in res:
        json.append(
            {"section_id": row[0], "title": row[1], "chapters": row[2], "read": row[3]}
        )

    return jsonify(json)


@app.route("/tandem/current_chapter")
def current_chapter():
    conn = get_db_connection()
    sql = """
    select max(id) from tandem_sections where read == 1
    """
    res = conn.execute(sql).fetchone()
    if not res[0]:
        section_id = 1
    else:
        section_id = res[0] + 1

    return jsonify(get_recent_reads(section_id))


def get_recent_reads(id):
    conn = get_db_connection()
    sql = """
    select b.title, ts.description, ts.id from tandem_sections ts
    left join books b on ts.book_id = b.id
    where ts.id >= ? and ts.id <= ?
    order by ts.id
    """
    res = conn.execute(sql, (id - 1, id + 1)).fetchall()

    sql2 = """
    select id, section_id, comments
    from annotations
    where section_id >= ? and section_id <= ?
    """
    res2 = conn.execute(sql2, (id - 1, id + 1))

    annotations = collections.defaultdict(list)
    for row in res2:
        annotations[row[1]].append({"anno_id": row[0], "comments": row[2]})

    labels = ["prev", "curr", "next"]
    if id == 1:
        json = {
            "prev": {
                "title": "Empire of Storms",
                "chapters": "Fireheart",
                "section_id": 0,
                "comments": "",
            },
            "curr": {
                "title": res[0][0],
                "chapters": res[0][1],
                "section_id": res[0][2],
                "comments": annotations[res[0][2]],
            },
            "next": {
                "title": res[1][0],
                "chapters": res[1][1],
                "section_id": res[1][2],
                "comments": annotations[res[1][2]],
            },
        }
    else:
        json = {
            labels[i]: {
                "title": row[0],
                "chapters": row[1],
                "section_id": row[2],
                "comments": annotations[row[2]],
            }
            for i, row in enumerate(res)
        }

    if len(json) == 2:
        json["next"] = {
            "title": "Completed",
            "chapters": "congratulations",
            "section_id": "",
            "comments": "",
        }

    return json


@app.route("/tandem/complete/<int:section_id>")
def complete_section(section_id):
    conn = get_db_connection()
    sql = """
    update tandem_sections
    set read = 1
    where id = ?
    """
    conn.execute(sql, (section_id,))
    conn.commit()

    return jsonify(get_recent_reads(section_id + 1))


@app.route("/tandem/new-comment/<int:section_id>", methods=["POST"])
def add_new_comment(section_id):
    new_comment = request.json.get("newComment")
    try:
        if new_comment:
            conn = get_db_connection()
            sql = """
            insert into annotations
            (comments, section_id)
            values (?, ?)
            """
            conn.execute(sql, (new_comment, section_id))
            conn.commit()
            return jsonify(get_recent_reads(section_id))
        else:
            return jsonify(get_recent_reads(section_id))
    except Exception as e:
        error_message = str(e)
        return jsonify({"error": error_message}), 500
