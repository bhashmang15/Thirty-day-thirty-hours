#importing library

from tkinter import *
import tkinter as tk
from tkinter import ttk

window = Tk()
window.title("Registration Screen")
window.geometry('400x300')
window.configure(background = "orange");


lbl=Label(window, text="Please fill below mentioned details")
lbl.grid(row=0,column=1)
Firstname = Label(window ,text = "First Name").grid(row = 1,column = 0)
LastName = Label(window ,text = "Last Name").grid(row = 2,column = 0)
Email = Label(window ,text = "Email Id").grid(row = 3,column = 0)
Mobile = Label(window ,text = "Contact Number").grid(row = 4,column = 0)
DOB = Label(window, text = "Date of Birth").grid(row=5, column =0)
Country= Label(window,text="Country").grid(row=6,column=0)
Employment= Label(window,text="Employment type").grid(row=7,column=0)
MaritalStat= Label(window, text="Marital Status").grid(row=8,column=0)
SSN=Label(window,text='Social Security Number').grid(row=9,column=0)
Religion=Label(window,text="Religion").grid(row=10,column=0)


Firstname1 = Entry(window).grid(row = 1,column = 1)
Lastname1 = Entry(window).grid(row = 2,column = 1)
Email1 = Entry(window).grid(row = 3,column = 1)
Mobile1 = Entry(window).grid(row = 4,column = 1)
Country=Entry(window).grid(row=5,column=1)
DOB1= Entry(window).grid(row=6,column=1)
#Dropdown menu for Employment
n = tk.StringVar()
emptype = ttk.Combobox(window,  textvariable = n)
emptype['values']=('Service', 'Business', 'Unemployed')
emptype.grid(row=7,column=1)
emptype.current()
#Radio Button for Marital status
rad1=Radiobutton(window,text='Single', value=1).grid(row=8,column=1)
rad2=Radiobutton(window,text='Married', value=2).grid(row=8,column=2)
SSN1=Entry(window).grid(row=9,column=1)
Religion1=Entry(window).grid(row=10,column=1)

#function declaration
def clicked():
    lbl.configure(text="Your details have been submitted!!")
btn = Button(window ,text="Submit", command=clicked)
btn.grid(row=11,column=1)
window.mainloop()
