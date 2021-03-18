from tkinter import *

root = Tk()

def myClick():
    myLabel = Label(root, text="Button is clicked!!")
    myLabel.pack()

myButton = Button(root, text="Click Me!", command=myClick, fg="white", bg="blue")
myButton.pack()

root.mainloop()