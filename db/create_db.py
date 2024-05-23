import sqlite3
con = sqlite3.connect("database.db")
cur = con.cursor()
cur.execute("CREATE TABLE books(title, year, score)")
cur.execute("INSERT INTO books (title, year) values ('Throne of Glass', 2012)")
con.commit()
res = cur.execute("select * from books").fetchall()
print(res)