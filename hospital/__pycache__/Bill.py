from tkinter import*
from PIL import Image,ImageTk
from tkinter import ttk
import random
import mysql.connector
from tkinter import messagebox

## create table bill(bno int,pid int,medicine varchar(100),bill int);

class about:
    def __init__(self,root) -> None:
        self.root3=root
        self.root3.title("Hospital Management System")
        self.root3.geometry("1295x550+230+220")

          #variable
        self.var_bno=StringVar()
        self.var_doctorc=StringVar()
        self.var_roomt=StringVar()
        self.var_roomc=StringVar()
        self.var_days=StringVar()
        self.var_bill=StringVar()
        self.var_pid=StringVar()



        #title
        lbl_title=Label(self.root3,text="BILL",font=("times new roman",18,"bold"),bg="light sky blue",fg="white",bd=4,relief=RIDGE)
        lbl_title.place(x=0,y=0,width=1295,height=50)

        #label left
        labelframeleft=LabelFrame(self.root3,bd=2,relief=RIDGE,text="Billing Info",padx=2,font=("times new roman",12,"bold"))
        labelframeleft.place(x=5,y=50,width=425,height=490)


         #billno
        bno=Label(labelframeleft,font=("ariel",12,"bold"),text="Bill No.",padx=2,pady=6)
        bno.grid(row=0,column=0,sticky=W)
        
        name=ttk.Entry(labelframeleft,textvariable=self.var_bno,font=("times new roman",13,"bold"),width=29)
        name.grid(row=0,column=1)

        doctorc=Label(labelframeleft,font=("ariel",12,"bold"),text="Consultation Charges",padx=2,pady=6)
        doctorc.grid(row=1,column=0,sticky=W)
        
        name=ttk.Entry(labelframeleft,textvariable=self.var_doctorc,font=("times new roman",13,"bold"),width=29)
        name.grid(row=1,column=1)

        bno=Label(labelframeleft,font=("ariel",12,"bold"),text="Room Type:",padx=2,pady=6)
        bno.grid(row=2,column=0,sticky=W)
        
        name=ttk.Entry(labelframeleft,textvariable=self.var_roomt,font=("times new roman",13,"bold"),width=29)
        name.grid(row=2,column=1)

        bno=Label(labelframeleft,font=("ariel",12,"bold"),text="Room Charges:",padx=2,pady=6)
        bno.grid(row=3,column=0,sticky=W)
        
        name=ttk.Entry(labelframeleft,textvariable=self.var_roomc,font=("times new roman",13,"bold"),width=29)
        name.grid(row=3,column=1)


        #dyas
        nodays=Label(labelframeleft,font=("ariel",12,"bold"),text="No of days:",padx=2,pady=6)
        nodays.grid(row=4,column=0,sticky=W)
        
        name=ttk.Entry(labelframeleft,textvariable=self.var_days,font=("times new roman",13,"bold"),width=29)
        name.grid(row=4,column=1)


        #total
        billA=Label(labelframeleft,font=("ariel",12,"bold"),text="Total Amount:",padx=2,pady=6)
        billA.grid(row=5,column=0,sticky=W)
        
        name=ttk.Entry(labelframeleft,textvariable=self.var_bill,font=("times new roman",13,"bold"),width=29)
        name.grid(row=5,column=1)

         #patient id
        pid=Label(labelframeleft,font=("ariel",12,"bold"),text="Patient id:",padx=2,pady=6)
        pid.grid(row=6,column=0,sticky=W)
        
        name=ttk.Entry(labelframeleft,textvariable=self.var_pid,font=("times new roman",13,"bold"),width=29)
        name.grid(row=6,column=1)
        
        ##buttons
        btn_frame=Frame(labelframeleft,bd=2,relief=RIDGE)
        btn_frame.place(x=0,y=370,width=412,height=40)

        btnadd=Button(btn_frame,text="Add",command=self.insert,font=("times new roman",13,"bold"),bg="skyblue",fg="black",width=9)
        btnadd.grid(row=0,column=0,padx=1)

        btnupdate=Button(btn_frame,text="Update",command=self.update,font=("times new roman",13,"bold"),bg="skyblue",fg="black",width=9)
        btnupdate.grid(row=0,column=1,padx=1)

        btndelete=Button(btn_frame,text="Delete",command=self.delete,font=("times new roman",13,"bold"),bg="skyblue",fg="black",width=9)
        btndelete.grid(row=0,column=2,padx=1)

        btnreset=Button(btn_frame,text="Reset",command=self.reset,font=("times new roman",13,"bold"),bg="skyblue",fg="black",width=9)
        btnreset.grid(row=0,column=3,padx=1)


        ##searchh
        table_frame=LabelFrame(self.root3,bd=2,relief=RIDGE,text="View Data",padx=2,font=("times new roman",12,"bold"))
        table_frame.place(x=435,y=50,width=860,height=460)

        searchby=Label(table_frame,font=("ariel",12,"bold"),text="Search",bg="light skyblue",fg="white")
        searchby.grid(row=0,column=0,sticky=W,padx=2)

        self.search_var=StringVar()
        combo_search=ttk.Combobox(table_frame,textvariable=self.search_var,font=("ariel",10,"bold"),width=20,state="readonly")
        combo_search["value"]=("bill_no", "p_id")
        combo_search.current(0)
        combo_search.grid(row=0,column=1,padx=2)

        self.txt_search=StringVar()
        txtsearch=ttk.Entry(table_frame,textvariable=self.txt_search,font=("times new roman",13,"bold"),width=24)
        txtsearch.grid(row=0,column=2,padx=2)

        btnsearch=Button(table_frame,text="Search",command=self.search,font=("times new roman",13,"bold"),bg="skyblue",fg="black",width=12)
        btnsearch.grid(row=0,column=3,padx=1)

        btnshow=Button(table_frame,text="Show",command=self.fetch_data,font=("times new roman",13,"bold"),bg="skyblue",fg="black",width=12)
        btnshow.grid(row=0,column=4,padx=1)

        
        ### right table
        data_frame=Frame(table_frame,bd=2,relief=RIDGE)
        data_frame.place(x=0,y=50,width=860,height=350)

        scrollx=ttk.Scrollbar(data_frame,orient=HORIZONTAL)
        scrolly=ttk.Scrollbar(data_frame,orient=VERTICAL)

        self.patient_data=ttk.Treeview(data_frame,column=("bill_no","doctor_charge","room_type","room_charge","no_of_days","bill","p_id"),xscrollcommand=scrollx.set,yscrollcommand=scrolly.set)
        
        scrollx.pack(side=BOTTOM,fill=X)
        scrolly.pack(side=RIGHT,fill=Y)

        scrollx.config(command=self.patient_data.xview)
        scrolly.config(command=self.patient_data.yview)


        self.patient_data.heading("bill_no",text="Bill No:")
        self.patient_data.heading("doctor_charge",text="Consultation Charges")
        self.patient_data.heading("room_type",text="Room type:")
        self.patient_data.heading("room_charge",text="Room Charge:")
        self.patient_data.heading("no_of_days",text="No of Days:")
        self.patient_data.heading("bill",text="Total Amount:")
        self.patient_data.heading("p_id",text="Patient Id:")

        self.patient_data["show"]="headings"

        self.patient_data.column("bill_no",width=80)
        self.patient_data.column("doctor_charge",width=80)
        self.patient_data.column("room_type",width=80)
        self.patient_data.column("room_charge",width=80)
        self.patient_data.column("no_of_days",width=80)
        self.patient_data.column("bill",width=80)
        self.patient_data.column("p_id",width=80)

        self.patient_data.pack(fill=BOTH,expand=1)
        self.patient_data.bind("<ButtonRelease-1>",self.get_cursor)
        self.fetch_data()

    def insert(self):
        if self.var_bno.get()=="" or self.var_bill.get()=="":
            messagebox.showerror("Error","All Fields Required")
        else:
            #try:
            con=mysql.connector.connect(host="localhost",username="root",password="password",database="hospital")
            cursor=con.cursor()
            cursor.execute("insert into bill values(%s,%s,%s,%s,%s,%s)",(
                                                                                    self.var_bno.get(),
                                                                                    self.var_doctorc.get(),
                                                                                    self.var_roomt.get(),
                                                                                    self.var_roomc.get(),
                                                                                    self.var_days.get(),
                                                                                    self.var_bill.get(),
                                                                                    #self.var_pid.get()
                                                                                ))
            cursor.execute("commit")
            self.fetch_data()
            messagebox.showinfo("success","Data Added",parent=self.root3)
            con.close()
            #except Exception as es:
            #   messagebox.showwarning("Warning",f"Something went wrong:{str(es)}",parent=self.root)

    def fetch_data(self):
        con=mysql.connector.connect(host="localhost",username="root",password="password",database="hospital")
        cursor=con.cursor()
        cursor.execute("select * from bill")
        rows=cursor.fetchall()
        if len(rows)!=0:
           self.patient_data.delete(*self.patient_data.get_children())
           for i in rows:
                self.patient_data.insert("",END,values=i)
        con.commit()
        con.close()

    def get_cursor(self,event=""):
        cursor_row=self.patient_data.focus()
        content=self.patient_data.item(cursor_row)
        row=content["values"]
        self.var_bno.set(row[0]),
        self.var_doctorc.set(row[1]),
        self.var_roomt.set(row[2]),
        self.var_roomc.set(row[3]),
        self.var_days.set(row[4]),
        self.var_bill.set(row[5]),
        self.var_pid.set(row[6]),
      
    def update(self):
        if self.var_bno.get()=="":
            messagebox.showerror("Error","Enter id",parent=self.root3)
        else:
            con=mysql.connector.connect(host="localhost",username="root",password="password",database="hospital")
            cursor=con.cursor()
            cursor.execute("update bill set doctor_charge=%s,room_type=%s,room_charge=%s,no_of_days=%s,bill=%s,p_id=%s where bill_no=%s",(
                                                                                                                   self.var_doctorc.get(),
                                                                                                                   self.var_roomt.get(),
                                                                                                                   self.var_roomc.get(),
                                                                                                                   self.var_days.get(),
                                                                                                                   self.var_bill.get(),
                                                                                                                   self.var_pid.get(),
                                                                                                                   self.var_bno.get()                                                                          
        ))
        con.commit()
        self.fetch_data()
        con.close()
        messagebox.showinfo("Update","Bill details has been updated",parent=self.root3)

    def delete(self):
        delete=messagebox.askyesno("message","Confirm deletion",parent=self.root3)
        if delete>0:
            con=mysql.connector.connect(host="localhost",username="root",password="password",database="hospital")
            cursor=con.cursor()
            query="delete from bill where bill_no=%s"
            value=(self.var_bno.get(),)
            cursor.execute(query,value)
        else:
            if not delete:
                return
        con.commit()
        self.fetch_data()
        con.close()

    def reset(self):
        self.var_bno.set(""),
        self.var_doctorc.set(""),
        self.var_roomt.set(""),
        self.var_roomc.set(""),
        self.var_days.set(""),
        self.var_bill.set(""),
        self.var_pid.set("")


    def search(self):
        con=mysql.connector.connect(host="localhost",username="root",password="password",database="hospital")
        cursor=con.cursor()
        cursor.execute("select * from bill where "+str(self.search_var.get())+" LIKE '%"+str(self.txt_search.get())+"%'")
        rows=cursor.fetchall()
        if len(rows)!=0:
            self.patient_data.delete(*self.patient_data.get_children())
            for i in rows:
                self.patient_data.insert("",END,values=i)
            con.commit()
        con.close()
    

    

        
        








if __name__=="__main__":
    root3=Tk()
    obj=about(root3)
    root3.mainloop()