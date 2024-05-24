import sqlite3
con = sqlite3.connect("database.db")
cur = con.cursor()
cur.execute("CREATE TABLE annotations (id, section_id, color, comments)")
con.commit()