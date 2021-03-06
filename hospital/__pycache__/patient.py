from tkinter import*
from PIL import Image,ImageTk
from tkinter import ttk
import random
import mysql.connector
from tkinter import messagebox


class patient_window:
    def __init__(self,root) -> None:
        self.root=root
        self.root.title("Hospital Management System")
        self.root.geometry("1295x550+230+220")


        #variable
        self.var_pid=StringVar()
        #x=random.randint(100,200)
        #self.var_id.set(str(x))

        self.var_name=StringVar()
        self.var_gender=StringVar()
        self.var_address=StringVar()
        self.var_mobile=StringVar()
        self.var_email=StringVar()
        self.var_age=StringVar()
        self.var_disease=StringVar()
        self.var_sid=StringVar()


        #title
        lbl_title=Label(self.root,text="ADD PATIENT DETAILS",font=("times new roman",18,"bold"),bg="light sky blue",fg="white",bd=4,relief=RIDGE)
        lbl_title.place(x=0,y=0,width=1295,height=50)

        #label left
        labelframeleft=LabelFrame(self.root,bd=2,relief=RIDGE,text="Patient Details",padx=2,font=("times new roman",12,"bold"))
        labelframeleft.place(x=5,y=50,width=425,height=490)

        #detailedform 1.no 2.name
        patient_no=Label(labelframeleft,text="Patient ID",font=("times new roman",12,"bold"),padx=2,pady=6)
        patient_no.grid(row=0,column=0,sticky=W)

        entry_ref=ttk.Entry(labelframeleft,textvariable=self.var_pid,width=29,font=("times new roman",13,"bold"))
        entry_ref.grid(row=0,column=1)

        #name
        patient_name=Label(labelframeleft,font=("ariel",12,"bold"),text="Patient Name:",padx=2,pady=6)
        patient_name.grid(row=1,column=0,sticky=W)
        name=ttk.Entry(labelframeleft,textvariable=self.var_name,font=("times new roman",13,"bold"),width=29)
        name.grid(row=1,column=1)

        #name
        #patient_name=Label(labelframeleft,font=("ariel",12,"bold"),text="PATIENT NAME",padx=2,pady=6)
        #patient_name.grid(row=1,column=0,sticky=W)
        #name=ttk.Entry(labelframeleft,font=("times new roman",13,"bold"),width=29)
        #name.grid(row=1,column=1)

        #gender
        la_gender=Label(labelframeleft,font=("ariel",12,"bold"),text="Gender",padx=2,pady=6)
        la_gender.grid(row=2,column=0,sticky=W)
        combo_gender=ttk.Combobox(labelframeleft,textvariable=self.var_gender,font=("ariel",12,"bold"),width=27)
        combo_gender["value"]=("Male", "Female", "Other")
        combo_gender.current(0)
        combo_gender.grid(row=2,column=1)


        #address
        la_code=Label(labelframeleft,font=("ariel",12,"bold"),text="Address:",padx=2,pady=6)
        la_code.grid(row=3,column=0,sticky=W)
        txtcode=ttk.Entry(labelframeleft,textvariable=self.var_address,font=("times new roman",13,"bold"),width=29)
        txtcode.grid(row=3,column=1)

        #mobile number
        la_mobile=Label(labelframeleft,font=("ariel",12,"bold"),text="Mobile No:",padx=2,pady=6)
        la_mobile.grid(row=4,column=0,sticky=W)
        txtno=ttk.Entry(labelframeleft,textvariable=self.var_mobile,font=("times new roman",13,"bold"),width=29)
        txtno.grid(row=4,column=1)

        #email
        la_email=Label(labelframeleft,font=("ariel",12,"bold"),text="Email:",padx=2,pady=6)
        la_email.grid(row=5,column=0,sticky=W)
        txtemail=ttk.Entry(labelframeleft,textvariable=self.var_email,font=("times new roman",13,"bold"),width=29)
        txtemail.grid(row=5,column=1)

        '''#previously visited or not
        la_visited=Label(labelframeleft,font=("ariel",12,"bold"),text="Previously visited",padx=2,pady=6)
        la_visited.grid(row=6,column=0,sticky=W)
        combo_visit=ttk.Combobox(labelframeleft,textvariable=self.var_visited,font=("ariel",12,"bold"),width=27,state="readonly")
        combo_visit["value"]=("Yes", "No")
        combo_visit.current(0)
        combo_visit.grid(row=6,column=1)'''


        #can add id proof here 



        #age
        la_add=Label(labelframeleft,font=("ariel",12,"bold"),text="Age:",padx=2,pady=6)
        la_add.grid(row=6,column=0,sticky=W)
        txtadd=ttk.Entry(labelframeleft,textvariable=self.var_age,font=("times new roman",13,"bold"),width=29)
        txtadd.grid(row=6,column=1)

         #disease
        la_add=Label(labelframeleft,font=("ariel",12,"bold"),text="Disease:",padx=2,pady=6)
        la_add.grid(row=7,column=0,sticky=W)
        txtadd=ttk.Entry(labelframeleft,textvariable=self.var_disease,font=("times new roman",13,"bold"),width=29)
        txtadd.grid(row=7,column=1)

         #staff id
        la_add=Label(labelframeleft,font=("ariel",12,"bold"),text="Staff ID:",padx=2,pady=6)
        la_add.grid(row=8,column=0,sticky=W)
        txtadd=ttk.Entry(labelframeleft,textvariable=self.var_sid,font=("times new roman",13,"bold"),width=29)
        txtadd.grid(row=8,column=1)


        ##update add
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



        #rightframebottom/////////////////////////////////////
        table_frame=LabelFrame(self.root,bd=2,relief=RIDGE,text="View Data",padx=2,font=("times new roman",12,"bold"))
        table_frame.place(x=435,y=50,width=860,height=490)

        searchby=Label(table_frame,font=("ariel",12,"bold"),text="Search",bg="light skyblue",fg="white")
        searchby.grid(row=0,column=0,sticky=W,padx=2)

        self.search_var=StringVar()
        combo_search=ttk.Combobox(table_frame,textvariable=self.search_var,font=("ariel",10),width=20,state="readonly")
        combo_search["value"]=("id", "Name","Mobile no.")
        combo_search.current(0)
        combo_search.grid(row=0,column=1,padx=2)

        self.txt_search=StringVar()
        txtsearch=ttk.Entry(table_frame,textvariable=self.txt_search,font=("times new roman",13),width=24)
        txtsearch.grid(row=0,column=2,padx=2)

        btnsearch=Button(table_frame,text="Search",command=self.search,font=("times new roman",13,"bold"),bg="skyblue",fg="black",width=12)
        btnsearch.grid(row=0,column=3,padx=1)

        btnshow=Button(table_frame,text="Show",command=self.fetch_data,font=("times new roman",13,"bold"),bg="skyblue",fg="black",width=12)
        btnshow.grid(row=0,column=4,padx=1)


        #showing data
        data_frame=Frame(table_frame,bd=2,relief=RIDGE)
        data_frame.place(x=0,y=50,width=860,height=350)

        scrollx=ttk.Scrollbar(data_frame,orient=HORIZONTAL)
        scrolly=ttk.Scrollbar(data_frame,orient=VERTICAL)

        self.patient_data=ttk.Treeview(data_frame,column=("p_id","p_name","p_gender","p_address","p_mobile","p_email","p_age","p_disease","s_id"),xscrollcommand=scrollx.set,yscrollcommand=scrolly.set)
        
        scrollx.pack(side=BOTTOM,fill=X)
        scrolly.pack(side=RIGHT,fill=Y)

        scrollx.config(command=self.patient_data.xview)
        scrolly.config(command=self.patient_data.yview)


        self.patient_data.heading("p_id",text="Patient ID")
        self.patient_data.heading("p_name",text="Patient name")
        self.patient_data.heading("p_gender",text="Gender")
        self.patient_data.heading("p_address",text="Address")
        self.patient_data.heading("p_mobile",text="Mobile No")
        self.patient_data.heading("p_email",text="Email")
        self.patient_data.heading("p_age",text="Age")
        self.patient_data.heading("p_disease",text="Disease")
        self.patient_data.heading("s_id",text="Staff id")

        self.patient_data["show"]="headings"

        self.patient_data.column("p_id",width=80)
        self.patient_data.column("p_name",width=80)
        self.patient_data.column("p_gender",width=80)
        self.patient_data.column("p_address",width=80)
        self.patient_data.column("p_mobile",width=80)
        self.patient_data.column("p_email",width=80)
        self.patient_data.column("p_age",width=80)
        self.patient_data.column("p_disease",width=80)
        self.patient_data.column("s_id",width=80)

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
            cursor.execute("insert into patients values(%s,%s,%s,%s,%s,%s,%s,%s,%s)",(
                                                                                    self.var_pid.get(),
                                                                                    self.var_name.get(),
                                                                                    self.var_gender.get(),
                                                                                    self.var_address.get(),
                                                                                    self.var_mobile.get(),
                                                                                    self.var_email.get(),
                                                                                    self.var_age.get(),
                                                                                    self.var_disease.get(),
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
        cursor.execute("select * from patients")
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
        self.var_pid.set(row[0]),
        self.var_name.set(row[1]),
        self.var_gender.set(row[2]),
        self.var_address.set(row[3]),
        self.var_mobile.set(row[4]),
        self.var_email.set(row[5]),
        self.var_age.set(row[6]),
        self.var_disease.set(row[7]),
        self.var_sid.set(row[8])

    def update(self):
        if self.var_mobile.get()=="":
            messagebox.showerror("Error","Enter mobile no",parent=self.root)
        else:
            con=mysql.connector.connect(host="localhost",username="root",password="password",database="hospital")
            cursor=con.cursor()
            cursor.execute("update patients set p_name=%s,p_gender=%s,p_address=%s,p_mobile=%s,p_email=%s,p_age=%s,p_disease=%s,s_id=%s where p_id=%s",(

                                                                                                                                        self.var_name.get(),
                                                                                                                                        self.var_gender.get(),
                                                                                                                                        self.var_address.get(),
                                                                                                                                        self.var_mobile.get(),
                                                                                                                                        self.var_email.get(),
                                                                                                                                        self.var_age.get(),
                                                                                                                                        self.var_disease.get(),
                                                                                                                                        self.var_sid.get(),
                                                                                                                                        self.var_pid.get()                                                                                
        ))
        con.commit()
        self.fetch_data()
        con.close()
        messagebox.showinfo("Update","Patient details has been updated",parent=self.root)

    def delete(self):
        delete=messagebox.askyesno("message","Confirm deletion",parent=self.root)
        if delete>0:
            con=mysql.connector.connect(host="localhost",username="root",password="password",database="hospital")
            cursor=con.cursor()
            query="delete from patients where p_id=%s"
            value=(self.var_pid.get(),)
            cursor.execute(query,value)
        else:
            if not delete:
                return
        con.commit()
        self.fetch_data()
        con.close()

    def reset(self):
        self.var_pid.set(""),
        self.var_name.set(""),
        #self.var_gender.set(""),
        self.var_address.set(""),
        self.var_mobile.set(""),
        self.var_email.set(""),
        self.var_age.set(""),
        self.var_disease.set(""),
        self.var_sid.set("")
        

         #   x=random.randint(100,200)
        #self.var_id.set(str(x))

    def search(self):
        con=mysql.connector.connect(host="localhost",username="root",password="password",database="hospital")
        cursor=con.cursor()
        cursor.execute("select * from patients where "+str(self.search_var.get())+" LIKE '%"+str(self.txt_search.get())+"%'")
        rows=cursor.fetchall()
        if len(rows)!=0:
            self.patient_data.delete(*self.patient_data.get_children())
            for i in rows:
                self.patient_data.insert("",END,values=i)
            con.commit()
        con.close()
    








if __name__=="__main__":
    root=Tk()
    obj=patient_window(root)
    root.mainloop()
