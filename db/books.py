import sqlite3
import pandas as pd

df = pd.read_csv("./db/books.csv")
df['date'] = pd.to_datetime(df['date']).dt.strftime('%Y-%m-%d')
df['word'] = df['word'].astype('int')
params = [(i+1, *tuple(x)) for i, x in enumerate(df.to_records(index=False))]
params = [(id, title, str(date), int(words), int(pages)) for id, title, date, words, pages in params]
print(params)



con = sqlite3.connect("database.db")
cur = con.cursor()
cur.execute("DROP TABLE IF EXISTS books")
cur.execute("CREATE TABLE books(id, title, date DATE, words INT, pages INT)")
cur.executemany("INSERT INTO books (id, title, date, words, pages) values (?, ?, ?, ?, ?)", params)
con.commit()
res = cur.execute("select * from books").fetchall()
print(res)