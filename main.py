import tkinter as tk
from tkinter import *
from tkinter import ttk
from tkinter import messagebox as mb

def check():
    if not (e1.get() or e2.get()):
        mb.showerror("Booking", "Please enter all details")
    else:    
        import MySQLdb as ms
        if(v1.get()==1):
            print(v1)
            a='AC'
            b=1000
        elif(v1.get()==2):
            print(v1)
            a='Suite'
            b=1500
        else:
            print(v1)
            a='Normal'
            b=500
        db = ms.connect('localhost', 'root', '', 'test')
        cursor = db.cursor()
        cursor.execute("SELECT count(*) FROM user")
        t = cursor.fetchone()[0]
        db.commit()
        t = t+1
        if t<11:
            cursor.execute("INSERT INTO user(room_number, name, number, room_type, date, month, amount) values(%s, %s, %s, %s, %s, %s, %s)", (t, e1.get(), e2.get(), a, combobox1.get(), combobox2.get(), b))
            db.commit()
            mb.showinfo("ALERT", "Room booked successfully. Room no is {t}".format(t= t))
        else:
            mb.showerror("ALERT", "Rooms fully booked")        
        cursor.close()
        db.close()
    
def bill():
    
    bill1 = int((int(e4.get())*100)+(int(e5.get())*70)+(int(e6.get())*500)+(int(e7.get())*300)+(int(e8.get())*200))
    bill2 = int((int(e9.get())*150)+(int(e10.get())*50)+(int(e11.get())*70)+(int(e12.get())*100)+(int(e13.get())*80)) 
    bill = int(bill1)+ int(bill2)
    print(bill)
    if not e3.get():
        mb.showerror("Bill", "Please enter room no.")
        e3.focus()
    else:
        mb.showinfo("Bill","Food bill is {bill1}. Drinks bill is {bill2}. \nTotal Food Bill for room no. {x} is {bill}".format(bill1=bill1, bill2=bill2, x=e3.get(), bill=bill)) 
        import MySQLdb as ms
        db = ms.connect('localhost', 'root', '', 'test')
        cursor = db.cursor()
        cursor.execute("SELECT amount FROM user where room_number=%s", (e3.get()))
        k = cursor.fetchone()[0]
        print(k)
        tot = int(k)+int(bill)        
        db.commit()
        cursor.execute("UPDATE user SET amount= %s WHERE room_number= %s", (tot, e3.get()))
        db.commit()
        cursor.close()
        db.close()
        print(tot)
        
def reset():
    e4.delete(0, END)
    e4.insert(END,'0')
    e5.delete(0, END)
    e5.insert(END,'0')
    e6.delete(0, END)
    e6.insert(END,'0')
    e7.delete(0, END)
    e7.insert(END,'0')
    e8.delete(0, END)
    e8.insert(END,'0')
    e9.delete(0, END)
    e9.insert(END,'0')
    e10.delete(0, END)
    e10.insert(END,'0')
    e11.delete(0, END)
    e11.insert(END,'0')
    e12.delete(0, END)
    e12.insert(END,'0')
    e13.delete(0, END)
    e13.insert(END,'0')
    
def total():
    if not e14.get():
        mb.showerror("ERROR", "Please enter room number!")
        e14.focus()
    else:
        import MySQLdb as ms
        db = ms.connect('localhost', 'root', '', 'test')
        cursor = db.cursor()
        cursor.execute("SELECT amount FROM user where room_number=%s", (e14.get()))
        try:    
            k = cursor.fetchone()[0]        
            mb.showinfo("Total Bill", "Total bill for Room no. {e14} is {k}".format(e14=e14.get(), k=k))
        except:
            mb.showerror("ERROR", "Room not reserved")
            
          
root=tk.Tk()
root.title("GST HOTEL")
lbtitle1 = tk.Label(root, text= "GST", fg='red', bg='yellow').grid(row=0, column=0, sticky=tk.E)
lbtitle2 = tk.Label(root, text= "HOTEL", fg='red', bg='yellow').grid(row=0, column=1, sticky=tk.W)

tk.Label(root, text='Select Date:', fg='blue').grid(row=1, column=0, pady=5, sticky=tk.W) 
elements = ['1', '2', '3', '4', '5', '6','7','8','9','10','11','12','13','14','15','16','17','19','20','21','22','23','24','25','26','27','28','29','30','31']
combobox1 = ttk.Combobox(root, values=elements)
combobox1.current(0) 
combobox1.grid(row=1, column=1, pady=5)

tk.Label(root, text='Select Month:', fg='blue').grid(row=2, column=0, pady=5, sticky=tk.W) 
elements = ['January', 'February','March','April','May','June','July','August','September','October','November','December']
combobox2 = ttk.Combobox(root, values=elements)
combobox2.current(0) 
combobox2.grid(row=2, column=1, pady=5)

lbl1 = tk.Label(root, text="Select Room type: ", fg='blue').grid(row=4, column=0, sticky=tk.W)   
v1=tk.IntVar()
tk.Radiobutton(root, text='AC', variable=v1, value=1).grid(row=5, column=0, sticky=tk.W)
tk.Radiobutton(root, text='Suite', variable=v1, value=2).grid(row=6, column=0, sticky=tk.W)
tk.Radiobutton(root, text='Normal', variable=v1, value=3).grid(row=7, column=0, sticky=tk.W)
    
