from tkinter import *
import tkinter as tk
import webbrowser
from PIL import ImageTk, Image
import googlesearch  # pip install google
class Google:
    def __init__(self, root):
        self.root = root
        self.root.title("Google Search Engine")
        self.root.geometry("800x480+235+170")
        self.root.iconbitmap('image/Google.ico')

        # label to create top  design
        l1 = Label(self.root, bg="black", width=500, height=2)
        l1.grid(sticky="w")

        # apps logo
        self.apps_logo = ImageTk.PhotoImage(Image.open('image/apps.jpg'))
        d = Label(self.root, image=self.apps_logo, borderwidth=0)
        d.place(x=15, y=11)
        # apps label
        apps = Label(self.root, text="Apps", bg="black", fg="white", cursor="hand2")
        apps.place(x=40, y=10)
        apps.bind("<Button-1>", lambda e: self.callback("https://about.google/intl/en/products/?tab=wh"))

        # drive logo
        self.d_logo = ImageTk.PhotoImage(Image.open('image/Google drive.png'))
        d = Label(self.root, image=self.d_logo, borderwidth=0)
        d.place(x=95, y=11)
        # drive label
        drive = Label(self.root, text="Google Drive", bg="black", fg="white", cursor="hand2")
        drive.place(x=120, y=10)
        drive.bind("<Button-1>", lambda e: self.callback("https://drive.google.com/"))

        # youtube logo
        self.yt_logo = ImageTk.PhotoImage(Image.open('image/youtube.png'))
        y = Label(self.root, image=self.yt_logo, borderwidth=0)
        y.place(x=210, y=12)
        # youtube label
        yt = Label(self.root, text="YouTube", bg="black", fg="white", cursor="hand2")
        yt.place(x=240, y=10)
        yt.bind("<Button-1>", lambda e:self.callback("https://www.youtube.com/"))

        # Gmail logo
        self.gm_logo = ImageTk.PhotoImage(Image.open('image/gmail.jpg'))
        l2 = Label(self.root, image=self.gm_logo, borderwidth=0)
        l2.place(x=310, y=12)

        # Gmail label
        gmail = Label(self.root, text="Gmail", bg="black", fg="white", cursor="hand2")
        gmail.place(x=340, y=10)
        gmail.bind("<Button-1>", lambda e: self.callback("https://mail.google.com/mail/"))

        # Gmail label
        g = Label(self.root, text="Gmail", cursor="hand2")
        g.place(x=630, y=50)
        g.bind("<Button-1>", lambda e: self.callback("https://mail.google.com/mail/"))

        # Images label
        i = Label(self.root, text="Images", cursor="hand2")
        i.place(x=670, y=50)
        i.bind("<Button-1>", lambda e: self.callback("https://www.google.co.in/imghp?hl=en&tab=wi&ogbl"))

        # signin button
        signin = Button(self.root, text="sign in", font=('roboto', 13, 'bold'), bg="#4583EC", fg="white", cursor="hand2")
        signin.place(x=730, y=50)
        signin.bind("<Button-1>", lambda e: self.callback("http://google.com"))

        # google logo
        self.g_logo = ImageTk.PhotoImage(Image.open('image/google logo.png'))
        l2 = Label(self.root, image=self.g_logo)
        l2.place(x=260, y=190)

        # search box
        self.text = Text(self.root, width=90, height=2, relief=RIDGE, font=('roboto', 10, 'bold'), borderwidth=2)
        self.text.place(x=120, y=300, width=550, height=35)

        # search button
        search = Button(self.root, text="Google Search", relief=RIDGE, font=('arial', 10), bg="#F3F3F3", fg="#222222",
                        cursor="hand2", command=self.search_query)
        search.place(x=380, y=360)

        #nepalaya Map
        map = Button(self.root, text="Nepalaya Library Location", font=('roboto', 13, 'bold'), bg="#4583EC", fg="white",
                        cursor="hand2")
        map.place(x=320, y=400)
        map.bind("<Button-1>", lambda e: self.callback("https://www.google.com/maps/search/nepalaya+college/@27.694859,85.283174,16.94z"))

    def callback(self, url):
        webbrowser.open(url)

    def search_query(self):
        query = self.text.get("1.0", "end-1c")
        s = googlesearch.search(query, tld="co.in", num=10, stop=2, pause=2)
        # print(s)
        for j in s:
            # print(j)
            webbrowser.open(j)
if __name__=="__main__":
    root=Tk()
    obj=Google(root)
    root.mainloop()