from tkinter import *
from PIL import Image,ImageTk
from tkinter import ttk,messagebox
import pymysql



class returnBook:

    def __init__(self,root):
        self.root=root
        self.root.title("Nepalaya Library")
        self.root.geometry("1200x480+35+170")
        self.root.config(bg="white")
        self.root.focus_force()

        #==========Title=========
        title = Label(self.root, text="Return Book Details",
                      font=("times new roman", 18, "bold"), bg="#033054", fg="white").place(x=10, y=10, width=1180,
                                                                                            height=30)
        #===========Variables========
        self.var_bid=StringVar()
        self.var_returnBy = StringVar()
        self.var_returnTo = StringVar()
        self.var_date=StringVar()



        #==========Widgets======
        lbl_bookId=Label(self.root,text="Book ID:",font=("times new roman",13,"bold"),bg="white").place(x=60,y=110)
        lbl_studentId = Label(self.root, text="Return By(Student ID):", font=("times new roman", 13, "bold"), bg="white").place(x=60,
                                                                                                              y=190)
        lbl_employeeID = Label(self.root, text="Return To(Employee ID):", font=("times new roman", 13, "bold"), bg="white").place(x=60,
                                                                                                              y=230)
        lbl_date = Label(self.root, text="Issue Date:", font=("times new roman", 13, "bold"), bg="white").place(x=60,
                                                                                                              y=270)
        #==========Entry Fields========
        self.txt_bookId = Entry(self.root, textvariable=self.var_bid, font=("times new roman", 13, "bold"), bg="lightyellow")
        self.txt_bookId.place(x=240, y=110, width=200)
        self.txt_studentId = Entry(self.root, textvariable=self.var_returnBy, font=("times new roman", 13, "bold"), bg="lightyellow")
        self.txt_studentId.place(x=240, y=190, width=200)
        self.txt_employeeId = Entry(self.root, textvariable=self.var_returnTo,  font=("times new roman", 13, "bold"), bg="lightyellow")
        self.txt_employeeId.place(x=240, y=230, width=200)
        self.txt_data = Entry(self.root, textvariable=self.var_date, font=("times new roman", 13, "bold"),
                                   bg="lightyellow")
        self.txt_data.place(x=240, y=270, width=200)


        #==========Buttons=========
        self.btn_return=Button(self.root,text="Return",font=("times new roman",15,"bold"), bg="#4caf50", fg="white", cursor="hand2",command=self.returns)
        self.btn_return.place(x=250,y=350,width=110,height=35)


        #==========Search Panel=======
        self.var_search_id=StringVar()
        lbl_search_id = Label(self.root, text="Search By Student ID:", font=("times new roman", 13, "bold"), bg="white").place(x=610,
                                                                                                               y=60)
        txt_search_id = Entry(self.root, textvariable=self.var_search_id, font=("times new roman", 13, "bold"),bg="lightyellow").place(x=790, y=60, width=190)
        btn_return = Button(self.root, text="Search", font=("times new roman", 15, "bold"), bg="#03a9f4", fg="white",
                              cursor="hand2",command=self.search).place(x=1000, y=60, width=110, height=23)

        #===========Content==================
        self.C_Frame=Frame(self.root,bd=2,relief=RIDGE)
        self.C_Frame.place(x=580,y=100,width=570,height=340)

        scrolly=Scrollbar(self.C_Frame,orient=VERTICAL)
        scrollx=Scrollbar(self.C_Frame,orient=HORIZONTAL)


        self.ReturnTable=ttk.Treeview(self.C_Frame,columns=("bid","returnBy","returnTo","date"),xscrollcommand=scrollx.set,yscrollcommand=scrolly.set)
        scrollx.pack(side=BOTTOM,fill=X)
        scrolly.pack(side=RIGHT, fill=Y)
        scrollx.config(command=self.ReturnTable.xview)
        scrolly.config(command=self.ReturnTable.yview)
        self.ReturnTable.heading("bid",text="Book ID")
        self.ReturnTable.heading("returnBy", text="Return By(Student ID)")
        self.ReturnTable.heading("returnTo", text="Return To(Employee ID)")
        self.ReturnTable.heading("date", text="Return Date")
        self.ReturnTable["show"]='headings'
        self.ReturnTable.column("bid",width=50 )
        self.ReturnTable.column("returnBy",width=150 )
        self.ReturnTable.column("returnTo",width=150 )
        self.ReturnTable.column("date",width=150 )
        self.ReturnTable.pack(fill=BOTH,expand=1)
        self.ReturnTable.bind("<ButtonRelease-1>",self.get_data)
        self.show()


    #===========================================================================================
    def get_data(self,ev):
        self.txt_bookId.config(state="readonly")
        self.txt_bookId
        r=self.ReturnTable.focus()
        content=self.ReturnTable.item(r)
        row=content["values"]
        #print(row)
        self.var_bid.set(row[0])
        self.var_returnBy.set(row[1])
        self.var_returnTo.set(row[2])
        self.var_date.set(row[3])


    def returns(self):
        try:
            con = pymysql.connect(host="localhost", user="root", password="arrowoonbj1@", database="n_library")
            cur = con.cursor()
            cur.execute("select bid from books where bid=%s ",(self.txt_bookId.get()))
            row = cur.fetchone()
            if row != None:
                cur.execute("select bid,emp_id,issueTo from issue,employee where bid=%s and emp_id=%s and issueTo=%s ", (self.txt_bookId.get(),self.txt_employeeId.get(),self.txt_studentId.get()))
                rows = cur.fetchone()
                if rows != None:
                    cur.execute("insert into returns(bid,returnBy,returnTo,date) value(%s,%s,%s,%s)", (
                            self.var_bid.get(),
                            self.var_returnBy.get(),
                            self.var_returnTo.get(),
                            self.var_date.get()
                    ))
                    con.commit()
                    cur.execute("update books set noOfBook=noOfBook+1 where bid=%s ", (self.txt_bookId.get()))
                    cur.execute("delete from issue where issueTo=%s ",(self.txt_studentId.get()))
                    con.commit()

                    con.close()
                    messagebox.showinfo("Success", "Book Return Successful", parent=self.root)
                    self.show()
                else:
                    messagebox.showerror("Error", "Book ID|Student ID not Present", parent=self.root)
            else:
                messagebox.showerror("Error", "Book ID not Present", parent=self.root)
        except Exception as es:
            messagebox.showerror("Error", f"Error Due to: {str(es)}", parent=self.root)


    def show(self):
        con = pymysql.connect(host="localhost", user="root", password="arrowoonbj1@", database="n_library")
        cur = con.cursor()
        try:
            cur.execute("select *  from returns ")
            rows=cur.fetchall()
            self.ReturnTable.delete(*self.ReturnTable.get_children())
            for row in rows:
                self.ReturnTable.insert('',END,values=row)

        except Exception as ex:
            messagebox.showerror("Error",f"Error due to {str(ex)}")
    def search(self):
        con = pymysql.connect(host="localhost", user="root", password="arrowoonbj1@", database="n_library")
        cur = con.cursor()
        try:
            cur.execute(f"select *  from returns where returnBy LIKE '%{self.var_search_id.get()}%'")
            rows=cur.fetchall()
            self.ReturnTable.delete(*self.ReturnTable.get_children())
            for row in rows:
                self.ReturnTable.insert('',END,values=row)

        except Exception as ex:
            messagebox.showerror("Error",f"Error due to {str(ex)}")

if __name__=="__main__":
    root=Tk()
    obj=returnBook(root)
    root.mainloop()