from tkinter import *
from PIL import ImageTk, Image
import pymysql
from tkinter import ttk,messagebox

class StudentIssue_Data:
    def __init__(self,root):
        self.root = root
        self.root.title("Nepalaya Library")
        self.root.geometry("1200x480+35+170")
        self.root.config(bg="white")
        self.root.focus_force()

        # ===========Variables========
        self.var_issueTo = StringVar()

        #self.bg = ImageTk.PhotoImage(file="image/student.jpg")
        #bg = Label(self.root, image=self.bg).place(x=0, y=0, relwidth=1, relheight=1)

        title = Label(self.root, text="Issue Report",font=("times new roman",20), fg="white", bg="#033054").place(x=0, y=0, relwidth=1,height=35)

        # Search Panel
        self.var_search = StringVar()
        lbl_search_roll = Label(self.root, text="Search By Book ID", bg="white").place(x=300, y=60)
        txt_search_roll = Entry(self.root, textvariable=self.var_search, bg="lightyellow")
        txt_search_roll.place(x=450,y=60,width=300)
       # btn_search=Button(self.root,text="Search",bg="#03a9f4",fg="white",cursor="hand2",command=self.searchStudented).place(x=470,y=60,width=120,height=20)
        txt_search_roll.bind("<Key>", self.searchIssue)

        # content
        self.C_Frame = Frame(self.root, bd=2, relief=RIDGE)
        self.C_Frame.place(x=190, y=100, width=780, height=340)

        scrolly = Scrollbar(self.C_Frame, orient=VERTICAL)
        scrollx = Scrollbar(self.C_Frame, orient=HORIZONTAL)
        self.issueReport = ttk.Treeview(self.C_Frame, columns=("bid", "issueTo", "issueBy", "date"), xscrollcommand=scrollx.set,yscrollcommand=scrolly.set)

        scrollx.pack(side=BOTTOM, fill=X)
        scrolly.pack(side=RIGHT, fill=Y)
        scrollx.config(command=self.issueReport.xview)
        scrolly.config(command=self.issueReport.yview)

        self.issueReport.heading("bid", text="Book ID")
        self.issueReport.heading("issueTo", text="Student ID")
        self.issueReport.heading("issueBy", text="Employee ID")
        self.issueReport.heading("date", text="Issue Date")
        self.issueReport["show"] = 'headings'
        self.issueReport.column("bid", width=50)
        self.issueReport.column("issueTo", width=150)
        self.issueReport.column("issueBy", width=150)
        self.issueReport.column("date", width=150)
        self.issueReport.pack(fill=BOTH, expand=1)
        # self.studentTable.bind("<ButtonRelease-1>",self.get_data)
        self.show()

        self.issueReport.pack(fill= BOTH,expand=1)


    #show

    def show(self):
        con = pymysql.connect(host="localhost", user="root", password="arrowoonbj1@", database="n_library")
        cur = con.cursor()
        try:
            cur.execute("SELECT * FROM issue")
            #WHERE issueTo = % s ", (self.var_issueTo.get(),)
            con.commit()
            rows = cur.fetchall()
            self.issueReport.delete(*self.issueReport.get_children())
            for row in rows:
                self.issueReport.insert('', END, value=(row[1], row[2], row[3], row[4]))
        except Exception as ex:
            messagebox.showerror("Error", f"Error due to {str(ex)}")

    def searchIssue(self,ev):
        #getStudent = "select * from " + studentTable
        con = pymysql.connect(host="localhost", user="root", password="arrowoonbj1@",database="n_library")
        cur = con.cursor()
        try:
            #cur.execute(getStudent)
            #con.commit()
            cur.execute("SELECT * FROM issue where bid LIKE '%"+self.var_search.get()+"%'")
            row = cur.fetchall()
            if len(row)>0:
                self.issueReport.delete(*self.issueReport.get_children())
                for i in row:
                    self.issueReport.insert('',END,value=(i[0],i[1],i[2],i[3]))
            else:
                self.issueReport.delete(*self.issueReport.get_children())
        except Exception as ex:
             messagebox.showerror("Error",f"Error due to {str(ex)}")




if __name__=="__main__":
    root=Tk()
    obj=StudentIssue_Data(root)
    root.mainloop()