label_1= Label(root, text="Charges: ₹1000").grid( row=5, column=1, sticky=tk.W, pady=1)
label_2 = Label(root, text= "Charges: ₹500").grid( row=6, column=1, sticky=tk.W, pady=1)
label_3 = Label(root, text= "Charges: ₹1500").grid(row =7, column= 1, sticky=tk.W, pady=1)

label_4= Label(root, text=" Enter Name: ", fg='blue').grid(row=8, column=0, sticky=tk.W, pady=5)
e1 = tk.Entry(root)
e1.grid(row=8, column=1, sticky=tk.W, pady=5)

label_5= Label(root, text= "Enter Mobile number: ", fg='blue').grid(row=9, column=0, sticky=tk.W, pady=5)
e2 = tk.Entry(root)
e2.grid(row=9, column=1, sticky=tk.W, pady=5)

button4= Button (root, text= "Submit" , fg= "red", width=15, command=check).grid( row=11, column=0, pady=5)
button5= Button (root, text= "Exit" , fg= "red", width=15, command=exit).grid( row=11, column=1, pady=5)

lb1 = tk.Label(root, text="GST", fg='red', bg='yellow').grid(row=16, column=0, sticky=tk.E)   
lb2 = tk.Label(root, text="RESTAURANT", fg='red', bg='yellow').grid(row=16, column=1, sticky=tk.W)

lb3 = tk.Label(root, text="Enter room no:", fg='blue').grid(row=17, column=0, sticky=tk.W, pady=10)
e3 = tk.Entry(root)
e3.grid(row=17, column=1)

lb4 = tk.Label(root, text="SELECT ITEMS AND QUANTITY:", fg='red').grid(row=18, column=0, sticky=tk.W)
lb5 = tk.Label(root, text="1. FOOD: ", fg='green').grid(row=19, column=0, pady=5, sticky=tk.W)
lb3 = tk.Label(root, text="Fries(₹100)", fg='blue').grid(row=20, column=0, sticky=tk.W)
lb3 = tk.Label(root, text="Salad(₹70)", fg='blue').grid(row=21, column=0, sticky=tk.W)
lb3 = tk.Label(root, text="Chicken Roll(₹500)", fg='blue').grid(row=22, column=0, sticky=tk.W)
lb3 = tk.Label(root, text="Burger(₹300)", fg='blue').grid(row=23, column=0, sticky=tk.W)
lb3 = tk.Label(root, text="Momos(₹200)", fg='blue').grid(row=24, column=0, sticky=tk.W)

e4 = tk.Entry(root)
e4.insert(END,'0')
e4.grid(row=20, column=1)

e5 = tk.Entry(root)
e5.insert(END,'0')
e5.grid(row=21, column=1)

e6 = tk.Entry(root)
e6.insert(END,'0')
e6.grid(row=22, column=1)

e7 = tk.Entry(root)
e7.insert(END,'0')
e7.grid(row=23, column=1)

e8 = tk.Entry(root)
e8.insert(END,'0')
e8.grid(row=24, column=1)

lb5 = tk.Label(root, text="2. JUICES ", fg='green').grid(row=25, column=0, pady=5, sticky=tk.W)
lb3 = tk.Label(root, text="Cocktail(₹150)", fg='blue').grid(row=26, column=0, sticky=tk.W)
lb3 = tk.Label(root, text="Sugarcane(₹50)", fg='blue').grid(row=27, column=0, sticky=tk.W)
lb3 = tk.Label(root, text="Grapes(₹70)", fg='blue').grid(row=28, column=0, sticky=tk.W)
lb3 = tk.Label(root, text="Mango(₹100)", fg='blue').grid(row=29, column=0, sticky=tk.W)
lb3 = tk.Label(root, text="Pineapple(₹80)", fg='blue').grid(row=30, column=0, sticky=tk.W)

e9 = tk.Entry(root)
e9.insert(END,'0')
e9.grid(row=26, column=1)

e10 = tk.Entry(root)
e10.insert(END,'0')
e10.grid(row=27, column=1)

e11 = tk.Entry(root)
e11.insert(END,'0')
e11.grid(row=28, column=1)

e12 = tk.Entry(root)
e12.insert(END,'0')
e12.grid(row=29, column=1)

e13 = tk.Entry(root)
e13.insert(END,'0')
e13.grid(row=30, column=1)

button1= Button (root, text= "Calculate Bill" , fg= "red", width=15, command=bill).grid(row=31, column=0, pady=5)
button2= Button (root, text= "Reset" , fg= "red", width=15, command=reset).grid(row=31, column=1, pady=5)

lb4 = tk.Label(root, text="Enter RoomNo. for total Bill:", fg='red').grid(row=32, column=0, sticky=tk.W)
e14 = tk.Entry(root)
e14.grid(row=33, column=0)
button6= Button (root, text= "Bill" , fg= "red", width=15, command=total).grid(row=33, column=1, pady=5)

root.mainloop()
