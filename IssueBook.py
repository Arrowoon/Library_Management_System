from tkinter import *
from PIL import Image,ImageTk
from tkinter import ttk,messagebox
import pymysql



class issueBook:

    def __init__(self,root):
        self.root=root
        self.root.title("Nepalaya Library")
        self.root.geometry("1200x480+35+170")
        self.root.config(bg="white")
        self.root.focus_force()

        #==========Title=========
        title = Label(self.root, text="Isuee Book Details",
                      font=("times new roman", 18, "bold"), bg="#033054", fg="white").place(x=10, y=10, width=1180,
                                                                                            height=30)
        #===========Variables========
        self.var_bid=StringVar()
        self.var_issueTo = StringVar()
        self.var_issueBy = StringVar()
        self.var_date=StringVar()
       # self.int_noOfBook=IntVar()



        #==========Widgets======
        lbl_bookId=Label(self.root,text="Book ID:",font=("times new roman",13,"bold"),bg="white").place(x=60,y=110)
        lbl_studentId = Label(self.root, text="Issue To(Student ID):", font=("times new roman", 13, "bold"), bg="white").place(x=60,
                                                                                                              y=190)
        lbl_employeeID = Label(self.root, text="Issue By(Employee ID):", font=("times new roman", 13, "bold"), bg="white").place(x=60,
                                                                                                              y=230)
        lbl_date = Label(self.root, text="Issue Date:", font=("times new roman", 13, "bold"), bg="white").place(x=60,
                                                                                                              y=270)
        #==========Entry Fields========
        self.txt_bookId = Entry(self.root, textvariable=self.var_bid, font=("times new roman", 13, "bold"), bg="lightyellow")
        self.txt_bookId.place(x=240, y=110, width=200)
        self.txt_studentId = Entry(self.root, textvariable=self.var_issueTo, font=("times new roman", 13, "bold"), bg="lightyellow")
        self.txt_studentId.place(x=240, y=190, width=200)
        self.txt_employeeId = Entry(self.root, textvariable=self.var_issueBy,  font=("times new roman", 13, "bold"), bg="lightyellow")
        self.txt_employeeId.place(x=240, y=230, width=200)
        self.txt_data = Entry(self.root, textvariable=self.var_date, font=("times new roman", 13, "bold"),
                                   bg="lightyellow")
        self.txt_data.place(x=240, y=270, width=200)


        #==========Buttons=========
        self.btn_issue=Button(self.root,text="Issue",font=("times new roman",15,"bold"), bg="#4caf50", fg="white", cursor="hand2",command=self.issue)
        self.btn_issue.place(x=250,y=350,width=110,height=35)


        #==========Search Panel=======
        self.var_search_id=StringVar()
        lbl_search_id = Label(self.root, text="Search By Student ID:", font=("times new roman", 13, "bold"), bg="white").place(x=610,
                                                                                                               y=60)
        txt_search_id = Entry(self.root, textvariable=self.var_search_id, font=("times new roman", 13, "bold"),bg="lightyellow").place(x=790, y=60, width=190)
        btn_issue = Button(self.root, text="Search", font=("times new roman", 15, "bold"), bg="#03a9f4", fg="white",
                              cursor="hand2",command=self.search).place(x=1000, y=60, width=110, height=23)

        #===========Content==================
        self.C_Frame=Frame(self.root,bd=2,relief=RIDGE)
        self.C_Frame.place(x=580,y=100,width=570,height=340)

        scrolly=Scrollbar(self.C_Frame,orient=VERTICAL)
        scrollx=Scrollbar(self.C_Frame,orient=HORIZONTAL)


        self.IssueTable=ttk.Treeview(self.C_Frame,columns=("bid","issueTo","issueBy","date"),xscrollcommand=scrollx.set,yscrollcommand=scrolly.set)
        scrollx.pack(side=BOTTOM,fill=X)
        scrolly.pack(side=RIGHT, fill=Y)
        scrollx.config(command=self.IssueTable.xview)
        scrolly.config(command=self.IssueTable.yview)
        self.IssueTable.heading("bid",text="Book ID")
        self.IssueTable.heading("issueTo", text="Issue To(Student ID)")
        self.IssueTable.heading("issueBy", text="Issue By(Employee ID)")
        self.IssueTable.heading("date", text="Issue Date")
        self.IssueTable["show"]='headings'
        self.IssueTable.column("bid",width=50 )
        self.IssueTable.column("issueTo",width=150 )
        self.IssueTable.column("issueBy",width=150 )
        self.IssueTable.column("date",width=150 )
        self.IssueTable.pack(fill=BOTH,expand=1)
        self.IssueTable.bind("<ButtonRelease-1>",self.get_data)
        self.show()


    #===========================================================================================
    def get_data(self,ev):
        self.txt_bookId.config(state="readonly")
        self.txt_bookId
        r=self.IssueTable.focus()
        content=self.IssueTable.item(r)
        row=content["values"]
        #print(row)
        self.var_bid.set(row[0])
        self.var_issueTo.set(row[1])
        self.var_issueBy.set(row[2])
        self.var_date.set(row[3])


    def issue(self):
        try:
            con = pymysql.connect(host="localhost", user="root", password="arrowoonbj1@", database="n_library")
            cur = con.cursor()
            cur.execute("select bid,noOfBook,stuid,emp_id from books,student,employee where bid=%s and stuid=%s and emp_id=%s ",(self.txt_bookId.get(),self.txt_studentId.get(),self.txt_employeeId.get()))
            row = cur.fetchone()

            if row == None:
                messagebox.showerror("Error", "Book ID|Student ID|Employee ID not Present", parent=self.root)

            elif row != None:
                #cur.execute("select noOfBook from books where noOfBook=%d")
                #rows = cur.fetchone()

                #for i in row:
                    #if i[1]>0:
                cur.execute("insert into issue(bid,issueTo,issueBy,date) value(%s,%s,%s,%s)", (
                            self.var_bid.get(),
                            self.var_issueTo.get(),
                            self.var_issueBy.get(),
                            self.var_date.get()
                ))
                con.commit()
                cur.execute("update books set noOfBook=noOfBook-1 where bid=%s ", (self.txt_bookId.get()))
                con.commit()
                con.close()
                messagebox.showinfo("Success", "Book Issue Successful", parent=self.root)
                self.show()
                    #else:
                        #messagebox.showerror("Unavailable","Book unavailable",parent=self.root)
        except Exception as es:
            messagebox.showerror("Error", f"Error Due to: {str(es)}", parent=self.root)


    def show(self):
        con = pymysql.connect(host="localhost", user="root", password="arrowoonbj1@", database="n_library")
        cur = con.cursor()
        try:
            cur.execute("select *  from issue ")
            rows=cur.fetchall()
            self.IssueTable.delete(*self.IssueTable.get_children())
            for row in rows:
                self.IssueTable.insert('',END,values=(row[1], row[2], row[3], row[4]))

        except Exception as ex:
            messagebox.showerror("Error",f"Error due to {str(ex)}")
    def search(self):
        con = pymysql.connect(host="localhost", user="root", password="arrowoonbj1@", database="n_library")
        cur = con.cursor()
        try:
            cur.execute(f"select *  from issue where issueTo LIKE '%{self.var_search_id.get()}%'")
            rows=cur.fetchall()
            self.IssueTable.delete(*self.IssueTable.get_children())
            for row in rows:
                self.IssueTable.insert('',END,values=row)

        except Exception as ex:
            messagebox.showerror("Error",f"Error due to {str(ex)}")

if __name__=="__main__":
    root=Tk()
    obj=issueBook(root)
    root.mainloop()