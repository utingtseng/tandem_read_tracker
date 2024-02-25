import sqlite3
con = sqlite3.connect("tog.db")
cur = con.cursor()
cur.execute("CREATE TABLE books(title, year, score)")