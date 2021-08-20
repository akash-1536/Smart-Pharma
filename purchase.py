from tkinter import*
import mysql.connector
import tkinter.messagebox
from tkinter import ttk
import tkinter.scrolledtext as scrolledtext
mydb=mysql.connector.connect(
    host="localhost",
    user="root",
    passwd="password123",
    database="pharmacy"
)
c=mydb.cursor()
#c.execute("CREATE DATABASE pharmacy")
#c.execute("CREATE TABLE dealer(D_ID int NOT NULL PRIMARY KEY AUTO_INCREMENT,D_name VARCHAR(100) NOT NULL,D_phno INTEGER(10) NOT NULL,D_add VARCHAR(255))")
#c.execute("CREATE TABLE inventory(Prod_name VARCHAR(100),DOE DATE NOT NULL,Prod_ID int,Qty int NOT NULL,CostPrice int NOT NULL,SellingPrice int NOT NULL,PRIMARY KEY(Prod_name,DOE))")
#c.execute("CREATE TABLE expired_inventory(Prod_name VARCHAR(100),DOE DATE NOT NULL,Prod_ID int,Qty int NOT NULL,CostPrice int NOT NULL,SellingPrice int NOT NULL,PRIMARY KEY(Prod_name,DOE))")
#c.execute("CREATE TABLE sales(S_ID int NOT NULL PRIMARY KEY AUTO_INCREMENT,S_date DATE NOT NULL,Cust_Fname VARCHAR(50),Cust_Lname VARCHAR(50),Prod_name VARCHAR(100),Qty int NOT NULL,U_price int,T_price int,DOE DATE NOT NULL,FOREIGN KEY(DOE,Prod_name) REFERENCES inventory(DOE,Prod_name))")
#c.execute("CREATE TABLE purchase(P_ID int NOT NULL PRIMARY KEY AUTO_INCREMENT,Prod_name VARCHAR(100),Prod_ID int,D_ID int NOT NULL,D_NAME VARCHAR(100),Qty int,CostPrice int,DOE DATE NOT NULL,DOP DATE NOT NULL,FOREIGN KEY(Prod_name,DOE)REFERENCES inventory(Prod_name,DOE),FOREIGN KEY (D_ID) references dealer(D_ID))")
#c.execute("SHOW TABLES")
#for tb in c:
#    print(tb)
c.execute("SELECT MAX(D_ID) from dealer")
for r in c:
    id=r[0]

