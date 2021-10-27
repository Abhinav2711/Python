from Tkinter import *
import time
from random import randint
root = Tk()
root.geometry("1150x700+0+0")
root.title("Restaurant Billing System")
Tops = Frame(root, width=1350, height=50, bd=8,bg='blue', relief="raise")
Tops.pack(side=TOP)
Bottoms = Frame(root, width=1350, height=50, bd=8, relief="raise")
Bottoms.pack(side=BOTTOM)
f1 = Frame(root, width=900, height=650, bd=8, relief="raise")
f1.pack(side=LEFT)
f1a = Frame(f1, width=900, height=330, bd=8, relief="raise")
f1a.pack(side=TOP)
f2a = Frame(f1, width=900, height=320, bd=8, relief="raise")
f2a.pack(side=BOTTOM)
f1aa = Frame(f1a, width=400, height=430, bd=8, relief="raise")
f1aa.pack(side=LEFT)
f1ab = Frame(f1a, width=400, height=430, bd=8, relief="raise")
f1ab.pack(side=RIGHT)
f2aa = Frame(f2a, width=450, height=330, bd=8, relief="raise")
f2aa.pack(side=LEFT)
f2ab = Frame(f2a, width=450, height=330, bd=8, relief="raise")
f2ab.pack(side=LEFT)
#f2 = Frame(root, width=440, height=650, bd=8, relief="raise")
#f2.pack(side=BOTTOM)
lblInfo = Label(Tops, font=('arial', 25, 'bold'), text="Restaurant Billing System", bd=10, anchor='w')
lblInfo.grid(row=0, column=0)
# ==============================Variables=====================
PaymentRef = StringVar()
idly = StringVar()
biryani = StringVar()
paneer_butter_masala = StringVar()
nimbu_pani = StringVar()
costidly = StringVar()
costbiryani = StringVar()
costpaneer_butter_masala = StringVar()
costnimbu_pani = StringVar()
dateRef = StringVar()
subTotal = StringVar()
vat = StringVar()
totalPrice = StringVar()
text_Input = StringVar()
dateRef.set(time.strftime("%d/%m/%y"))
operator = ""
vat.set(0)
idly.set(0)
biryani.set(0)
paneer_butter_masala.set(0)
nimbu_pani.set(0)
subTotal.set(0)
totalPrice.set(0)
costidly.set(30)
costbiryani.set(180)
costnimbu_pani.set(20)
costpaneer_butter_masala.set(180)
# =============================Functions==================
def tPrice():
    cBprice = int(costidly.get())
    bBprice = int(costbiryani.get())
    fFprice = int(costpaneer_butter_masala.get())
    sDprice = int(costnimbu_pani.get())
    cBno = int(idly.get())
    bBno = int(biryani.get())
    fFno = int(paneer_butter_masala.get())
    sDno = int(nimbu_pani.get())
    tempVat = int(vat.get())
    subPrice = (cBprice * cBno + bBprice * bBno + fFprice * fFno + sDprice * sDno)
    totalCost = str('%d' % subPrice)
    totalCostwithVat = str('%d' % (subPrice + (subPrice * tempVat) / 100))
    subTotal.set(totalCost)
    totalPrice.set(totalCostwithVat)
def iExit():
    qexit = messagebox.askyesno("Billing System", "Do you want to exit?")
    if qexit > 0:
        root.destroy()
        return
def reset():
    global x
    x = x + 1
    PaymentRef.set("")
    idly.set(0)
    biryani.set(0)
    paneer_butter_masala.set(0)
    nimbu_pani.set(0)
    subTotal.set(0)
    totalPrice.set(0)
def refNo():
    global x
    y = str(x)
    randomRef = str(y)
    PaymentRef.set("BILL" + randomRef)
def btnClearDisplay():
    global operator
    operator = ""
    text_Input.set("")
def btnEqualsInput():
    global operator
    sumup = str(eval(operator))
    text_Input.set(sumup)
    operator = ""
