import tkinter as tk
from tkinter import *
from tkinter import messagebox as mb

class Total():
    
    root=tk.Tk()
    root.title("BILLING")
    root.configure(bg='black')

    def calc(self):
        if not self.e14.get():
            mb.showerror("ERROR", "Please enter room number!")
            self.e14.focus()
        else:
            import MySQLdb as ms
            db = ms.connect('localhost', 'root', '', 'test')
            cursor = db.cursor()
            cursor.execute("SELECT amount FROM user where room_number=%s", (self.e14.get()))
            try:    
                k = cursor.fetchone()[0]        
                mb.showinfo("Total Bill", "Total bill for Room no. {e14} is {k}".format(e14=self.e14.get(), k=k))
            except:
                mb.showerror("ERROR", "Room not reserved")

    def back(self):
        self.root.destroy()
        from start import StartPage
    
    def __init__(self):    
        self.lb4 = tk.Label(self.root, text="Enter RoomNo. to generate Bill:", fg='yellow', bg='black', font='georgia 10 bold').grid(row=32, column=0, sticky=tk.W)
        self.e14 = tk.Entry(self.root, fg='white', bg='black', font='georgia 10 bold', highlightcolor='white', cursor='dot')
        self.e14.grid(row=33, column=0)
        self.button6= Button (self.root, text= "Bill" , fg='white', bg='black', font='georgia 10 bold', width=15, command=self.calc).grid(row=33, column=1, pady=5, padx=5)
        self.button7= Button (self.root, text= "Return" , fg='white', bg='black', font='georgia 10 bold', width=15, command=self.back).grid(row=34, column=0, pady=5, padx=5)
        self.button8= Button (self.root, text= "Exit" , fg='white', bg='black', font='georgia 10 bold', width=15, command=exit).grid(row=34, column=1, pady=5, padx=5)
    
        self.root.mainloop()

Total()

