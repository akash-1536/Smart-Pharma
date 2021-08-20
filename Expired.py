import mysql.connector
from tkinter import *
from datetime import date
import tkinter.messagebox
from tkinter import ttk
import tkinter.scrolledtext as scrolledtext
import random

mydb=mysql.connector.connect(
    host="localhost",
    user="root",
    passwd="password123",
    database="pharmacy"
)
# print(mydb.connection_id)
c = mydb.cursor()
"""

# dealer table
c.execute(
    "CREATE TABLE dealer(D_ID int NOT NULL PRIMARY KEY AUTO_INCREMENT,D_name VARCHAR(100) NOT NULL,D_phno VARCHAR(50) NOT NULL,D_add VARCHAR(255))")

# inventory
c.execute(
    "CREATE TABLE inventory(Prod_name VARCHAR(100),DOE DATE NOT NULL,Prod_ID int,Qty int NOT NULL,CostPrice int NOT NULL,SellingPrice int NOT NULL,PRIMARY KEY(Prod_name,DOE))")

# expired_inventory
c.execute(
    "CREATE TABLE expired_inventory(Prod_name VARCHAR(100),DOE DATE NOT NULL,Prod_ID int,Qty int NOT NULL,CostPrice int NOT NULL,SellingPrice int NOT NULL,PRIMARY KEY(Prod_name,DOE))")

# sales TABLE
c.execute(
    "CREATE TABLE sales(S_ID int NOT NULL PRIMARY KEY AUTO_INCREMENT,S_date DATE NOT NULL,Cust_Fname VARCHAR(50),Cust_Lname VARCHAR(50),Prod_name VARCHAR(100),Qty int NOT NULL,U_price int,T_price int,DOE DATE NOT NULL)")

# purchase TABLE
c.execute(
    "CREATE TABLE purchase(P_ID int NOT NULL PRIMARY KEY AUTO_INCREMENT,Prod_name VARCHAR(100),Prod_ID int,D_ID int NOT NULL,D_NAME VARCHAR(100),Qty int,CostPrice int,DOE DATE NOT NULL,DOP DATE NOT NULL)")
"""

