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

mobile_number=StringVar()
mobile_number.set('')
mobile_numberLabel = Label(midFrame,text="MOBILE_NUMBER:",font=('verdana',12),fg='BLUE')
mobile_numberLabel.grid(row=0,column=0,padx=10,pady=10)
mobile_numberTextBox=Entry(midFrame,font=('verdana',16),textvariable=mobile_number)
mobile_numberTextBox.grid(row=0,column=1,padx=10,pady=10)

anyLabel = Label(midFrame,text="(OR)",font=('verdana',12),fg='BLUE')
anyLabel.grid(row=1,column=1,padx=10,pady=10)

email_address=StringVar()
email_address.set('')
email_addressLabel = Label(midFrame,text="EMAIL ADDRESS :",font=('verdana',12),fg='BLUE')
email_addressLabel.grid(row=2,column=0,padx=10,pady=10)
email_addressTextBox=Entry(midFrame,font=('verdana',16),textvariable=email_address)
email_addressTextBox.grid(row=2,column=1,padx=10,pady=10)

def home():
     window.destroy()
     import home
     
view_customer = Button(midFrame, text="BACK", fg="Black",bg="blue",width=35,command=home)
view_customer.grid(row=3, column=0)


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

def search():
    for i in tv.get_children():
        tv.delete(i)  
    conn = sqlite3.connect('customer.db')
    cursor = conn.cursor()
    mobnumber=str(mobile_number.get())
    email=str(email_address.get())
    cursor.execute("select * from 'add_customer' where mobile_number=? or email_address=? ",(mobnumber,email,))
    data=cursor.fetchall()
    for i in data:
        tv.insert("",'end',values=i)
        

    
search_customer = Button(midFrame, text="SEARCH", fg="Black",bg="GREEN",width=35,command=search)
search_customer.grid(row=3, column=1)



window.mainloop()