# ---------- Students page ----------

from tkinter import *
from tkinter import ttk
from tkinter import  messagebox
import pymysql


class Student :
    def __init__(self,root):
        self.root = root
        self.root.title("Student Data Management System")
        self.root.geometry("1360x710+0+0")

        title = Label(self.root , text="Student Data Management System" , bd=10 , relief=GROOVE , font=("Times new roman",40,"bold"),bg="#9aecf9",fg="#030939")
        title.pack(side=TOP,fill=X)

    #---------- All Variables ----------

        self.roll = StringVar()
        self.name = StringVar()
        self.email = StringVar()
        self.gender = StringVar()
        self.contact = StringVar()
        self.dob = StringVar()
        self.searchby = StringVar()
        self.searchtxt = StringVar()
        self.fees = StringVar()
        self.scholarship = StringVar()


# ---------- Manage Frame ----------

        ManageFrame = Frame(self.root , bd=4 , relief=RIDGE , bg="#030939")
        ManageFrame.place(x=20 , y=100 , width=450 , height=590)

        m_title = Label(ManageFrame , text="Manage Students" , bg="#030939" , fg="white" , font=("Times new roman",25,"bold"))
        m_title.grid(row=0 , columnspan=2 , pady=20)

        self.lblRoll = Label(ManageFrame , text="Roll No" , bg="#030939" , fg="white" , font=("Times new roman",15,"bold"))
        self.lblRoll.grid(row=1 , column=0 , pady=5 , padx=20 , sticky="w")

        self.txtRoll = Entry(ManageFrame , textvariable=self.roll ,  font=("Times new roman",15,"bold") , bd=5 , relief=GROOVE)
        self.txtRoll.grid(row=1 , column=1 , pady=5 , padx=20 , sticky="w")

        self.lblName = Label(ManageFrame, text="Name", bg="#030939", fg="white", font=("Times new roman", 15, "bold"))
        self.lblName.grid(row=2, column=0, pady=5, padx=20, sticky="w")

        self.txtName = Entry(ManageFrame, textvariable=self.name , font=("Times new roman", 15, "bold"), bd=5, relief=GROOVE)
        self.txtName.grid(row=2, column=1, pady=5, padx=20, sticky="w")

        self.lblEmail = Label(ManageFrame, text="Email", bg="#030939", fg="white", font=("Times new roman", 15, "bold"))
        self.lblEmail.grid(row=3, column=0, pady=5, padx=20, sticky="w")

        self.txtEmail = Entry(ManageFrame, textvariable=self.email , font=("Times new roman", 15, "bold"), bd=5, relief=GROOVE)
        self.txtEmail.grid(row=3, column=1, pady=5, padx=20, sticky="w")

        self.lblGender = Label(ManageFrame, text="Gender", bg="#030939", fg="white", font=("Times new roman", 15, "bold"))
        self.lblGender.grid(row=4, column=0, pady=5, padx=20, sticky="w")

        self.comboGender = ttk.Combobox(ManageFrame , textvariable=self.gender , font=("Times new roman", 13, "bold") , state="readonly")
        self.comboGender["values"]=("Male","Female","Other")
        self.comboGender.grid(row=4, column=1, pady=5, padx=20, sticky="w")
        self.comboGender.current(0)

        self.lblContact = Label(ManageFrame, text="Contact", bg="#030939", fg="white", font=("Times new roman", 15, "bold"))
        self.lblContact.grid(row=5, column=0, pady=5, padx=20, sticky="w")

        self.txtContact = Entry(ManageFrame, textvariable=self.contact , font=("Times new roman", 14, "bold"), bd=5, relief=GROOVE)
        self.txtContact.grid(row=5, column=1, pady=5, padx=20, sticky="w")

        self.lblDOB = Label(ManageFrame, text="DOB", bg="#030939", fg="white", font=("Times new roman", 15, "bold"))
        self.lblDOB.grid(row=6, column=0, pady=5, padx=20, sticky="w")

        self.txtDOB = Entry(ManageFrame, textvariable=self.dob , font=("Times new roman", 15, "bold"), bd=5, relief=GROOVE)
        self.txtDOB.grid(row=6, column=1, pady=5, padx=20, sticky="w")

        self.lblFees = Label(ManageFrame, text="Fees", bg="#030939", fg="white", font=("Times new roman", 15, "bold"))
        self.lblFees.grid(row=7, column=0, pady=5, padx=20, sticky="w")

        self.txtFees = Entry(ManageFrame, textvariable=self.fees, font=("Times new roman", 14, "bold"), bd=5,relief=GROOVE)
        self.txtFees.grid(row=7, column=1, pady=5, padx=20, sticky="w")

        self.lblScholarship = Label(ManageFrame, text="Scholarship Y/N", bg="#030939", fg="white", font=("Times new roman", 15, "bold"))
        self.lblScholarship.grid(row=8, column=0, pady=5, padx=20, sticky="w")

        self.txtScholarship = Entry(ManageFrame, textvariable=self.scholarship, font=("Times new roman", 14, "bold"), bd=5,relief=GROOVE)
        self.txtScholarship.grid(row=8, column=1, pady=5, padx=20, sticky="w")

        self.lblAddress = Label(ManageFrame, text="Address", bg="#030939", fg="white", font=("Times new roman", 15, "bold"))
        self.lblAddress.grid(row=9, column=0, pady=5, padx=20, sticky="w")

        self.txtAddress = Text(ManageFrame , width=19 , height=3 , font=("" , 15))
        self.txtAddress.grid(row=9, column=1, pady=5, padx=20, sticky="w")


    # ---------- Button Frame ----------

        ButtonFrame = Frame(ManageFrame , bd=4, relief=RIDGE, bg="#030939")
        ButtonFrame.place(x=13, y=520, width=420)

        add = Button(ButtonFrame , text="Add" , width=10 , command=self.addStudents).grid(row=0 , column=0 , padx=10 , pady=10)
        update = Button(ButtonFrame, text="Update", width=10 , command=self.updateData).grid(row=0, column=1, padx=10, pady=10)
        delete = Button(ButtonFrame, text="Delete", width=10 , command=self.deleteData).grid(row=0, column=2, padx=10, pady=10)
        clear = Button(ButtonFrame, text="Clear", width=10 , command=self.clear).grid(row=0, column=3, padx=10, pady=10)


