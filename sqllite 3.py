import sqlite3
con=sqlite3.connect("testdb")
cur=con.cursor()
cur.execute("insert into test values(10);")
cur.execute("insert into test values(20);")
cur.execute("select*from test;")
rows=cur.fetchall()
for row in rows:
    print(row)
