import tkinter as tk
window = tk.Tk()
greeting = tk.Label(text = "i am abhinav")
greeting.pack()

label = tk.Label(
    text = "hello tkinter",
    foreground = "white",
    background = "black",
    width = 10,
    height = 2
)
label.pack()

frame1 = tk.Frame(master=window, width=100, height=100, bg="red")
frame1.pack(fill=tk.BOTH, side=tk.LEFT, expand=True)
frame2 = tk.Frame(master=window, width=100, height=100, bg="black")
frame2.pack(fill=tk.BOTH, side=tk.RIGHT, expand=True)
frame3 = tk.Frame(master=window, width=100, height=100, bg="grey")
frame3.pack(fill=tk.BOTH, side=tk.BOTTOM, expand=True)
frame4 = tk.Frame(master=window, width=100, height=100, bg="yellow")
frame4.pack(fill=tk.BOTH, side=tk.TOP, expand=True)


button = tk.Button(
 text="Click me!",
 width=25,
 height=5,
 bg="red",
 fg="blue",
)

button.pack()

entry = tk.Entry(fg="green", bg="yellow", width=50)

entry.pack()

text_box = tk.Text()
text_box.pack()

window.mainloop()
