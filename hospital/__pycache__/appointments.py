from tkinter import*
from PIL import Image,ImageTk
from tkinter import ttk
import random
import mysql.connector
from tkinter import messagebox


class appointment:
    def __init__(self,root) -> None:
        self.root=root
        self.root.title("Hospital Management System")
        self.root.geometry("1295x550+230+220")

        #variable
        #x=random.randint(100,200)
        #self.var_pid.set(str(x))
        self.var_ano=IntVar()
        self.var_adate=StringVar()
        self.var_purpose=StringVar()
        self.var_visited=StringVar()
        self.var_pid=IntVar()
        self.var_sid=IntVar()
        
        
        #title
        lbl_title=Label(self.root,text="APPOINTMENTS",font=("times new roman",18,"bold"),bg="light sky blue",fg="white",bd=4,relief=RIDGE)
        lbl_title.place(x=0,y=0,width=1295,height=50)

        #label left
        labelframeleft=LabelFrame(self.root,bd=2,relief=RIDGE,text="Appointment Details",padx=2,font=("times new roman",12,"bold"))
        labelframeleft.place(x=5,y=50,width=425,height=490)


        #appoitment no
        appointment_no=Label(labelframeleft,text="Appointment No:",font=("ariel",12,"bold"),padx=2,pady=6)
        appointment_no.grid(row=0,column=0,sticky=W)

        entry_ref=ttk.Entry(labelframeleft,textvariable=self.var_ano,width=25,font=("times new roman",13,"bold"))
        entry_ref.grid(row=0,column=1)


        #date
        date=Label(labelframeleft,font=("ariel",12,"bold"),text="Date(YYYY-MM-DD) :",padx=2,pady=6)
        date.grid(row=1,column=0,sticky=W)

        name=ttk.Entry(labelframeleft,textvariable=self.var_adate,font=("times new roman",13,"bold"),width=25)
        name.grid(row=1,column=1)

        #purpose of appointment 
        purpose=Label(labelframeleft,font=("ariel",12,"bold"),text="Purpose :",padx=2,pady=6)
        purpose.grid(row=2,column=0,sticky=W)
        
        name=ttk.Entry(labelframeleft,textvariable=self.var_purpose,font=("times new roman",13,"bold"),width=25)
        name.grid(row=2,column=1)

        #previously visited or not
        la_visited=Label(labelframeleft,font=("ariel",12,"bold"),text="Previously visited :",padx=2,pady=6)
        la_visited.grid(row=3,column=0,sticky=W)
        combo_visit=ttk.Combobox(labelframeleft,textvariable=self.var_visited,font=("times new roman",13,"bold"),width=23,state="readonly")
        combo_visit["value"]=("Yes", "No")
        combo_visit.current(0)
        combo_visit.grid(row=3,column=1)

        pid=Label(labelframeleft,text="Patient ID :",font=("ariel",12,"bold"),padx=2,pady=6)
        pid.grid(row=4,column=0,sticky=W)

        entry_ref=ttk.Entry(labelframeleft,textvariable=self.var_pid,width=25,font=("times new roman",13,"bold"))
        entry_ref.grid(row=4,column=1)

        sid=Label(labelframeleft,text="Staff ID :",font=("ariel",12,"bold"),padx=2,pady=6)
        sid.grid(row=5,column=0,sticky=W)

        entry_ref=ttk.Entry(labelframeleft,textvariable=self.var_sid,width=25,font=("times new roman",13,"bold"))
        entry_ref.grid(row=5,column=1)

        
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
        table_frame=LabelFrame(self.root,bd=2,relief=RIDGE,text="View Data",padx=2,font=("times new roman",12,"bold"))
        table_frame.place(x=435,y=50,width=860,height=460)

        searchby=Label(table_frame,font=("ariel",12,"bold"),text="Search",bg="light skyblue",fg="white")
        searchby.grid(row=0,column=0,sticky=W,padx=2)

        self.search_var=StringVar()
        combo_search=ttk.Combobox(table_frame,textvariable=self.search_var,font=("ariel",10,"bold"),width=20,state="readonly")
        combo_search["value"]=("p_id", "appointment_no","s_id")
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

        self.patient_data=ttk.Treeview(data_frame,column=("appointment_no","a_date","disease","prev_visited","p_id","s_id"),xscrollcommand=scrollx.set,yscrollcommand=scrolly.set)
        
        scrollx.pack(side=BOTTOM,fill=X)
        scrolly.pack(side=RIGHT,fill=Y)

        scrollx.config(command=self.patient_data.xview)
        scrolly.config(command=self.patient_data.yview)


        self.patient_data.heading("appointment_no",text="Appointment No")
        self.patient_data.heading("a_date",text="Appointment Date")
        self.patient_data.heading("disease",text="Purpose")
        self.patient_data.heading("prev_visited",text="Visited")
        self.patient_data.heading("p_id",text="Patient ID")
        self.patient_data.heading("s_id",text="Staff ID")
        

        self.patient_data["show"]="headings"

        self.patient_data.column("appointment_no",width=80)
        self.patient_data.column("a_date",width=80)
        self.patient_data.column("disease",width=80)
        self.patient_data.column("prev_visited",width=80)
        self.patient_data.column("p_id",width=80)
        self.patient_data.column("s_id",width=80)

        self.patient_data.pack(fill=BOTH,expand=1)
        self.patient_data.bind("<ButtonRelease-1>",self.get_cursor)
        self.fetch_data()


    def insert(self):
        if self.var_ano.get()=="" or self.var_adate.get()=="" or self.var_purpose.get()=="" or self.var_pid.get()=="" or self.var_sid.get()=="":
            messagebox.showerror("Error","All Fields Required")
        else:
            #try:
            con=mysql.connector.connect(host="localhost",username="root",password="password",database="hospital")
            cursor=con.cursor()
            cursor.execute("insert into appointments values(%s,%s,%s,%s,%s,%s)",(
                                                                                    self.var_ano.get(),
                                                                                    self.var_adate.get(),
                                                                                    self.var_purpose.get(),
                                                                                    self.var_visited.get(),
                                                                                    self.var_pid.get(),
                                                                                    self.var_sid.get()
                                                                                    
                                                                                ))
            cursor.execute("commit")
            self.fetch_data()
            messagebox.showinfo("success","Data Added",parent=self.root)
            con.close()
            #except Exception as es:
            #   messagebox.showwarning("Warning",f"Something went wrong:{str(es)}",parent=self.root)

    def fetch_data(self):
        con=mysql.connector.connect(host="localhost",username="root",password="password",database="hospital")
        cursor=con.cursor()
        cursor.execute("select * from appointments")
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
        self.var_ano.set(row[0]),
        self.var_adate.set(row[1]),
        self.var_purpose.set(row[2]),
        self.var_visited.set(row[3]),
        self.var_pid.set(row[4]),
        self.var_sid.set(row[5])
        

    def update(self):
        if self.var_adate.get()=="":
            messagebox.showerror("Error","Enter mobile no",parent=self.root)
        else:
            con=mysql.connector.connect(host="localhost",username="root",password="password",database="hospital")
            cursor=con.cursor()
            cursor.execute("update appointments set p_id=%s,disease=%s,s_id=%s,a_date=%s,prev_visited=%s where appointment_no=%s",(

                                                                                                                                        self.var_pid.get(),
                                                                                                                                        self.var_purpose.get(),
                                                                                                                                        self.var_sid.get(),
                                                                                                                                        self.var_adate.get(),
                                                                                                                                        self.var_visited.get(),
                                                                                                                                        self.var_ano.get()                                                                                
        ))
        con.commit()
        self.fetch_data()
        con.close()
        messagebox.showinfo("Update","Customer details has been updated",parent=self.root)

    def delete(self):
        delete=messagebox.askyesno("Message","Confirm deletion",parent=self.root)
        if delete>0:
            con=mysql.connector.connect(host="localhost",username="root",password="password",database="hospital")
            cursor=con.cursor()
            query="delete from appointments where appointment_no=%s"
            value=(self.var_ano.get(),)
            cursor.execute(query,value)
        else:
            if not delete:
                return
        con.commit()
        self.fetch_data()
        con.close()

    def reset(self):
        self.var_ano.set(""),
        self.var_adate.set(""),
        self.var_purpose.set(""),
        self.var_visited.set(""),
        self.var_pid.set(""),
        self.var_sid.set(""),
        

        #x=random.randint(100,200)
        #self.var_id.set(str(x))

    def search(self):
        con=mysql.connector.connect(host="localhost",username="root",password="password",database="hospital")
        cursor=con.cursor()
        cursor.execute("select * from appointments where "+str(self.search_var.get())+" LIKE '%"+str(self.txt_search.get())+"%'")
        rows=cursor.fetchall()
        if len(rows)!=0:
            self.patient_data.delete(*self.patient_data.get_children())
            for i in rows:
                self.patient_data.insert("",END,values=i)
            con.commit()
        con.close()
    

    

     







if __name__=="__main__":
    root=Tk()
    obj=appointment(root)
    root.mainloop()

