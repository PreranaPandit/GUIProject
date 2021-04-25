from tkinter import *
from PIL import ImageTk, Image
from tkinter import messagebox

root = Tk()
root.title('New Window')
root.iconbitmap('E:/images/global.ico')

#Creates new window
def open():
    global my_img
    top = Toplevel()
    top.title('Check new window')
    top.iconbitmap('E:/images/global.ico')
    my_img = ImageTk.PhotoImage(Image.open("E:/images/smartphone.png"))
    my_label = Label(top, image=my_img).pack()
    # closing the window using button.destroy

    btn2 = Button(top, text="Close Window", command = top.destroy).pack()

btn = Button(root, text="Open", command=open).pack()


mainloop()

