from tkinter import *
from PIL import Image,ImageTk
from tkinter import ttk,messagebox
import pymysql
class EmpBook:
    def __init__(self,root):
        self.root=root
        self.root.title("Nepalaya Library")
        self.root.geometry("1200x480+35+170")
        self.root.config(bg="white")
        self.root.focus_force()

        #==========Title=========
        title = Label(self.root, text="Management Book Details",
                      font=("times new roman", 18, "bold"), bg="#033054", fg="white").place(x=10, y=10, width=1180,
                                                                                            height=30)
        #===========Variables========
        self.var_bid=StringVar()
        self.var_title = StringVar()
        self.var_course = StringVar()
        self.var_author = StringVar()
        self.var_publication = StringVar()
        self.var_totalNum = StringVar()



        #==========Widgets======
        lbl_bookId=Label(self.root,text="Book ID:",font=("times new roman",13,"bold"),bg="white").place(x=40,y=80)
        lbl_title = Label(self.root, text="Book Title:", font=("times new roman", 13, "bold"), bg="white").place(x=40,
                                                                                                              y=120)
        lbl_course = Label(self.root, text="Course:", font=("times new roman", 13, "bold"), bg="white").place(x=40,
                                                                                                              y=160)
        lbl_author = Label(self.root, text="Author:", font=("times new roman", 13, "bold"), bg="white").place(x=40,
                                                                                                              y=200)
        lbl_publication = Label(self.root, text="Publication:", font=("times new roman", 13, "bold"), bg="white").place(x=40,
                                                                                                              y=240)
        lbl_numOfBook = Label(self.root, text="Number Of Books:", font=("times new roman", 13, "bold"), bg="white").place(x=40,
                                                                                                              y=280)
        #==========Entry Fields========
        self.txt_bookId = Entry(self.root, textvariable=self.var_bid, font=("times new roman", 13, "bold"), bg="lightyellow")
        self.txt_bookId.place(x=190, y=80, width=200)
        self.txt_title = Entry(self.root, textvariable=self.var_title, font=("times new roman", 13, "bold"), bg="lightyellow")
        self.txt_title.place(x=190,y=120, width=200)
        self.txt_course = Entry(self.root, textvariable=self.var_course, font=("times new roman", 13, "bold"), bg="lightyellow")
        self.txt_course.place(x=190, y=160, width=200)
        self.txt_author = Entry(self.root, textvariable=self.var_author,  font=("times new roman", 13, "bold"), bg="lightyellow")
        self.txt_author.place(x=190, y=200, width=200)
        self.txt_publication = Entry(self.root, textvariable=self.var_publication, font=("times new roman", 13, "bold"),
                                   bg="lightyellow")
        self.txt_publication.place(x=190, y=240, width=200)
        self.txt_numOfBook = Entry(self.root, textvariable=self.var_totalNum, font=("times new roman", 13, "bold"),bg="lightyellow")
        self.txt_numOfBook.place(x=190, y=280, width=200)

        #==========Buttons=========
        self.btn_add=Button(self.root,text="Save",font=("times new roman",15,"bold"), bg="#2196f3", fg="white", cursor="hand2",command=self.add)
        self.btn_add.place(x=100,y=350,width=110,height=35)
        self.btn_update = Button(self.root, text="Update", font=("times new roman", 15, "bold"), bg="#4caf50", fg="white", cursor="hand2",command=self.update)
        self.btn_update.place(x=220, y=350, width=110, height=35)
        self.btn_delete = Button(self.root, text="Delete", font=("times new roman", 15, "bold"), bg="#f44336", fg="white", cursor="hand2",command=self.delete)
        self.btn_delete.place(x=340, y=350, width=110, height=35)
        self.btn_clear = Button(self.root, text="Clear", font=("times new roman", 15, "bold"), bg="#607d8b", fg="white", cursor="hand2",command=self.clear)
        self.btn_clear.place(x=460, y=350, width=110, height=35)


        #==========Search Panel=======
        self.var_search=StringVar()
        lbl_search_book = Label(self.root, text="Search By Title:", font=("times new roman", 13, "bold"), bg="white").place(x=680,
                                                                                                               y=60)
        txt_search_book = Entry(self.root, textvariable=self.var_search, font=("times new roman", 13, "bold"),bg="lightyellow").place(x=820, y=60, width=190)
        btn_search = Button(self.root, text="Search", font=("times new roman", 15, "bold"), bg="#03a9f4", fg="white",
                              cursor="hand2",command=self.search).place(x=1030, y=60, width=110, height=23)

        #===========Content==================
        self.C_Frame=Frame(self.root,bd=2,relief=RIDGE)
        self.C_Frame.place(x=620,y=100,width=570,height=340)

        scrolly=Scrollbar(self.C_Frame,orient=VERTICAL)
        scrollx=Scrollbar(self.C_Frame,orient=HORIZONTAL)


        self.BookTable=ttk.Treeview(self.C_Frame,columns=("bid","title","course","author","publication","noOfBook"),xscrollcommand=scrollx.set,yscrollcommand=scrolly.set)
        scrollx.pack(side=BOTTOM,fill=X)
        scrolly.pack(side=RIGHT, fill=Y)
        scrollx.config(command=self.BookTable.xview)
        scrolly.config(command=self.BookTable.yview)
        self.BookTable.heading("bid",text="Book ID")
        self.BookTable.heading("title", text="Book Title")
        self.BookTable.heading("course", text="Course")
        self.BookTable.heading("author", text="Author")
        self.BookTable.heading("publication", text="Publication Name")
        self.BookTable.heading("noOfBook", text="No Of Available Book")
        self.BookTable["show"]='headings'
        self.BookTable.column("bid",width=50 )
        self.BookTable.column("title", width=200)
        self.BookTable.column("course",width=100 )
        self.BookTable.column("author",width=150 )
        self.BookTable.column("publication",width=150 )
        self.BookTable.column("noOfBook",width=150 )
        self.BookTable.pack(fill=BOTH,expand=1)
        self.BookTable.bind("<ButtonRelease-1>",self.get_data)
        self.show()

    #=======================================================
    def clear(self):
        self.show()
        self.var_bid.set("")
        self.var_title.set("")
        self.var_course.set("")
        self.var_search.set("")
        self.var_author.set("")
        self.var_publication.set("")
        self.var_totalNum.set("")
        self.txt_bookId.config(state="normal")

    def delete(self):
        con = pymysql.connect(host="localhost", user="root", password="arrowoonbj1@", database="n_library")
        cur = con.cursor()
        try:
            if self.var_bid.get() == "":
                messagebox.showerror("Error", "Book ID should be required", parent=self.root)
            else:
                cur.execute("select *  from books where bid=%s", (self.var_bid.get(),))
                row = cur.fetchone()
                if row == None:
                    messagebox.showerror("Error", "Please select course from the list first", parent=self.root)
                else:
                    op=messagebox.askyesno("Confirm","Do you really want to delete?",parent=self.root)
                    if op==True:
                        cur.execute("delete from books where bid=%s", (self.var_bid.get(),))
                        con.commit()
                        messagebox.showinfo("Delete","Book deleted Successfully",parent=self.root)
                        self.clear()

        except Exception as ex:
            messagebox.showerror("Error",f"Error due to {str(ex)}")


    def get_data(self,ev):
        self.txt_bookId.config(state="readonly")
        self.txt_bookId
        r=self.BookTable.focus()
        content=self.BookTable.item(r)
        row=content["values"]
        #print(row)
        self.var_bid.set(row[0])
        self.var_title.set(row[1])
        self.var_course.set(row[2])
        self.var_author.set(row[3])
        self.var_publication.set(row[4])
        self.var_totalNum.set(row[5])

    def add(self):
        con = pymysql.connect(host="localhost", user="root", password="arrowoonbj1@", database="n_library")
        cur = con.cursor()
        try:
            if self.var_bid.get() == "":
                messagebox.showerror("Error","Book ID should be required", parent=self.root)
            else:
                cur.execute("select *  from books where bid=%s", (self.var_bid.get(),))
                row=cur.fetchone()
                if row!=None:
                    messagebox.showerror("Error", "Book ID already present", parent=self.root)
                else:
                    cur.execute("insert into books(bid,title,course,author,publication,noOfBook) value(%s,%s,%s,%s,%s,%s)",(
                        self.var_bid.get(),
                        self.var_title.get(),
                        self.var_course.get(),
                        self.var_author.get(),
                        self.var_publication.get(),
                        self.var_totalNum.get()
                    ))
                    con.commit()
                    messagebox.showinfo("Success", "Book Added Successful", parent=self.root)
                    self.show()

        except Exception as ex:
            messagebox.showerror("Error",f"Error due to {str(ex)}")

    def update(self):
        con = pymysql.connect(host="localhost", user="root", password="arrowoonbj1@", database="n_library")
        cur = con.cursor()
        try:
            if self.var_bid.get() == "":
                messagebox.showerror("Error","Book ID should be required", parent=self.root)
            else:
                cur.execute("select *  from books where bid=%s", (self.var_bid.get(),))
                row=cur.fetchone()
                if row==None:
                    messagebox.showerror("Error", "Select Book from list", parent=self.root)
                else:
                    cur.execute("update books set title=%s,course=%s,author=%s,publication=%s,noOfBook=%s where  bid=%s",(

                        self.var_title.get(),
                        self.var_course.get(),
                        self.var_author.get(),
                        self.var_publication.get(),
                        self.var_totalNum.get(),
                        self.var_bid.get()

                    ))
                    con.commit()
                    messagebox.showinfo("Success", "Book Update Successful", parent=self.root)
                    self.show()

        except Exception as ex:
            messagebox.showerror("Error",f"Error due to {str(ex)}")



    def show(self):
        con = pymysql.connect(host="localhost", user="root", password="arrowoonbj1@", database="n_library")
        cur = con.cursor()
        try:
            cur.execute("select *  from books ")
            rows=cur.fetchall()
            self.BookTable.delete(*self.BookTable.get_children())
            for row in rows:
                self.BookTable.insert('',END,values=row)

        except Exception as ex:
            messagebox.showerror("Error",f"Error due to {str(ex)}")

    def search(self):
        con = pymysql.connect(host="localhost", user="root", password="arrowoonbj1@", database="n_library")
        cur = con.cursor()
        try:
            cur.execute(f"select *  from books where title LIKE '%{self.var_search.get()}%'")
            rows=cur.fetchall()
            self.BookTable.delete(*self.BookTable.get_children())
            for row in rows:
                self.BookTable.insert('',END,values=row)

        except Exception as ex:
            messagebox.showerror("Error",f"Error due to {str(ex)}")




if __name__=="__main__":
    root=Tk()
    obj=EmpBook(root)
    root.mainloop()