from tkinter import *
from PIL import ImageTk, Image


root = Tk()

# title
root.title('Radio Button')
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
    Radiobutton(root, text=text, variable=pizza, value=mode).pack(anchor=W)

# function clicked
def clicked(value):
    myLabel = Label(root, text=value)
    myLabel.pack()

myButton = Button(root,text="Click",command=lambda :clicked(pizza.get())).pack()

mainloop()