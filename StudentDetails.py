from tkinter import *
from PIL import ImageTk, Image
import pymysql
from tkinter import ttk,messagebox

mypass = "arrowoonbj1@"
mydatabase = "n_library"

con = pymysql.connect(host="localhost", user="root", password=mypass, database=mydatabase)
cur = con.cursor()

studentTable = "student"  # Book Table
class Student_Data:
    def __init__(self,root):
        self.root = root
        self.root.title("Nepalaya Library")
        self.root.geometry("1200x480+35+170")
        self.root.config(bg="white")
        self.root.focus_force()

        #self.bg = ImageTk.PhotoImage(file="image/student.jpg")
        #bg = Label(self.root, image=self.bg).place(x=0, y=0, relwidth=1, relheight=1)

        title = Label(self.root, text="Issue Details",font=("times new roman",20), fg="white", bg="#033054").place(x=0, y=0, relwidth=1,height=35)

        # Search Panel
        self.var_search = StringVar()
        lbl_search_roll = Label(self.root, text="Search By Name", bg="white").place(x=300, y=60)
        txt_search_roll = Entry(self.root, textvariable=self.var_search, bg="lightyellow")
        txt_search_roll.place(x=450,y=60,width=300)
       # btn_search=Button(self.root,text="Search",bg="#03a9f4",fg="white",cursor="hand2",command=self.searchStudented).place(x=470,y=60,width=120,height=20)
        txt_search_roll.bind("<Key>", self.searchStudented)

        # content
        self.C_Frame = Frame(self.root, bd=2, relief=RIDGE)
        self.C_Frame.place(x=190, y=100, width=780, height=340)

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
        # self.studentTable.bind("<ButtonRelease-1>",self.get_data)
        self.show()

        self.studentTable.pack(fill= BOTH,expand=1)


    #show

    def show(self):
        #getStudent = "select * from " + studentTable
        con = pymysql.connect(host="localhost", user="root", password=mypass, database=mydatabase)
        cur = con.cursor()
        try:
            #cur.execute(getStudent)
            con.commit()
            cur.execute("SELECT * FROM student ORDER BY fl_name")
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