# ==================================Order Info===========================
lblRef = Label(f1aa, font=('arial', 16, 'bold'), fg="red", text="Reference No", bd=16, justify='left')
lblRef.grid(row=0, column=0)
txtRef = Entry(f1aa, font=('arial', 16, 'bold'), textvariable=PaymentRef, bd=10, insertwidth=2, justify='left')
txtRef.grid(row=0, column=1)
# --------------
lblCb = Label(f1aa, font=('arial', 16, 'bold'), text="Idly", bd=16, justify='left')
lblCb.grid(row=1, column=0)
txtCb = Entry(f1aa, font=('arial', 16, 'bold'), textvariable=idly, bd=10, insertwidth=2, justify='left')
txtCb.grid(row=1, column=1)
# --------------
lblBb = Label(f1aa, font=('arial', 16, 'bold'), text="Biryani", bd=16, justify='left')
lblBb.grid(row=2, column=0)
txtBb = Entry(f1aa, font=('arial', 16, 'bold'), textvariable=biryani, bd=10, insertwidth=2, justify='left')
txtBb.grid(row=2, column=1)
# --------------
lblFf = Label(f1aa, font=('arial', 16, 'bold'), text="Paneer butter masala", bd=16, justify='left')
lblFf.grid(row=3, column=0)
txtFf = Entry(f1aa, font=('arial', 16, 'bold'), textvariable=paneer_butter_masala, bd=10, insertwidth=2, justify='left')
txtFf.grid(row=3, column=1)
# --------------
lblSd = Label(f1aa, font=('arial', 16, 'bold'), text="Nimbu pani", bd=16, justify='left')
lblSd.grid(row=4, column=0)
txtSd = Entry(f1aa, font=('arial', 16, 'bold'), textvariable=nimbu_pani, bd=10, insertwidth=2, justify='left')
txtSd.grid(row=4, column=1)
# ===================================Payment Info==========================
lbldate = Label(f1ab, font=('arial', 16, 'bold'), text="Date", bd=16, justify='left')
lbldate.grid(row=0, column=0)
txtdate = Entry(f1ab, font=('arial', 16, 'bold'), textvariable=dateRef, bd=10, insertwidth=2, justify='left')
txtdate.grid(row=0, column=1)
# --------------
lblCcb = Label(f1ab, font=('arial', 16, 'bold'), text="Price of Idly", bd=16, justify='left')
lblCcb.grid(row=1, column=0)
txtCcb = Entry(f1ab, font=('arial', 16, 'bold'), textvariable=costidly, bd=10, insertwidth=2, justify='left')
txtCcb.grid(row=1, column=1)
# --------------
lblCbb = Label(f1ab, font=('arial', 16, 'bold'), text="Price of Biryani", bd=16, justify='left')
lblCbb.grid(row=2, column=0)
txtCbb = Entry(f1ab, font=('arial', 16, 'bold'), textvariable=costbiryani, bd=10, insertwidth=2, justify='left')
txtCbb.grid(row=2, column=1)
# --------------
lblCff = Label(f1ab, font=('arial', 16, 'bold'), text="Price of Paneer butter masala", bd=16, justify='left')
lblCff.grid(row=3, column=0)
txtCff = Entry(f1ab, font=('arial', 16, 'bold'), textvariable=costpaneer_butter_masala, bd=10, insertwidth=2,
               justify='left')
txtCff.grid(row=3, column=1)
# --------------
lblCsd = Label(f1ab, font=('arial', 16, 'bold'), text="Price of Nimbu pani", bd=16, justify='left')
lblCsd.grid(row=4, column=0)
txtCsd = Entry(f1ab, font=('arial', 16, 'bold'), textvariable=costnimbu_pani, bd=10, insertwidth=2, justify='left')
txtCsd.grid(row=4, column=1)
# ==========================Total Payment Info======
lblPrice = Label(f2aa, font=('arial', 16, 'bold'), text="Price", bd=16, justify='left')
lblPrice.grid(row=0, column=0)
txtPrice = Entry(f2aa, font=('arial', 16, 'bold'), textvariable=subTotal, bd=10, insertwidth=2, justify='left')
txtPrice.grid(row=0, column=1)
# --------------
lblVat = Label(f2aa, font=('arial', 16, 'bold'), text="VAT", bd=16, justify='left')
lblVat.grid(row=1, column=0)
txtVat = Entry(f2aa, font=('arial', 16, 'bold'), textvariable=vat, bd=10, insertwidth=2, justify='left')
txtVat.grid(row=1, column=1)
# --------------
lblTp = Label(f2aa, font=('arial', 16, 'bold'), text="Total Price", bd=16, justify='left')
lblTp.grid(row=2, column=0)
txtTp = Entry(f2aa, font=('arial', 16, 'bold'), textvariable=totalPrice, bd=10, insertwidth=2, justify='left')
txtTp.grid(row=2, column=1)
#updatelabel=Label(Bottoms,font=('arial',16,'bold'),text="Total Price")
#updatelabel.pack(fill='both' )
# ==============Buttons==========
btnTotal = Button(f2ab, padx=16, pady=16, bd=8, fg="black", font=('arial', 16, 'bold'), width=15,
                  text="Total Price", command=tPrice).grid(row=0, column=1)
btnRefer = Button(f2ab, padx=16, pady=16, bd=8, fg="black", font=('arial', 16, 'bold'), width=15,
                  text="Sales Reference", command=refNo).grid(row=0, column=0)
btnCrtb = Button(f2ab, padx=16, pady=16, bd=8, fg="black", font=('arial', 16, 'bold'), width=10,
                 text="Generate bill", command=create_bill).grid(row=0, column=2)
btnReset = Button(f2ab, padx=16, pady=16, bd=8, fg="black", font=('arial', 16, 'bold'), width=15,
                  text="Reset", command=reset).grid(row=1, column=0)
btnExit = Button(f2ab, padx=16, pady=16, bd=8, fg="black", font=('arial', 16, 'bold'), width=15,
                 text="Exit", command=iExit).grid(row=1, column=1)
btnSndb = Button(f2ab, padx=16, pady=16, bd=8, fg="black", font=('arial', 16, 'bold'), width=10,
                 text="Send bill", command=send_bill).grid(row=1, column=2)
root.mainloop()
