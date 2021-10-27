import tkinter as tk
window = tk.Tk()
greeting = tk.Label(text = "")
greeting.pack()

frame1 = tk.Frame(master=window, width=100, height=100, bg="red")
frame1.pack(fill=tk.BOTH, side=tk.LEFT, expand=True)
frame2 = tk.Frame(master=window, width=100, height=100, bg="yellow")
frame2.pack(fill=tk.BOTH, side=tk.RIGHT, expand=True)
frame3 = tk.Frame(master=window, width=100, height=100, bg="blue")
frame3.pack(fill=tk.BOTH, side=tk.BOTTOM, expand=True)
frame4 = tk.Frame(master=window, width=100, height=100, bg="green")
frame4.pack(fill=tk.BOTH, side=tk.TOP, expand=True)

label = tk.Label(
text = "BILLING",
foreground = "red",
background = "white",
width = 15,
height = 5
)
label.pack()


entry = tk.Entry(fg="yellow", bg="blue", width=50)

entry.pack()

text_box = tk.Text()


text1 = tk.Text(window, height = 10, width = 50)
text1.config(state ="normal")
text1.insert(tk.INSERT, "\n \n customer name")
text1.insert(tk.INSERT, "\n \n item name")
text1.insert(tk.INSERT, "\n \n rate")
text1.insert(tk.INSERT, "\n \n bill amount")
text1.config(state = "disabled")
text1.pack()

button = tk.Button(
text="CALCULATE",
width=25,
height=5,
bg="blue",
fg="yellow",
)

button.pack()

window.mainloop()
