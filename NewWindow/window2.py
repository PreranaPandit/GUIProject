from tkinter import *
from PIL import ImageTk, Image
from tkinter import messagebox

root = Tk()
root.title('Message Box')
root.iconbitmap('E:/images/global.ico')

#Creates new window

def open():
    global my_img
    top = Toplevel()
    top.title('Check message box')
    top.iconbitmap('E:/images/global.ico')
    my_img = ImageTk.PhotoImage(Image.open("E:/images/smartphone.png"))
    my_label = Label(top, image=my_img).pack()

btn = Button(root, text="Open", command=open).pack()


mainloop()

