import mysql.connector
from tkinter import *
import datetime
import tkinter.messagebox as Messagebox
import os

#Enter your password
mydb=mysql.connector.connect(
    host="localhost",
    user="root",
    passwd="password123",
    database="pharmacy"
)

c=mydb.cursor()

d=datetime.datetime.now()
dat=datetime.datetime.now().date()

prod_list=[]
prod_price=[]
prod_quan=[]
prod_dic={}

inq=[]
bc=[]

class Sales:
    def __init__(self,master,*args):
        self.master=master
        
        self.left=Frame(master,width=800,bg='white',height=768)
        self.left.pack(side=LEFT)
        
        self.right=Frame(master,width=566,bg='lightblue',height=768)
        self.right.pack(side=LEFT)
        
        self.header=Label(self.left,text="COVID-19 Relief Pharmacy",font=('arial 40 bold'),bg='white',fg='steelblue')
        self.header.place(x=50,y=0)

        self.date=Label(self.right,text=str(d.strftime("%A"))+","+str(d.strftime("%B"))+" "+str(d.strftime("%d"))+" "+str(d.strftime("%Y")),font=('arial 12 bold'),bg='lightblue')
        self.date.place(x=200,y=0)
        
        self.time=Label(self.right,text=str(d.strftime("%X"))+" "+str(d.strftime("%p")),font=('arial 12 bold'),bg='lightblue')
        self.time.place(x=240,y=20)

        self.cart=Label(self.right,text="Preview",font=('arial 27 bold'),bg='lightblue',fg='red')
        self.cart.place(x=0,y=50)
        
        self.Product=Label(self.right,text="Product",font=('arial 18 bold'),bg='lightblue')
        self.Product.place(x=0,y=110)
        
        self.Qty=Label(self.right,text="Quantity",font=('arial 18 bold'),bg='lightblue')
        self.Qty.place(x=250,y=110)
        
        self.Amt=Label(self.right,text="Amount",font=('arial 18 bold'),bg='lightblue')
        self.Amt.place(x=450,y=110)
        
        self.name=Label(self.left,text="Medicine's Name",font=('arial 18 bold'),bg='white')
        self.name.place(x=0,y=100)
        
        self.entern=Entry(self.left,width=25,font=('arial 18 italic bold'),bg='lightyellow')
        self.entern.place(x=200,y=100)
        self.entern.focus()
        
        self.search=Button(self.left,text="Search",width=25,height=2,bg='orange',activebackground='purple',command=self.data)
        self.search.place(x=345,y=150)
        
        self.price=Label(self.left,text="",font=('arial 27 bold'),bg='white',fg='green')
        self.price.place(x=0,y=200)

        self.totalp=Label(self.right,text="",font=('arial 27 bold'),bg='lightblue',fg='blue')
        self.totalp.place(x=0,y=600)        

        c.execute("SELECT Qty from inventory")
        Inv=c.fetchall()
        for i in Inv:
            inq.append(i[0])

        
    def data(self,*args):
        
        self.get_n=self.entern.get()
        if self.get_n=="":
            Messagebox.showwarning("Insert Status","Medicine Name not entered!!")    
        else:
            c.execute("SELECT SellingPrice,Qty,DOE from Inventory where Prod_name=%s order by DOE",(self.get_n,))
            y=c.fetchall()
            self.aprice=[]
            self.doex=[]
            for i in y:
                self.aprice.append(i[1])
                self.doex.append(i[2])
            self.stock=sum(self.aprice)
            for i in y:
                if i[0]!=None and i[1]!=None and i[2]!=None:
                    self.p=i[0] 
                    self.price.configure(text="Price is ₹ "+str(self.p))

                    self.q=Label(self.left,text="Enter Quantity",font=('arial 18 bold'),bg='white')
                    self.q.place(x=0,y=300)

                    self.enterq=Entry(self.left,width=25,font=('arial 18 italic bold'),bg='lightyellow')
                    self.enterq.place(x=200,y=300)
                    self.enterq.focus()

                    self.add=Button(self.left,text="Add to Cart",width=25,height=2,bg='orange',activebackground='purple',command=self.add_cart)
                    self.add.place(x=345,y=350)

                    self.paid=Label(self.left,text="Amount Paid",font=('arial 18 bold'),bg='white')
                    self.paid.place(x=0,y=420)

                    self.enterp=Entry(self.left,width=25,font=('arial 18 italic bold'),bg='lightyellow')
                    self.enterp.place(x=200,y=420)

                    self.change=Button(self.left,text="Calculate Change",width=25,height=2,bg='orange',activebackground='purple',command=self.change_fun)
                    self.change.place(x=345,y=470)
                    
                    Messagebox.showinfo("Inventory Status","Stock available is %s."%self.stock)       
                    break

            if y==[]:
                Messagebox.showerror("Sorry","%s is not available at the Moment!!"%self.get_n)
                self.entern.focus()
                self.entern.delete(0,END)           
                    
    def add_cart(self,*args):
        self.quan=int(self.enterq.get())
        if self.quan > int(self.stock):
            Messagebox.showerror("Error","Stock available is only %s!!\nPlease enter correct amount"%self.stock )
            self.enterq.delete(0,END)
            self.enterq.focus()
        else:
            self.final=float(self.quan)*float(self.p)
            flag=1
            for i in range(len(prod_list)):
               if prod_list[i]==self.get_n:
                   prod_quan[i]+=self.quan
                   prod_price[i]+=self.final
                   flag=0
                   break
            if flag==1:
                prod_list.append(self.get_n)
                prod_quan.append(self.quan)
                prod_price.append(self.final)

            self.x_index=0
            self.y_index=150
            self.count=0
            for self.i in prod_list:
                self.tempn=Label(self.right,text=str(prod_list[self.count]),font=('arial 18 bold'),bg='lightblue')
                self.tempn.place(x=0,y=self.y_index)

                self.tempq=Label(self.right,text=str(prod_quan[self.count]),font=('arial 18 bold'),bg='lightblue')
                self.tempq.place(x=250,y=self.y_index)

                self.tempp=Label(self.right,text=str(prod_price[self.count])+'0',font=('arial 18 bold'),bg='lightblue')
                self.tempp.place(x=450,y=self.y_index)

                self.y_index+=40
                self.count+=1

                self.totalp.configure(text="Total : ₹ "+str(sum(prod_price))+'0') 

                self.q.place_forget()
                self.enterq.place_forget()
                self.price.configure(text="")
                self.add.destroy()

                self.entern.focus()
                self.entern.delete(0,END)
            Messagebox.showinfo("Success","Added to your Cart")

            if self.get_n not in prod_dic.keys():
                prod_dic[self.get_n]=self.aprice
            co=0
            for i in range(len(self.aprice)):
                co+=1
                if self.quan>=self.aprice[i]:
                    self.quan-=self.aprice[i]
                    self.aprice[i]=0
                else:
                    self.aprice[i]-=self.quan
                    break
            prod_dic[self.get_n]=self.aprice
            
            for x in range(co):
                c.execute("UPDATE inventory SET Qty=%s WHERE Prod_name=%s and DOE=%s",(prod_dic[self.get_n][x],self.get_n,self.doex[x]))
                mydb.commit()
            
        
    def change_fun(self,*args):
        self.amount=float(self.enterp.get())
    
        self.ototal=float(sum(prod_price))
        self.bal=self.amount-self.ototal

        if self.bal<0:
            Messagebox.showerror("Error","Enter Right Amount to avoid cancellation of Bill")
            self.enterp.focus()
            self.enterp.delete(0,END)
            
        else:

            self.name.place_forget()
            self.entern.place_forget()
            self.search.destroy()

            self.change.configure(state='disabled')
            
            self.na=Label(self.left,text="Customer's Details",font=('arial 18 bold'),bg='white')
            self.na.place(y=100)

            self.fn=Label(self.left,text="First Name",font=('arial 18 bold'),bg='white')
            self.fn.place(y=150)
            self.fn.focus()

            self.fne=Entry(self.left,font=('arial 18 bold italic'),bg='lightyellow',width=25)
            self.fne.place(x=250,y=150)
        
            self.ln=Label(self.left,text="Last Name",font=('arial 18 bold'),bg='white')
            self.ln.place(y=200)

            self.lne=Entry(self.left,font=('arial 18 bold italic'),bg='light yellow',width=25)
            self.lne.place(x=250,y=200)

            self.n=Button(self.left,text="Store Name",width=25,height=2,bg='orange',activebackground='purple',command=self.names)
            self.n.place(x=295,y=250)
            
            self.t_bal=Label(self.left,text="Balance: ₹ "+str(self.bal)+'0',font=('arial 30 bold'),fg='green',bg='white')
            self.t_bal.place(y=340)

            self.fn=[]
            self.fq=[]
            self.fd=[]
            self.sp=[]
        
            c.execute("SELECT Prod_name,Qty,DOE,SellingPrice from Inventory")
            w=c.fetchall()
            for i in w:
                self.fn.append(i[0])
                self.fq.append(i[1])
                self.fd.append(i[2])
                self.sp.append(i[3])
            
            global bc
            bc=[0 for i in range(len(self.fn))]
            for i in range(len(self.fq)):
                bc[i]=inq[i]-self.fq[i]

    def names(self,*args):
        
        self.fns=str(self.fne.get())
        self.lns=str(self.lne.get())

        self.bill=Button(self.left,text="Generate Bill",width=90,height=2,bg='red',activebackground='blue',command=self.generate_bill)
        self.bill.place(x=70,y=600)

        self.n.configure(state='disabled')

    def generate_bill(self,*args):
        
        global bc
        for i in range(len(inq)):
            if bc[i]==0:
                continue
            else:
                sq=("INSERT INTO SALES(S_date,Cust_Fname,Cust_Lname,Prod_name,Qty,U_price,T_price,DOE) VALUES(%s,%s,%s,%s,%s,%s,%s,%s)")
                c.execute(sq,(dat,self.fns,self.lns,self.fn[i],bc[i],self.sp[i],bc[i]*self.sp[i],self.fd[i]))
                mydb.commit()
               
        Messagebox.showinfo("Success","Your Bill is being generated!!")
        self.bill.configure(state='disabled')
        
        c.execute("DELETE FROM inventory where Qty=0")
        mydb.commit()
        
        f=open("bill.txt","a")
        f.write(str(dat))
        f.write("\n")
        f.close()

        cd=0
        ct=0
        f=open("bill.txt","r")
        x=f.read()
        for i in x.split("\n"):
            if i==str(dat):
                cd+=1
            if i:
                ct+=1
        f.close()

        # in the folder where you have all the code Create a folder called Invoice
        #In invoice folder a new folder will be created with name as date and all bills of that date are stored in it
        directory="C:/Users/akaas/AppData/Local/Programs/Python/Python38/Project/Invoice/" + str(dat) + "/"
        if not os.path.exists(directory):
            os.makedirs(directory)

        com="\t\tCOVID-19 Relief Pharmacy Pvt Ltd\n"
        add="\t\t       Chennai,India\n"
        phone="\t\t        9799999999\n"
        sample="\t\t         Invoice\n"
        datee="\t\t"+str(dat)
        tim="\t" +str(d.strftime("%X"))+" "+str(d.strftime("%p"))

        table_head="\n\n\t-----------------------------------------\n\tS.No\t  Products\t Qty\t  Amount\n\t-----------------------------------------"
        final=com+add+phone+sample+datee+tim+"\n\n\t"+"Bill Number : "+str(ct)+"\n\tCustomer Name : "+self.fns+" "+self.lns+table_head


        #The bill is stored as Invoice number of that particular date
        file="C:/Users/akaas/AppData/Local/Programs/Python/Python38/Project/Invoice/%s/"%str(dat)+"Invoice"+str(cd)+".txt"
        f=open(file,'w')
        f.write(final)

        for i in range(len(prod_list)):
            f.write("\n\t" + str(i+1)+"\t  "+str(prod_list[i]+"       ")[:7]+"\t "+str(prod_quan[i])+ "\t  "+str(prod_price[i])+"0")
        f.write("\n\n\tTOTAL: Rs " + str(sum(prod_price))+"0" )
        f.write("\n\tThanks for visiting")
        f.close()

        #Opening the bill 
        os.system( "C:/Users/akaas/AppData/Local/Programs/Python/Python38/Project/Invoice/%s/Invoice%s.txt"%(str(dat),str(cd)) )
        
root=Tk()
Sale=Sales(root)
root.geometry("1366x768")
root.title("Sales")
root.mainloop()
