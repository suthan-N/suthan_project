import tkinter
from tkinter import *
import sqlite3
import tkinter.messagebox as msg


window = Tk()
window.geometry('1200x600')
re_img = PhotoImage(file='c1.png')
bg_label = Label(window,image=re_img)
bg_label.place(x=0,y=0,relwidth=1,relheight=1)
window.title("CUSTOMER LOG  MANAGEMENT SYSTEM")
window.iconbitmap('icon.ico')
TopHeadingFrame = Frame(window,width=700,bd=1)
TopHeadingFrame.pack(side=TOP)
HeadingLabel = Label(TopHeadingFrame,text="CUSTOMER LOG  MANAGEMENT SYSTEM",font=('verdana',26),fg='green')
HeadingLabel.grid(row=0,column=0,padx=20,pady=20)

midFrame = Frame(window,width=500,bd=1)
midFrame.pack(side=TOP)

entry_date=StringVar()
entry_date.set('')
entry_dateLabel = Label(midFrame,text="DATE OF ENTRY:",font=('verdana',12),fg='BLUE')
entry_dateLabel.grid(row=0,column=0,padx=10,pady=10)
entry_dateTextBox=Entry(midFrame,font=('verdana',16),textvariable=entry_date)
entry_dateTextBox.grid(row=0,column=1,padx=10,pady=10)



first_name=StringVar()
first_name.set('')
first_nameLabel = Label(midFrame,text="FIRST NAME:",font=('verdana',12),fg='BLUE')
first_nameLabel.grid(row=2,column=0,padx=10,pady=10)
first_nameTextBox=Entry(midFrame,font=('verdana',16),textvariable=first_name)
first_nameTextBox.grid(row=2,column=1,padx=10,pady=10)

middle_name=StringVar()
middle_name.set('')
middle_nameLabel = Label(midFrame,text="MIDDLE NAME:",font=('verdana',12),fg='BLUE')
middle_nameLabel.grid(row=3,column=0,padx=10,pady=10)
middle_nameTextBox=Entry(midFrame,font=('verdana',16),textvariable=middle_name)
middle_nameTextBox.grid(row=3,column=1,padx=10,pady=10)

last_name=StringVar()
last_name.set('')
last_nameLabel = Label(midFrame,text="LAST NAME :",font=('verdana',12),fg='BLUE')
last_nameLabel.grid(row=4,column=0,padx=10,pady=10)
last_nameTextBox=Entry(midFrame,font=('verdana',16),textvariable=last_name)
last_nameTextBox.grid(row=4,column=1,padx=10,pady=10)

mobile_number=StringVar()
mobile_number.set('')
mobile_numberLabel = Label(midFrame,text="MOBILE NUMBER :",font=('verdana',12),fg='BLUE')
mobile_numberLabel.grid(row=5,column=0,padx=10,pady=10)
mobile_numberTextBox=Entry(midFrame,font=('verdana',16),textvariable=mobile_number)
mobile_numberTextBox.grid(row=5,column=1,padx=10,pady=10)


email_address=StringVar()
email_address.set('')
email_addressLabel = Label(midFrame,text="EMAIL ADDRESS :",font=('verdana',12),fg='BLUE')
email_addressLabel.grid(row=6,column=0,padx=10,pady=10)
email_addressTextBox=Entry(midFrame,font=('verdana',16),textvariable=email_address)
email_addressTextBox.grid(row=6,column=1,padx=10,pady=10)

place=StringVar()
place.set('')
placeLabel = Label(midFrame,text="PLACE :",font=('verdana',12),fg='BLUE')
placeLabel.grid(row=7,column=0,padx=10,pady=10)
placeTextBox=Entry(midFrame,font=('verdana',16),textvariable=place)
placeTextBox.grid(row=7,column=1,padx=10,pady=10)

conn = sqlite3.connect('customer.db')
cursor = conn.cursor()
cursor.execute("""create table if not exists'add_customer'
(entry_date text,first_name text,middle_name text,last_name text,mobile_number int,email_address text,place text)""")
conn.commit()

def add_new_customer():
    conn = sqlite3.connect('customer.db')
    cursor = conn.cursor()
    cursor.execute("""insert into 'add_customer'
    (Entry_date,First_name,Middle_name,Last_name,Mobile_number,Email_address,Place)values(?,?,?,?,?,?,?)""",
    (str(entry_date.get()),str(first_name.get()),str(middle_name.get()),
     str(last_name.get()),str(mobile_number.get()),str(email_address.get()),str(place.get())))
    
    conn.commit()

    if cursor.rowcount>0:
         msg.showinfo( title='Confirmation',message='New Customer Added',icon='info')
       
    else:    
         msg.showinfo( title='Error',message='Costomer not added !',icon='warning')

register = Button(midFrame, text="ADD", fg="Black",bg="green yellow",width=35,command=add_new_customer)
register.grid(row=8, column=1)


def login(): 
    window.destroy()
    import login

loginLabel = Label(midFrame,text="Already Register:",font=('verdana',8),fg='BLUE')
loginLabel.grid(row=9,column=0,padx=10,pady=10)

def view_customer():
     window.destroy()
     import view_customer
     
login = Button(midFrame, text="VIEW", fg="Black",bg="GREEN",width=35,command=view_customer)
login.grid(row=9, column=1)

window.mainloop()


window.mainloop()