import sqlite3
# 查看数据库结构

def dict_factory(cursor, row):
    d = {}
    for idx, col in enumerate(cursor.description):
        d[col[0]] = row[idx]
    return d


list1 = ["account", "record", "investment"]
con = sqlite3.connect("ATM.db")

con.row_factory = dict_factory
c = con.cursor()
for i in list1:
    print(i)
    c.execute("select * from %s " % i)
    output = c.fetchall()
    for i in output:
        print(i)