class Database:
    def __init__(self, master, *args, **kwargs):
        self.master = master

        self.heading = Label(master, text="EXPIRED INVENTORY", font=('arial 40 bold'), fg=('steelblue'))
        self.heading.place(x=430, y=0)

        # lables
        self.name_l = Label(master,text="Enter product Name",font=('arial 18 bold'))
        self.name_l.place(x=0,y=70)

        self.doe = Label(master, text="Enter DOE", font=('arial 18 bold'))
        self.doe.place(x=0, y=120)

        self.p_id = Label(master, text="Enter Product ID", font=('arial 18 bold'))
        self.p_id.place(x=0, y=170)

        self.qty = Label(master, text="Enter Quantity", font=('arial 18 bold'))
        self.qty.place(x=0, y=220)

        self.cp = Label(master, text="Enter Cost Price", font=('arial 18 bold'))
        self.cp.place(x=0, y=270)

        self.sp = Label(master, text="Enter Selling Price", font=('arial 18 bold'))
        self.sp.place(x=0, y=320)


        # entries for lables
        self.name_e= Entry(master, width=25, font=('arial 18 bold'))
        self.name_e.place(x=250, y=70)

        self.doe_e = Entry(master, width=25, font=('arial 18 bold'))
        self.doe_e.place(x=250, y=120)

        self.pid_e = Entry(master, width=25, font=('arial 18 bold'))
        self.pid_e.place(x=250, y=170)

        self.qty_e = Entry(master, width=25, font=('arial 18 bold'))
        self.qty_e.place(x=250, y=220)

        self.cp_e = Entry(master, width=25, font=('arial 18 bold'))
        self.cp_e.place(x=250, y=270)

        self.sp_e = Entry(master, width=25, font=('arial 18 bold'))
        self.sp_e.place(x=250, y=320)

        # button for search
        self.btn_add = Button(master,text="Search", width=25, height=2, bg="steelblue", fg="white",
                              command=self.search_row)

        self.btn_add.place(x=250,y=370)

        # button to view expired inventory
        self.btn_view = Button(master, text="VIEW THE EXPIRED INVENTORY", width=30, height=2, bg="red", fg="white", command=self.EXPIRED_LIST)
        self.btn_view.place(x=250, y=420)
        self.tBox = scrolledtext.ScrolledText(master, width=70, height=40)
        self.tBox.place(x=590, y=70)

        # button to view inventory
        self.btn_view = Button(master, text="VIEW THE INVENTORY", width=30, height=2, bg="lightgreen", fg="white",
                               command=self.inventory_list)
        self.btn_view.place(x=250, y=470)
        self.tBox = scrolledtext.ScrolledText(master, width=70, height=40)
        self.tBox.place(x=590, y=70)
        # scrolled box on the right


        """
        self.doe_l = Label(master, text="View expired items", font=('arial 18 bold'))
        self.doe_l.place(x=0, y=500)

        self.btn_add = Button(master, text="Search", width=25, height=2, bg="red", fg="white",command=self.date_check)

        self.btn_add.place(x=250, y=500) 



    Date check
    def date_check(self,*args, **kwargs):
        tdy = date.today()
        c.execute("SELECT * FROM inventory WHERE DOE < '%s'" % (tdy,))
        result = c.fetchall()
        self.tBox.insert(END, "   PRODUCT NAME  |     DOE     | PRODUCT ID |  QTY  |   CP    | SP  \n")
        for x in result:
            fx1 = str(x[0])  # to access values of eac h column
            fx2 = str(x[1])
            fx3 = str(x[2])
            fx4 = str(x[3])
            fx5 = str(x[4])
            fx6 = str(x[5])
            self.tBox.insert(END, (
                    "   " + fx1 + " " * (17 - len(fx1)) + "| " + fx2 + " " * (13 - len(fx2)) + "| " + fx3 + " " * (
                    12 - len(fx3)) + "| " + fx4 + " " * (10 - len(fx4)) + "| " + fx5 + " " * (
                                10 - len(fx5)) + "| " + fx6 + " " * (10 - len(fx6)) + "| "))

            self.tBox.insert(END, "\n")
        self.tBox.config(state="disabled")"""

    def search_row(self, *args, **kwargs):
        self.tBox.config(state= "normal")
        self.tBox.delete(1.0, END)
        self.name = self.name_e.get()
        self.Doe = self.doe_e.get()
        self.pid = self.pid_e.get()
        self.qty_f = self.qty_e.get()
        self.c=self.cp_e.get()
        self.s=self.sp_e.get()
        if(self.Doe!=''):
            sql = "SELECT* FROM expired_inventory where Prod_name=%s OR DOE=%s OR Prod_ID=%s OR Qty=%s OR CostPrice=%s OR SellingPrice=%s "
            c.execute(sql, (self.name, self.Doe, self.pid, self.qty_f, self.c, self.s))
            rows = c.fetchall()
        if (self.Doe == ''):
            sql = "SELECT* FROM expired_inventory where Prod_name=%s OR Prod_ID=%s OR Qty=%s OR CostPrice=%s OR SellingPrice=%s "
            c.execute(sql, (self.name, self.pid, self.qty_f, self.c, self.s))
            rows = c.fetchall()

        self.tBox.insert(END, "   PRODUCT NAME  |     DOE     | PRODUCT ID |  QTY  |   CP    | SP  \n")
        for x in rows:
            fx1 = str(x[0])  # to access values of eac h column
            fx2 = str(x[1])
            fx3 = str(x[2])
            fx4 = str(x[3])
            fx5 = str(x[4])
            fx6 = str(x[5])
            self.tBox.insert(END, (
                        "   " + fx1 + " " * (17 - len(fx1)) + "| " + fx2 + " " * (13 - len(fx2)) + "| " + fx3 + " " * (
                            12 - len(fx3)) + "| " + fx4 + " " * (10 - len(fx4)) + "| " + fx5 + " " * (10 - len(fx5)) + "| " + fx6 + " " * (10 - len(fx6)) + "| "))

            self.tBox.insert(END, "\n")
        self.tBox.config(state="disabled")

    # function to view the items in the inventory
    def EXPIRED_LIST(self,*args,**kwargs):
        win=Tk()
        frm=Frame(win)
        win.title("LIST OF ITEMS IN EXPIRED INVENTORY")
        frm.pack(side=tkinter.LEFT,padx=10)
        tv=ttk.Treeview(frm,columns=(1,2,3,4,5,6) , show="headings",height=25)
        tv.pack()
        tv.heading(1,text="PRODUCT NAME")
        tv.column(1,minwidth=0,width=150)

        tv.heading(2, text="DOE")
        tv.column(2, minwidth=0, width=150)

        tv.heading(3, text="PRODUCT ID")
        tv.column(3, minwidth=0, width=150)

        tv.heading(4, text="QTY")
        tv.column(4, minwidth=0, width=150)

        tv.heading(5, text="COST PRICE")
        tv.column(5, minwidth=0, width=150)

        tv.heading(6, text="SELLING PRICE")
        tv.column(6, minwidth=0, width=150)


        tdy = date.today()
        c.execute("SELECT * FROM inventory WHERE DOE < '%s'" % (tdy,))
        result = c.fetchall()
        for x in result:
            fx1 = str(x[0])  # to access values of eac h column
            fx2 = str(x[1])
            fx3 = str(x[2])
            fx4 = str(x[3])
            fx5 = str(x[4])
            fx6 = str(x[5])
            tv.insert('', 'end', values=(x[0], x[1], x[2], x[3], x[4], x[5]))
        c.execute("DELETE FROM inventory WHERE DOE < '%s'" % (tdy,))
        mydb.commit()
        for x in result:
            fx1 = str(x[0])  # to access values of each column
            fx2 = str(x[1])
            fx3 = str(x[2])
            fx4 = str(x[3])
            fx5 = str(x[4])
            fx6 = str(x[5])
            s = "INSERT INTO expired_inventory (Prod_name, DOE, Prod_ID, Qty, CostPrice, SellingPrice) VALUES(%s, %s, %s, %s, %s, %s)	"
            c.execute(s,(fx1,fx2,fx3,fx4,fx5,fx6))
            mydb.commit()


    # inventory

    def inventory_list(self,*args,**kwargs):
        win=Tk()
        frm=Frame(win)
        win.title("LIST OF ITEMS IN INVENTORY")
        frm.pack(side=tkinter.LEFT,padx=10)
        tv=ttk.Treeview(frm,columns=(1,2,3,4,5,6) , show="headings",height=25)
        tv.pack()
        tv.heading(1,text="PRODUCT NAME")
        tv.column(1,minwidth=0,width=150)

        tv.heading(2, text="DOE")
        tv.column(2, minwidth=0, width=150)

        tv.heading(3, text="PRODUCT ID")
        tv.column(3, minwidth=0, width=150)

        tv.heading(4, text="QTY")
        tv.column(4, minwidth=0, width=150)

        tv.heading(5, text="COST PRICE")
        tv.column(5, minwidth=0, width=150)

        tv.heading(6, text="SELLING PRICE")
        tv.column(6, minwidth=0, width=150)

        sql = "select* from inventory"
        c.execute(sql)
        rows = c.fetchall()
        for x in rows:
            tv.insert('', 'end', values=(x[0], x[1], x[2], x[3], x[4], x[5]))

root =  Tk()
b = Database(root)
root.geometry("1336x768+0+0")
root.title("Inventory")
root.mainloop()
