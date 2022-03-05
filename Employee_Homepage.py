from tkinter import *
from PIL import Image,ImageTk
from book_crud import EmpBook
from Details_Student import Student_Data
from IssueBook import issueBook
from ReturnBook import returnBook
from tkinter import messagebox
import os
import pymysql
class EmployeeHome:
    def __init__(self,root):
        self.root=root
        self.root.title("Nepalaya Library")
        self.root.geometry("1350x650+0+0")
        self.root.config(bg="white")

        #====icons==
        self.logo_dash=ImageTk.PhotoImage(file="image/Nepalaya_logo1.png")

        #===title===
        title=Label(self.root,image=self.logo_dash,compound=LEFT,padx=10 ,text="Library Management System", font=("times new roman",20,"bold"),bg="#033054",fg="white").place(x=0,y=0,relwidth=1,height=50)

        #===Menu====
        M_Frame = LabelFrame(self.root,text="Menus",font=("times new roman",15),bg="white")
        M_Frame.place(x=10,y=70,width=1340,height=80)

        btn_book=Button(M_Frame,text="Book",font=("times new roman",15,"bold"),bg="#0b5377",fg="white", cursor="hand2", command=self.add_book).place(x=20,y=5,width=180,height=40)
        btn_student = Button(M_Frame, text="Student", font=("times new roman", 15, "bold"), bg="#0b5377", fg="white",
                          cursor="hand2",command=self.Student_Details).place(x=230, y=5, width=180, height=40)
        btn_issued = Button(M_Frame, text="Issue Book", font=("times new roman", 15, "bold"), bg="#0b5377", fg="white",
                          cursor="hand2",command=self.Issue_Details).place(x=440, y=5, width=180, height=40)
        btn_returned = Button(M_Frame, text="Return Book", font=("times new roman", 15, "bold"), bg="#0b5377", fg="white",
                          cursor="hand2",command=self.Return_Details).place(x=650, y=5, width=180, height=40)
        btn_logout = Button(M_Frame, text="Logout", font=("times new roman", 15, "bold"), bg="#0b5377", fg="white",
                          cursor="hand2",command=self.logout).place(x=860, y=5, width=180, height=40)
        btn_exit = Button(M_Frame, text="Exit", font=("times new roman", 15, "bold"), bg="#0b5377", fg="white",
                          cursor="hand2",command=self.exit_).place(x=1070, y=5, width=180, height=40)

        #======content_window===
        self.bg_img=Image.open("image/Student2.jpg")
        self.bg_img=self.bg_img.resize((1000,450),Image.ANTIALIAS)
        self.bg_img=ImageTk.PhotoImage(self.bg_img)

        self.lbl_bg=Label(self.root,image=self.bg_img).place(x=10,y=155,width=1000,height=450)

        #=====Update_details=====
        self.lbl_book=Label(self.root,text="Total Type of Books\n[0]",font=("times new roman",17),bd=7,relief=RIDGE,bg="#e43b06",fg="white")
        self.lbl_book.place(x=1040,y=190,width=200,height=70)

        self.lbl_student = Label(self.root, text="Total Students\n[0]", font=("times new roman", 17), bd=7, relief=RIDGE,
                              bg="#ff1493", fg="white")
        self.lbl_student.place(x=1040, y=290, width=200, height=70)

        self.lbl_issue = Label(self.root, text="Total Issues\n[0]", font=("times new roman", 17), bd=7, relief=RIDGE,
                              bg="#0676ad", fg="white")
        self.lbl_issue.place(x=1040, y=390, width=200, height=70)

        self.lbl_return = Label(self.root, text="Total Returns\n[0]", font=("times new roman", 17), bd=7, relief=RIDGE,
                              bg="#038074", fg="white")
        self.lbl_return.place(x=1040, y=490, width=200, height=70)


        # ===footer===
        footer = Label(self.root, text="Nepalaya-Library\nContact Us for any Technical Issue: 01-xxxx375",
                      font=("times new roman", 12), bg="#262626", fg="white").pack(side=BOTTOM,fill=X)
        self.update_details()

    def update_details(self):
        con = pymysql.connect(host="localhost", user="root", password="arrowoonbj1@", database="n_library")
        cur = con.cursor()
        try:
            cur.execute("select *  from books ")
            cr = cur.fetchall()
            self.lbl_book.config(text=f"Total Type of books\n[{str(len(cr))}]")

            cur.execute("select *  from student ")
            cr = cur.fetchall()
            self.lbl_student.config(text=f"Total Students\n[{str(len(cr))}]")

            cur.execute("select *  from issue ")
            cr = cur.fetchall()
            self.lbl_issue.config(text=f"Total issue\n[{str(len(cr))}]")

            cur.execute("select *  from returns ")
            cr = cur.fetchall()
            self.lbl_return.config(text=f"Total Returns\n[{str(len(cr))}]")


            self.lbl_book.after(200,self.update_details)

        except Exception as ex:
            messagebox.showerror("Error", f"Error due to {str(ex)}")

    def add_book(self):
        self.new_win=Toplevel(self.root)
        self.new_obj=EmpBook(self.new_win)

    def Student_Details(self):
        self.new_win=Toplevel(self.root)
        self.new_obj=Student_Data(self.new_win)

    def Issue_Details(self):
        self.new_win=Toplevel(self.root)
        self.new_obj=issueBook(self.new_win)

    def Return_Details(self):
        self.new_win=Toplevel(self.root)
        self.new_obj=returnBook(self.new_win)

    def logout(self):
        op=messagebox.askyesno("Confirm","Do you really want to logout?",parent=self.root)
        if op==True:
            self.root.destroy()
            os.system("python Employee_Login.py")

    def exit_(self):
        op=messagebox.askyesno("Confirm","Do you really want to Exit?",parent=self.root)
        if op==True:
            self.root.destroy()

if __name__=="__main__":
    root=Tk()
    obj=EmployeeHome(root)
    root.mainloop()