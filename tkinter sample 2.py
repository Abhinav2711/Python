from Tkinter import *

class Window(Tk):
    def __init__(self, parent):
        Tk.__init__(self, parent)
        self.parent = parent
        self.initialize()

    def initialize(self):
        self.geometry("600x400+30+30")
        wButton = Button(self, text='text', command = self.OnButtonClick())
        wButton.pack()

    def OnButtonClick(self):
        top = Toplevel()
        top.title("title")
        top.geometry("300x150+30+30")
        topButton = Button(top, text="CLOSE", command = self.destroy)
        topButton.pack()


if __name__ == "__main__":
    window = Window(None)

    window.title("title")

    window.mainloop()
