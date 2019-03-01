import tkinter as tk
from tkinter import *
from tkinter import messagebox as mb

class LoginPage():
    
    root = tk.Tk()
    root.title("Login Page")
    root.configure(bg='black')
    
    def login(self):
        if not self.e1.get() and not self.e2.get():
            mb.showerror("ERROR", "Please enter Username and Password")
            self.e1.focus()
        elif not self.e1.get():
            mb.showerror("ERROR", "Enter Username")
            self.e1.focus()
        elif not self.e2.get():
            mb.showerror("ERROR", "Enter Password")   
            self.e2.focus() 
        else:
            username = self.e1.get()
            password = self.e2.get()
            import MySQLdb as ms
            db = ms.connect('Localhost', 'root', '', 'test')
            cursor = db.cursor()
            cursor.execute("SELECT username, password FROM login WHERE username='{username}' AND password='{password}'".format(username=username, password=password))
            db.commit()
            
            try:
                k = cursor.fetchone()
                
                if username == k[0] and password == k[1]:
                    mb.showinfo("LOGIN", "Login Successful")
                    self.root.destroy()
                    from start import StartPage
                    
            except:
                mb.showerror("LOGIN", "Login Unsuccessful. \nPlease enter correct username and password")
                self.e1.focus()    
            
    def __init__(self):
        self.lbl1= Label(self.root, text="Enter Username", bg='black', fg='yellow', font='georgia 9 bold').grid(row=0, column=0, sticky=tk.E)
        self.lbl2= Label(self.root, text="And Password", fg='yellow', bg='black', font='georgia 9 bold').grid(row=0, column=1, sticky=tk.W)
        self.lbl3= Label(self.root, text="Username:", fg='red', bg='black', font='georgia 8 bold').grid(row=1, column=0, sticky=tk.W)
        self.e1= Entry(self.root, fg='yellow', bg='black', font='georgia 8 bold')
        self.e1.grid(row=1, column=1, padx=5)
        self.lbl4= Label(self.root, text="Password:", fg='red', bg='black', font='georgia 8 bold').grid(row=2, column=0, sticky=tk.W, pady=5)
        self.e2= Entry(self.root, fg='yellow', bg='black', font='georgia 8 bold', show='*')
        self.e2.grid(row=2, column=1, pady=4, padx=5)
        self.btn1= Button(self.root, text="Login", command=self.login, fg='yellow', bg='black', font='georgia 8 bold').grid(row=3, column=0, pady=4)
        self.btn2= Button(self.root, text="Exit", command=exit, fg='yellow', bg='black', font='georgia 8 bold').grid(row=3, column=1, pady=4)
        
        self.root.mainloop()
        
LoginPage()
        
    
    
    
