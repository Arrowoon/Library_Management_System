from tkinter import *
from PIL import Image,ImageTk
import pymysql
from tkinter import messagebox,ttk
import os
from StudentIssueReport import StudentIssue_Data
class StudentLogin:
    def __init__(self,root):

        self.root = root
        self.root.title("Nepalaya Library")
        self.root.geometry("1350x700+0+0")
        self.root.config(bg="white")

        # Background====
        #self.bg = ImageTk.PhotoImage(file="image/Library1.jpg")
        #bg = Label(self.root, image=self.bg).place(x=250, y=0, relwidth=1, relheight=1)

        left_lbl=Label(self.root,bg="#08A3D2",bd=0)
        left_lbl.place(x=0,y=0,relheight=1,width=600)

        right_lbl = Label(self.root, bg="#031F3C", bd=0)
        right_lbl.place(x=600, y=0, relheight=1, relwidth=1)

        # left Image
        self.left = ImageTk.PhotoImage(file="image/student1.jpg")
        left = Label(self.root, image=self.left).place(x=80, y=120, width=350, height=450)

        # Login Frame
        login_frame = Frame(self.root, bg="white")
        login_frame.place(x=430, y=120, width=700, height=450)

        title = Label(login_frame, text="LOGIN HERE", font=("times new roman", 20, "bold"), fg="green", bg="white").place(
            x=200, y=50)


        #==============row1
        id = Label(login_frame, text="Student ID", font=("times new roman", 15, "bold"), fg="gray", bg="white").place(
            x=200, y=120)
        self.txt_id = Entry(login_frame, font=("timeds new roman", 15), bg="lightgray")
        self.txt_id.place(x=200, y=150, width=300, height=30)


        #=======================row2
        password = Label(login_frame, text="Password", font=("times new roman", 15, "bold"), fg="gray",
                         bg="white").place(
            x=200, y=200)
        self.txt_password = Entry(login_frame, font=("timeds new roman", 15), bg="lightgray", show="*")
        self.txt_password.place(x=200, y=230, width=300, height=30)

        btn_reg=Button(login_frame,text="Register new Account?",font=("times new roman",12),bg="white",bd=0,fg="#B00857",cursor="hand2",command=self.register_student).place(x=200,y=270)

        btn_forget = Button(login_frame, text="Forget Password?", font=("times new roman", 12), bg="white", bd=0,
                         fg="red", cursor="hand2", command=self.forget_password_window).place(x=380, y=270)
        btn_login = Button(login_frame, text="Login", font=("times new roman", 15,"bold"), fg="white",
                         bg="#B00857",cursor="hand2",command=(self.login)).place(x=200, y=330, width=150,height=35)

    def reset(self):
        self.cmb_quest.current(0)
        self.txt_new_pass.delete(0,END)
        self.txt_answer.delete(0,END)
        self.txt_password.delete(0,END)
        self.txt_id.delete(0,END)

    def forget_password(self):
        if self.cmb_quest.get()=="Select"or self.txt_answer.get()=="" or self.txt_new_pass.get()=="":
            messagebox.showerror("Error","All fields are required",parent=self.root2)
        else:
            try:
                con = pymysql.connect(host="localhost", user="root", password="arrowoonbj1@", database="n_library")
                cur = con.cursor()
                cur.execute("select * from student where stuid=%s and question=%s and answer=%s", (self.txt_id.get(),self.cmb_quest.get(),self.txt_answer.get()))
                row = cur.fetchone()
                if row == None:
                    messagebox.showerror("Error", "Please Select Correct Security Question / Enter Answer",
                                         parent=self.root2)
                else:
                    cur.execute("update student set password=%s where stuid=%s",
                                (self.txt_new_pass.get(),self.txt_id.get()))
                    con.commit()
                    con.close()
                    messagebox.showinfo("Success","Your password has been reset,please login with new password",parent=self.root2)
                    self.reset()
                    self.root2.destroy()

            except Exception as es:
                messagebox.showerror("Error", f"Error Due to: {str(es)}", parent=self.root)


    def forget_password_window(self):
        if self.txt_id.get()=="":
            messagebox.showerror("Error", "Please enter the student Id to reset your password",
                                 parent=self.root)
        else:
            try:
                con = pymysql.connect(host="localhost", user="root", password="arrowoonbj1@", database="n_library")
                cur = con.cursor()
                cur.execute("select * from student where stuid=%s",self.txt_id.get())
                row = cur.fetchone()
                if row == None:
                    messagebox.showerror("Error", "Please enter the valid ID to reset your password",
                                         parent=self.root)
                else:
                    con.close()
                    self.root2 = Toplevel()
                    self.root2.title("Nepalaya Library")
                    self.root2.geometry("400x400+550+160")
                    self.root2.config(bg="white")
                    self.root2.focus_force()
                    self.root2.grab_set()

                    t = Label(self.root2, text="Forget Password", font=("times new roman", 17, "bold"), bg="white",
                              fg="red").place(x=0, y=10, relwidth=1)

                    # ---------------------------Forget Password

                    question = Label(self.root2, text="Security Question", font=("times new roman", 15, "bold"),
                                     fg="gray",
                                     bg="white").place(
                        x=80, y=85)
                    self.cmb_quest = ttk.Combobox(self.root2, font=("timeds new roman", 13), state="readonly",
                                                  justify=CENTER)
                    self.cmb_quest['values'] = (
                    "Select", "Your First Pet Name", "Your Birth Place", "Your Best Friend Name")
                    self.cmb_quest.place(x=80, y=115, width=250)
                    self.cmb_quest.current(0)

                    answer = Label(self.root2, text="Answer", font=("times new roman", 15, "bold"), fg="gray",
                                   bg="white").place(
                        x=80, y=165)
                    self.txt_answer = Entry(self.root2, font=("timeds new roman", 15), bg="lightgray")
                    self.txt_answer.place(x=80, y=205, width=250)

                    new_password = Label(self.root2, text="New Password", font=("times new roman", 15, "bold"),
                                         fg="gray",
                                         bg="white").place(
                        x=80, y=245)
                    self.txt_new_pass = Entry(self.root2, font=("timeds new roman", 15), bg="lightgray")
                    self.txt_new_pass.place(x=80, y=275, width=250)

                    btn_change_password = Button(self.root2, text="Reset Password", bg="green", fg="white",
                                                 font=("times new roman", 13, "bold"),command=self.forget_password).place(x=120, y=325)

            except Exception as es:
                messagebox.showerror("Error", f"Error Due to: {str(es)}", parent=self.root)

    def register_student(self):
        self.root.destroy()
        import Student_Register

    def login(self):
       if self.txt_id.get()=="" or self.txt_password.get()=="":
           messagebox.showerror("Error","All fields are required",parent=self.root)
       else:
           try:
               con=pymysql.connect(host="localhost",user="root",password="arrowoonbj1@",database="n_library")
               cur=con.cursor()
               cur.execute("select * from student where stuid=%s and password=%s",(self.txt_id.get(),self.txt_password.get()))
               row=cur.fetchone()
               if row==None:
                   messagebox.showerror("Error","Invalid Username & Password",parent=self.root)

               else:
                   messagebox.showinfo("Success", f"Welcome: {self.txt_id.get()}", parent=self.root)
                   self.root.destroy()
                   os.system("python Student_Homepage.py")
               con.close()

           except Exception as es:
               messagebox.showerror("Error",f"Error Due to: {str(es)}",parent=self.root)

    def Student(self):
        self.root.destroy()
        import Student_Homepage


root=Tk()
obj=StudentLogin(root)
root.mainloop()
