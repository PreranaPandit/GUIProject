from tkinter import *

root = Tk()

'''
e = Entry(root)
e.pack()

def myClick():
    myLabel = Label(root, text="Button is clicked!!")
    myLabel.pack()

myButton = Button(root, text="Click Me!", command=myClick)
myButton.pack()

root.mainloop()

'''

e = Entry(root, width=50)
e.pack()

'''
e1 = Entry(root, width=50, fg="blue", bg="white", borderwidth=5)
e1.pack()
'''




def myClick():
    textoutput = "Hello " + e.get()

    myLabel = Label(root, text=textoutput)

    myLabel.pack()

myButton = Button(root, text="Click Me!", command=myClick)
myButton.pack()

root.mainloop()
