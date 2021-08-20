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

class Dealer_page:
    def __init__(self,master,*args,**kwargs):
        self.master=master
        self.heading=Label(master,text="DEALERS",font=('arial 40 bold'),fg='steelblue',bg='powderblue')
        self.heading.place(x=600,y=0)

        #labels and entries for the window
        self.dname_1 = Label(master, text="Enter Dealer's name", font=('arial 18 bold'))
        self.dname_1.place(x=0, y=100)

        self.D_ID_1 = Label(master, text="Enter Dealer's ID", font=('arial 18 bold'))
        self.D_ID_1.place(x=0, y=150)

        self.D_phno_1 = Label(master, text="Enter Dealer's phone number", font=('arial 18 bold'))
        self.D_phno_1.place(x=0, y=200)

        self.D_add_1 = Label(master, text="Enter Dealer's address", font=('arial 18 bold'))
        self.D_add_1.place(x=0, y=250)

        #entry boxes for labels
        self.Dname_e = Entry(master, width=30, font=('arial 18 bold'))
        self.Dname_e.place(x=360, y=100)

        self.D_ID_e = Entry(master, width=30, font=('arial 18 bold'))
        self.D_ID_e.place(x=360, y=150)

        self.D_phno_e = Entry(master, width=30, font=('arial 18 bold'))
        self.D_phno_e.place(x=360, y=200)

        self.D_add_e = Entry(master, width=30, font=('arial 18 bold'))
        self.D_add_e.place(x=360, y=250)


        # button to search by name
        self.btn_D_srcname = Button(master, text="Search", font=('arail 13 bold'), width=10, height=1, bg="steelblue",fg='white',command=self.search_name)
        self.btn_D_srcname.place(x=1220, y=60)

        # button to clear
        self.btn_clear = Button(master, text="Clear all fields", font=('arial 13 bold'), width=18, height=2,bg="steelblue", fg='white',command=self.clear_all)
        self.btn_clear.place(x=360, y=300)

        #button to add to dealer list
        self.btn_D_addtolist = Button(master, text="Add to list", font=('arail 13 bold'), width=18, height=2, bg="steelblue",fg='white',command=self.add_dealer)
        self.btn_D_addtolist.place(x=562, y=300)

        #button to show all dealers
        self.btn_D_list = Button(master, text="View list of dealers", font=('arail 13 bold'), width=18, height=2,bg="steelblue", fg='white',command=self.dealer_list)
        self.btn_D_list.place(x=532, y=690)

        #adding textbox
        self.tBox = scrolledtext.ScrolledText(master, width=70, height=40)
        self.tBox.place(x=770, y=100)

    #function to clear entry boxes
    def clear_all(self, *args, **kwargs):
        self.Dname_e.delete(0, END)
        self.D_ID_e.delete(0, END)
        self.D_phno_e.delete(0, END)
        self.D_add_e.delete(0, END)

    #function for displaying dealer list
    def dealer_list(self,*args,**kwargs):
        win=Tk()
        frm=Frame(win)
        win.title("LIST OF DEALERS")

        frm.pack(side=tkinter.LEFT,padx=10)
        tv=ttk.Treeview(frm,columns=(1,2,3,4),show="headings",height=25)
        tv.pack()
        tv.heading(1,text="DEALER'S ID")
        tv.column(1,minwidth=0,width=150)
        tv.heading(2, text="DEALER'S NAME")
        tv.column(2, minwidth=0, width=150)
        tv.heading(3, text="DEALER'S PHNO.")
        tv.column(3, minwidth=0, width=150)
        tv.heading(4, text="DEALER'S ADDRESS")
        tv.column(4, minwidth=0, width=150)
        sql="SELECT* FROM dealer"
        c.execute(sql)
        rows=c.fetchall()
        for x in rows:
            tv.insert('','end',values=(x[0],x[1],x[2],x[3]))

    #function to add new dealer
    def add_dealer(self, *args, **kwargs):
        # get from entry box
        self.Dname = self.Dname_e.get()
        self.D_ID = self.D_ID_e.get()
        self.D_phno = self.D_phno_e.get()
        self.D_add = self.D_add_e.get()

        if (
                self.Dname == '' or self.D_phno == '' or self.D_add == ''):
            tkinter.messagebox.showinfo("Error", "Please fill all entries")
        else:
            print("GG")
            q = "SELECT* FROM dealer WHERE D_name=%s AND D_phno=%s AND D_add=%s"  # start of comment
            c.execute(q, (self.Dname, self.D_phno,self.D_add))
            data = "error"
            for i in c:
                data = i
            if (data == "error"):
                print("DNE")
                q = """INSERT INTO dealer(D_name,D_phno,D_add) VALUES(%s,%s,%s)"""
                c.execute(q, (self.Dname, self.D_phno, self.D_add))
                mydb.commit()
                tkinter.messagebox.showinfo("Success", "New Dealer added")

            else:
                print("present")  # end of comment
                tkinter.messagebox.showinfo("ERROR","Dealer already in database")

    #search dealer by name
    def search_name(self,*args,**kwargs):
        self.tBox.config(state="normal")
        self.tBox.delete(1.0, END)
        self.Dname=self.Dname_e.get()
        self.D_ID=self.D_ID_e.get()
        self.D_phno=self.D_phno_e.get()
        self.D_add = self.D_add_e.get()
        sql = "SELECT* FROM dealer WHERE D_name=%s OR D_ID=%s OR D_phno=%s OR D_add=%s"
        c.execute(sql,(self.Dname,self.D_ID,self.D_phno,self.D_add))
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
b=Dealer_page(root)
root.geometry("1366x768+0+0")
root.title("DEALER")
root.mainloop()