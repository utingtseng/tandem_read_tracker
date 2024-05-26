params = []
book_dict = {"EOS": 6, "TOD": 7}
with open('./db/tandem.txt') as file:
    for i, line in enumerate(file):
        line = line.strip()
        book, desc = line.split(":")
        info = desc.split("-")
        if len(info) == 2:
            entry = (i+1, book_dict[book], int(info[0]), int(info[1]), desc.strip())
        else:
            entry = (i+1, book_dict[book], int(info[0]), int(info[0]), desc.strip())
        params.append(entry)

print(params)

import sqlite3
con = sqlite3.connect("database.db")
cur = con.cursor()
cur.execute("DROP TABLE IF EXISTS tandem_sections")
cur.execute("CREATE TABLE tandem_sections(id, book_id, start_chap, end_chap, description, read)")
cur.executemany("INSERT INTO tandem_sections (id, book_id, start_chap, end_chap, description) values (?, ?, ?, ?, ?)", params)
con.commit()
res = cur.execute("select * from tandem_sections").fetchall()
print(res)