from tkinter import *

OPTIONS = [
    "California",
    "458",
    "FF",
    "ENZO",
    "LaFerrari"
    ]

root = Tk()

variable = StringVar()
variable.set(OPTIONS[0])

w = OptionMenu(root, variable, *OPTIONS)       #选址
w.pack()

mainloop()
