from tkinter import *
from PIL import ImageTk, Image
from tkinter import messagebox

root = Tk()
root.title('Message Box')
root.iconbitmap('E:/images/global.ico')

# showinfo, showwarning, showerror, askquestion, askokcancel, askyesno
#try all


def popup():
    #showinfo messagebox
    response = messagebox.askyesno("This is my Popup", "Hello World!")
    Label(root, text=response).pack()

    if response == 1:
        Label(root, text="Clicked Yes").pack()
    else:
        Label(root, text="Clicked No").pack()



Button(root, text="Popup",command=popup).pack()

mainloop()

