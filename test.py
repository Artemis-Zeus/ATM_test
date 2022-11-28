import sqlite3

def dict_factory(cursor, row):
    d = {}
    for idx, col in enumerate(cursor.description):
        d[col[0]] = row[idx]
    return d

con = sqlite3.connect("atm_databse.db")
# atm_databse/atm
# deposit/record
# Investment/investment
con.row_factory = dict_factory
c = con.cursor()
c.execute("select * from atm ")
output = c.fetchall()
for i in output:
    print(i)
