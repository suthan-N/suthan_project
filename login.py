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

username=StringVar()
username.set('')
usernameLabel = Label(midFrame,text="USERNAME :",font=('verdana',12),fg='BLUE')
usernameLabel.grid(row=0,column=0,padx=10,pady=10)
usernameTextBox=Entry(midFrame,font=('verdana',16),textvariable=username)
usernameTextBox.grid(row=0,column=1,padx=10,pady=10)

email=StringVar()
email.set('')
emailLabel = Label(midFrame,text="EMAIL ID:",font=('verdana',12),fg='BLUE')
emailLabel.grid(row=1,column=0,padx=10,pady=10)
emailTextBox=Entry(midFrame,font=('verdana',16),textvariable=email)
emailTextBox.grid(row=1,column=1,padx=10,pady=10)

password=StringVar()
password.set('')
passwordLabel = Label(midFrame,text="PASSWORD :",font=('verdana',12),fg='BLUE')
passwordLabel.grid(row=2,column=0,padx=10,pady=10)
passwordTextBox=Entry(midFrame,font=('verdana',16),textvariable=password)
passwordTextBox.grid(row=2,column=1,padx=10,pady=10)


def login():
    conn = sqlite3.connect('customer.db')
    cursor = conn.cursor()
    cursor.execute("""select * from 'admindata' where username = ? and email = ? and password = ?""",(username.get(),email.get(),password.get()))
    if len(list(cursor.fetchall()))>0:
        msg.showinfo( title='Login Confirmation',message='Login successfully',icon='info')
        window.destroy()
        import home
    else:
        msg.showinfo( title='Error!',message='user not defined',icon='warning')
        window.destroy()
        import register


login = Button(midFrame, text="LOGIN", fg="Black",bg="red",width=35,command=login)
login.grid(row=4, column=1)

def register(): 
    window.destroy()
    import register 
registerLabel = Label(midFrame,text="Not a user!",font=('verdana',8),fg='BLUE')
registerLabel.grid(row=3,column=0,padx=10,pady=10)
register = Button(midFrame, text="REGISTER", fg="Black",bg="green yellow",width=35,command=register)
register.grid(row=4, column=0)


window.mainloop()