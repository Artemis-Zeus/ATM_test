# jeddy 、Sakura、Franklif、Artemis、Xylophone、jyf、recomoonmoon加入
# Bank ATM

from tkinter import *
from tkinter import messagebox
import sqlite3
import time
from tkinter import ttk

ARIAL = ("arial", 11, "bold")

class Bank:
    def __init__(self, root):
        self.money = None
        self.conn = sqlite3.connect("ATM.db", timeout=100)
        self.login = False
        self.root = root
        self.header = Label(self.root, text="WGS BANK", bg="#304655", fg="white", font=("arial", 20, "bold"))
        self.header.pack(fill=X)
        self.frame = Frame(self.root, bg="#e5d4cd", width=600, height=400)
        # Login Page Form Components
        self.userlabel = Label(self.frame, text="Account Number", bg="#e5d4cd", fg="#b59283", font=ARIAL)
        self.uentry = Entry(self.frame, bg="honeydew", highlightcolor="#b59283",
                            highlightthickness=2,
                            highlightbackground="white")
        self.plabel = Label(self.frame, text="Password", bg="#e5d4cd", fg="#b59283", font=ARIAL)
        self.pentry = Entry(self.frame, bg="honeydew", show="*", highlightcolor="#b59283",
                            highlightthickness=2,
                            highlightbackground="white")
        self.button1 = Button(self.frame, text="REGISTER", bg="#b59283", fg="white", font=ARIAL,
                              command=self.register)
        self.button = Button(self.frame, text="LOGIN", bg="#b59283", fg="white", font=ARIAL, command=self.verify)
        self.q = Button(self.frame, text="Quit", bg="#b59283", fg="white", font=ARIAL, command=self.root.destroy)
        self.userlabel.place(x=205, y=60, width=120, height=20)
        self.uentry.place(x=213, y=90, width=200, height=25)
        self.plabel.place(x=185, y=130, width=120, height=20)
        self.pentry.place(x=213, y=160, width=200, height=25)
        self.button1.place(x=165, y=260, width=120, height=30)
        self.button.place(x=335, y=260, width=120, height=30)
        self.q.place(x=545, y=355, width=60, height=30)

        self.frame.pack()

    def register(self):
        self.userlabel = Label(self.frame, text="Account Name", bg="#e5d4cd", fg="#b59283", font=ARIAL)#这里重构一下文字
        self.userlabel.place(x=205, y=60, width=120, height=20)
        self.button.destroy()
        self.button1.destroy()
        def register1():
            a = self.uentry.get()
            b = self.pentry.get()
            print(a)#测试用

            self.conn.execute("INSERT INTO account (name,acc_no,bal,pw) \
                          VALUES (?,123,0,? )", (a, b))#acc_no 手动设置
            self.conn.commit()#不要随意commit用户注册数据
            messagebox._show("Register Info", "Register successful!")  # 成功提示栏
            self.header.destroy()
            self.frame.destroy()
            self.__init__(root)
        self.button3 = Button(self.frame, text="Register", bg="#b59283", fg="white", font=ARIAL, command=register1)
        self.button3.place(x=210, y=230, width=120, height=40)


    def database_fetch(self):  # Fetching Account data from database
        self.acc_list = []
        self.temp = self.conn.execute("select name,pw,acc_no,bal from account where acc_no = ? ", (self.ac,))
        for i in self.temp:
            self.money = i[3]
            self.acc_list.append("Name = {}".format(i[0]))
            self.acc_list.append("Account no = {}".format(i[2]))
            self.ac = i[2]
            self.acc_list.append("Balance = {}".format(i[3]))

    def verify(self):  # verification
        ac = False
        self.temp = self.conn.execute("select name,pw,acc_no,bal from account where acc_no = ? ",
                                      (int(self.uentry.get()),))
        for i in self.temp:
            self.ac = i[2]
            if i[2] == self.uentry.get():
                ac = True
            elif i[1] == self.pentry.get():
                ac = True
                m = "{} Login Successful".format(i[0])
                self.database_fetch()
                messagebox._show("Login Info", m)
                self.frame.destroy()
                self.MainMenu()
            else:
                ac = True
                m = " Login Unsuccessful ! Wrong Password !"
                messagebox._show("Login Info", m)

        if not ac:
            m = " Wrong Account Number !"
            messagebox._show("Login Info", m)

    def MainMenu(self):  # Main interface appears after logging in
        self.frame = Frame(self.root, bg="#e5d4cd", width=1080, height=720)
        root.title("User Interface")
        root.geometry("1080x720")

        self.accInfo = Button(self.frame, text="Account Information", bg="#b59283", fg="white", font=ARIAL,
                             command=self.account_info)
        self.transfer = Button(self.frame, text="Transfer", bg="#b59283", fg="white", font=ARIAL, command=self.transfer)

        self.investment = Button(self.frame, text="Investment", bg="#b59283", fg="white", font=ARIAL,
                                 command=self.investment)
        self.balInquiry = Button(self.frame, text="Balance Inquiry", bg="#b59283", fg="white", font=ARIAL,
                              command=self.Balance)
        self.deposit = Button(self.frame, text="Deposit", bg="#b59283", fg="white", font=ARIAL,
                              command=self.deposit_money)
        self.withdrawal = Button(self.frame, text="Withdrawal", bg="#b59283", fg="white", font=ARIAL,
                               command=self.withdraw_money)
        self.recInquiry = Button(self.frame, text="Record Inquiry", bg="#b59283", fg="white", font=ARIAL,
                                     command=self.record)
        self.q = Button(self.frame, text="Quit", bg="#b59283", fg="white", font=ARIAL, command=self.root.destroy)
        Label(self.frame, text="Welcome to WGS Bank!", font=('Times',18,'bold'),bg='#e5d4cd').place(x=370, y=320, width=340, height=50)
        self.accInfo.place(x=-5, y=0, width=200, height=50)
        self.transfer.place(x=-5, y=235, width=200, height=50)
        self.recInquiry.place(x=-5, y=450, width=200, height=50)
        self.balInquiry.place(x=-5, y=635, width=200, height=50)
        self.deposit.place(x=880, y=0, width=200, height=50)
        self.investment.place(x=880, y=317, width=200, height=50)
        self.withdrawal.place(x=880, y=635, width=200, height=50)
        self.q.place(x=480, y=635, width=120, height=50)
        self.frame.pack()

    def account_info(self):
        self.database_fetch()
        text = "\n\n\n" + self.acc_list[0] + "\n\n" + self.acc_list[1] + "\n\n" + self.acc_list[2]
        Label(self.frame, text=text, font=("Times",15,"bold"),bg="#e5d4cd").place(x=300, y=200, width=480, height=200)

    def Balance(self):
        self.database_fetch()
        text="\n\n" + self.acc_list[2]
        Label(self.frame, text=text, font=("Times",15,"bold"),bg="#e5d4cd").place(x=300, y=200, width=480, height=200)

    def transfer(self):
        self.database_fetch()
        print(self.ac)
        Label(self.frame,bg="#e5d4cd").place(x=300, y=200, width=480, height=200)
        Label(self.frame, text="Target Account:", font=("Times",15,"bold"),bg="#e5d4cd").place(x=300, y=220, width=480
, height=25)
        Label(self.frame, text="Transfer Amount:", font=("Times",15,"bold"),bg="#e5d4cd").place(x=300, y=290, width=480
, height=25)
        self.target_account = Entry(self.frame, bg="honeydew", highlightcolor="#b59283",
                                    highlightthickness=2,
                                    highlightbackground="white")
        self.money_box = Entry(self.frame, bg="honeydew", highlightcolor="#b59283",
                               highlightthickness=2,
                               highlightbackground="white")
        self.submitButton = Button(self.frame, text="Submit", bg="#b59283", fg="white", font=ARIAL)
        self.target_account.place(x=400, y=250, width=280, height=25)
        self.money_box.place(x=400, y=320, width=280, height=25)
        self.submitButton.place(x=500, y=360, width=80, height=30)
        self.submitButton.bind("<Button-1>", self.transfer_trans)

    def transfer_trans(self, flag):
        if self.money >= int(self.money_box.get()) >= 0:
            Label(self.frame, text="Transaction Complete!", font=("Times",15,"bold"),bg="#e5d4cd").place(x=300, y=200, width=480
, height=200)
            self.conn.execute("update account set bal = bal - ? where acc_no = ?", (self.money_box.get(), self.ac))
            self.conn.commit()
            self.conn.execute("INSERT INTO record(f_id,s_id,money,bill_no) VALUES(?,?,?,?)",
                              (self.ac, int(self.target_account.get()), int(self.money_box.get()),
                               str(time.time()).replace(".", "-")))
            self.conn.commit()

        elif int(self.money_box.get()) < 0:
            Label(self.frame, text="Transaction Failed!\n The transfer amount should be greater than 0!",
                               font=("Times",15,"bold"),bg="#e5d4cd").place(x=300, y=200, width=480
, height=200)
        else:
            Label(self.frame, text="Insufficient Balance!",
                               font=("Times",15,"bold"),bg="#e5d4cd").place(x=300, y=200, width=480
, height=200)

    def record(self):
        self.database_fetch()
        c = self.conn.cursor()
        c.execute("select * from record where f_id={} OR s_id={}".format(self.ac, self.ac))
        output = c.fetchall()
        heads = ["f_id", "s_id", 'money', 'type', 'withdrawal']
        self.tree = ttk.Treeview(self.frame, show='headings')
        self.tree["columns"] = ("f_id", "s_id", 'money', 'type', 'bill_no')   #定义列
        self.tree.column("f_id", width=40)   #设置列
        self.tree.column("s_id", width=50)
        self.tree.column('money', width=60)
        self.tree.column("type", width=80)
        self.tree.column("bill_no", width=130)
        self.tree.heading("f_id", text="Send.")   #设置显示的表头名
        self.tree.heading("s_id", text="Rec.")  # Recipient
        self.tree.heading("money", text="Amount")
        self.tree.heading("type", text="Type")
        self.tree.heading("bill_no", text="Bill No.")
        for i in range(len(output)):
            self.tree.insert("", i, text=" ", values=output[i])
        self.tree.place(x=300, y=200, width=480, height=200)

    def investment(self):
        self.database_fetch()
        Label(self.frame).place(x=300, y=200, width=480, height=200)

        # Label(self.frame, text="financial product:", font=ARIAL).place(x=320, y=50, width=150, height=20)
        # Label(self.frame, text="Investment product:1；time:1.2；money:1000").place(x=220, y=80, width=295, height=20)
        # Label(self.frame, text="Investment product:2；time:1.4；money:1200").place(x=220, y=100, width=295, height=20)
        # Label(self.frame, text="Investment product:3；time:1.6；money:2500").place(x=220, y=120, width=295, height=20)

