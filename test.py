import tkinter as tk
from tkinter import *
from tkinter import ttk
from tkinter import messagebox as mb

class Book():
    root=tk.Tk()
    root.title("GST HOTEL")
    root.configure(bg='black')
    
    def back(self):
        self.root.destroy()
        from start import StartPage
        
#     def tick(self):
#         self.p = [1,2,3,4,5,6,7,8,9,10]
#         self.q = [11,12,13,14,15]
#         self.r = [16,17,18,19,20]
#         if not self.e1.get() or not self.e2.get():
#             mb.showerror("Booking", "Please enter all details")
#             self.h = self.combobox1.get() +' '+ self.combobox2.get() +' '+ self.combobox3.get()
#             import MySQLdb as ms
#             db = ms.connect('localhost', 'root', '', 'test')
#             cursor = db.cursor()
#             if(self.v1.get == 1):
#                 for i in p:
                    
    def check(self):
        if not self.e1.get() or not self.e2.get():
            mb.showerror("Booking", "Please enter all details")
        else:    
            self.h = self.combobox1.get() +' '+ self.combobox2.get() +' '+ self.combobox3.get()
            import MySQLdb as ms
            db = ms.connect('localhost', 'root', '', 'test')
            cursor = db.cursor()
            if(self.v1.get()==1):
                cursor.execute("SELECT count(*) FROM user WHERE room_type='AC'")
                t = cursor.fetchone()[0]
                db.commit()
                t = t+1
                if t<11:
                    cursor.execute("SELECT count(*) FROM user")
                    l = cursor.fetchone()[0]
                    db.commit()
                    l = l+1
                    cursor.execute("INSERT INTO user(room_number, name, number, room_type, date, amount) values(%s, %s, %s, %s, %s, %s)", (l, self.e1.get(), self.e2.get(), 'AC', self.h, '1000'))
                    db.commit()
                    mb.showinfo("ALERT", "AC Room booked successfully. Room no is {t}".format(t= l))
                else:
                    mb.showerror("ALERT", "AC Rooms fully booked")        

            elif(self.v1.get()==2):
                cursor.execute("SELECT count(*) FROM user WHERE room_type='Suite'")
                t = cursor.fetchone()[0]
                db.commit()
                t = t+1
                if t<11:
                    cursor.execute("SELECT count(*) FROM user")
                    l = cursor.fetchone()[0]
                    db.commit()
                    l = l+1
                    cursor.execute("INSERT INTO user(room_number, name, number, room_type, date, amount) values(%s, %s, %s, %s, %s, %s)", (l, self.e1.get(), self.e2.get(), 'Suite', self.h, '1500'))
                    db.commit()
                    mb.showinfo("ALERT", "Suite Room booked successfully. Room no is {t}".format(t= l))
                else:
                    mb.showerror("ALERT", "Suite Rooms fully booked")        

            else:
                cursor.execute("SELECT count(*) FROM user WHERE room_type='Normal'")
                t = cursor.fetchone()[0]
                db.commit()
                t = t+1
                if t<11:
                    cursor.execute("SELECT count(*) FROM user")
                    l = cursor.fetchone()[0]
                    db.commit()
                    l = l+1
                    cursor.execute("INSERT INTO user(room_number, name, number, room_type, date, amount) values(%s, %s, %s, %s, %s, %s)", (l, self.e1.get(), self.e2.get(), 'Normal', self.h, '500'))
                    db.commit()
                    mb.showinfo("ALERT", "Room booked successfully. Room no is {t}".format(t= l))
                else:
                    mb.showerror("ALERT", "Rooms fully booked")        
            cursor.close()
            db.close()            

    def __init__(self):
                               
        self.lbl6 =tk.Label(self.root, text='Select Date:', fg='white', bg='black', font='georgia 10 bold').grid(row=0, column=0, pady=5, sticky=tk.W) 
        elements = ['1', '2', '3', '4', '5', '6','7','8','9','10','11','12','13','14','15','16','17','19','20','21','22','23','24','25','26','27','28','29','30','31']
        self.combobox1 = ttk.Combobox(self.root, values=elements, font='georgia 8 bold')
        self.combobox1.current(0) 
        self.combobox1.grid(row=0, column=1, pady=5)
        
        self.lbl7 = tk.Label(self.root, text='Select Month:', fg='white', bg='black', font='georgia 10 bold').grid(row=1, column=0, pady=5, sticky=tk.W) 
        elements = ['January', 'February','March','April','May','June','July','August','September','October','November','December']
        self.combobox2 = ttk.Combobox(self.root, values=elements, font='georgia 8 bold')
        self.combobox2.current(0) 
        self.combobox2.grid(row=1, column=1, pady=5)
        
        self.lbl1 = tk.Label(self.root, text='Select Year:', fg='white', bg='black', font='georgia 10 bold').grid(row=2, column=0, pady=5, sticky=tk.W) 
        elements = ['2016', '2017', '2018', '2019', '2020', '2021', '2022', '2023', '2024', '2025', '2026', '2027', '2028', '2029', '2030']
        self.combobox3 = ttk.Combobox(self.root, values=elements, font='georgia 8 bold')
        self.combobox3.current(0) 
        self.combobox3.grid(row=2, column=1, pady=5)
        
        self.lbl1 = tk.Label(self.root, text="Select Room type: ", fg='white', bg='black', font='georgia 10 bold').grid(row=4, column=0, sticky=tk.W)   
        self.v1=tk.IntVar()
        self.rad1 = tk.Radiobutton(self.root, text='AC', variable= self.v1, value=1, fg='white', bg='black', font='georgia 10 bold', selectcolor='black', activebackground='black', activeforeground='white').grid(row=5, column=0, sticky=tk.W)
        self.rad2 = tk.Radiobutton(self.root, text='Suite', variable= self.v1, value=2, fg='white', bg='black', font='georgia 10 bold', selectcolor='black', activebackground='black', activeforeground='white').grid(row=6, column=0, sticky=tk.W)
        self.rad3 = tk.Radiobutton(self.root, text='Normal', variable= self.v1, value=3, fg='white', bg='black', font='georgia 10 bold', selectcolor='black', activebackground='black', activeforeground='white').grid(row=7, column=0, sticky=tk.W)
            
        self.label_1 = Label(self.root, text="Charges: ₹1000", fg='yellow', bg='black', font='georgia 10 bold').grid( row=5, column=1, sticky=tk.W, pady=1)
        self.label_2 = Label(self.root, text= "Charges: ₹1500", fg='yellow', bg='black', font='georgia 10 bold').grid( row=6, column=1, sticky=tk.W, pady=1)
        self.label_3 = Label(self.root, text= "Charges: ₹500", fg='yellow', bg='black', font='georgia 10 bold').grid(row =7, column= 1, sticky=tk.W, pady=1)
        
        self.label_4= Label(self.root, text=" Enter Name: ",fg='white', bg='black', font='georgia 10 bold').grid(row=8, column=0, sticky=tk.W, pady=5)
        self.e1 = tk.Entry(self.root,fg='white', bg='black', font='georgia 10 bold', highlightcolor='white', cursor='dot')
        self.e1.grid(row=8, column=1, sticky=tk.W, pady=5, padx=5)
        
        self.label_5= Label(self.root, text= "Enter Mobile number: ", fg='white', bg='black', font='georgia 10 bold').grid(row=9, column=0, sticky=tk.W, pady=5)
        self.e2 = tk.Entry(self.root,fg='white', bg='black', font='georgia 10 bold', highlightcolor='white', cursor='dot')
        self.e2.grid(row=9, column=1, sticky=tk.W, pady=5, padx=5)
        
        self.button4= Button (self.root, text= "Submit" , fg='white', bg='black', font='georgia 10 bold', width=15, command=self.check).grid( row=11, column=0, pady=5)
        self.button5= Button (self.root, text= "Exit" , fg='white', bg='black', font='georgia 10 bold', width=15, command=exit).grid( row=11, column=1, pady=5, padx=5)

        self.button6= Button (self.root, text= "Return" , fg='white', bg='black', font='georgia 10 bold', width=15, command=self.back).grid( row=12, column=1, pady=5, padx=5)

        self.root.mainloop()
Book()