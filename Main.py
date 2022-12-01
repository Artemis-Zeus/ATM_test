# jeddy 、Sakura、Franklif、Artemis、Xylophone、jyf、recomoonmoon加入
# Bank ATM
# Account Number : 10 ------------ Password : trial

from tkinter import *
from tkinter import messagebox
import sqlite3
import time
from tkinter import ttk

ARIAL = ("arial", 10, "bold")


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
        self.button1 = Button(self.frame, text="REGISITER", bg="#50A8B0", fg="white", font=ARIAL, command=self.regisiter)
        self.button = Button(self.frame, text="LOGIN", bg="#50A8B0", fg="white", font=ARIAL, command=self.verify)
        self.q = Button(self.frame, text="Quit", bg="#50A8B0", fg="white", font=ARIAL, command=self.root.destroy)
        self.userlabel.place(x=145, y=100, width=120, height=20)
        self.uentry.place(x=153, y=130, width=200, height=20)
        self.plabel.place(x=125, y=160, width=120, height=20)
        self.pentry.place(x=153, y=190, width=200, height=20)
        self.button1.place(x=155,y=250,width=120,height=20)
        self.button.place(x=155, y=230, width=120, height=20)
        self.q.place(x=480, y=360, width=120, height=20)

        self.frame.pack()

    def regisiter(self):
        # self.frame = Frame(self.root, bg="#728B8E", width=800, height=400)
        # root.geometry("800x400")
        #self.userlabel = Label(self.frame, text="Account Name", bg="#728B8E", fg="white", font=ARIAL)#这里重构一下文字
        def regisiter1():
            a=self.uentry.get()
            b=self.pentry.get()
            print(a)

            # self.conn.execute("INSERT INTO account (name,acc_no,bal,pw) \
            #              VALUES (?,123,0,? )", (a, b))
            # self.conn.commit()
            # messagebox._show("sucessful")#这里加一个成功提示
        self.button3 = Button(self.frame, text="ok", bg="#50A8B0", fg="white", font=ARIAL, command=regisiter1)
        self.button3.place(x=155, y=230, width=120, height=40)






        # self.frame.pack()

        #self.label=Lable
        # count_name = E1.get()
        # count_password = (E2.get())
        # print(count_name)
        # print(count_password)
        # print(type(count_name))
        # print(type(count_password))
        #
        # conn.execute("INSERT INTO account (name,acc_no,bal,pw) \
        #             VALUES (?,11,0,? )", (count_name, count_password))
        # conn.commit()
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
        root.title("User Interface")
        root.geometry("800x400")

        self.detail = Button(self.frame, text="Account Details", bg="#50A8B0", fg="white", font=ARIAL,
                             command=self.account_detail)
        self.transfer = Button(self.frame, text="Transfer", bg="#50A8B0", fg="white", font=ARIAL, command=self.transfer)

        self.investment = Button(self.frame, text="Investment", bg="#50A8B0", fg="white", font=ARIAL,
                                 command=self.investment)
        self.enquiry = Button(self.frame, text="Balance Enquiry", bg="#50A8B0", fg="white", font=ARIAL,
                              command=self.Balance)
        self.deposit = Button(self.frame, text="Deposit Money", bg="#50A8B0", fg="white", font=ARIAL,
                              command=self.deposit_money)
        self.withdrawl = Button(self.frame, text="Withdraw Money", bg="#50A8B0", fg="white", font=ARIAL,
                                command=self.withdraw_money)
        self.history_button = Button(self.frame, text="CHECK RECORDS", bg="#50A8B0", fg="white", font=ARIAL,
                                     command=self.history)
        self.q = Button(self.frame, text="Quit", bg="#50A8B0", fg="white", font=ARIAL, command=self.root.destroy)

        self.detail.place(x=0, y=0, width=200, height=50)
        self.transfer.place(x=0, y=105, width=200, height=50)
        self.history_button.place(x=0, y=210, width=200, height=50)
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
        self.label.place(x=220, y=50, width=360, height=200)

    def Balance(self):
        self.database_fetch()
        self.label = Label(self.frame, text="\n\n" + self.acc_list[2], font=ARIAL)
        self.label.place(x=220, y=50, width=360, height=200)

    def transfer(self):
        self.database_fetch()
        print(self.ac)
        self.label = Label(self.frame)
        self.label.place(x=220, y=50, width=360, height=200)
        Label(self.frame, text="Target Account:", font=ARIAL).place(x=220, y=70, width=360, height=20)
        Label(self.frame, text="Transfer Amount:", font=ARIAL).place(x=220, y=130, width=360, height=20)
        self.target_account = Entry(self.frame, bg="honeydew", highlightcolor="#50A8B0",
                                    highlightthickness=2,
                                    highlightbackground="white")
        self.money_box = Entry(self.frame, bg="honeydew", highlightcolor="#50A8B0",
                               highlightthickness=2,
                               highlightbackground="white")
        self.submitButton = Button(self.frame, text="Submit", bg="#50A8B0", fg="white", font=ARIAL)
        self.target_account.place(x=300, y=90, width=200, height=20)
        self.money_box.place(x=300, y=150, width=200, height=20)
        self.submitButton.place(x=360, y=200, width=80, height=20)
        self.submitButton.bind("<Button-1>", self.transfer_trans)

    def transfer_trans(self, flag):
        if self.money >= int(self.money_box.get()) >= 0:
            self.label = Label(self.frame, text="Transaction Completed !", font=ARIAL)
            self.label.place(x=220, y=50, width=360, height=200)
            self.conn.execute("update account set bal = bal - ? where acc_no = ?", (self.money_box.get(), self.ac))
            self.conn.commit()
            self.conn.execute("INSERT INTO record(f_id,s_id,money,bill_no) VALUES(?,?,?,?)",
                              (self.ac, int(self.target_account.get()), int(self.money_box.get()),
                               str(time.time()).replace(".", "-")))
            self.conn.commit()

        elif int(self.money_box.get()) < 0:
            self.label = Label(self.frame, text="Transaction False!\n The transfer amount should be greater than 0!",
                               font=ARIAL)
            self.label.place(x=220, y=50, width=360, height=200)
        else:
            self.label = Label(self.frame, text="Insufficient Balance!",
                               font=ARIAL)
            self.label.place(x=220, y=50, width=360, height=200)

    def history(self):
        self.database_fetch()
        c = self.conn.cursor()
        c.execute("select * from record where f_id={} OR s_id={}".format(self.ac, self.ac))
        output = c.fetchall()
        heads = ["f_id", "s_id", 'money', 'type', 'withdraw']
        self.tree = ttk.Treeview(self.frame, show='headings')
        self.tree["columns"] = ("f_id", "s_id", 'money', 'type', 'bill_no')  # #定义列
        self.tree.column("f_id", width=40)  # #设置列
        self.tree.column("s_id", width=50)
        self.tree.column('money', width=60)
        self.tree.column("type", width=80)
        self.tree.column("bill_no", width=130)
        self.tree.heading("f_id", text="Send.")  # #设置显示的表头名
        self.tree.heading("s_id", text="Rec.")  # Recipient
        self.tree.heading("money", text="Amount")
        self.tree.heading("type", text="Type")
        self.tree.heading("bill_no", text="Bill No.")
        for i in range(len(output)):
            self.tree.insert("", i, text=" ", values=output[i])
        self.tree.place(x=220, y=50, width=360, height=200)

    def investment(self):
        pass

    def deposit_money(self):
        temp=self.withdraw_deposit()
        temp.bind("<Button-1>", self.deposit_trans)

    def deposit_trans(self, flag):
        if int(self.money_box.get()) >= 0:
            self.label = Label(self.frame)
            self.label.place(x=220, y=50, width=360, height=200)
            self.label = Label(self.frame, text="Transaction Completed !", font=ARIAL)
            self.label.place(x=220, y=50, width=360, height=200)
            self.conn.execute("update account set bal = bal + ? where acc_no = ?", (self.money_box.get(), self.ac))
            self.conn.execute("INSERT INTO record(f_id,  money, type, bill_no) VALUES(?,?,?,?)", (self.ac, self.money_box.get(), "Withdraw",str(time.time()).replace(".", "-")))
            self.conn.commit()
        else:
            self.label = Label(self.frame, text="Transaction False!\n The deposit amount should be greater than 0",
                               font=ARIAL)
            self.label.place(x=220, y=50, width=360, height=200)

    def withdraw_deposit(self):
        self.money_box = Entry(self.frame, bg="honeydew", highlightcolor="#50A8B0",
                               highlightthickness=2,
                               highlightbackground="white")
        self.submitButton = Button(self.frame, text="Submit", bg="#50A8B0", fg="white", font=ARIAL)

        self.money_box.place(x=220, y=100, width=200, height=20)
        self.submitButton.place(x=420, y=100, width=55, height=20)
        return self.submitButton

    def withdraw_money(self):
        temp=self.withdraw_deposit()
        temp.bind("<Button-1>", self.withdraw_trans)

    def withdraw_trans(self, flag):
        self.label = Label(self.frame)
        self.label.place(x=220, y=50, width=360, height=200)
        self.database_fetch()
        if int(self.money_box.get()) < 0:
            self.label = Label(self.frame, text="The withdrawal amount cannot be less than 0!",
                               font=ARIAL)
            self.label.place(x=220, y=70, width=360, height=200)

        elif int(self.money_box.get()) <= self.money:
            self.label = Label(self.frame, text="Money Withdrawl !", font=ARIAL)
            self.label.place(x=220, y=70, width=360, height=200)
            self.conn.execute("update account set bal = bal - ? where acc_no = ?", (self.money_box.get(), self.ac))
            self.conn.execute("INSERT INTO record(f_id,  money, type, bill_no) VALUES(?,?,?,?)", (self.ac, self.money_box.get(), "Withdraw",str(time.time()).replace(".", "-")))
            self.conn.commit()

        else:
            self.label = Label(self.frame, text="Insufficient Balance!",
                               font=ARIAL)
            self.label.place(x=220, y=70, width=360, height=200)


root = Tk()
root.title("Sign In")
root.geometry("600x420")
icon = PhotoImage(file="icon.png")
root.tk.call("wm", 'iconphoto', root._w, icon)
obj = Bank(root)
root.mainloop()
