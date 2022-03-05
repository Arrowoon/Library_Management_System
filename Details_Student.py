from tkinter import *
from PIL import ImageTk, Image
import pymysql
from tkinter import ttk,messagebox

mypass = "arrowoonbj1@"
mydatabase = "n_library"

class Student_Data:
    def __init__(self,root):
        self.root = root
        self.root.title("Nepalaya Library")
        self.root.geometry("1200x480+35+170")
        self.root.config(bg="white")
        self.root.focus_force()

        #self.bg = ImageTk.PhotoImage(file="image/student.jpg")
        #bg = Label(self.root, image=self.bg).place(x=0, y=0, relwidth=1, relheight=1)

        title = Label(self.root, text="Student Details",font=("times new roman",20), fg="white", bg="#033054").place(x=0, y=0, relwidth=1,height=35)

        # ===========Variables========
        self.var_stuid = StringVar()
        self.var_name = StringVar()
        self.var_semYear = StringVar()
        self.var_address = StringVar()
        self.var_email = StringVar()
        self.var_department = StringVar()

        # ==========Widgets======
        lbl_studentId = Label(self.root, text="Student ID:", font=("times new roman", 13, "bold"), bg="white").place(x=40,
                                                                                                               y=110)
        lbl_name = Label(self.root, text="Student Name:", font=("times new roman", 13, "bold"), bg="white").place(x=40,
                                                                                                                 y=150)
        lbl_semYear = Label(self.root, text="Semester/Year:", font=("times new roman", 13, "bold"), bg="white").place(x=40,
                                                                                                              y=190)
        lbl_address = Label(self.root, text="Address:", font=("times new roman", 13, "bold"), bg="white").place(x=40,
                                                                                                              y=230)
        lbl_email = Label(self.root, text="Email:", font=("times new roman", 13, "bold"), bg="white").place(
            x=40,y=270)
        lbl_department = Label(self.root, text="Department:", font=("times new roman", 13, "bold"),
                              bg="white").place(x=40,
                                                y=310)
        # ==========Entry Fields========
        self.txt_studentId = Entry(self.root, textvariable=self.var_stuid, font=("times new roman", 13, "bold"),
                                bg="lightyellow")
        self.txt_studentId.place(x=190, y=110, width=200)
        self.txt_name = Entry(self.root, textvariable=self.var_name, font=("times new roman", 13, "bold"),
                               bg="lightyellow")
        self.txt_name.place(x=190, y=150, width=200)
        self.txt_semYear = Entry(self.root, textvariable=self.var_semYear, font=("times new roman", 13, "bold"),
                                bg="lightyellow")
        self.txt_semYear.place(x=190, y=190, width=200)
        self.txt_address = Entry(self.root, textvariable=self.var_address, font=("times new roman", 13, "bold"),
                                bg="lightyellow")
        self.txt_address.place(x=190, y=230, width=200)
        self.txt_email = Entry(self.root, textvariable=self.var_email, font=("times new roman", 13, "bold"),
                                     bg="lightyellow")
        self.txt_email.place(x=190, y=270, width=200)
        self.txt_department = Entry(self.root, textvariable=self.var_department, font=("times new roman", 13, "bold"),
                                   bg="lightyellow")
        self.txt_department.place(x=190, y=310, width=200)

        # ==========Buttons=========
        self.btn_update = Button(self.root, text="Update", font=("times new roman", 15, "bold"), bg="#4caf50", fg="white",
                              cursor="hand2", command=self.update)
        self.btn_update.place(x=100, y=380, width=110, height=35)
        self.btn_delete = Button(self.root, text="Delete", font=("times new roman", 15, "bold"), bg="#f44336",
                                 fg="white", cursor="hand2", command=self.delete)
        self.btn_delete.place(x=220, y=380, width=110, height=35)






        # Search Panel
        self.var_search = StringVar()
        lbl_search_roll = Label(self.root, text="Search By Name", bg="white").place(x=500, y=60)
        txt_search_roll = Entry(self.root, textvariable=self.var_search, bg="lightyellow")
        txt_search_roll.place(x=650,y=60,width=300)
       # btn_search=Button(self.root,text="Search",bg="#03a9f4",fg="white",cursor="hand2",command=self.searchStudented).place(x=470,y=60,width=120,height=20)
        txt_search_roll.bind("<Key>", self.searchStudented)

        # content
        self.C_Frame = Frame(self.root, bd=2, relief=RIDGE)
        self.C_Frame.place(x=400, y=100, width=780, height=340)

        scrolly = Scrollbar(self.C_Frame, orient=VERTICAL)
        scrollx = Scrollbar(self.C_Frame, orient=HORIZONTAL)
        self.studentTable = ttk.Treeview(self.C_Frame, columns=("stuid", "fl_name", "sem_year", "address", "email", "department"), xscrollcommand=scrollx.set,yscrollcommand=scrolly.set)

        scrollx.pack(side=BOTTOM, fill=X)
        scrolly.pack(side=RIGHT, fill=Y)
        scrollx.config(command=self.studentTable.xview)
        scrolly.config(command=self.studentTable.yview)

        self.studentTable.heading("stuid", text="Student ID")
        self.studentTable.heading("fl_name", text="Name")
        self.studentTable.heading("sem_year", text="Semester/Year")
        self.studentTable.heading("address", text="Address")
        self.studentTable.heading("email", text="Email")
        self.studentTable.heading("department", text="Department")
        self.studentTable["show"] = 'headings'
        self.studentTable.column("stuid", width=50)
        self.studentTable.column("fl_name", width=150)
        self.studentTable.column("sem_year", width=150)
        self.studentTable.column("address", width=150)
        self.studentTable.column("email", width=150)
        self.studentTable.column("department", width=100)
        self.studentTable.pack(fill=BOTH, expand=1)
        self.studentTable.bind("<ButtonRelease-1>",self.get_data)
        self.show()

        self.studentTable.pack(fill= BOTH,expand=1)

    def clear(self):
        self.show()
        self.var_stuid.set("")
        self.var_name.set("")
        self.var_semYear.set("")
        self.var_search.set("")
        self.var_address.set("")
        self.var_email.set("")
        self.var_department.set("")
        self.txt_studentId.config(state="normal")



    def get_data(self,ev):
        self.txt_studentId.config(state="readonly")
        self.txt_studentId
        r=self.studentTable.focus()
        content=self.studentTable.item(r)
        row=content["values"]
        #print(row)
        self.var_stuid.set(row[0])
        self.var_name.set(row[1])
        self.var_semYear.set(row[2])
        self.var_address.set(row[3])
        self.var_email.set(row[4])
        self.var_department.set(row[5])



    def update(self):
        con = pymysql.connect(host="localhost", user="root", password="arrowoonbj1@", database="n_library")
        cur = con.cursor()
        try:
            if self.var_stuid.get() == "":
                messagebox.showerror("Error","Student ID should be required", parent=self.root)
            else:
                cur.execute("select *  from student where stuid=%s", (self.var_stuid.get(),))
                row=cur.fetchone()
                if row==None:
                    messagebox.showerror("Error", "Select Student from list", parent=self.root)
                else:
                    cur.execute("update student set fl_name=%s,sem_year=%s,address=%s,email=%s,department=%s where  stuid=%s",(

                        self.var_name.get(),
                        self.var_semYear.get(),
                        self.var_address.get(),
                        self.var_email.get(),
                        self.var_department.get(),
                        self.var_stuid.get()

                    ))
                    con.commit()
                    messagebox.showinfo("Success", "Student Details Update Successful", parent=self.root)
                    self.show()

        except Exception as ex:
            messagebox.showerror("Error",f"Error due to {str(ex)}")

    def delete(self):
        con = pymysql.connect(host="localhost", user="root", password="arrowoonbj1@", database="n_library")
        cur = con.cursor()
        try:
            if self.var_stuid.get() == "":
                messagebox.showerror("Error", "Student ID should be required", parent=self.root)
            else:
                cur.execute("select *  from student where stuid=%s", (self.var_stuid.get(),))
                row = cur.fetchone()
                if row == None:
                    messagebox.showerror("Error", "Please select student from the list first", parent=self.root)
                else:
                    op=messagebox.askyesno("Confirm","Do you really want to delete?",parent=self.root)
                    if op==True:
                        cur.execute("delete from student where stuid=%s", (self.var_stuid.get(),))
                        con.commit()
                        messagebox.showinfo("Delete","Student Details deleted Successfully",parent=self.root)
                        self.clear()

        except Exception as ex:
            messagebox.showerror("Error",f"Error due to {str(ex)}")


    #===================================show====================================

    def show(self):
        con = pymysql.connect(host="localhost", user="root", password="arrowoonbj1@", database="n_library")
        cur = con.cursor()
        try:
            cur.execute("select * from student ")
            rows = cur.fetchall()
            self.studentTable.delete(*self.studentTable.get_children())

            for row in rows:
                self.studentTable.insert('', END, value=(row[0], row[1], row[2], row[3], row[4], row[5]))

        except Exception as ex:
            messagebox.showerror("Error", f"Error due to {str(ex)}")


    def searchStudented(self,ev):
        #getStudent = "select * from " + studentTable
        con = pymysql.connect(host="localhost", user="root", password=mypass,database=mydatabase)
        cur = con.cursor()
        try:
            #cur.execute(getStudent)
            #con.commit()
            cur.execute("SELECT * FROM student where fl_name LIKE '%"+self.var_search.get()+"%'")
            row = cur.fetchall()
            if len(row)>0:
                self.studentTable.delete(*self.studentTable.get_children())
                for i in row:
                    self.studentTable.insert('',END,value=(i[0],i[1],i[2],i[3],i[4],i[5]))
            else:
                self.studentTable.delete(*self.studentTable.get_children())
        except Exception as ex:
             messagebox.showerror("Error",f"Error due to {str(ex)}")




if __name__=="__main__":
    root=Tk()
    obj=Student_Data(root)
    root.mainloop()