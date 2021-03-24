from tkinter import *
from PIL import ImageTk, Image
from tkinter import messagebox
from tkinter import filedialog

root = Tk()
root.title('Message Box')
root.iconbitmap('E:/images/global.ico')

root.filename = filedialog.askopenfilename(initialdir="/Downloads", title="Select a file", filetypes=(("png files","*.png"),("all files","*.*")))



mainloop()

