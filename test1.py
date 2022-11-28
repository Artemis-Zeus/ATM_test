import sqlite3

def dict_factory(cursor, row):
    d = {}
    for idx, col in enumerate(cursor.description):
        d[col[0]] = row[idx]
    return d

con = sqlite3.connect("Investment.db") #打开数据库
con.row_factory = dict_factory
c = con.cursor()
# conn = sqlite3.connect("ChineseCharactersLite.db")
# c = conn.cursor()
c.execute("select * from investment ")
# """select name from sqlite_master where type='table' order by name"""
output = c.fetchall()
for i in output:
    print (i)
