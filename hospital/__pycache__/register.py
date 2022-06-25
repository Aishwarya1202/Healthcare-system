from tkinter import*
from PIL import Image,ImageTk
from tkinter import ttk
import random
from tkinter import messagebox
import random
import time
import datetime
import mysql.connector

##create table register(fname varchar(100),lname varchar(100),mobile int,email varchar(100),securityq varchar(100),securitya varchar(100),pwd varchar(100),cpwd varchar(100));
class register:
    def __init__(self,root):
        self.root=root
        self.root.title("Register")
        self.root.geometry("1550x800+0+0")


        ##variable
        self.var_fname=StringVar()
        self.var_lname=StringVar()
        self.var_mobile=StringVar()
        self.var_email=StringVar()
        self.var_securityq=StringVar()
        self.var_securitya=StringVar()
        self.var_pwd=StringVar()
        self.var_cpwd=StringVar()

        self.bg=ImageTk.PhotoImage(file=r"C:\Users\Aishwarya\Desktop\hospital\images\login_bg.jpg")

        lbl_bg=Label(self.root,image=self.bg)
        lbl_bg.place(x=0,y=0,relwidth=1,relheight=1)

        ##frame
        frame=Frame(self.root,bg="gray")
        frame.place(x=350,y=100,width=800,height=550)

        register_lbl=Label(frame,text="REGISTER HERE",font=("times new roman",15,"bold"),fg="gray",bg="black")
        register_lbl.place(x=20,y=20)


        ##name and other entries
        fname=Label(frame,text="First Name",font=("times new roman",15,"bold"),bg="gray")
        fname.place(x=50,y=100)

        fname_entry=Entry(frame,textvariable=self.var_fname,font=("times new roman",15,"bold"))
        fname_entry.place(x=50,y=130,width=250)

        lname=Label(frame,text="Last Name",font=("times new roman",15,"bold"),bg="gray")
        lname.place(x=50,y=160)

        lname_entry=Entry(frame,textvariable=self.var_lname,font=("times new roman",15,"bold"))
        lname_entry.place(x=50,y=190,width=250)

        contact=Label(frame,text="Mobile No:",font=("times new roman",15,"bold"),bg="gray")
        contact.place(x=50,y=220)

        contact_entry=Entry(frame,textvariable=self.var_mobile,font=("times new roman",15,"bold"))
        contact_entry.place(x=50,y=250,width=250)

        Email=Label(frame,text="Email",font=("times new roman",15,"bold"),bg="gray")
        Email.place(x=50,y=280)

        email_entry=Entry(frame,textvariable=self.var_email,font=("times new roman",15,"bold"))
        email_entry.place(x=50,y=310,width=250)

        securityq=Label(frame,text="Select Security Question",font=("times new roman",15,"bold"),bg="gray")
        securityq.place(x=50,y=340)
        self.combo_sq=ttk.Combobox(frame,textvariable=self.var_securityq,font=("ariel",12,"bold"),width=27,state="readonly")
        self.combo_sq["value"]=("select", "Your nickname", "Your childhood friend name","Your School name")
        self.combo_sq.place(x=50,y=370,width=250)
        self.combo_sq.current(0)
        
        securitya=Label(frame,text="Security Answer",font=("times new roman",15,"bold"),bg="gray")
        securitya.place(x=50,y=400)

        seq_entry=Entry(frame,textvariable=self.var_securitya,font=("times new roman",15,"bold"))
        seq_entry.place(x=50,y=430,width=250)
        
        pwd1=Label(frame,text="Password",font=("times new roman",15,"bold"),bg="gray")
        pwd1.place(x=500,y=340)

        pwd1_entry=Entry(frame,textvariable=self.var_pwd,font=("times new roman",15,"bold"))
        pwd1_entry.place(x=500,y=370,width=250)

        cpwd=Label(frame,text="Confirm Password",font=("times new roman",15,"bold"),bg="gray")
        cpwd.place(x=500,y=400)

        cpwd_entry=Entry(frame,textvariable=self.var_cpwd,font=("times new roman",15,"bold"))
        cpwd_entry.place(x=500,y=430,width=250)


        btnregister=Button(frame,text="Register",command=self.register_data,font=("times new roman",20,"bold"),bg="black",fg="gray",width=9)
        btnregister.place(x=50,y=490,width=200,height=45)

        btnlogin=Button(frame,text="Login",font=("times new roman",20,"bold"),bg="black",fg="gray",width=9)
        btnlogin.place(x=500,y=490,width=200,height=45)


    def register_data(self):
        if self.var_fname.get()=="" or self.var_email.get()=="":
            messagebox.showerror("Error","All Fields are Required")
        elif self.var_pwd.get()!=self.var_cpwd.get():
            messagebox.showerror("Error","Password dosent match")
        else:
            con=mysql.connector.connect(host="localhost",username="root",password="password",database="login")
            cursor=con.cursor()
            query=("select * from register where email=%s")
            value=(self.var_email.get(),)
            cursor.execute(query,value)
            row=cursor.fetchone()
            if row!=None:
                messagebox.showerror("Error","This email is already registered. Try Login!")
            else:
                cursor.execute("insert into register values(%s,%s,%s,%s,%s,%s,%s,%s)",(
                                                                                        self.var_fname.get(),
                                                                                        self.var_lname.get(),
                                                                                        self.var_mobile.get(),
                                                                                        self.var_email.get(),
                                                                                        self.var_securityq.get(),
                                                                                        self.var_securitya.get(),
                                                                                        self.var_pwd.get(),
                                                                                        self.var_cpwd.get()
                                                                                    ))
            con.commit()
            con.close()
            messagebox.showinfo("Success","Registerd!")










if __name__=="__main__":
    root=Tk()
    app=register(root)
    root.mainloop()