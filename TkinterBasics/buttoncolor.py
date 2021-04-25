from tkinter import *

root = Tk()

def myClick():
    myLabel = Label(root, text="Button is clicked!!")
    myLabel.pack()

myButton = Button(root, text="CLICK", command=myClick, fg="white", bg="gray")
myButton.pack()

root.mainloop()

