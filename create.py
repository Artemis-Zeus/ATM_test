# 创建转账记录数据库deposit
# 格式如下：
# 原账户no 目标账户no 金额 时间戳

import sqlite3
import time
import random

# 在内存中创建数据库
db_name="ATM.db"
con = sqlite3.connect(db_name)

# 创建游标对象

# {'name': 'Demo', 'acc_no': 10, 'acc_type': 'savings', 'bal': 988, 'pass': 'trial'} ->{'name': 'Demo', 'acc_no': 10, 'bal': 988, 'pass': 'trial'}

cur = con.cursor()
# account: name | acc_no | bal | pw
# record: f_id | s_id | money | bill_no | type
# investment: id | year | rate | money
# 新建表abc，包含id，name，age三列，sqlite可以省略类型,ID为主键（主键不能重复）并且不能为空，若已有该表则报错
cur.execute("CREATE TABLE account(name TEXT, acc_no INT, bal INT, pw TEXT)")
cur.execute("INSERT INTO account(name,acc_no,bal,pw) VALUES(?,?,?,?)", ("Lewis",  1, 1000,"Lewis" ))
cur.execute("INSERT INTO account(name,acc_no,bal,pw) VALUES(?,?,?,?)", ("Jeddy",  2, 2000,"Jeddy" ))
cur.execute("INSERT INTO account(name,acc_no,bal,pw) VALUES(?,?,?,?)", ("Sakura", 3, 3500,"Sakura" ))
cur.execute("INSERT INTO account(name,acc_no,bal,pw) VALUES(?,?,?,?)", ("Sakura", 10, 1700,"Sakura" ))

cur.execute("CREATE TABLE investment(id INT, t INT, rate FLOAT, money INT)")
cur.execute("INSERT INTO investment(id,t,rate,money) VALUES(?,?,?,?)", (1, 1, 1.2, 1000))
time.sleep(2)
cur.execute("INSERT INTO investment(id,t,rate,money) VALUES(?,?,?,?)", (2, 2, 1.4, 1200))
time.sleep(2)
cur.execute("INSERT INTO investment(id,t,rate,money) VALUES(?,?,?,?)", (10, 3, 1.6, 2500))

cur.execute("CREATE TABLE record(f_id INT, s_id INT, money INT, type TEXT, bill_no TEXT)")
cur.execute("INSERT INTO record(f_id, s_id,money, type, bill_no) VALUES(?,?,?,?,?)", (1, 2, 100, "transfer","1669544906-4822485"))
cur.execute("INSERT INTO record(f_id, money, type, bill_no) VALUES(?,?,?,?)", (2,  100, "withdraw","1669544907-483701"))
cur.execute("INSERT INTO record(f_id,  money, type, bill_no) VALUES(?,?,?,?)", (1, 200, "Deposit","1669544909-486321"))

cur.execute("select * from investment")
output = cur.fetchall()
print(output)
con.commit()
cur.close()
con.close()
