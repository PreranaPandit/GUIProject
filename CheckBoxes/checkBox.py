from tkinter import *
from PIL import ImageTk, Image
from tkinter import messagebox
from tkinter import filedialog

root = Tk()
root.title('Message Box')
root.iconbitmap('E:/images/global.ico')


var = IntVar()

checkButton = Checkbutton(root, text="Check this box!", variable = var)
checkButton.pack()

#myButton = Button(root, text="Show Selection")

mainloop()

