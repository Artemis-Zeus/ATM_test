# jeddy 、Sakura、Franklif、Artemis、Xylophone、jyf加入
# Bank ATM
# created by github.com/rajatbhatia1998
# Account Number : 10 ------------ Password : trial

from tkinter import *
from tkinter import messagebox
import sqlite3
import time

ARIAL = ("arial", 10, "bold")


# abcd
class Bank:
    def __init__(self, root):
        self.money = None
        self.conn = sqlite3.connect("ATM.db", timeout=100)
        self.login = False
        self.root = root
        self.header = Label(self.root, text="R~R BANK", bg="#50A8B0", fg="white", font=("arial", 20, "bold"))
        self.header.pack(fill=X)
        self.frame = Frame(self.root, bg="#728B8E", width=600, height=400)
        # Login Page Form Components
        self.userlabel = Label(self.frame, text="Account Number", bg="#728B8E", fg="white", font=ARIAL)
        self.uentry = Entry(self.frame, bg="honeydew", highlightcolor="#50A8B0",
                            highlightthickness=2,
                            highlightbackground="white")
        self.plabel = Label(self.frame, text="Password", bg="#728B8E", fg="white", font=ARIAL)
        self.pentry = Entry(self.frame, bg="honeydew", show="*", highlightcolor="#50A8B0",
                            highlightthickness=2,
                            highlightbackground="white")
        self.button = Button(self.frame, text="LOGIN", bg="#50A8B0", fg="white", font=ARIAL, command=self.verify)
        self.q = Button(self.frame, text="Quit", bg="#50A8B0", fg="white", font=ARIAL, command=self.root.destroy)
        self.userlabel.place(x=145, y=100, width=120, height=20)
        self.uentry.place(x=153, y=130, width=200, height=20)
        self.plabel.place(x=125, y=160, width=120, height=20)
        self.pentry.place(x=153, y=190, width=200, height=20)
        self.button.place(x=155, y=230, width=120, height=20)
        self.q.place(x=480, y=360, width=120, height=20)

        self.frame.pack()

    def database_fetch(self):  # Fetching Account data from database
        self.acc_list = []
        self.temp = self.conn.execute("select name,pw,acc_no,bal from account where acc_no = ? ", (self.ac,))
        for i in self.temp:
            self.money = i[3]
            self.acc_list.append("Name = {}".format(i[0]))
            self.acc_list.append("Account no = {}".format(i[2]))
            self.ac = i[2]
            self.acc_list.append("Balance = {}".format(i[3]))

    def verify(self):  # verifying of authorised user
        ac = False
        self.temp = self.conn.execute("select name,pw,acc_no,bal from account where acc_no = ? ",
                                      (int(self.uentry.get()),))
        for i in self.temp:
            self.ac = i[2]
            if i[2] == self.uentry.get():
                ac = True
            elif i[1] == self.pentry.get():
                ac = True
                m = "{} Login SucessFull".format(i[0])
                self.database_fetch()
                messagebox._show("Login Info", m)
                self.frame.destroy()
                self.MainMenu()
            else:
                ac = True
                m = " Login UnSucessFull ! Wrong Password"
                messagebox._show("Login Info!", m)

        if not ac:
            m = " Wrong Acoount Number !"
            messagebox._show("Login Info!", m)

    def MainMenu(self):  # Main App Appears after logined !
        self.frame = Frame(self.root, bg="#728B8E", width=800, height=400)
        root.geometry("800x400")
        self.detail = Button(self.frame, text="Account Details", bg="#50A8B0", fg="white", font=ARIAL,
                             command=self.account_detail)
        self.transfer = Button(self.frame, text="Transfer", bg="#50A8B0", fg="white", font=ARIAL, command=self.transfer)
        self.history = Button(self.frame, text="Historic Records", bg="#50A8B0", fg="white", font=ARIAL,
                              command=self.history)
        self.investment = Button(self.frame, text="Investment", bg="#50A8B0", fg="white", font=ARIAL,
                                 command=self.investment)
        self.enquiry = Button(self.frame, text="Balance Enquiry", bg="#50A8B0", fg="white", font=ARIAL,
                              command=self.Balance)
        self.deposit = Button(self.frame, text="Deposit Money", bg="#50A8B0", fg="white", font=ARIAL,
                              command=self.deposit_money)
        self.withdrawl = Button(self.frame, text="Withdrawl Money", bg="#50A8B0", fg="white", font=ARIAL,
                                command=self.withdrawl_money)
        self.q = Button(self.frame, text="Quit", bg="#50A8B0", fg="white", font=ARIAL, command=self.root.destroy)
        self.detail.place(x=0, y=0, width=200, height=50)
        self.transfer.place(x=0, y=105, width=200, height=50)
        self.history.place(x=0, y=210, width=200, height=50)
        self.investment.place(x=600, y=170, width=200, height=50)
        self.enquiry.place(x=0, y=315, width=200, height=50)
        self.deposit.place(x=600, y=0, width=200, height=50)
        self.withdrawl.place(x=600, y=315, width=200, height=50)
        self.q.place(x=340, y=340, width=120, height=20)
        self.frame.pack()

    def account_detail(self):
        self.database_fetch()
        text = "\n\n\n" + self.acc_list[0] + "\n" + self.acc_list[1] + "\n" + self.acc_list[2]
        self.label = Label(self.frame, text=text, font=ARIAL)
        self.label.place(x=250, y=50, width=300, height=200)

    def Balance(self):
        self.database_fetch()
        self.label = Label(self.frame, text="\n\n" + self.acc_list[2], font=ARIAL)
        self.label.place(x=250, y=50, width=300, height=200)

    def transfer(self):
        self.database_fetch()
        print(self.ac)
        Label(self.frame, text="Target Account:").place(x=250, y=50, width=100, height=20)
        Label(self.frame, text="Transfer Amount:").place(x=250, y=100, width=100, height=20)
        self.target_account = Entry(self.frame, bg="honeydew", highlightcolor="#50A8B0",
                                    highlightthickness=2,
                                    highlightbackground="white")
        self.money_box = Entry(self.frame, bg="honeydew", highlightcolor="#50A8B0",
                               highlightthickness=2,
                               highlightbackground="white")
        self.submitButton = Button(self.frame, text="Submit", bg="#50A8B0", fg="white", font=ARIAL)
        self.target_account.place(x=250, y=70, width=200, height=20)
        self.money_box.place(x=250, y=120, width=200, height=20)
        self.submitButton.place(x=445, y=120, width=55, height=20)
        self.submitButton.bind("<Button-1>", self.transfer_trans)

    def transfer_trans(self, flag):
        if self.money >= int(self.money_box.get()) >= 0:
            self.label = Label(self.frame, text="Transaction Completed !", font=ARIAL)
            self.label.place(x=250, y=50, width=300, height=200)
            self.conn.execute("update account set bal = bal - ? where acc_no = ?", (self.money_box.get(), self.ac))
            self.conn.commit()
            self.conn.execute("INSERT INTO record(f_id,s_id,money,bill_no) VALUES(?,?,?,?)",
                               (self.ac, int(self.target_account.get()), int(self.money_box.get()),
                                str(time.time()).replace(".", "-")))
            self.conn.commit()

        elif int(self.money_box.get()) < 0:
            self.label = Label(self.frame, text="Transaction False!\n The transfer amount should be greater than 0!",
                               font=ARIAL)
            self.label.place(x=250, y=50, width=300, height=200)
        else:
            self.label = Label(self.frame, text="Insufficient Balance!",
                               font=ARIAL)
            self.label.place(x=250, y=50, width=300, height=200)

    def history(self):
        pass

    def investment(self):
        self.database_fetch()
        Label(self.frame, text="financial product:").place(x=320, y=25, width=150, height=20)

        Label(self.frame, text="Investment product:1；time:1.2；money:1000").place(x=250, y=50, width=295, height=20)
        Label(self.frame, text="Investment product:2；time:1.4；money:1200").place(x=250, y=70, width=295, height=20)
        Label(self.frame, text="Investment product:3；time:1.6；money:2500").place(x=250, y=90, width=295, height=20)
        self.money_input1 = Entry(self.frame, bg="honeydew", highlightcolor="#50A8B0",
                                  highlightthickness=2,
                                  highlightbackground="white")
        self.money_input1.place(x=545, y=50, width=55, height=20)
        self.money_input2 = Entry(self.frame, bg="honeydew", highlightcolor="#50A8B0",
                                  highlightthickness=2,
                                  highlightbackground="white")
        self.money_input2.place(x=545, y=70, width=55, height=20)
        self.money_input3 = Entry(self.frame, bg="honeydew", highlightcolor="#50A8B0",
                                  highlightthickness=2,
                                  highlightbackground="white")
        self.money_input3.place(x=545, y=90, width=55, height=20)
        self.submitButton = Button(self.frame, text="Submit", bg="#50A8B0", fg="white", font=ARIAL)
        self.submitButton.place(x=445, y=115, width=55, height=20)
        self.submitButton.bind("<Button-1>", self.investment_trans)  # execute investment_trans

    def investment_trans(self, flag):
        top = Toplevel(width=400, height=400)
        top.title('investment')
        invertment_list = [{'id': 1, 't': 1, 'rate': 1.2, 'money': 1000}, {'id': 2, 't': 2, 'rate': 1.4, 'money': 1200},
                           {'id': 3, 't': 3, 'rate': 1.6, 'money': 2500}]
        terminal = []  # Store of investment product information purchased by users
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
            payment = x * 1000 + s * 1200 + l * 2500  # total price
            if self.money >= payment > 0:
                if x > 0:
                    time = x
                    money_ = 1000 * x
                    terminal.append({'id': 1, 't': time, 'rate': 1.2, 'money': money_})
                elif s > 0:
                    time = s
                    money_ = 1200 * s
                    terminal.append({'id': 2, 't': time, 'rate': 1.4, 'money': money_})
                elif l > 0:
                    time = l
                    money_ = 2500 * l
                    terminal.append({'id': 3, 't': time, 'rate': 1.6, 'money': money_})
                self.label = Label(top, text="Purchase completed!", font=ARIAL)
                self.label.place(x=120, y=80, width=150, height=200)
                self.label = Label(top, text="Investment product you have:", font=ARIAL)
                self.label.place(x=120, y=110, width=150, height=200)

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

                for i in terminal:
                    counter = 0
                    tree.insert("", counter, text="line1",
                                values=(i.get('id'), i.get('t'), i.get('rate'), i.get('money')))  # #给第0行添加数据，索引值可重复
                    counter += 1
                tree.pack()

                self.conn.execute("update account set bal = bal - ? where acc_no = ?", (payment, self.ac))
                self.conn.commit()
            elif self.money <= 0:
                self.label = Label(top, text="There is no balance in your account!", font=ARIAL)
                self.label.place(x=100, y=100, width=240, height=200)
            elif self.money < payment:
                self.label = Label(top, text="Insufficient account balance!", font=ARIAL)
                self.label.place(x=100, y=100, width=200, height=200)
        else:
            self.label = Label(top, text="Incorrect input of investment prduct shares!", font=ARIAL)
            self.label.place(x=100, y=100, width=250, height=200)

    def deposit_money(self):
        self.money_box = Entry(self.frame, bg="honeydew", highlightcolor="#50A8B0",
                               highlightthickness=2,
                               highlightbackground="white")
        self.submitButton = Button(self.frame, text="Submit", bg="#50A8B0", fg="white", font=ARIAL)

        self.money_box.place(x=250, y=100, width=200, height=20)
        self.submitButton.place(x=445, y=100, width=55, height=20)
        self.submitButton.bind("<Button-1>", self.deposit_trans)

    def deposit_trans(self, flag):
        if int(self.money_box.get()) >= 0:
            self.label = Label(self.frame, text="Transaction Completed !", font=ARIAL)
            self.label.place(x=250, y=50, width=300, height=200)
            self.conn.execute("update account set bal = bal + ? where acc_no = ?", (self.money_box.get(), self.ac))
            self.conn.commit()
        else:
            self.label = Label(self.frame, text="Transaction False!\n The deposit amount should be greater than 0",
                               font=ARIAL)
            self.label.place(x=250, y=50, width=300, height=200)

    def withdrawl_money(self):
        self.money_box = Entry(self.frame, bg="honeydew", highlightcolor="#50A8B0",
                               highlightthickness=2,
                               highlightbackground="white")
        self.submitButton = Button(self.frame, text="Submit", bg="#50A8B0", fg="white", font=ARIAL)

        self.money_box.place(x=250, y=100, width=200, height=20)
        self.submitButton.place(x=445, y=100, width=55, height=20)
        self.submitButton.bind("<Button-1>", self.withdrawl_trans)

    def withdrawl_trans(self, flag):
        self.database_fetch()
        if int(self.money_box.get()) < 0:
            self.label = Label(self.frame, text="The withdrawal amount cannot be less than 0!",
                               font=ARIAL)
            self.label.place(x=250, y=50, width=300, height=200)

        elif int(self.money_box.get()) <= self.money:
            self.label = Label(self.frame, text="Money Withdrawl !", font=ARIAL)
            self.label.place(x=250, y=50, width=300, height=200)
            self.conn.execute("update account set bal = bal - ? where acc_no = ?", (self.money_box.get(), self.ac))
            self.conn.commit()

        else:
            self.label = Label(self.frame, text="Insufficient Balance!",
                               font=ARIAL)
            self.label.place(x=250, y=50, width=300, height=200)


root = Tk()
root.title("Sign In")
root.geometry("600x420")
icon = PhotoImage(file="icon.png")
root.tk.call("wm", 'iconphoto', root._w, icon)
obj = Bank(root)
root.mainloop()

'''If you like this project give a star ,,,,,,Thanks !'''