# ---------- Details Frame ----------

        DetailsFrame = Frame(self.root, bd=4, relief=RIDGE, bg="#030939")
        DetailsFrame.place(x=500, y=100, width=840, height=590)

        self.lblSearch =  Label(DetailsFrame , text="Search By", bg="#030939", fg="white", font=("Times new roman", 20, "bold"))
        self.lblSearch.grid(row=0, column=0, pady=10, padx=20, sticky="w")

        self.comboSearch = ttk.Combobox(DetailsFrame , textvariable=self.searchby , width=10 , font=("Times new roman", 13, "bold"), state="readonly")
        self.comboSearch["values"] = ("RollNo", "Name", "Contact")
        self.comboSearch.current(0)
        self.comboSearch.grid(row=0, column=1, pady=10, padx=20, sticky="w")

        self.txtSearch = Entry(DetailsFrame , textvariable=self.searchtxt , width=15 , font=("Times new roman", 14, "bold"), bd=5, relief=GROOVE)
        self.txtSearch.grid(row=0, column=2, pady=10, padx=20, sticky="w")

        searchbtn = Button(DetailsFrame , text="Search", width=10 , pady=5 , command=self.searchData).grid(row=0, column=3, padx=10, pady=10)
        showbtn = Button(DetailsFrame , text="Show All", width=10 , pady=5 , command=self.fetchData).grid(row=0, column=4, padx=10, pady=10)

# ---------- Information Frame --------

        infoFrame = Frame(DetailsFrame, relief=RIDGE, bg="#030939")
        infoFrame.place(x=10, y=500, width=800, height=60)

        self.lblinfo = Label(infoFrame, text="", bg="#030939", fg="white",font=("Times new roman", 20, "bold"))
        self.lblinfo.grid(row=0, column=0, pady=10, padx=20, sticky="w")

