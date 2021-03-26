from tkinter import *
from PIL import ImageTk, Image
from tkinter import messagebox
from tkinter import filedialog

root = Tk()
root.title('Message Box')
root.iconbitmap('E:/images/global.ico')

clicked = StringVar()

drop = OptionMenu(root, clicked,"Moday","Tuesday","Wednesday","Thursday","Friday")
drop.pack()




mainloop()

