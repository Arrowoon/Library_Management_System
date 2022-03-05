from tkinter import *
from PIL import Image,ImageTk
from BookDetails import Book_Data
from tkinter import messagebox
from StudentIssueReport import StudentIssue_Data
from StudentReturnReport import StudentReturn_Data
import os
import pymysql
class StudentHome:
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

        btn_book=Button(M_Frame,text="Book Details",font=("times new roman",15,"bold"),bg="#0b5377",fg="white", cursor="hand2", command=self.Book_Details).place(x=20,y=5,width=180,height=40)

        btn_issued = Button(M_Frame, text="Issue Report", font=("times new roman", 15, "bold"), bg="#0b5377", fg="white",
                          cursor="hand2",command=self.Issue_Report).place(x=270, y=5, width=180, height=40)
        btn_returned = Button(M_Frame, text="Return Report", font=("times new roman", 15, "bold"), bg="#0b5377", fg="white",
                          cursor="hand2",command=self.Return_Report).place(x=520, y=5, width=180, height=40)
        btn_logout = Button(M_Frame, text="Logout", font=("times new roman", 15, "bold"), bg="#0b5377", fg="white",
                          cursor="hand2",command=self.logout).place(x=770, y=5, width=180, height=40)
        btn_exit = Button(M_Frame, text="Exit", font=("times new roman", 15, "bold"), bg="#0b5377", fg="white",
                          cursor="hand2",command=self.exit_).place(x=1020, y=5, width=180, height=40)

        #======content_window===
        self.bg_img=Image.open("image/student4.jpeg")
        self.bg_img=self.bg_img.resize((850,450),Image.ANTIALIAS)
        self.bg_img=ImageTk.PhotoImage(self.bg_img)

        self.lbl_bg=Label(self.root,image=self.bg_img).place(x=150,y=155,width=950,height=450)




        # ===footer===
        footer = Label(self.root, text="Nepalaya-Library\nContact Us for any Technical Issue: 01-xxxx375",
                      font=("times new roman", 12), bg="#262626", fg="white").pack(side=BOTTOM,fill=X)

    def Book_Details(self):
        self.new_win=Toplevel(self.root)
        self.new_obj=Book_Data(self.new_win)

    def Issue_Report(self):
        self.new_win = Toplevel(self.root)
        self.new_obj = StudentIssue_Data(self.new_win)

    def Return_Report(self):
        self.new_win = Toplevel(self.root)
        self.new_obj = StudentReturn_Data(self.new_win)

    def logout(self):
        op = messagebox.askyesno("Confirm", "Do you really want to logout?", parent=self.root)
        if op == True:
            self.root.destroy()
            os.system("python Student_Login.py")

    def exit_(self):
        op = messagebox.askyesno("Confirm", "Do you really want to Exit?", parent=self.root)
        if op == True:
            self.root.destroy()


if __name__=="__main__":
    root=Tk()
    obj=StudentHome(root)
    root.mainloop()