#################################################################
        self.tree = ttk.Treeview(self.frame, show='headings')
        self.tree["columns"] = ("Product ID", "Term", 'Per Amount',"Interest Rate",'amount')   #定义列
        self.tree.column("Product ID", width=80,anchor='center')   #设置列
        self.tree.column("Term", width=60,anchor='center')
        self.tree.column('Per Amount', width=90,anchor='center')
        self.tree.column("Interest Rate", width=90,anchor='center')
        self.tree.column("amount",width=50,anchor='center')
        self.tree.heading("Product ID", text="Product ID")  #设置显示的表头名
        self.tree.heading("Term", text="Term")  # Recipient
        self.tree.heading("Per Amount", text="Per Amount")
        self.tree.heading("Interest Rate", text="Interest Rate")
        self.tree.heading("amount", text="Amount")
        for i in range(3):
            self.tree.insert("",i,values=(i, str(i+1)+" year",1000+750*i ,1.2+i*0.2,''))
        self.tree.place(x=300, y=200, width=480, height=200)
#######################################

        self.money_input1 = Entry(self.frame, bg="honeydew", highlightcolor="#b59283",
                                  highlightthickness=2,
                                  highlightbackground="white")
        self.money_input1.place(x=715, y=225, width=55, height=20)
        self.money_input2 = Entry(self.frame, bg="honeydew", highlightcolor="#b59283",
                                  highlightthickness=2,
                                  highlightbackground="white")
        self.money_input2.place(x=715, y=245, width=55, height=20)
        self.money_input3 = Entry(self.frame, bg="honeydew", highlightcolor="#b59283",
                                  highlightthickness=2,
                                  highlightbackground="white")
        self.money_input3.place(x=715, y=265, width=55, height=20)
        self.submitButton = Button(self.frame, text="Submit", bg="#b59283", fg="white", font=ARIAL)
        self.submitButton.place(x=510, y=350, width=60, height=30)
        self.submitButton.bind("<Button-1>", self.investment_trans)  # execute investment_trans

    def investment_trans(self, flag):
        top = Toplevel(width=400, height=400)
        top.title('investment')
        investment_list = [{'id': 1, 't': 1, 'rate': 1.2, 'money': 1000}, {'id': 2, 't': 2, 'rate': 1.4, 'money': 1750},
                           {'id': 3, 't': 3, 'rate': 1.6, 'money': 2500}]
        terminal = []  # Store the investment product information purchased by users
        x = self.money_input1.get()
        if x == '':
            x = 0
        else:
            x = int(x)
        s = self.money_input2.get()
        if s == '':
            s = 0
        else:
            s = int(s)
        l = self.money_input3.get()
        if l == '':
            l = 0
        else:
            l = int(l)
        if x >= 0 and s >= 0 and l >= 0:
            payment = x * 1000 + s * 1750 + l * 2500  # total price
            if self.money >= payment > 0:
                if x > 0:
                    time = x
                    money_ = 1000 * x
                    terminal.append({'id': 0, 't': time, 'rate': 1.2, 'money': money_})
                if s > 0:
                    time = s
                    money_ = 1750 * s
                    terminal.append({'id': 1, 't': time, 'rate': 1.4, 'money': money_})
                if l > 0:
                    time = l
                    money_ = 2500 * l
                    terminal.append({'id': 2, 't': time, 'rate': 1.6, 'money': money_})
                Label(top, text="Purchase complete!", font=("Times",15,"bold"),bg="#e5d4cd").place(x=120, y=80, width=150, height=200)
                Label(top, text="Investment product you have:", font=("Times",15,"bold"),bg="#e5d4cd").place(x=120, y=110, width=150, height=200)

                tree = ttk.Treeview(top)  # #创建表格对象
                tree["columns"] = ("id", "time", "rate", "money")  # 定义列:理财产品，持有年限，年利率，购买的金额
                tree.column("id", width=70)  # #设置列
                tree.column("time", width=70)
                tree.column("rate", width=70)
                tree.column("money", width=70)
                tree.heading("id", text="id")  # #设置显示的表头名
                tree.heading("time", text="time")
                tree.heading("rate", text="rate")
                tree.heading("money", text="money")

                counter = 0
                for i in terminal:
                    tree.insert("", counter, text="line%s"%counter,
                                values=(i.get('id'), i.get('t'), i.get('rate'), i.get('money')))  # #给第0行添加数据，索引值可重复
                    counter += 1
                tree.pack()

                self.conn.execute("update account set bal = bal - ? where acc_no = ?", (payment, self.ac))
                self.conn.commit()
            elif self.money <= 0:
                Label(top, text="There is no balance in your account!", font=("Times",15,"bold"),bg="#e5d4cd").place(x=100, y=100, width=280, height=200)
            elif self.money < payment:
                Label(top, text="Insufficient account balance!", font=("Times",15,"bold"),bg="#e5d4cd").place(x=100, y=100, width=280, height=200)
        else:
            Label(top, text="Incorrect input of investment product shares!", font=("Times",15,"bold"),bg="#e5d4cd").place(x=100, y=100, width=280, height=200)

    def deposit_money(self):
        temp = self.withdraw_deposit("deposit")
        temp.bind("<Button-1>", self.deposit_trans)

    def deposit_trans(self, flag):
        if int(self.money_box.get()) >= 0:
            Label(self.frame,bg="#e5d4cd").place(x=300, y=200, width=480, height=200)
            Label(self.frame, text="Transaction Completed !", font=("Times",15,"bold"),bg="#e5d4cd").place(x=300, y=200, width=480
, height=200)
            self.conn.execute("update account set bal = bal + ? where acc_no = ?", (self.money_box.get(), self.ac))
            self.conn.execute("INSERT INTO record(f_id,  money, type, bill_no) VALUES(?,?,?,?)",
                              (self.ac, self.money_box.get(), "Deposit", str(time.time()).replace(".", "-")))
            self.conn.commit()
        else:
            Label(self.frame, text="Transaction failed!\n The deposit amount should be greater than 0",
                               font=("Times",15,"bold"),bg="#e5d4cd").place(x=300, y=200, width=480
, height=200)

    def withdraw_deposit(self,tip):
        Label(self.frame,bg='#e5d4cd').place(x=300, y=200, width=480, height=200)
        self.money_box = Entry(self.frame, bg="honeydew", highlightcolor="#b59283",
                               highlightthickness=2,
                               highlightbackground="white")
        self.submitButton = Button(self.frame, text="Submit", bg="#b59283", fg="white", font=ARIAL)
        Label(self.frame, text="The amount of money you want to %s:"%tip, font=("Times",15,"bold"),bg="#e5d4cd").place(x=300, y=250, width=480
, height=20)
        self.money_box.place(x=440, y=300, width=200, height=25)
        self.submitButton.place(x=500, y=360, width=80, height=25)
        return self.submitButton

    def withdraw_money(self):
        temp = self.withdraw_deposit("withdraw")
        temp.bind("<Button-1>", self.withdraw_trans)

    def withdraw_trans(self, flag):
        Label(self.frame).place(x=300, y=200, width=480, height=200)
        self.database_fetch()
        if int(self.money_box.get()) < 0:
            Label(self.frame, text="The withdraw amount cannot be less than 0!",
                               font=("Times",15,"bold"),bg="#e5d4cd").place(x=300, y=70, width=480
, height=200)

        elif int(self.money_box.get()) <= self.money:
            Label(self.frame, text="Withdraw Successful!", font=("Times",15,"bold"),bg="#e5d4cd").place(x=300, y=200, width=480
, height=200)
            self.conn.execute("update account set bal = bal - ? where acc_no = ?", (self.money_box.get(), self.ac))
            self.conn.execute("INSERT INTO record(f_id,  money, type, bill_no) VALUES(?,?,?,?)",
                              (self.ac, self.money_box.get(), "Withdraw", str(time.time()).replace(".", "-")))
            self.conn.commit()

        else:
            Label(self.frame, text="Insufficient Balance!",
                               font=("Times",15,"bold"),bg="#e5d4cd").place(x=300, y=200, width=480
, height=200)


root = Tk()
root.title("Login Interface")
root.geometry("600x420")
# 防止用户调整窗口分辨率
root.resizable(0,0)
icon = PhotoImage(file="icon.png")
root.tk.call("wm", 'iconphoto', root._w, icon)
obj = Bank(root)
root.mainloop()
