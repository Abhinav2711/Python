from tkinter import *

from tkinter import Menu

def newfile():
    print("newfile")
    n = input("Enter a number: ")
    factorial = 1
    if int(n) >= 1:
        for i in range (1,int(n)+1):
            factorial = factorial * i
        print("Factorail of ",n , " is : ",factorial)
    print("newfile")

def editfile():
    print("editfile")
    Number = int(input("\nPlease Enter the Range number: "))
    i = 0
    First_Value = 0
    Second_Value = 1
           
    while(i < Number):
        if(i <= 1):
            Next = i
        else:
            Next = First_Value + Second_Value
            First_Value = Second_Value
            Second_Value = Next
        print(Next)
        i = i + 1

def exitfile():
    print("exitfile")
    window.destroy()
    
window = Tk()

window.title("Welcome to LikeGeeks app")

menu = Menu(window)

new_item = Menu(menu)

new_item.add_command(label='New',command=newfile)

new_item.add_separator()

new_item.add_command(label='Edit',command=editfile)

new_item.add_separator()

new_item.add_command(label='Exit',command=exitfile)

menu.add_cascade(label='File', menu=new_item)

window.config(menu=menu)

window.mainloop()