# ---------- Table Frame ----------

        TableFrame = Frame(DetailsFrame, bd=4, relief=RIDGE, bg="#030939")
        TableFrame.place(x=10, y=80, width=800, height=400)

        scroll_x = Scrollbar(TableFrame , orient=HORIZONTAL)
        scroll_y = Scrollbar(TableFrame, orient=VERTICAL)
        self.StudentTable = ttk.Treeview(TableFrame , columns=("RollNo","Name","Email","Gender","Contact","DOB","Fees","Scholarship","Address") , xscrollcommand=scroll_x.set , yscrollcommand=scroll_y.set)
        scroll_x.pack(side=BOTTOM , fill=X)
        scroll_y.pack(side=RIGHT , fill=Y)
        scroll_x.config(command=self.StudentTable.xview)
        scroll_y.config(command=self.StudentTable.yview)
        self.StudentTable.heading("RollNo" , text="Roll No.")
        self.StudentTable.heading("Name", text="Name")
        self.StudentTable.heading("Email", text="Email")
        self.StudentTable.heading("Gender", text="Gender")
        self.StudentTable.heading("Contact", text="Contact")
        self.StudentTable.heading("DOB", text="D.O.B")
        self.StudentTable.heading("Fees", text="Fees")
        self.StudentTable.heading("Scholarship", text="Scholarship")
        self.StudentTable.heading("Address", text="Address")

        self.StudentTable["show"] = "headings"
        self.StudentTable.column("RollNo",width=50)
        self.StudentTable.column("Name", width=150)
        self.StudentTable.column("Email", width=100)
        self.StudentTable.column("Gender", width=100)
        self.StudentTable.column("Contact", width=100)
        self.StudentTable.column("DOB", width=100)
        self.StudentTable.column("Fees", width=100)
        self.StudentTable.column("Scholarship", width=100)
        self.StudentTable.column("Address", width=200)
        self.StudentTable.pack(fill=BOTH , expand=1)
        self.StudentTable.bind("<ButtonRelease-1>" , self.getCursor)
        self.fetchData()

    def addStudents(self):
        self.lblinfo.config(text="")
        try:
            if self.txtRoll.get()=="" or self.txtName.get()=="":
                self.lblinfo.config(text="Mandatory fields left empty !!")
                #messagebox.showerror("Error","Mandatory fields left empty !!")
            elif len(self.txtContact.get())!=10:
                self.lblinfo.config(text="Invalid contact !!")
                #messagebox.showerror("Error","Invalid contact !!")
            else :
                conn = pymysql.connect(host="LOCALHOST" , user="root" , password="" , database="dbms")
                cur = conn.cursor()
                cur.execute("insert into students values(%s,%s,%s,%s,%s,%s,%s,%s,%s)" , (self.txtRoll.get(),
                                                                                   self.txtName.get(),
                                                                                   self.txtEmail.get(),
                                                                                   self.comboGender.get(),
                                                                                   self.txtContact.get(),
                                                                                   self.txtDOB.get(),
                                                                                   self.txtFees.get(),
                                                                                   self.txtScholarship.get(),
                                                                                   self.txtAddress.get('1.0',END)
                                                                                   ))
                conn.commit()
                self.fetchData()
                self.clear()
                conn.close()
                self.lblinfo.config(text="Record Inserted !!")
                #messagebox.showinfo("Success" , "Record inserted")
        except:
            self.lblinfo.config(text="Cannot Insert")
            #messagebox.showerror("Error","Cannot Insert")

    # Adds data to StudentTable
    def fetchData(self):
        self.lblinfo.config(text="")
        conn = pymysql.connect(host="LOCALHOST", user="root", password="", database="dbms")
        cur = conn.cursor()
        cur.execute("select * from students")
        rows = cur.fetchall()
        if len(rows) != 0 :
            self.StudentTable.delete(*self.StudentTable.get_children())
            for row in rows:
                self.StudentTable.insert('',END,values=row)
            conn.commit()
        conn.close()

    def clear(self):
        self.lblinfo.config(text="")
        self.txtRoll.delete(0,END)
        self.txtName.delete(0 , END)
        self.txtEmail.delete(0, END)
        self.comboGender.delete(0, END)
        self.txtContact.delete(0, END)
        self.txtDOB.delete(0, END)
        self.txtFees.delete(0, END)
        self.txtScholarship.delete(0, END)
        self.txtAddress.delete('1.0',END)

    def getCursor(self,ev):
        self.lblinfo.config(text="")
        cursor_row = self.StudentTable.focus()
        content = self.StudentTable.item(cursor_row)
        row = content["values"]
        self.txtRoll.delete(0, END)
        self.txtRoll.insert(END,row[0])
        self.txtName.delete(0, END)
        self.txtName.insert(END,row[1])
        self.txtEmail.delete(0, END)
        self.txtEmail.insert(END,row[2])
        self.comboGender.set(row[3])
        self.txtContact.delete(0, END)
        self.txtContact.insert(END,row[4])
        self.txtDOB.delete(0, END)
        self.txtDOB.insert(END,row[5])
        self.txtFees.delete(0, END)
        self.txtFees.insert(END,row[6])
        self.txtScholarship.delete(0, END)
        self.txtScholarship.insert(END,row[7])
        self.txtAddress.delete('1.0', END)
        self.txtAddress.insert(END,row[8])

    def updateData(self):
        try:
            if self.txtRoll.get()=="" or self.txtName.get()=="":
                self.lblinfo.config(text="Mandatory fields left empty !!")
                #messagebox.showerror("Error","Mandatory fields left empty !!")
            elif len(self.txtContact.get())!=10:
                self.lblinfo.config(text="Invalid contact !!")
                #messagebox.showerror("Error","Invalid contact !!")
            else :
                self.lblinfo.config(text="")
                conn = pymysql.connect(host="LOCALHOST", user="root", password="", database="dbms")
                cur = conn.cursor()
                opt = messagebox.askyesno("Warning", "Do you want to update the record ?",parent=self.root)
                if opt == True:
                    cur.execute("update students set Name=%s,Email=%s,Gender=%s,Contact=%s,DOB=%s,Fees=%s,Scholarship=%s,Address=%s where RollNo=%s", (
                                                                                      self.txtName.get(),
                                                                                      self.txtEmail.get(),
                                                                                      self.comboGender.get(),
                                                                                      self.txtContact.get(),
                                                                                      self.txtDOB.get(),
                                                                                      self.txtFees.get(),
                                                                                      self.txtScholarship.get(),
                                                                                      self.txtAddress.get('1.0', END),
                                                                                      self.txtRoll.get()
                                                                                      ))

                    conn.commit()
                    self.fetchData()
                    self.clear()
                    conn.close()
                    self.lblinfo.config(text="Record Updated")
                    #messagebox.showinfo("Success" , "Record updated")
                else:
                    self.lblinfo.config(text="Record Not Updated")
        except:
            self.lblinfo.config(text="Cannot update")

    def deleteData(self):
        try:
            self.lblinfo.config(text="")
            conn = pymysql.connect(host="LOCALHOST", user="root", password="", database="dbms")
            cur = conn.cursor()
            opt = messagebox.askyesno("Warning", "Do you want to delete the record ?",parent=self.root)
            if opt == True:
                cur.execute("delete from students where RollNo LIKE %s" , self.txtRoll.get())
                conn.commit()
                conn.close()
                self.fetchData()
                self.clear()
                self.lblinfo.config(text="Record Deleted !!")
            else:
                self.lblinfo.config(text="Record Not Deleted !!")
        except:
            self.lblinfo.config(text="Cannot Delete")

    def searchData(self):
        self.lblinfo.config(text="")
        try:
            conn = pymysql.connect(host="LOCALHOST", user="root", password="", database="dbms")
            cur = conn.cursor()
            cur.execute("select * from students where " + str(self.comboSearch.get()) + " LIKE '%" + str(self.txtSearch.get()) + "%'")
            rows = cur.fetchall()
            if len(rows) != 0 :
                self.StudentTable.delete(*self.StudentTable.get_children())
                for row in rows:
                    self.StudentTable.insert('',END,values=row)
                conn.commit()
            conn.close()
        except:
            self.lblinfo.config(text="Please enter values")



"""root = Tk()
ob = Student(root)
root.mainloop()"""
