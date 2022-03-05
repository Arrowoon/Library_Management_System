from tkinter import *
from tkinter import ttk, messagebox
from PIL import Image,ImageTk
import pymysql
class Home:
    def __init__(self,root):
        self.root=root
        self.root.title("Nepalaya Library")
        self.root.geometry("1350x700+0+0")
        self.root.config(bg="white")


        # Bg Image

        self.logo=ImageTk.PhotoImage(file="image/Nepalaya logo.png")
        logo = Label(self.root, image=self.logo,bd=0,bg="white").place(x=0, y=-80, relwidth=1, relheight=1)

        title = Label(logo, text="WELCOME TO NEPALAYA LIBRARY", font=("times new roman", 25, "bold"), fg="green", bg="white",bd=0).place(
            x=350, y=50)

        btn_employee = Button(logo, text="Employee Login", font=("times new roman", 15, "bold"), fg="white",
                           bg="#B00857", cursor="hand2",command=self.login_employee).place(x=200, y=500, width=250, height=35)
        btn_student = Button(logo, text="Student Login", font=("times new roman", 15, "bold"), fg="white",
                           bg="#B00857", cursor="hand2",command=self.login_student).place(x=800, y=500, width=250, height=35)

    def login_employee(self):
        self.root.destroy()
        import Employee_Login

    def login_student(self):
        self.root.destroy()
        import Student_Login


root=Tk()
obj=Home(root)
root.mainloop()