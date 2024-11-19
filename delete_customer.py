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
mobile_numberLabel = Label(midFrame,text="MOBILE NUMBER :",font=('verdana',12),fg='BLUE')
mobile_numberLabel.grid(row=0,column=0,padx=10,pady=10)
mobile_numberTextBox=Entry(midFrame,font=('verdana',16),textvariable=mobile_number)
mobile_numberTextBox.grid(row=0,column=1,padx=10,pady=10)


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

def view_customer():   
    for i in tv.get_children():
        tv.delete(i)  
    conn = sqlite3.connect('customer.db')
    cursor = conn.cursor()
    cursor.execute("select * from 'add_customer'")
    conn.commit()
    data=cursor.fetchall()
    for i in data:
        tv.insert("",'end',values=i)

view_customer = Button(midFrame, text="VIEW", fg="Black",bg="GREEN",width=20,command=view_customer)
view_customer.grid(row=1, column=0)

def delete_customer():   
    for i in tv.get_children():
        tv.delete(i)  
    conn = sqlite3.connect('customer.db')   
    cursor = conn.cursor()
    cursor.execute("delete from 'add_customer' where mobile_number=?",(mobile_number.get(),))
    
    if cursor.rowcount>0:
         msg.showinfo( title='Confirmation',message='Deleted successfully',icon='info')
    else:    
         msg.showinfo( title='Error',message='Not Deleted',icon='warning')
    cursor.close()
    conn.commit()
delete_customer = Button(midFrame, text="DELETE", fg="Black",bg="#bd6868",width=20,command=delete_customer)
delete_customer.grid(row=1, column=1)

def home():
     window.destroy()
     import home
     
view_customer = Button(midFrame, text="HOME", fg="Black",bg="blue",width=20,command=home)
view_customer.grid(row=1, column=2)

window.mainloop()