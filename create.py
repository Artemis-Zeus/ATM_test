# 创建转账记录数据库deposit
# 格式如下：
# 原账户no 目标账户no 金额 时间戳

import sqlite3
import time
import random

# 在内存中创建数据库
con = sqlite3.connect("Investment.db")

# 创建游标对象
cur = con.cursor()

# 新建表abc，包含id，name，age三列，sqlite可以省略类型,ID为主键（主键不能重复）并且不能为空，若已有该表则报错
cur.execute("CREATE TABLE investment(id INT, t INT, rate FLOAT, money INT)")
cur.execute("INSERT INTO investment(id,t,rate,money) VALUES(?,?,?,?)", (1, 1, 1.2, 1000))
cur.execute("INSERT INTO investment(id,t,rate,money) VALUES(?,?,?,?)", (2, 2, 1.4, 1200))
cur.execute("INSERT INTO investment(id,t,rate,money) VALUES(?,?,?,?)", (10, 3, 1.6, 2500))

cur.execute("select * from investment")
output = cur.fetchall()
print(output)
con.commit()
cur.close()
con.close()
