from tkinter import *
from PIL import ImageTk, Image
from tkinter import messagebox

root = Tk()
root.title('Message Box')
root.iconbitmap('E:/images/global.ico')

def popup():
    #showinfo messagebox
    messagebox.showinfo("This is my Popup", "Hello World!")

Button(root, text="Popup",command=popup).pack()

mainloop()

