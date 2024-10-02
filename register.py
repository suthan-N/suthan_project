import tkinter
from tkinter import *
from tkinter import ttk
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
HeadingLabel = Label(TopHeadingFrame,text="CUSTOMER LOG  MANAGEMENT SYSTEM - register",font=('verdana',26),fg='green')
HeadingLabel.grid(row=0,column=0,padx=20,pady=20)

midFrame = Frame(window,width=500,bd=1)
midFrame.pack(side=TOP)

            
name=StringVar()
name.set('')
NameLabel = Label(midFrame,text="NAME:",font=('verdana',12),fg='BLUE')
NameLabel.grid(row=0,column=0,padx=10,pady=10)
NameTextBox=Entry(midFrame,font=('verdana',16),textvariable=name)
NameTextBox.grid(row=0,column=1,padx=10,pady=10)

combo_box = Label(midFrame,text="GENDER :",font=('verdana',12),fg='BLUE')
combo_box.grid(row=1,column=0,padx=10,pady=10)
gender=['Male','Female','Other']
combo_box=ttk.Combobox(midFrame,values=gender)
combo_box.grid(row=1,column=1)

id=StringVar()
id.set('')
idLabel = Label(midFrame,text="ID:",font=('verdana',12),fg='BLUE')
idLabel.grid(row=2,column=0,padx=10,pady=10)
idTextBox=Entry(midFrame,font=('verdana',16),textvariable=id)
idTextBox.grid(row=2,column=1,padx=10,pady=10)

username=StringVar()
username.set('')
usernameLabel = Label(midFrame,text="USERNAME:",font=('verdana',12),fg='BLUE')
usernameLabel.grid(row=3,column=0,padx=10,pady=10)
usernameTextBox=Entry(midFrame,font=('verdana',16),textvariable=username)
usernameTextBox.grid(row=3,column=1,padx=10,pady=10)

password=StringVar()
password.set('')
passwordLabel = Label(midFrame,text="PASSWORD:",font=('verdana',12),fg='BLUE')
passwordLabel.grid(row=4,column=0,padx=10,pady=10)
passwordTextBox=Entry(midFrame,font=('verdana',16),textvariable=password)
passwordTextBox.grid(row=4,column=1,padx=10,pady=10)

mobile=StringVar()
mobile.set('')
mobileLabel = Label(midFrame,text="MOBILE NUMBER:",font=('verdana',12),fg='BLUE')
mobileLabel.grid(row=5,column=0,padx=10,pady=10)
mobileTextBox=Entry(midFrame,font=('verdana',16),textvariable=mobile)
mobileTextBox.grid(row=5,column=1,padx=10,pady=10)


email=StringVar()
email.set('')
emailLabel = Label(midFrame,text="EMAIL ID:",font=('verdana',12),fg='BLUE')
emailLabel.grid(row=6,column=0,padx=10,pady=10)
emailTextBox=Entry(midFrame,font=('verdana',16),textvariable=email)
emailTextBox.grid(row=6,column=1,padx=10,pady=10)

conn = sqlite3.connect('customer.db')
cursor = conn.cursor()
cursor.execute("""create table if not exists'admindata'
(name text,id int,userName text,password text,mobile text,email text,gender combo_box)""")
conn.commit()

def register():
    conn = sqlite3.connect('customer.db')
    cursor = conn.cursor()
    cursor.execute("""insert into 'admindata'
    (name,gender,id,userName,password,mobile,email)values(?,?,?,?,?,?,?)""",
    (str(name.get()),combo_box.get(),str(id.get()),str(username.get()),str(password.get()),str(mobile.get()),str(email.get())))
    conn.commit()

    if cursor.rowcount>0:
          msg.showinfo( title='Confirmation',message='New user registered',icon='info')
          window.destroy()
          import login
    else:
         msg.showinfo( title='Error',message='user not added !',icon='warning')  

register = Button(midFrame, text="REGISTER", fg="Black",bg="green yellow",width=35,command=register)
register.grid(row=8, column=1)


def login(): 
    window.destroy()
    import login

loginLabel = Label(midFrame,text="Already Register:",font=('verdana',8),fg='BLUE')
loginLabel.grid(row=9,column=0,padx=10,pady=10)
login = Button(midFrame, text="LOGIN", fg="Black",bg="red",width=35,command=login)
login.grid(row=9, column=1)


window.mainloop()