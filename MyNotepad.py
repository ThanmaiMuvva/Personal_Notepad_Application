from subprocess import call 
import tkinter as tk
from tkinter import ttk
from turtle import back
from PIL import Image,ImageTk 
import time 

global login
login = "no"
usernames = []
passwords = []
notes = []
notelist = []
with open("admin.txt") as file:
    for line in file:
        a,b = line.split(',')
        usernames.append(a)
        passwords.append(b[:len(b)-1])
    file.close()

with open("notes.txt") as file:
    i=0
    for line in file:
        a,b = line.split(",")
        notes.append(a)
        a = int(a)
        notelist.append([])
        notelist[i].append(list(b.split(":")))
        i +=1 
    file.close() 

class Application:
    def __init__(self,master):
        self.master = master 
        self.master.minsize(600,400)
        self.master.title("My Notepad")
        self.master.configure(background = "light blue")
        self.welcome_page()

    def welcome_page(self):
        for i in self.master.winfo_children():
            i.destroy()
        self.frame1 = tk.Frame(self.master, width = 600, height = 400)
        self.frame1.pack()
        self.frame1.configure(background = "light blue")
        self.label1 = ttk.Label(self.frame1,text = "Enter the username", foreground="black", background="light blue")
        self.label1.pack()
        self.label1.place(x=125,y=80)
        self.label2 = ttk.Label(self.frame1,text = "Enter the password", foreground="black", background="light blue")
        self.label2.pack()
        self.label2.place(x=125,y=120)
        self.label3 = ttk.Label(self.frame1, text = "")
        self.label3.pack()
        self.label3.place(x=125,y=140) 
        self.username = tk.StringVar()
        self.nameEntered1 = ttk.Entry(self.frame1, width =25, textvariable= self.username, foreground = "black")
        self.nameEntered1.pack()
        self.nameEntered1.place_configure(x=125,y=100)
        self.password = tk.StringVar()
        self.nameEntered2 = ttk.Entry(self.frame1, width = 25, textvariable=self.password,show = "*", foreground="black")
        self.nameEntered2.pack()
        self.nameEntered2.place_configure(x=125, y=140)
        self.button = ttk.Button(self.frame1,text= "Enter",command = self.Enter)
        self.button.pack()
        self.button.place(x=160,y=170)
        self.Button2 = ttk.Button(self.frame1,text= "Create account",command = self.Create_Account)
        self.Button2.pack()
        self.Button2.place(x=155,y=240)
        self.image1 = Image.open(r"lgperson.png")
        self.test = ImageTk.PhotoImage(self.image1)
        self.label4 = tk.Label(image = self.test, bg = "light blue")
        self.label4.image1 = self.test 
        self.label4.pack()
        self.label4.place(x=280, y= 50 )

    def Enter(self):
        global login 
        for i in range(0,len(usernames)):
            if self.username.get() == usernames[i] and self.password.get() == passwords[i]:
                login = "yes"  
                global index 
                index = i
                self.label3.configure(text = "Login successful",background="light blue",font = ('Helvetica bold',15))
                self.label3.place(x =110,y=200)
                self.frame1.after(1000,self.welcome)
            if login == "no":
                self.label3.configure(text = "Invalid Credentials",background="light blue",font = ('Helvetica bold',15))
                self.label3.place(x=100,y=200)
    
    def welcome(self):
        for i in self.master.winfo_children():
            i.destroy()
        self.frame2 = tk.Frame(self.master,width = 600,height = 400)
        self.frame2.pack()
        self.frame2.configure(background = "light blue")
        self.label5 = ttk.Label(self.frame2,text = "Welcome  " + usernames[index],background="light blue", font=('Helvetica bold',15))
        self.label5.pack()
        self.label5.place(x=180,y=150)
        self.frame2.after(1000,self.loginpage)

    def loginpage(self):
        for i in self.master.winfo_children():
            i.destroy()
        self.frame3 = tk.Frame(self.master, width=600,height=400)
        self.frame3.pack()
        self.frame3.configure(background = "light blue")
        self.label1 = ttk.Label(self.frame3,text = "This is your homepage",background="light blue",font = ('Helvetica bold',15))
        self.label1.pack()
        self.label1.place(x=180,y=40)
        self.label2 = ttk.Label(self.frame3,text = "Your notes are:",background="light blue",foreground="black",font = ('Helvetica bold',15))
        self.label2.pack()
        self.label2.place(x=180,y=80)
        self.button1 = ttk.Button(self.frame3,text = "Note 1", command = self.notewrite1)
        self.button1.pack()
        self.button1.place(x=180,y=120)
        self.button2 = ttk.Button(self.frame3,text = "Note 2", command = self.notewrite2)
        self.button2.pack()
        self.button2.place(x=180,y=160)
        self.button3 = ttk.Button(self.frame3,text = "Note 3", command = self.notewrite3)
        self.button3.pack()
        self.button3.place(x=180,y=200)
        self.button4 = ttk.Button(self.frame3,text = "Note 4", command = self.notewrite4)
        self.button4.pack()
        self.button4.place(x=180,y=240)
        self.button5 = ttk.Button(self.frame3,text = "Note 5", command = self.notewrite5)
        self.button5.pack()
        self.button5.place(x=180,y=280)

    def notewrite1(self):
        for i in self.master.winfo_children():
            i.destroy()
        self.frame4 = tk.Frame(self.master, width=600,height=400)
        self.frame4.pack()
        self.frame4.configure(background = "light blue")
        self.label1 = ttk.Label(self.frame4,text = "Note " + str(1),background="light blue", font = (('Helvetica bold'),15))
        self.label1.pack()
        self.label1.place(x=125,y=40)
        self.note = tk.StringVar()
        self.note = self.note.get() +  str(notelist[index][0])
        self.label2 = ttk.Entry(self.frame4,width = 25,textvariable= self.note,foreground="black",font = ('Helvetica bold',15))
        self.label2.pack()
        self.label2.place_configure(x=40,y=80,height=100)
    
    def notewrite2(self):
        for i in self.master.winfo_children():
            i.destroy()
        self.frame4 = tk.Frame(self.master, width=600,height=400)
        self.frame4.pack()
        self.frame4.configure(background = "light blue")
        self.label1 = ttk.Label(self.frame4,text = "Note " + str(2),background="light blue", font = (('Helvetica bold'),15))
        self.label1.pack()
        self.label1.place(x=125,y=40)
        self.note = tk.StringVar()
        self.note = self.note.get() +  str(notelist[index][1])
        self.label2 = ttk.Entry(self.frame4,width = 25,textvariable= self.note,foreground="black",font = ('Helvetica bold',15))
        self.label2.pack()
        self.label2.place_configure(x=40,y=80,height=100)

    def notewrite3(self):
        for i in self.master.winfo_children():
            i.destroy()
        self.frame4 = tk.Frame(self.master, width=600,height=400)
        self.frame4.pack()
        self.frame4.configure(background = "light blue")
        self.label1 = ttk.Label(self.frame4,text = "Note " + str(3),background="light blue", font = (('Helvetica bold'),15))
        self.label1.pack()
        self.label1.place(x=125,y=40)
        self.note = tk.StringVar()
        self.note = self.note.get() +  str(notelist[index][2])
        self.label2 = ttk.Entry(self.frame4,width = 25,textvariable= self.note,foreground="black",font = ('Helvetica bold',15))
        self.label2.pack()
        self.label2.place_configure(x=40,y=80,height=100)

    def notewrite4(self):
        for i in self.master.winfo_children():
            i.destroy()
        self.frame4 = tk.Frame(self.master, width=600,height=400)
        self.frame4.pack()
        self.frame4.configure(background = "light blue")
        self.label1 = ttk.Label(self.frame4,text = "Note " + str(4),background="light blue", font = (('Helvetica bold'),15))
        self.label1.pack()
        self.label1.place(x=125,y=40)
        self.note = tk.StringVar()
        self.note = self.note.get() +  str(notelist[index][3])
        self.label2 = ttk.Entry(self.frame4,width = 25,textvariable= self.note,foreground="black",font = ('Helvetica bold',15))
        self.label2.pack()
        self.label2.place_configure(x=40,y=80,height=100)
    
    def notewrite5(self):
        for i in self.master.winfo_children():
            i.destroy()
        self.frame4 = tk.Frame(self.master, width=600,height=400)
        self.frame4.pack()
        self.frame4.configure(background = "light blue")
        self.label1 = ttk.Label(self.frame4,text = "Note " + str(5),background="light blue", font = (('Helvetica bold'),15))
        self.label1.pack()
        self.label1.place(x=125,y=40)
        self.note = tk.StringVar()
        self.note = self.note.get() +  str(notelist[index][4])
        self.label2 = ttk.Entry(self.frame4,width = 25,textvariable= self.note,foreground="black",font = ('Helvetica bold',15))
        self.label2.pack()
        self.label2.place_configure(x=40,y=80,height=100)

    def Create_Account(self):
        for i in self.master.winfo_children():
            i.destroy()
        self.frame5 = tk.Frame(self.master,width = 600,height = 400)
        self.frame5.pack()
        self.frame5.configure(background = "light blue")
        self.image1 = Image.open(r"lgperson.png")
        self.test = ImageTk.PhotoImage(self.image1)
        self.label1 = tk.Label(image = self.test, bg = "light blue")
        self.label1.image1 = self.test 
        self.label1.pack()
        self.label1.place(x=280, y= 50 )
        self.label2 = ttk.Label(self.frame5,text = "Enter your Name", foreground="black", background="light blue")
        self.label2.pack()
        self.label2.place(x=125,y=80)
        self.label4 = ttk.Label(self.frame5,text = "Enter your Username", foreground="black", background="light blue")
        self.label4.pack()
        self.label4.place(x=125,y=160)
        self.label5 = ttk.Label(self.frame5,text = "Enter your Password", foreground="black", background="light blue")
        self.label5.pack()
        self.label5.place(x=125,y=200)
        self.label6 = ttk.Label(self.frame5,text = "Re-enter your password", foreground="black", background="light blue")
        self.label6.pack()
        self.label6.place(x=125,y=240)
        self.pname = tk.StringVar()
        self.pnameEntered1 = ttk.Entry(self.frame5,width = 25, textvariable= self.pname, foreground="black")
        self.pnameEntered1.pack()
        self.pnameEntered1.place_configure(x=125,y=100)
        self.pusername = tk.StringVar()
        self.pnameEntered2 = ttk.Entry(self.frame5,width = 25, textvariable= self.pusername, foreground="black")
        self.pnameEntered2.pack()
        self.pnameEntered2.place_configure(x=125,y=180)
        self.password1 = tk.StringVar()
        self.pnameEntered3 = ttk.Entry(self.frame5,width = 25, textvariable= self.password1,show="*", foreground="black")
        self.pnameEntered3.pack()
        self.pnameEntered3.place_configure(x=125,y=220)
        self.password2 = tk.StringVar()
        self.pnameEntered4 = ttk.Entry(self.frame5,width = 25, textvariable= self.password2,show="*", foreground="black")
        self.pnameEntered4.pack()
        self.pnameEntered4.place_configure(x=125,y=260)
        self.button3 = ttk.Button(self.frame5, text = "Enter",command = self.storingdata)
        self.button3.pack()
        self.button3.place(x=150,y=290)
        
    def storingdata(self):
        if self.pusername.get() not in usernames:
            if self.password1.get() == self.password2.get():
                usernames.append(self.pusername.get())
                passwords.append(self.password1.get())
                self.file = open("admin.txt","a")
                self.file.write(self.pusername.get())
                self.file.write(",")
                self.file.write(self.password1.get())
                self.file.write("\n")
                self.file.close()
                self.label1 = ttk.Label(self.frame5,text = "Account created sucessfully",background="light blue",foreground="black")
                self.label1.pack()
                self.label1.place(x=125,y=320)
                self.frame5.after(1000,self.back_to_login_page)
            else:
                self.label1 = ttk.Label(self.frame5,text = "Passwords does not match",background="light blue",foreground="black")
                self.label1.pack()
                self.label1.place(x=125,y=320)
                self.frame5.after(1000,self.Create_Account)
        else:
            self.label1 = ttk.Label(self.frame5,text = "Username already in use",background="light blue",foreground="black")
            self.label1.pack()
            self.label1.place(x=125,y=320)
            self.frame5.after(1000,self.Create_Account)

    def back_to_login_page(self):        
        self.welcome_page()    
   

window = tk.Tk()
Application(window)
window.mainloop()