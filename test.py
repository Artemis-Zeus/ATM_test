import sqlite3


def dict_factory(cursor, row):
    d = {}
    for idx, col in enumerate(cursor.description):
        d[col[0]] = row[idx]
    return d


list1 = ["account", "record", "investment"]
con = sqlite3.connect("ATM.db")
# 三个数据库/表，替换上面db文件可以查看数据库里面的格式
# atm_databse/atm
# deposit/record
# Investment/investment

con.row_factory = dict_factory
c = con.cursor()
for i in list1:
    print(i)
    c.execute("select * from %s " % i)
    output = c.fetchall()
    for i in output:
        print(i)
