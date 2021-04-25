from tkinter import *
from PIL import ImageTk, Image
from tkinter import messagebox
from tkinter import filedialog

root = Tk()
root.title('Dropdown Menu')
root.iconbitmap('E:/images/global.ico')

def show():
    myLabel = Label(root, text=clicked.get()).pack()

clicked = StringVar()
clicked.set("Monday")

drop = OptionMenu(root, clicked,"Moday","Tuesday","Wednesday","Thursday","Friday")
drop.pack()

myButton = Button(root, text="Show selection", command=show).pack()




mainloop()

