from tkinter import *
from PIL import ImageTk, Image


root = Tk()

# title
root.title('Images Insertion')
# icon images
# png icons does not support somoetimes
root.iconbitmap('E:/images/global.ico')

r = IntVar()
r.set("2")

# function clicked
def clicked(value):
    myLabel = Label(root, text=value)
    myLabel.pack()

Radiobutton(root, text="Option 1", variable=r ,value=1, command = lambda:clicked(r.get())).pack()
Radiobutton(root, text="Option 2", variable=r ,value=2, command = lambda:clicked(r.get())).pack()

myLabel = Label(root, text=r.get())
myLabel.pack()


root.mainloop()