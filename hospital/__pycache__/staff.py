from tkinter import*
from PIL import Image,ImageTk
from tkinter import ttk
import random
import mysql.connector
from tkinter import messagebox


class doctor:
    def __init__(self,root) -> None:
        self.root=root
        self.root.title("Hospital Management System")
        self.root.geometry("1295x550+230+220")

        
        #variable
        self.var_id=IntVar()
        #x=random.randint(100,200)
        #self.var_id.set(str(x))

        self.var_name=StringVar()
        self.var_gender=StringVar()
        self.var_mobile=IntVar()
        self.var_email=StringVar()
        self.var_designation=StringVar()
        self.var_specialisation=StringVar()
        
        


        #title
        lbl_title=Label(self.root,text="STAFF DETAILS",font=("times new roman",18,"bold"),bg="light sky blue",fg="white",bd=4,relief=RIDGE)
        lbl_title.place(x=0,y=0,width=1295,height=50)

        #label left
        labelframeleft=LabelFrame(self.root,bd=2,relief=RIDGE,text="STAFF DETAILS",padx=2,font=("times new roman",12,"bold"))
        labelframeleft.place(x=5,y=50,width=520,height=350)

        #doctor name
        #id
        staff_no=Label(labelframeleft,text="Staff ID :",font=("times new roman",12,"bold"),padx=2,pady=6)
        staff_no.grid(row=0,column=0,sticky=W)

        entry_ref=ttk.Entry(labelframeleft,textvariable=self.var_id,width=29,font=("times new roman",13,"bold"))
        entry_ref.grid(row=0,column=1)


        #name
        staff_name=Label(labelframeleft,font=("ariel",12,"bold"),text="Staff Name :",padx=2,pady=6)
        staff_name.grid(row=1,column=0,sticky=W)

        name=ttk.Entry(labelframeleft,textvariable=self.var_name,font=("times new roman",13,"bold"),width=29)
        name.grid(row=1,column=1)

        #gender
        la_gender=Label(labelframeleft,font=("ariel",12,"bold"),text="Gender :",padx=2,pady=6)
        la_gender.grid(row=2,column=0,sticky=W)
        combo_gender=ttk.Combobox(labelframeleft,textvariable=self.var_gender,font=("ariel",12,"bold"),width=27)
        combo_gender["value"]=("Male", "Female", "Other")
        combo_gender.current(0)
        combo_gender.grid(row=2,column=1)

        #mobile no
        patient_mobno=Label(labelframeleft,font=("ariel",12,"bold"),text="Mobile No :",padx=2,pady=6)
        patient_mobno.grid(row=3,column=0,sticky=W)
        
        name=ttk.Entry(labelframeleft,textvariable=self.var_mobile,font=("times new roman",13,"bold"),width=29)
        name.grid(row=3,column=1)

        #email
        patient_mobno=Label(labelframeleft,font=("ariel",12,"bold"),text="Email :",padx=2,pady=6)
        patient_mobno.grid(row=4,column=0,sticky=W)
        
        name=ttk.Entry(labelframeleft,textvariable=self.var_email,font=("times new roman",13,"bold"),width=29)
        name.grid(row=4,column=1)


        #designation
        designation=Label(labelframeleft,font=("ariel",12,"bold"),text="Designation :",padx=2,pady=6)
        designation.grid(row=5,column=0,sticky=W)
        combo_gender=ttk.Combobox(labelframeleft,textvariable=self.var_designation,font=("ariel",12,"bold"),width=27,state="readonly")
        combo_gender["value"]=("Doctor", "Trainee","Visitor","Nurse", "Receptionist")
        combo_gender.current(0)
        combo_gender.grid(row=5,column=1)

        #specialisation
        spaciality=Label(labelframeleft,font=("ariel",12,"bold"),text="Specialisation :",padx=2,pady=6)
        spaciality.grid(row=6,column=0,sticky=W)
        
        name=ttk.Entry(labelframeleft,textvariable=self.var_specialisation,font=("times new roman",13,"bold"),width=29)
        name.grid(row=6,column=1)

        

        ##buttons
        btn_frame=Frame(labelframeleft,bd=2,relief=RIDGE)
        btn_frame.place(x=0,y=240,width=412,height=40)

        btnadd=Button(btn_frame,text="Add",command=self.insert,font=("times new roman",13,"bold"),bg="skyblue",fg="black",width=9)
        btnadd.grid(row=0,column=0,padx=1)

        btnupdate=Button(btn_frame,text="Update",command=self.update,font=("times new roman",13,"bold"),bg="skyblue",fg="black",width=9)
        btnupdate.grid(row=0,column=1,padx=1)

        btndelete=Button(btn_frame,text="Delete",command=self.delete,font=("times new roman",13,"bold"),bg="skyblue",fg="black",width=9)
        btndelete.grid(row=0,column=2,padx=1)

        btnreset=Button(btn_frame,text="Reset",command=self.reset,font=("times new roman",13,"bold"),bg="skyblue",fg="black",width=9)
        btnreset.grid(row=0,column=3,padx=1)

        
        ##searchh
        table_frame=LabelFrame(self.root,bd=2,relief=RIDGE,text="Staff Details",padx=2,font=("times new roman",12,"bold"))
        table_frame.place(x=550,y=55,width=600,height=350)

        scrollx=ttk.Scrollbar(table_frame,orient=HORIZONTAL)
        scrolly=ttk.Scrollbar(table_frame,orient=VERTICAL)

        self.patient_data=ttk.Treeview(table_frame,column=("s_id","s_name","s_gender","s_mobile","s_email","designation","specialization"),xscrollcommand=scrollx.set,yscrollcommand=scrolly.set)
        
        scrollx.pack(side=BOTTOM,fill=X)
        scrolly.pack(side=RIGHT,fill=Y)

        scrollx.config(command=self.patient_data.xview)
        scrolly.config(command=self.patient_data.yview)

        self.patient_data.heading("s_id",text="Staff ID")
        self.patient_data.heading("s_name",text="Staff Name")
        self.patient_data.heading("s_gender",text="Gender")
        self.patient_data.heading("s_mobile",text="Mobile no")
        self.patient_data.heading("s_email",text="Email")
        self.patient_data.heading("designation",text="Designation")
        self.patient_data.heading("specialization",text="Specialisation")
        
        
        self.patient_data["show"]="headings"

        self.patient_data.column("s_id",width=80)
        self.patient_data.column("s_name",width=80)
        self.patient_data.column("s_gender",width=80)
        self.patient_data.column("s_mobile",width=80)
        self.patient_data.column("s_email",width=80)
        self.patient_data.column("designation",width=80)
        self.patient_data.column("specialization",width=80)
        
    
        self.patient_data.pack(fill=BOTH,expand=1)
        self.patient_data.bind("<ButtonRelease-1>",self.get_cursor)
        self.fetch_data()

    def insert(self):
        if self.var_mobile.get()=="" or self.var_email.get()=="":
            messagebox.showerror("Error","All Fields Required")
        else:
            #try:
            con=mysql.connector.connect(host="localhost",username="root",password="password",database="hospital")
            cursor=con.cursor()
            cursor.execute("insert into staff values(%s,%s,%s,%s,%s,%s,%s)",(
                                                                                    self.var_id.get(),
                                                                                    self.var_name.get(),
                                                                                    self.var_gender.get(),
                                                                                    self.var_mobile.get(),
                                                                                    self.var_email.get(),
                                                                                    self.var_designation.get(),
                                                                                    self.var_specialisation.get()
                                                                                    
                                                                                    
                                                                                ))
            cursor.execute("commit")
            self.fetch_data()
            messagebox.showinfo("Success","Data Added",parent=self.root)
            con.close()
            #except Exception as es:
            #   messagebox.showwarning("Warning",f"Something went wrong:{str(es)}",parent=self.root)

    def fetch_data(self):
        con=mysql.connector.connect(host="localhost",username="root",password="password",database="hospital")
        cursor=con.cursor()
        cursor.execute("select * from staff")
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
        self.var_id.set(row[0]),
        self.var_name.set(row[1]),
        self.var_gender.set(row[2]),
        self.var_mobile.set(row[3]),
        self.var_email.set(row[4]),
        
        self.var_designation.set(row[5]),
        self.var_specialisation.set(row[6]),
        

    def update(self):
        if self.var_id.get()=="" or self.var_name.get()=="" or self.var_gender.get()=="" or self.var_mobile.get()=="" or self.var_designation.get()=="" or self.var_specialisation.get()=="":
            messagebox.showerror("Error","Enter Details !!",parent=self.root)
        else:
            con=mysql.connector.connect(host="localhost",username="root",password="password",database="hospital")
            cursor=con.cursor()
            cursor.execute("update staff set s_name=%s,s_gender=%s,s_mobile=%s,s_email=%s,designation=%s,specialization=%s where s_id=%s",(

                                                                                                                                        self.var_name.get(),
                                                                                                                                        self.var_gender.get(),
                                                                                                                                        self.var_mobile.get(),
                                                                                                                                        self.var_email.get(),
                                                                                                                                        self.var_designation.get(),
                                                                                                                                        self.var_specialisation.get(),
                                                                                                                                        self.var_id.get()                                                                                
        ))
        con.commit()
        self.fetch_data()
        con.close()
        messagebox.showinfo("Update","Customer details has been updated",parent=self.root)

    def delete(self):
        delete=messagebox.askyesno("message","Confirm deletion",parent=self.root)
        if delete>0:
            con=mysql.connector.connect(host="localhost",username="root",password="password",database="hospital")
            cursor=con.cursor()
            query="delete from staff where s_id=%s"
            value=(self.var_id.get(),)
            cursor.execute(query,value)
        else:
            if not delete:
                return
        con.commit()
        self.fetch_data()
        con.close()

    def reset(self):
        self.var_id.set(""),
        self.var_name.set(""),
        self.var_gender.set(""),
        self.var_mobile.set(""),
        self.var_email.set(""),
        self.var_specialisation.set(""),
        self.var_designation.set("")

        #x=random.randint(1000,2000)
        #self.var_id.set(str(x))

    def search(self):
        con=mysql.connector.connect(host="localhost",username="root",password="password",database="hospital")
        cursor=con.cursor()
        cursor.execute("select * from staff where "+str(self.search_var.get())+" LIKE '%"+str(self.txt_search.get())+"%'")
        rows=cursor.fetchall()
        if len(rows)!=0:
            self.patient_data.delete(*self.patient_data.get_children())
            for i in rows:
                self.patient_data.insert("",END,values=i)
            con.commit()
        con.close()
    

    

     





if __name__=="__main__":
    root=Tk()
    obj=doctor(root)
    root.mainloop()