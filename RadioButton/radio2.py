from tkinter import *
from PIL import ImageTk, Image


root = Tk()

# title
root.title('Images Insertion')
# icon images
# png icons does not support somoetimes
root.iconbitmap('E:/images/global.ico')

#creating modes for radio button
MODES = [
    ("Pepperoni","Pepperoni"),
    ("Cheese","Cheese"),
    ("Mushroom","Mushroom"),
    ("Onion","Onion")
]

pizza = StringVar()
pizza.set("Pepperoni")

for text, mode in MODES:
    Radiobutton(root, text=text, variable=pizza, value=mode).pack()

# function clicked
def clicked(value):
    myLabel = Label(root, text=value)
    myLabel.pack()


myLabel = Label(root, text=pizza.get())
myLabel.pack()

myButton = Button(root,text="Click",command=lambda :clicked(pizza.get())).pack()


mainloop()