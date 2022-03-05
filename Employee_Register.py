from tkinter import *
from tkinter import ttk, messagebox
from PIL import Image,ImageTk
import pymysql
import os
import cv2
import numpy as np
class EmployeeRegister:
    def __init__(self,root):
        self.root=root
        self.root.title("Nepalaya Library")
        self.root.geometry("1350x700+0+0")
        self.root.config(bg="white")

        # Bg Image
        self.bg=ImageTk.PhotoImage(file="image/Library1.jpg")
        bg=Label(self.root,image=self.bg).place(x=250,y=0,relwidth=1,relheight=1)

        # left Image
        self.left = ImageTk.PhotoImage(file="image/sideimg.jpg")
        left = Label(self.root, image=self.left).place(x=80, y=100, width=400, height=500)

        # Register Frame
        frame1=Frame(self.root,bg="white")
        frame1.place(x=480,y=100,width=700,height=500)

        title=Label(frame1,text="REGISTER HERE",font=("times new roman",20,"bold"),fg="green",bg="white").place(x=50,y=20)

        #----------------------row1

        emp_id = Label(frame1, text="Employee ID", font=("times new roman", 15, "bold"), fg="gray", bg="white").place(
            x=50, y=70)
        self.txt_empid=Entry(frame1,font=("timeds new roman",15),bg="lightgray")
        self.txt_empid.place(x=50, y=100, width=250)


        fl_name = Label(frame1, text="Name", font=("times new roman", 15, "bold"), fg="gray", bg="white").place(
            x=370, y=70)
        self.txt_flname = Entry(frame1, font=("timeds new roman", 15), bg="lightgray")
        self.txt_flname.place(x=370, y=100, width=250)


        #---------------------------row2

        email = Label(frame1, text="Email Address", font=("times new roman", 15, "bold"), fg="gray", bg="white").place(
            x=50, y=135)
        self.txt_email = Entry(frame1, font=("timeds new roman", 15), bg="lightgray")
        self.txt_email.place(x=50, y=165, width=250)

        department = Label(frame1, text="Department", font=("times new roman", 15, "bold"), fg="gray", bg="white").place(
            x=370, y=135)
        self.txt_department = Entry(frame1, font=("timeds new roman", 15), bg="lightgray")
        self.txt_department.place(x=370, y=165, width=250)


        #---------------------------row3

        question = Label(frame1, text="Security Question", font=("times new roman", 15, "bold"), fg="gray", bg="white").place(
            x=50, y=205)
        self.cmb_quest = ttk.Combobox(frame1, font=("timeds new roman", 13),state="readonly",justify=CENTER)
        self.cmb_quest['values']=("Select","Your First Pet Name","Your Birth Place","Your Best Friend Name")
        self.cmb_quest.place(x=50, y=235, width=250)
        self.cmb_quest.current(0)

        answer = Label(frame1, text="Answer", font=("times new roman", 15, "bold"), fg="gray",
                           bg="white").place(
            x=370, y=205)
        self.txt_answer = Entry(frame1, font=("timeds new roman", 15), bg="lightgray")
        self.txt_answer.place(x=370, y=235, width=250)


        # ---------------------------row4

        password = Label(frame1, text="Password", font=("times new roman", 15, "bold"), fg="gray",
                           bg="white").place(
            x=50, y=275)
        self.txt_password = Entry(frame1, font=("timeds new roman", 15), bg="lightgray")
        self.txt_password.place(x=50, y=305, width=250)

        cpassword = Label(frame1, text="Confirm Password", font=("times new roman", 15, "bold"), fg="gray",
                    bg="white").place(
            x=370, y=275)
        self.txt_cpassword = Entry(frame1, font=("timeds new roman", 15), bg="lightgray")
        self.txt_cpassword.place(x=370, y=305, width=250)


        #Radio Buttons
        #self.var_radio1=StringVar()
        #radiobtn1 = ttk.Radiobutton(frame1,variable=self.var_radio1, text="Take photo sample", value=1).place(x=50, y=350)


        #radiobtn2 = ttk.Radiobutton(frame1,variable=self.var_radio1, text="No photo sample", value=0).place(x=200, y=350)




        #---------Terms & Conditions------
        self.var_chk=IntVar()
        chk=Checkbutton(frame1,text="I Agree The Terms & Conditions",variable=self.var_chk,onvalue=1,offvalue=0,bg="white",font=("times new roman",12)).place(x=50,y=347)

        self.var_photo = StringVar()
        btn_photo = Button(frame1, text="Proceed to Face Biometric Scan ",font=("times new roman", 12), bg="white", bd=0,
                           fg="red", cursor="hand2", command=self.generate_dataset).place(x=230, y=380)

        btn_registerh=Button(frame1,text="Register Now",font=("timeds new roman",10),bg="green",fg="white",cursor="hand2",command=self.register_employeeData).place(x=230,y=420,width=200)

        btn_login = Button(self.root, text="Sign In", font=("timeds new roman", 10), bg="green", fg="white",
                     cursor="hand2",command=self.login_window).place(x=180, y=480, width=200)

    def login_window(self):
        self.root.destroy()
        os.system("python Employee_Login.py")

    def clear(self):
        self.txt_empid.delete(0,END)
        self.txt_flname.delete(0, END)
        self.txt_email.delete(0, END)
        self.txt_department.delete(0, END)
        self.txt_answer.delete(0, END)
        self.txt_password.delete(0, END)
        self.txt_cpassword.delete(0, END)
        self.cmb_quest.current(0)

    def register_employeeData(self):

        if self.txt_empid.get()=="" or self.txt_flname.get()=="" or self.txt_email.get()=="" or self.txt_department.get()=="" or self.cmb_quest.get()=="Select" or self.txt_answer.get()=="" or self.txt_password.get()=="" or self.txt_cpassword.get()=="":
            messagebox.showerror("Error","All Fields Are Required",parent=self.root)
        elif self.txt_password.get()!=self.txt_cpassword.get():
            messagebox.showerror("Error","Password & Confirm Password should be same",parent=self.root)
        elif self.var_chk.get()==0:
            messagebox.showerror("Error", "Please Agree our terms & condition", parent=self.root)
         #else:
            #try:
                #cur=con.cursor()
                #cur.execute("select * from employee where email=%s")
                #row=cur.fetchone()
                #print(row)
                #if row!=None:
                    #messagebox.showerror("Error", "User already Exist, Please try with another email", parent=self.root)
                #else:
                    #cur.execute("insert into employee (emp_id,fl_name,email,department,question,answer,password,photo_sample) value(%s,%s,%s,%s,%s,%s,%s,%s)",
                     #           (self.txt_empid.get(),
                      #           self.txt_flname.get(),
                      #           self.txt_email.get(),
                      #           self.txt_department.get(),
                      #           self.cmb_quest.get(),
                      #           self.txt_answer.get(),
                       #          self.txt_password.get(),
                       #          ))
                #con.commit()
                #con.close()
        else:
            try:
                messagebox.showinfo("Success", "Register Successful", parent=self.root)
                self.clear()
                self.login_window()

            except Exception as es:
                messagebox.showerror("Error", f"Error due to: {str(es)}", parent=self.root)
                #messagebox.showinfo("Success", "Register Successful", parent=self.root)


    #=======================generate data set or take a photo Sample===
    def generate_dataset(self):
        if self.txt_empid.get()=="" or self.txt_flname.get()==""  or self.txt_email.get()=="" or self.txt_department.get()=="" or self.cmb_quest.get()=="Select" or self.txt_answer.get()=="" or self.txt_password.get()=="" or self.txt_cpassword.get()=="":
            messagebox.showerror("Error","All Fields Are Required",parent=self.root)
        elif self.txt_password.get()!=self.txt_cpassword.get():
            messagebox.showerror("Error","Password & Confirm Password should be same",parent=self.root)
        elif self.var_chk.get()==0:
            messagebox.showerror("Error", "Please Agree our terms & condition", parent=self.root)
        else:
            try:
                con = pymysql.connect(host="localhost", user="root", password="arrowoonbj1@", database="n_library")
                cur = con.cursor()
                cur.execute("select * from employee")
                rows = cur.fetchall()
                # print(row)
                id=1
                #if row != None:
                    #messagebox.showerror("Error", "User already Exist, Please try with another email", parent=self.root)
                #else:
                for x in rows:
                    id+=1
                cur.execute("insert into employee (emp_id,fl_name,email,department,question,answer,password) value(%s,%s,%s,%s,%s,%s,%s)",
                        (self.txt_empid.get(),  #==id+1,
                         self.txt_flname.get(),
                         self.txt_email.get(),
                         self.txt_department.get(),
                         self.cmb_quest.get(),
                         self.txt_answer.get(),
                         self.txt_password.get()
                         ))
                con.commit()
                con.close()






        #=================== load predefined data on face frontals from op[encv]  =======
                face_classifier=cv2.CascadeClassifier("haarcascade_frontalface_default.xml")
                def face_cropped(img):
                    gray=cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
                    faces=face_classifier.detectMultiScale(gray,1.3,5)
                    #scalling factor=1.3
                    #minimum neighbor=5
                    for(x,y,w,h) in faces:
                        face_cropped=img[y:y+h,x:x+w]
                        return face_cropped
                cap=cv2.VideoCapture(0)
                img_id=0
                while True:
                    ret,my_frame=cap.read()
                    if face_cropped(my_frame) is not None:
                        img_id+=1
                        face=cv2.resize(face_cropped(my_frame),(450,450))
                        face=cv2.cvtColor(face,cv2.COLOR_BGR2GRAY)
                        file_name_path="data/user."+str(id)+"."+str(img_id)+".jpg"
                        cv2.imwrite(file_name_path,face)
                        cv2.putText(face,str(img_id),(50,50),cv2.FONT_HERSHEY_COMPLEX,2,(0,255,0),2)
                        cv2.imshow("Crooped Face",face)

                    if cv2.waitKey(1)==13 or int(img_id)==30:
                        break
                cap.release()
                cv2.destroyAllWindows()
                messagebox.showinfo("Result","Generating data set completed!!")


                #+++++++++++++++++++++++++++++TRAIN DATA+++++++++++++++++++++++++++++
                #====================================================================

                data_dir = ("data")
                path = [os.path.join(data_dir, file) for file in os.listdir(data_dir)]

                faces = []
                ids = []

                for image in path:
                    img = Image.open(image).convert('L')  # Gray scale image
                    imageNp = np.array(img, 'uint8')
                    id = int(os.path.split(image)[1].split('.')[1])

                    faces.append(imageNp)
                    ids.append(id)
                    cv2.imshow("Training", id) #cv2.imshow("Training", imageNp)
                    cv2.waitKey(1) == 13
                ids = np.array(ids)

                # =================Train the classifier And Save ==========
                clf = cv2.face.LBPHFaceRecognizer_create()
                clf.train(faces, ids)
                clf.write("classifier.xml")
                cv2.destroyAllWindows()
                messagebox.showinfo("Result", "Training datasets completed!!")

            except Exception as es:
                messagebox.showerror("Error", f"Error due to: {str(es)}", parent=self.root)

if __name__=="__main__":
    root=Tk()
    obj=EmployeeRegister(root)
    root.mainloop()