import sqlite3

con=sqlite3.connect("ATM.db")
out=con.execute("select * from account")
print(out)