class purchase_page:
    def __init__(self,master,*args,**kwargs):

        self.master=master
        self.heading=Label(master,text="PURCHASE",font=('arial 40 bold'),fg='steelblue')
        self.heading.place(x=500,y=0)

        #labels and entries for window
        self.name_1=Label(master,text="Enter product name",font=('arial 18 bold'))
        self.name_1.place(x=0,y=70)

        self.prod_ID_1 = Label(master, text="Enter product ID", font=('arial 18 bold'))
        self.prod_ID_1.place(x=0, y=120)

        self.qty_1=Label(master,text="Enter quantity",font=('arial 18 bold'))
        self.qty_1.place(x=0,y=170)

        self.D_ID_1 = Label(master, text="Enter Dealer ID", font=('arial 18 bold'))
        self.D_ID_1.place(x=0, y=220)

        self.D_name_1 = Label(master, text="Enter Dealer name", font=('arial 18 bold'))
        self.D_name_1.place(x=0, y=270)

        self.CP_1 = Label(master, text="Enter cost price per unit", font=('arial 18 bold'))
        self.CP_1.place(x=0, y=320)

        self.DOE_1 = Label(master, text="Date of expiry", font=('arial 18 bold'))
        self.DOE_1.place(x=0, y=370)

        self.DOP_1 = Label(master, text="Date of purchase", font=('arial 18 bold'))
        self.DOP_1.place(x=0, y=420)

        #entry box for labels
        self.name_e=Entry(master,width=30,font=('arial 18 bold'))
        self.name_e.place(x=330,y=70)

        self.prod_ID_e = Entry(master, width=30, font=('arial 18 bold'))
        self.prod_ID_e.place(x=330, y=120)

        self.qty_e = Entry(master, width=30, font=('arial 18 bold'))
        self.qty_e.place(x=330, y=170)

        self.D_ID_e = Entry(master, width=21, font=('arial 18 bold'))
        self.D_ID_e.place(x=330, y=220)

        self.D_name_e = Entry(master, width=30, font=('arial 18 bold'))
        self.D_name_e.place(x=330, y=270)

        self.CP_e = Entry(master, width=30, font=('arial 18 bold'))
        self.CP_e.place(x=330, y=320)

        self.DOE_e = Entry(master, width=30, font=('arial 18 bold'))
        self.DOE_e.place(x=330, y=370)

        self.DOP_e = Entry(master, width=30, font=('arial 18 bold'))
        self.DOP_e.place(x=330, y=420)

        #button to add
        self.btn_add=Button(master,text="Add to inventory",font=('arial 13 bold'),width=18,height=2,bg="steelblue",fg='white',command=self.get_items)
        self.btn_add.place(x=532,y=470)

        #button to clear
        self.btn_clear=Button(master,text="Clear all fields",font=('arial 13 bold'),width=18,height=2,bg="steelblue",fg='white',command=self.clear_all)
        self.btn_clear.place(x=330,y=470)

        #button to show purchase history
        self.btn_p_history=Button(master,text="View purchase history",font=('arail 13 bold'),width=18,height=2,bg="steelblue",fg='white',command=self.purc_history)
        self.btn_p_history.place(x=532,y=700)

        #button for searcing dealer ID
        self.btn_D_ID=Button(master,text="Search",font=('arail 13 bold'),width=10,height=1,bg="steelblue",fg='white',command=self.search_dealer)
        self.btn_D_ID.place(x=616,y=220)

        #add text box
        self.tBox=scrolledtext.ScrolledText(master,width=70,height=42)
        self.tBox.place(x=770, y=70)
        #scroll=Scrollbar(self,command=self.tBox.yview)
        #scroll.place(x=840,y=71,sticky="nsew")
        #self.tBox['yscrollcommand']=scroll.set

        self.tBox.insert(END,"You have "+str(id)+" dealers\n\n")

        sql = "SELECT* FROM dealer"
        c.execute(sql)
        rows = c.fetchall()
        self.tBox.insert(END,"  DEALER ID  |   DEALER NAME   | DEALER PHONE NO | DEALER ADDRESS \n")
        for x in rows:
            fx1=str(x[0])
            fx2 = str(x[1])
            fx3 = str(x[2])
            fx4 = str(x[3])
            self.tBox.insert(END,("   "+fx1+" "*(10-len(fx1))+"| "+fx2+" "*(16-len(fx2))+"| "+fx3+" "*(16-len(fx3))+"| "+fx4))
            self.tBox.insert(END,"\n")
        self.tBox.config(state="disabled")

    def get_items(self,*args,**kwargs):
       #get from entry box
        self.name=self.name_e.get()
        self.qty=self.qty_e.get()
        self.prod_ID=self.prod_ID_e.get()
        self.D_ID=self.D_ID_e.get()
        self.D_name=self.D_name_e.get()
        self.CP=self.CP_e.get()
        self.DOE=self.DOE_e.get()
        self.DOP=self.DOP_e.get()

        if(self.name==''or self.qty==''or self.prod_ID==''or self.D_ID=='' or self.D_name=='' or self.CP=='' or self.DOE=='' or self.DOP==''):
            tkinter.messagebox.showinfo("Error","Please fill all entries")
        else:
            print("GG")
            q="SELECT* FROM inventory WHERE Prod_name=%s AND DOE=%s"#start of comment
            c.execute(q,(self.name,self.DOE))
            data="error"
            for i in c:
                data=i
            if(data=="error"):
                print("DNE")
                self.SP = float(self.CP) * 1.1
                q = """INSERT INTO inventory(Prod_name,DOE,Prod_ID,Qty,CostPrice,SellingPrice) VALUES(%s,%s,%s,%s,%s,%s)"""
                c.execute(q, (self.name, self.DOE, self.prod_ID, self.qty, self.CP, self.SP))
            else:
                print("present")#end of comment
                ini = "SELECT* FROM inventory WHERE Prod_name=%s AND DOE=%s"
                c.execute(ini,(self.name,self.DOE))
                for r in c:
                    self.old_qty=r[3]
                    self.new_qty=int(self.old_qty)+int(self.qty)
                    sql="UPDATE inventory SET Qty=%s WHERE Prod_name=%s AND DOE=%s"
                    c.execute(sql,(self.new_qty,self.name,self.DOE))

            # REMOVE DEALER INSERTION ONCE DEALER WINDOW HAS BEEN MADE
           # d="""INSERT INTO DEALER(D_name,D_phno,D_add) VALUES(%s,%s,%s)"""
           # c.execute(d,('ABC','8291701407','Mumbai'))
            sql = """INSERT INTO purchase(Prod_name,Prod_ID,D_ID,D_NAME,Qty,CostPrice,DOE,DOP) VALUES(%s,%s,%s,%s,%s,%s,%s,%s)"""
            c.execute(sql, (self.name, self.prod_ID, self.D_ID, self.D_name, self.qty, self.CP, self.DOE, self.DOP))
            mydb.commit()
            tkinter.messagebox.showinfo("Success","Successfully added to inventory")


    #function for clear entries button
    def clear_all(self,*args,**kwargs):
        #num=id+1
        self.name_e.delete(0,END)
        self.qty_e.delete(0,END)
        self.CP_e.delete(0,END)
        self.prod_ID_e.delete(0,END)
        self.D_name_e.delete(0,END)
        self.D_ID_e.delete(0,END)
        self.DOP_e.delete(0,END)
        self.DOE_e.delete(0,END)

    #function for purchase history button
    def purc_history(self,*args,**kwargs):
        win=Tk()
        frm=Frame(win)
        win.title("PURCHASE HISTORY")

        frm.pack(side=tkinter.LEFT,padx=10)
        tv=ttk.Treeview(frm,columns=(1,2,3,4,5,6,7,8),show="headings",height=25)
        tv.pack()
        tv.heading(1,text="Purchase ID")
        tv.column(1,minwidth=0,width=150)
        tv.heading(2, text="Product Name")
        tv.column(2, minwidth=0, width=150)
        tv.heading(3, text="Quantity")
        tv.column(3, minwidth=0, width=150)
        tv.heading(4, text="Dealer Name")
        tv.column(4, minwidth=0, width=150)
        tv.heading(5, text="Dealer ID")
        tv.column(5, minwidth=0, width=150)
        tv.heading(6, text="Cost Price")
        tv.column(6, minwidth=0, width=150)
        tv.heading(7, text="Date Of Expiry")
        tv.column(7, minwidth=0, width=150)
        tv.heading(8, text="Date Of Purchase")
        tv.column(8, minwidth=0, width=150)
        sql="SELECT P_ID,Prod_name,Qty,D_name,D_ID,CostPrice,DOE,DOP FROM purchase"
        c.execute(sql)
        rows=c.fetchall()
        for x in rows:
            tv.insert('','end',values=(x[0],x[1],x[2],x[3],x[4],x[5],x[6],x[7]))

    #function to search dealer
    def search_dealer(self,*args,**kwargs):
        self.tBox.config(state="normal")
        self.tBox.delete(1.0, END)
        self.Dname=self.D_name_e.get()
        self.D_ID=self.D_ID_e.get()
        sql = "SELECT* FROM dealer WHERE D_name=%s OR D_ID=%s"
        c.execute(sql,(self.Dname,self.D_ID))
        rows = c.fetchall()
        self.tBox.insert(END,"  DEALER ID  |   DEALER NAME   | DEALER PHONE NO | DEALER ADDRESS \n")
        for x in rows:
            fx1=str(x[0])
            fx2 = str(x[1])
            fx3 = str(x[2])
            fx4 = str(x[3])
            self.tBox.insert(END,("   "+fx1+" "*(10-len(fx1))+"| "+fx2+" "*(16-len(fx2))+"| "+fx3+" "*(16-len(fx3))+"| "+fx4))
            self.tBox.insert(END,"\n")
        self.tBox.config(state="disabled")


root=Tk()
fr=Frame(root)
b=purchase_page(root)
root.geometry("1366x768+0+0")
root.title("PURCHASE")
root.mainloop()