from tkinter import *

window = Tk()

window.title(" billing system")

window.geometry('400x150')

lbl = Label(window, text="Customer name")

lbl.grid(column=1,row=0)

lbl1 = Label(window, text="Mobile number")

lbl1.grid(column=1,row=10)

lbl2 = Label(window, text="Bill number")

lbl2.grid(column=1,row=20)

lbl3 = Label(window, text="Item name")

lbl3.grid(column=1,row=30)

lbl4 = Label(window, text="Rate")

lbl4.grid(column=1,row=40)

lbl5 = Label(window, text="Total")

lbl5.grid(column=1,row=50)

txt = Entry(window,width=25)

txt.grid(column=2, row=0)

txt1 = Entry(window,width=25)

txt1.grid(column=2, row=10)

txt2 = Entry(window,width=25)

txt2.grid(column=2, row=20)

txt3 = Entry(window,width=25)

txt3.grid(column=2, row=30)

txt4 = Entry(window,width=25)

txt4.grid(column=2, row=40)

txt5 = Entry(window,width=25)

txt5.grid(column=2, row=50)

def clicked():

    lbl.configure(text="Button was clicked !!")
    lbl.configure(text=txt.get())
    lbl1.configure(text="Button was clicked !!")
    lbl1.configure(text=txt2.get())
    lbl2.configure(text="Button was clicked !!")
    lbl2.configure(text=txt2.get())
    lbl3.configure(text="Button was clicked !!")
    lbl3.configure(text=txt3.get())
    lbl4.configure(text="Button was added !!")
    lbl4.configure(text=txt4.get())
    lbl5.configure(text="Button was calculated !!")
    lbl5.configure(text=txt5.get())
btn = Button(window, text="Click Me", command=clicked)

btn.grid(column=4, row=0)

btn1 = Button(window, text="Click Me", command=clicked)

btn1.grid(column=4, row=10)

btn2 = Button(window, text="Click Me", command=clicked)

btn2.grid(column=4, row=20)

btn3 = Button(window, text="Click Me", command=clicked)

btn3.grid(column=4, row=30)

btn4 = Button(window, text="ADD", command=clicked)

btn4.grid(column=4, row=40)

calculatebtn = Button(window, text="Calculate", command=clicked)

calculatebtn.grid(column=4, row=50)

window.mainloop()
