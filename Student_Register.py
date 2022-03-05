from tkinter import *
from tkinter import ttk, messagebox
from PIL import Image,ImageTk
import pymysql
import os
class StudentRegister:
    def __init__(self,root):
        self.root=root
        self.root.title("Nepalaya Library")
        self.root.geometry("1350x700+0+0")
        self.root.config(bg="white")

        # Bg Image
        self.bg=ImageTk.PhotoImage(file="image/Library1.jpg")
        bg=Label(self.root,image=self.bg).place(x=250,y=0,relwidth=1,relheight=1)

        # left Image
        self.left = ImageTk.PhotoImage(file="image/sideimg1.jpg")
        left = Label(self.root, image=self.left).place(x=80, y=100, width=400, height=500)

        # Register Frame
        frame1=Frame(self.root,bg="white")
        frame1.place(x=480,y=100,width=700,height=500)

        title=Label(frame1,text="REGISTER HERE",font=("times new roman",20,"bold"),fg="green",bg="white").place(x=50,y=30)

        #----------------------row1

        stu_id = Label(frame1, text="Student ID", font=("times new roman", 15, "bold"), fg="gray", bg="white").place(
            x=50, y=70)
        self.txt_stuid=Entry(frame1,font=("timeds new roman",15),bg="lightgray")
        self.txt_stuid.place(x=50, y=95, width=250)


        fl_name = Label(frame1, text="Name", font=("times new roman", 15, "bold"), fg="gray", bg="white").place(
            x=370, y=70)
        self.txt_flname = Entry(frame1, font=("timeds new roman", 15), bg="lightgray")
        self.txt_flname.place(x=370, y=95, width=250)

        # ----------------------row1

        sem_year = Label(frame1, text="Semester/Year", font=("times new roman", 15, "bold"), fg="gray", bg="white").place(
            x=50, y=125)
        self.txt_sem_year = Entry(frame1, font=("timeds new roman", 15), bg="lightgray")
        self.txt_sem_year.place(x=50, y=150, width=250)

        address = Label(frame1, text="Address", font=("times new roman", 15, "bold"), fg="gray", bg="white").place(
            x=370, y=125)
        self.txt_address = Entry(frame1, font=("timeds new roman", 15), bg="lightgray")
        self.txt_address.place(x=370, y=150, width=250)


        #---------------------------row2

        email = Label(frame1, text="Email Address", font=("times new roman", 15, "bold"), fg="gray", bg="white").place(
            x=50, y=185)
        self.txt_email = Entry(frame1, font=("timeds new roman", 15), bg="lightgray")
        self.txt_email.place(x=50, y=215, width=250)

        department = Label(frame1, text="Department", font=("times new roman", 15, "bold"), fg="gray", bg="white").place(
            x=370, y=185)
        self.txt_department = Entry(frame1, font=("timeds new roman", 15), bg="lightgray")
        self.txt_department.place(x=370, y=215, width=250)


        #---------------------------row3

        question = Label(frame1, text="Security Question", font=("times new roman", 15, "bold"), fg="gray", bg="white").place(
            x=50, y=245)
        self.cmb_quest = ttk.Combobox(frame1, font=("timeds new roman", 13),state="readonly",justify=CENTER)
        self.cmb_quest['values']=("Select","Your First Pet Name","Your Birth Place","Your Best Friend Name")
        self.cmb_quest.place(x=50, y=275, width=250)
        self.cmb_quest.current(0)

        answer = Label(frame1, text="Answer", font=("times new roman", 15, "bold"), fg="gray",
                           bg="white").place(
            x=370, y=245)
        self.txt_answer = Entry(frame1, font=("timeds new roman", 15), bg="lightgray")
        self.txt_answer.place(x=370, y=275, width=250)


        # ---------------------------row4

        password = Label(frame1, text="Password", font=("times new roman", 15, "bold"), fg="gray",
                           bg="white").place(
            x=50, y=310)
        self.txt_password = Entry(frame1, font=("timeds new roman", 15), bg="lightgray")
        self.txt_password.place(x=50, y=340, width=250)

        cpassword = Label(frame1, text="Confirm Password", font=("times new roman", 15, "bold"), fg="gray",
                    bg="white").place(
            x=370, y=310)
        self.txt_cpassword = Entry(frame1, font=("timeds new roman", 15), bg="lightgray")
        self.txt_cpassword.place(x=370, y=340, width=250)


        #---------Terms & Conditions------
        self.var_chk=IntVar()
        chk=Checkbutton(frame1,text="I Agree The Terms & Conditions",variable=self.var_chk,onvalue=1,offvalue=0,bg="white",font=("times new roman",12)).place(x=50,y=380)

        btn_registerh=Button(frame1,text="Register Now",font=("timeds new roman",10),bg="green",fg="white",cursor="hand2",command=self.register_studentData).place(x=230,y=420,width=200)

        btn_login = Button(self.root, text="Sign In", font=("timeds new roman", 10), bg="green", fg="white",
                     cursor="hand2",command=self.login_window).place(x=180, y=480, width=200)

    def login_window(self):
        self.root.destroy()
        os.system("python Student_Login.py")

    def clear(self):
        self.txt_stuid.delete(0,END)
        self.txt_flname.delete(0, END)
        self.txt_sem_year.delete(0, END)
        self.txt_address.delete(0, END)
        self.txt_email.delete(0, END)
        self.txt_department.delete(0, END)
        self.txt_answer.delete(0, END)
        self.txt_password.delete(0, END)
        self.txt_cpassword.delete(0, END)
        self.cmb_quest.current(0)

    def register_studentData(self):
        if self.txt_stuid.get()=="" or self.txt_flname.get()=="" or self.txt_sem_year.get()=="" or self.txt_address.get()=="" or self.txt_email.get()=="" or self.txt_department.get()=="" or self.cmb_quest.get()=="Select" or self.txt_answer.get()=="" or self.txt_password.get()=="" or self.txt_cpassword.get()=="":
            messagebox.showerror("Error","All Fields Are Required",parent=self.root)
        elif self.txt_password.get()!=self.txt_cpassword.get():
            messagebox.showerror("Error","Password & Confirm Password should be same",parent=self.root)
        elif self.var_chk.get()==0:
            messagebox.showerror("Error", "Please Agree our terms & condition", parent=self.root)
        else:
            try:
                con=pymysql.connect(host="localhost",user="root",password="arrowoonbj1@",database="n_library")
                cur=con.cursor()
                cur.execute("select * from student where email=%s",self.txt_email.get())
                row=cur.fetchone()
                #print(row)
                if row!=None:
                    messagebox.showerror("Error", "User already Exist, Please try with another email", parent=self.root)
                else:
                    cur.execute("insert into student (stuid,fl_name,sem_year,address,email,department,question,answer,password) value(%s,%s,%s,%s,%s,%s,%s,%s,%s)",
                                (self.txt_stuid.get(),
                                 self.txt_flname.get(),
                                 self.txt_sem_year.get(),
                                 self.txt_address.get(),
                                 self.txt_email.get(),
                                 self.txt_department.get(),
                                 self.cmb_quest.get(),
                                 self.txt_answer.get(),
                                 self.txt_password.get()
                                 ))
                con.commit()
                con.close()
                messagebox.showinfo("Success", "Register Successful", parent=self.root)
                self.clear()
                self.login_window()

            except Exception as es:
                messagebox.showerror("Error", f"Error due to: {str(es)}", parent=self.root)
            #messagebox.showinfo("Success", "Register Successful", parent=self.root)


root=Tk()
obj=StudentRegister(root)
root.mainloop()