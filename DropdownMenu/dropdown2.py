from tkinter import *
from PIL import ImageTk, Image
from tkinter import messagebox
from tkinter import filedialog

root = Tk()
root.title('Dropdown Menu')
root.iconbitmap('E:/images/global.ico')


def show():
    myLabel = Label(root, text=clicked.get()).pack()

# making options into list
options= [
    "Monday",
    "Tuesday",
    "Wednesday",
    "Thursday",
    "Friday",
    "Saturday",
    "Sunday"
]

clicked = StringVar()
clicked.set("Monday")

drop = OptionMenu(root, clicked,*options)
drop.pack()

myButton = Button(root, text="Show selection", command=show).pack()




mainloop()

