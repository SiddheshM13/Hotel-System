import tkinter as tk
from tkinter import *
from tkinter import messagebox as mb
from tkinter import ttk

class Checkout:
    root=tk.Tk()
    root.title('CHECKOUT')
    root.configure(bg='black')

    def back(self):
        self.root.destroy()
        from start import StartPage
    
    def fetch(self):
        import MySQLdb as ms
        db=ms.connect('Localhost', 'root', '', 'test')
        cursor=db.cursor()
        try:    
            cursor.execute("SELECT * FROM user WHERE room_number= {r}".format(r=self.e1.get()))    
            k=cursor.fetchone()
            db.commit()
            name = k[1]
            number = k[2]
            room_type = k[3]
            date = k[4]
            amount = k[5]
            
            self.e2.delete(0, END)
            self.e3.delete(0, END)
            self.e4.delete(0, END)
            self.e5.delete(0, END)
            self.e6.delete(0, END)
    
            self.e2.insert(END, name)
            self.e3.insert(END, number)
            self.e4.insert(END, room_type)
            self.e5.insert(END, date)
            self.e6.insert(END, amount)
        except:
            mb.showerror("CHECKOUT", "Room is vacant")
            self.e1.delete(0,END)
            self.e1.focus()
            self.e2.delete(0,END)
            self.e3.delete(0,END)
            self.e4.delete(0,END)
            self.e5.delete(0,END)
            self.e6.delete(0,END)

    
    def checkout(self):
        self.k=self.combobox1.get() + ' ' + self.combobox2.get() + ' '+ self.combobox3.get()
        import MySQLdb as ms
        db = ms.connect('localhost', 'root', '', 'test')
        cursor = db.cursor()
        cursor.execute("SELECT room_number from user where room_number={f}".format(f=self.e1.get()))
        try:
            k=cursor.fetchone()[0]
            db.commit()
            cursor.execute("INSERT INTO record(room_number, name, number, room_type, amount, indate, outdate) values(%s, %s, %s, %s, %s, %s, %s)", (self.e1.get(), self.e2.get(), self.e3.get(), self.e4.get(), self.e6.get(), self.e5.get(), self.k))
            db.commit()
            cursor.execute("DELETE FROM user WHERE room_number={f}".format(f=self.e1.get()))
            db.commit()
            mb.showinfo("ALERT", "Checked-out successfully. \nTotal bill is ₹{f}".format(f=self.e6.get()))
        except:
            mb.showerror("ALERT", "Room is vacant")

                            
    def __init__(self):
        self.lbl6 = tk.Label(self.root, text='Checkout', fg='white', bg='black', font='georgia 12 bold').grid(row=0, column=0, sticky=tk.E)
        self.lbl7 = tk.Label(self.root, text='Page', fg='white', bg='black', font='georgia 12 bold').grid(row=0, column=1, sticky=tk.W)
                
        self.lbl1 = tk.Label(self.root, text='Room No: ', fg='yellow', bg='black', font='georgia 10 bold').grid(row=1, column=0, sticky=tk.W)
        self.e1 = tk.Entry(self.root, fg='yellow', bg='black', font='courier 9 bold')
        self.e1.grid(row=1, column=1, pady=5, padx=2, sticky=tk.W)
        self.lbl2 = tk.Label(self.root, text='Name: ', fg='yellow', bg='black', font='georgia 10 bold').grid(row=2, column=0, sticky=tk.W)
        self.e2 = tk.Entry(self.root, fg='yellow', bg='black', font='courier 9 bold')
        self.e2.grid(row=2, column=1, pady=5, padx=2, sticky=tk.W)
        self.lbl3 = tk.Label(self.root, text='Contact: ', fg='yellow', bg='black', font='georgia 10 bold').grid(row=3, column=0, sticky=tk.W)
        self.e3 = tk.Entry(self.root, fg='yellow', bg='black', font='courier 9 bold')
        self.e3.grid(row=3, column=1, pady=5, padx=2, sticky=tk.W)
        self.lbl4 = tk.Label(self.root, text='Room Type: ', fg='yellow', bg='black', font='georgia 10 bold').grid(row=4, column=0, sticky=tk.W)
        self.e4 = tk.Entry(self.root, fg='yellow', bg='black', font='courier 9 bold')
        self.e4.grid(row=4, column=1, pady=5, padx=2, sticky=tk.W)
        self.lbl5 = tk.Label(self.root, text='Check-in Date: ', fg='yellow', bg='black', font='georgia 10 bold').grid(row=5, column=0, sticky=tk.W)
        self.e5 = tk.Entry(self.root, fg='yellow', bg='black', font='courier 9 bold')
        self.e5.grid(row=5, column=1, pady=5, padx=2, sticky=tk.W)
        self.lbl6 = tk.Label(self.root, text='Total Bill:', fg='yellow', bg='black', font='georgia 10 bold').grid(row=6, column=0, sticky=tk.W)
        self.e6 = tk.Entry(self.root, fg='yellow', bg='black', font='courier 9 bold')
        self.e6.grid(row=6, column=1, pady=5, padx=2, sticky=tk.W)
        
        self.lbl7 =tk.Label(self.root, text='Checkout Date:', fg='yellow', bg='black', font='georgia 10 bold').grid(row=7, column=0, pady=5, sticky=tk.W) 
        elements = ['1', '2', '3', '4', '5', '6','7','8','9','10','11','12','13','14','15','16','17','19','20','21','22','23','24','25','26','27','28','29','30','31']
        self.combobox1 = ttk.Combobox(self.root, values=elements, width= 17, font='courier 9 bold')
        self.combobox1.current(0) 
        self.combobox1.grid(row=7, column=1, pady=5, padx=2, sticky=tk.W)
        
        self.lbl8 = tk.Label(self.root, text='Select Month:', fg='yellow', bg='black', font='georgia 10 bold').grid(row=8, column=0, pady=5, sticky=tk.W) 
        elements = ['January', 'February','March','April','May','June','July','August','September','October','November','December']
        self.combobox2 = ttk.Combobox(self.root, values=elements, width= 17, font='courier 9 bold')
        self.combobox2.current(0) 
        self.combobox2.grid(row=8, column=1, pady=5, padx=2, sticky=tk.W)
        
        self.lbl9 = tk.Label(self.root, text='Select Year:', fg='yellow', bg='black', font='georgia 10 bold').grid(row=9, column=0, pady=5, sticky=tk.W) 
        elements = ['2016', '2017', '2018', '2019', '2020', '2021', '2022', '2023', '2024', '2025', '2026', '2027', '2028', '2029', '2030']
        self.combobox3 = ttk.Combobox(self.root, values=elements, width= 17, font='courier 9 bold')
        self.combobox3.current(0) 
        self.combobox3.grid(row=9, column=1, pady=5, padx=2, sticky=tk.W)

        self.button1= Button (self.root, text= "Checkout" , fg='red', bg='black', font='georgia 10 bold', width=15, command=self.checkout).grid( row=10, column=0, pady=5)
        self.button2= Button (self.root, text= "Fetch" , fg='red', bg='black', font='georgia 10 bold', width=15, command=self.fetch).grid( row=10, column=1, pady=5, padx=5)
        self.button3= Button (self.root, text= "Return" , fg='red', bg='black', font='georgia 10 bold', width=15, command=self.back).grid( row=11, column=0, pady=5, padx=5)
        self.button4= Button (self.root, text= "Exit" , fg='red', bg='black', font='georgia 10 bold', width=15, command=exit).grid( row=11, column=1, pady=5, padx=5)

        self.root.mainloop()
        
Checkout()