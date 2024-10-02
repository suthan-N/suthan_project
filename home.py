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
HeadingLabel = Label(TopHeadingFrame,text="CUSTOMER LOG  MANAGEMENT SYSTEM - Login",font=('verdana',26),fg='green')
HeadingLabel.grid(row=0,column=0,padx=20,pady=20)


midFrame = Frame(window,width=500,bd=1)
midFrame.pack(side=TOP)

def add_customer():
    window.destroy()
    import add_new_customer
add_customer = Button(midFrame, text="ADD NEW CUSTOMER", fg="Black",bg="#687a25",width=35,command=add_customer)
add_customer.grid(row=0, column=0,padx=10,pady=10)

def view_customer():
    window.destroy()
    import view_customer
view_customer = Button(midFrame, text="VIEW CUSTOMER", fg="Black",bg="#687a25",width=35,command=view_customer)
view_customer.grid(row=1, column=0,padx=10,pady=10)

def search_customer():
    window.destroy()
    import search_customer
search_customer = Button(midFrame, text="SEARCH CUSTOMER", fg="Black",bg="#687a25",width=35,command=search_customer)
search_customer.grid(row=2, column=0,padx=10,pady=10)

def delete_customer():
    window.destroy()
    import delete_customer
delete_customer = Button(midFrame, text="DELETE CUSTOMER", fg="Black",bg="#687a25",width=35,command=delete_customer)
delete_customer.grid(row=3, column=0,padx=10,pady=10)

def logout():
    window.destroy()
    import login
login = Button(midFrame, text="LOGOUT", fg="Black",bg="red",width=35,command=logout)
login.grid(row=4, column=0,padx=10,pady=10)

window.mainloop()
