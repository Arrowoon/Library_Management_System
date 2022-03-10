from tkinter import *
from PIL import Image,ImageTk
import pymysql
import os
import cv2
import numpy as np
from tkinter import messagebox,ttk
class EmployeeLogin:
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
        self.left = ImageTk.PhotoImage(file="image/employee1.jpg")
        left = Label(self.root, image=self.left).place(x=80, y=120, width=350, height=450)

        # Login Frame
        login_frame = Frame(self.root, bg="white")
        login_frame.place(x=430, y=120, width=700, height=450)

        title = Label(login_frame, text="LOGIN HERE", font=("times new roman", 20, "bold"), fg="green", bg="white").place(
            x=200, y=50)


        #==============row1
        email = Label(login_frame, text="Email Address", font=("times new roman", 15, "bold"), fg="gray", bg="white").place(
            x=200, y=120)
        self.txt_email = Entry(login_frame, font=("timeds new roman", 15), bg="lightgray")
        self.txt_email.place(x=200, y=150, width=300, height=30)


        #=======================row2
        password = Label(login_frame, text="Password", font=("times new roman", 15, "bold"), fg="gray",
                         bg="white").place(
            x=200, y=200)
        self.txt_password = Entry(login_frame, font=("timeds new roman", 15), bg="lightgray",show="*")
        self.txt_password.place(x=200, y=230, width=300, height=30)

        btn_reg=Button(login_frame,text="Register new Account?",font=("times new roman",12),bg="white",bd=0,fg="#B00857",cursor="hand2",command=self.register_window).place(x=200,y=270)

        btn_forget = Button(login_frame, text="Forget Password?", font=("times new roman", 12), bg="white", bd=0,
                         fg="red", cursor="hand2", command=self.forget_password_window).place(x=380, y=270)
        btn_login = Button(login_frame, text="Login", font=("times new roman", 15,"bold"), fg="white",
                         bg="#B00857",cursor="hand2",command=self.login).place(x=200, y=330, width=150,height=35)

    def reset(self):
        self.cmb_quest.current(0)
        self.txt_new_pass.delete(0,END)
        self.txt_answer.delete(0,END)
        self.txt_password.delete(0,END)
        self.txt_email.delete(0,END)

    def forget_password(self):
        if self.cmb_quest.get()=="Select"or self.txt_answer.get()=="" or self.txt_new_pass.get()=="":
            messagebox.showerror("Error","All fields are required",parent=self.root2)
        else:
            try:
                con = pymysql.connect(host="localhost", user="root", password="arrowoonbj1@", database="n_library")
                cur = con.cursor()
                cur.execute("select * from employee where email=%s and question=%s and answer=%s", (self.txt_email.get(),self.cmb_quest.get(),self.txt_answer.get()))
                row = cur.fetchone()
                if row == None:
                    messagebox.showerror("Error", "Please Select Correct Security Question / Enter Answer",
                                         parent=self.root2)
                else:
                    cur.execute("update employee set password=%s where email=%s",
                                (self.txt_new_pass.get(),self.txt_email.get()))
                    con.commit()
                    con.close()
                    messagebox.showinfo("Success","Your password has been reset,please login with new password",parent=self.root2)
                    self.reset()
                    self.root2.destroy()

            except Exception as es:
                messagebox.showerror("Error", f"Error Due to: {str(es)}", parent=self.root)


    def forget_password_window(self):
        if self.txt_email.get()=="":
            messagebox.showerror("Error", "Please enter the email address to reset your password",
                                 parent=self.root)
        else:
            try:
                con = pymysql.connect(host="localhost", user="root", password="arrowoonbj1@", database="n_library")
                cur = con.cursor()
                cur.execute("select * from employee where email=%s",self.txt_email.get())
                row = cur.fetchone()
                if row == None:
                    messagebox.showerror("Error", "Please enter the valid email address to reset your password",
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



    def login(self):
       if self.txt_email.get()=="" or self.txt_password.get()=="":
           messagebox.showerror("Error","All fields are required",parent=self.root)
       else:
           try:
               con=pymysql.connect(host="localhost",user="root",password="arrowoonbj1@",database="n_library")
               cur=con.cursor()
               cur.execute("select * from employee where email=%s and password=%s",(self.txt_email.get(),self.txt_password.get()))
               row=cur.fetchone()
               if row==None:
                   messagebox.showerror("Error","Invalid Email & Password",parent=self.root)

               else:

                   # ==============Face Recognition=======================
                   def draw_boundray(img, classifier, scaleFactor, minNeighbors, color, text, clf):
                       gray_image = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
                       features = classifier.detectMultiScale(gray_image, scaleFactor, minNeighbors)

                       coord = []

                       for (x, y, w, h) in features:
                           cv2.rectangle(img, (x, y), (x + w, y + h), (0, 255, 0), 3)
                           id, predict = clf.predict(gray_image[y:y + h, x:x + w])
                           confidence = int((100 * (1 - predict / 300)))

                           con = pymysql.connect(host="localhost", user="root", password="arrowoonbj1@",
                                                 database="n_library")
                           cur = con.cursor()

                           cur.execute("select fl_name from employee where id=" + str(id))
                           n = cur.fetchone()
                           n = ''+''.join(n)

                           cur.execute("select email from employee where id=" + str(id))
                           e = cur.fetchone()
                           e = ''+''.join(e)

                           cur.execute("select department from employee where id=" + str(id))
                           d = cur.fetchone()
                           d = ''+''.join(d)

                           if confidence > 77:
                               cv2.putText(img, f"Name:{n}", (x, y - 55), cv2.FONT_HERSHEY_COMPLEX, 0.8,
                                           (255, 255, 255), 3)
                               cv2.putText(img, f"Email:{e}", (x, y - 30), cv2.FONT_HERSHEY_COMPLEX, 0.8,
                                           (255, 255, 255), 3)
                               cv2.putText(img, f"Department:{d}", (x, y - 5), cv2.FONT_HERSHEY_COMPLEX, 0.8,
                                           (255, 255, 255), 3)
                           else:
                               cv2.rectangle(img, (x, y), (x + w, y + h), (0, 0, 255), 3)
                               cv2.putText(img, "Unknown Face", (x, y - 5), cv2.FONT_HERSHEY_COMPLEX, 0.8,
                                           (255, 255, 255), 3)

                           coord = [x, y, w, h]
                       return coord

                   def recognize(img, clf, faceCascade):
                       coord = draw_boundray(img, faceCascade, 1.1, 10, (255, 255, 255), "Face", clf)
                       return img

                   faceCascade = cv2.CascadeClassifier("haarcascade_frontalface_default.xml")
                   clf = cv2.face.LBPHFaceRecognizer_create()
                   clf.read("classifier.xml")

                   video_cap = cv2.VideoCapture(0)



                   while True:
                       ret, img = video_cap.read()
                       img = recognize(img, clf, faceCascade)
                       cv2.imshow("Wecome To Face Recognition", img)

                       if cv2.waitKey(1) == 13:
                           break
                   video_cap.release()
                   cv2.destroyAllWindows()

                   #messagebox.showinfo("Result", "DATA MATCH")
                   messagebox.showinfo("Success", f"Welcome: {self.txt_email.get()}", parent=self.root)
                   self.root.destroy()
                   os.system("python Employee_Homepage.py")

               con.close()

           except Exception as es:
               messagebox.showerror("Error",f"Error Due to: {str(es)}",parent=self.root)

    def Employee(self):
        self.root.destroy()
        import Employee_Homepage

    def register_window(self):
        self.root.destroy()
        os.system("python Employee_Register.py")



root=Tk()
obj=EmployeeLogin(root)
root.mainloop()
