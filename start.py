import tkinter as tk
from tkinter import *
from tkinter import messagebox as mb

class StartPage():
    
    root = tk.Tk()
    root.geometry('205x295')
    root.title("START")
    root.configure(bg='black')
    def bill(self):
        self.root.destroy()
        from test import Book

    def total(self):
        self.root.destroy()
        from totalbill import Total
        
    def food(self):
        self.root.destroy()
        from food import Food

    def checkout(self):
        self.root.destroy()
        from checkout import Checkout
    
    def __init__(self):
        self.lbl1 = tk.Label(self.root, text ='Select choice:', bg='black', fg='yellow', font='Georgia 10 bold').grid(row=0, column=0, sticky=tk.W, pady=10)
        self.btn1 = tk.Button(self.root, text ='Book Rooms', width=20, fg='yellow', bg='black', font='courier 10 bold', command=self.bill).grid(row=1, column=0, sticky=tk.E, padx=20)
        self.btn2 = tk.Button(self.root, text ='Food Bill', width=20, fg='yellow', bg='black', font='courier 10 bold', command=self.food).grid(row=2, column=0, sticky=tk.E, pady=5, padx=20)
        self.btn3 = tk.Button(self.root, text ='Total Bill', width=20, fg='yellow', bg='black', font='courier 10 bold', command=self.total).grid(row=3, column=0, sticky=tk.E, padx=20)   
        self.btn4 = tk.Button(self.root, text ='Checkout', width=20, fg='yellow', bg='black', font='courier 10 bold', command=self.checkout).grid(row=4, column=0, sticky=tk.E, padx=20, pady=5)   
        self.btn5 = tk.Button(self.root, text ='Current Records', width=20, fg='yellow', bg='black', font='courier 10 bold', command=self.checkout).grid(row=5, column=0, sticky=tk.E, padx=20)   
        self.btn6 = tk.Button(self.root, text ='Complete Records', width=20, fg='yellow', bg='black', font='courier 10 bold', command=self.checkout).grid(row=6, column=0, sticky=tk.E, padx=20, pady=5)   
        self.btn7 = tk.Button(self.root, text ='Quit', width=15, fg='yellow', bg='black', font='courier 10 bold', command=exit).grid(row=7, column=0, padx=20, pady=10)   

        self.root.mainloop()
        
StartPage()        