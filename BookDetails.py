from tkinter import *
from PIL import ImageTk, Image
import pymysql
from tkinter import ttk,messagebox

mypass = "arrowoonbj1@"
mydatabase = "n_library"

con = pymysql.connect(host="localhost", user="root", password=mypass, database=mydatabase)
cur = con.cursor()

bookTable = "books"  # Book Table
class Book_Data:
    def __init__(self,root):
        self.root = root
        self.root.title("Nepalaya Library")
        self.root.geometry("1200x480+35+170")
        self.root.config(bg="white")
        self.root.focus_force()

        #self.bg = ImageTk.PhotoImage(file="image/student.jpg")
        #bg = Label(self.root, image=self.bg).place(x=0, y=0, relwidth=1, relheight=1)

        title = Label(self.root, text="Book Details",font=("times new roman",20), fg="white", bg="#033054").place(x=0, y=0, relwidth=1,height=35)

        # Search Panel
        self.var_search = StringVar()
        lbl_search_roll = Label(self.root, text="Search By Name", bg="white").place(x=300, y=60)
        txt_search_roll = Entry(self.root, textvariable=self.var_search, bg="lightyellow")
        txt_search_roll.place(x=450,y=60,width=300)
       # btn_search=Button(self.root,text="Search",bg="#03a9f4",fg="white",cursor="hand2",command=self.searchStudented).place(x=470,y=60,width=120,height=20)
        txt_search_roll.bind("<Key>", self.searchBook)

        # content
        self.C_Frame = Frame(self.root, bd=2, relief=RIDGE)
        self.C_Frame.place(x=190, y=100, width=780, height=340)

        scrolly = Scrollbar(self.C_Frame, orient=VERTICAL)
        scrollx = Scrollbar(self.C_Frame, orient=HORIZONTAL)
        self.bookTable = ttk.Treeview(self.C_Frame, columns=("bid", "title", "course", "author", "publication", "noOfBook"), xscrollcommand=scrollx.set,yscrollcommand=scrolly.set)

        scrollx.pack(side=BOTTOM, fill=X)
        scrolly.pack(side=RIGHT, fill=Y)
        scrollx.config(command=self.bookTable.xview)
        scrolly.config(command=self.bookTable.yview)

        self.bookTable.heading("bid", text="Book ID")
        self.bookTable.heading("title", text="Book Name")
        self.bookTable.heading("course", text="Course")
        self.bookTable.heading("author", text="Author")
        self.bookTable.heading("publication", text="Publication")
        self.bookTable.heading("noOfBook", text="Total Copies")
        self.bookTable["show"] = 'headings'
        self.bookTable.column("bid", width=50)
        self.bookTable.column("title", width=150)
        self.bookTable.column("course", width=150)
        self.bookTable.column("author", width=150)
        self.bookTable.column("publication", width=150)
        self.bookTable.column("noOfBook", width=100)
        self.bookTable.pack(fill=BOTH, expand=1)
        # self.studentTable.bind("<ButtonRelease-1>",self.get_data)
        self.show()

        self.bookTable.pack(fill= BOTH,expand=1)


    #show

    def show(self):

        getBook = "select * from " + bookTable
        try:
            cur.execute(getBook)
            con.commit()
            rows = cur.fetchall()
            self.bookTable.delete(*self.bookTable.get_children())
            for row in rows:
                self.bookTable.insert('', END, value=(row[0], row[1], row[2], row[3], row[4], row[5]))
        except Exception as ex:
            messagebox.showerror("Error", f"Error due to {str(ex)}")

    def searchBook(self,ev):
        #getStudent = "select * from " + studentTable
        con = pymysql.connect(host="localhost", user="root", password=mypass,database=mydatabase)
        cur = con.cursor()
        try:
            #cur.execute(getStudent)
            #con.commit()
            cur.execute("SELECT * FROM books where title LIKE '%"+self.var_search.get()+"%'")
            row = cur.fetchall()
            if len(row)>0:
                self.bookTable.delete(*self.bookTable.get_children())
                for i in row:
                    self.bookTable.insert('',END,value=(i[0],i[1],i[2],i[3],i[4],i[5]))
            else:
                self.bookTable.delete(*self.bookTable.get_children())
        except Exception as ex:
             messagebox.showerror("Error",f"Error due to {str(ex)}")




if __name__=="__main__":
    root=Tk()
    obj=Book_Data(root)
    root.mainloop()