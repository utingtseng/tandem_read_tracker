import sqlite3

con = sqlite3.connect("database.db")
cur = con.cursor()
# cur.execute("DROP TABLE IF EXISTS annotations")
# create_sql= '''
# CREATE TABLE annotations
# ( ID INTEGER PRIMARY KEY AUTOINCREMENT, section_id, comments)
# '''
# cur.execute(create_sql)
res = cur.execute("select * from annotations")
for row in res:
    print("/ ".join(row))
con.commit()
con.close
