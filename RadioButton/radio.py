from tkinter import *
from PIL import ImageTk, Image


root = Tk()

# title
root.title('Images Insertion')
# icon images
# png icons does not support somoetimes
root.iconbitmap('E:/images/global.ico')

r = IntVar()


Radiobutton(root, text="Option 1", variable=r ,value=1).pack()
Radiobutton(root, text="Option 2", variable=r ,value=2).pack()



root.mainloop()