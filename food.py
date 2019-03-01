import tkinter as tk
from tkinter import messagebox as mb
from tkinter import *

class Food:
    root = tk.Tk()
    root.title("FOOD MENU")
    root.config(bg='black')
    root.geometry('200x440')
    
    def bill(self):        
        bill1 = int((int(self.e4.get())*100)+(int(self.e5.get())*70)+(int(self.e6.get())*500)+(int(self.e7.get())*300)+(int(self.e8.get())*200))
        bill2 = int((int(self.e9.get())*150)+(int(self.e10.get())*50)+(int(self.e11.get())*70)+(int(self.e12.get())*100)+(int(self.e13.get())*80)) 
        bill = int(bill1)+ int(bill2)
        print(bill)
        if not self.e3.get():
            mb.showerror("Bill", "Please enter room no.")
            self.e3.focus()
        else:
            import MySQLdb as ms
            db = ms.connect('localhost', 'root', '', 'test')
            cursor = db.cursor()
            cursor.execute("SELECT room_number from user where room_number={f}".format(f=self.e3.get()))
            try:
                k=cursor.fetchone()[0]
                mb.showinfo("Bill","Food bill is ₹{bill1}. Drinks bill is ₹{bill2}. \nTotal Food Bill for room no. {x} is ₹{bill}".format(bill1=bill1, bill2=bill2, x=self.e3.get(), bill=bill)) 
                cursor.execute("SELECT amount FROM user where room_number=%s", (self.e3.get()))
                l = cursor.fetchone()[0]
                print(l)
                tot = int(l)+int(bill)        
                db.commit()
                cursor.execute("UPDATE user SET amount= %s WHERE room_number= %s", (tot, self.e3.get()))
                db.commit()
                cursor.close()
                db.close()
                print(tot)
            except:
                mb.showerror("ALERT", "Room number invalid")

            
    def reset(self):
        self.e4.delete(0, END)
        self.e4.insert(END,'0')
        self.e5.delete(0, END)
        self.e5.insert(END,'0')
        self.e6.delete(0, END)
        self.e6.insert(END,'0')
        self.e7.delete(0, END)
        self.e7.insert(END,'0')
        self.e8.delete(0, END)
        self.e8.insert(END,'0')
        self.e9.delete(0, END)
        self.e9.insert(END,'0')
        self.e10.delete(0, END)
        self.e10.insert(END,'0')
        self.e11.delete(0, END)
        self.e11.insert(END,'0')
        self.e12.delete(0, END)
        self.e12.insert(END,'0')
        self.e13.delete(0, END)
        self.e13.insert(END,'0')
    
    def back(self):
        self.root.destroy()
        from start import StartPage
    
    def __init__(self):        
        self.lb3 = tk.Label(self.root, text="Enter room no:", fg='yellow', bg='black', font='courier 11 bold').grid(row=17, column=0, sticky=tk.W, pady=10)
        self.e3 = tk.Entry(self.root, fg='white', bg='black', font='courier 10 bold', width=5)
        self.e3.grid(row=17, column=1, padx=5, sticky=tk.W)
        
        self.lb4 = tk.Label(self.root, text="Select items:", fg='yellow', bg='black', font='georgia 10 bold').grid(row=18, column=0, sticky=tk.W)
        self.lb5 = tk.Label(self.root, text="1. FOOD: ", fg='red', bg='black', font='georgia 8 bold').grid(row=19, column=0, pady=5, sticky=tk.W)
        self.lb11 = tk.Label(self.root, text="Fries(₹100)", fg='white', bg='black', font='georgia 8 bold').grid(row=20, column=0, sticky=tk.W)
        self.lb12 = tk.Label(self.root, text="Salad(₹70)", fg='white', bg='black', font='georgia 8 bold').grid(row=21, column=0, sticky=tk.W)
        self.lb13 = tk.Label(self.root, text="Chicken Roll(₹500)", fg='white', bg='black', font='georgia 8 bold').grid(row=22, column=0, sticky=tk.W)
        self.lb14 = tk.Label(self.root, text="Burger(₹300)", fg='white', bg='black', font='georgia 8 bold').grid(row=23, column=0, sticky=tk.W)
        self.lb15 = tk.Label(self.root, text="Momos(₹200)", fg='white', bg='black', font='georgia 8 bold').grid(row=24, column=0, sticky=tk.W)
        
        self.e4 = tk.Entry(self.root, fg='yellow', bg='black', font='georgia 10 bold', selectbackground='black', width=5)
        self.e4.insert(END,'0')
        self.e4.grid(row=20, column=1, pady=2, sticky=tk.W)
        
        self.e5 = tk.Entry(self.root, fg='yellow', bg='black', font='georgia 10 bold', width=5, selectbackground='black')
        self.e5.insert(END,'0')
        self.e5.grid(row=21, column=1, pady=2, sticky=tk.W)
        
        self.e6 = tk.Entry(self.root, fg='yellow', bg='black', font='georgia 10 bold', width=5, selectbackground='black')
        self.e6.insert(END,'0')
        self.e6.grid(row=22, column=1, pady=2, sticky=tk.W)
        
        self.e7 = tk.Entry(self.root, fg='yellow', bg='black', font='georgia 10 bold', width=5, selectbackground='black')
        self.e7.insert(END,'0')
        self.e7.grid(row=23, column=1, sticky=tk.W, pady=2)
        
        self.e8 = tk.Entry(self.root, fg='yellow', bg='black', font='georgia 10 bold', width=5, selectbackground='black')
        self.e8.insert(END,'0')
        self.e8.grid(row=24, column=1, sticky=tk.W, pady=2)
        
        self.lb5 = tk.Label(self.root, text="2. JUICES ", fg='red', bg='black', font='georgia 10 bold').grid(row=25, column=0, pady=5, sticky=tk.W)
        self.lb6 = tk.Label(self.root, text="Cocktail(₹150)", fg='white', bg='black', font='georgia 10 bold').grid(row=26, column=0, sticky=tk.W)
        self.lb7 = tk.Label(self.root, text="Sugarcane(₹50)", fg='white', bg='black', font='georgia 10 bold').grid(row=27, column=0, sticky=tk.W)
        self.lb8 = tk.Label(self.root, text="Grapes(₹70)", fg='white', bg='black', font='georgia 10 bold').grid(row=28, column=0, sticky=tk.W)
        self.lb9 = tk.Label(self.root, text="Mango(₹100)", fg='white', bg='black', font='georgia 10 bold').grid(row=29, column=0, sticky=tk.W)
        self.lb10 = tk.Label(self.root, text="Pineapple(₹80)", fg='white', bg='black', font='georgia 10 bold').grid(row=30, column=0, sticky=tk.W)
        
        self.e9 = tk.Entry(self.root, fg='yellow', bg='black', font='georgia 10 bold', width=5, selectbackground='black')
        self.e9.insert(END,'0')
        self.e9.grid(row=26, column=1, pady=2, sticky=tk.W)

        self.e10 = tk.Entry(self.root, fg='yellow', bg='black', font='georgia 10 bold', width=5, selectbackground='black')
        self.e10.insert(END,'0')
        self.e10.grid(row=27, column=1, pady=2, sticky=tk.W)

        self.e11 = tk.Entry(self.root, fg='yellow', bg='black', font='georgia 10 bold', width=5, selectbackground='black')
        self.e11.insert(END,'0')
        self.e11.grid(row=28, column=1, pady=2, sticky=tk.W)

        self.e12 = tk.Entry(self.root, fg='yellow', bg='black', font='georgia 10 bold', width=5, selectbackground='black')
        self.e12.insert(END,'0')
        self.e12.grid(row=29, column=1, pady=2, sticky=tk.W)

        self.e13 = tk.Entry(self.root, fg='yellow', bg='black', font='georgia 10 bold', width=5, selectbackground='black')
        self.e13.insert(END,'0')
        self.e13.grid(row=30, column=1, pady=2, sticky=tk.W)
        
        self.button1= tk.Button(self.root, text= "Bill" , fg= "yellow", bg='black', font='courier 9 bold', width=10, command=self.bill).grid(row=31, column=0, pady=5)
        self.button2= tk.Button(self.root, text= "Reset" , fg= "yellow", bg='black', font='courier 9 bold', width=6, command=self.reset).grid(row=31, column=1, pady=5, sticky=tk.W)
        self.button3= tk.Button(self.root, text= "Return" , fg= "yellow", bg='black', font='courier 9 bold', width=10, command=self.back).grid(row=32, column=0, pady=5)
        self.button4= tk.Button(self.root, text= "Exit" , fg= "yellow", bg='black', font='courier 9 bold', width=6, command=exit).grid(row=32, column=1, pady=5, sticky=tk.W)
        
        self.root.mainloop()

Food()