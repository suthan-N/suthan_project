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
HeadingLabel = Label(TopHeadingFrame,text="CUSTOMER LOG  MANAGEMENT SYSTEM",font=('verdana',26),fg='green')
HeadingLabel.grid(row=0,column=0,padx=20,pady=20)



midFrame = Frame(window,width=500,bd=1)
midFrame.pack(side=TOP)

def home():
     window.destroy()
     import home
     
view_customer = Button(midFrame, text="BACK", fg="Black",bg="#f59342",width=35,command=home)
view_customer.grid(row=9, column=1)

viewFrame = Frame(window,bd=1)
viewFrame.pack(side=TOP,fill=X)

tv=ttk.Treeview(viewFrame,column=('Entry_date','First_name','Middle_name',
                                  'Last_name','Mobile_number','Email_address','Place'))

tv.heading('#1',text='Entry_date')
tv.heading('#2',text='First_name')
tv.heading('#3',text='Middle_name')
tv.heading('#4',text='Last_name')
tv.heading('#5',text='Mobile_number')
tv.heading('#6',text='Email_address')
tv.heading('#7',text='Place')

tv.column('#0',width=0,stretch=0)
tv.column('#1',width=50)
tv.column('#2',width=50)
tv.column('#3',width=50)
tv.column('#4',width=50)
tv.column('#5',width=50)
tv.column('#6',width=50)
tv.column('#7',width=50)
tv.pack(fill=X)


conn = sqlite3.connect('customer.db')
cursor = conn.cursor()
cursor.execute("select * from 'add_customer'")
data=cursor.fetchall()
for i in data:
        tv.insert("",'end',values=i)


window.mainloop()
window.mainloop()