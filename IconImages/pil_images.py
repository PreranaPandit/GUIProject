from tkinter import *
from PIL import ImageTk, Image

root = Tk()
# title
root.title('Images Insertion')
# icon images
# png icons does not support sometimes
root.iconbitmap('E:/images/global.ico')


my_image = ImageTk.PhotoImage(Image.open("E:/images/medicine.png"))
my_label = Label( image= my_image)
my_label.pack()

# Button quit option
button_quit = Button(root, text="Exit", command=root.quit,width=20)
button_quit.pack()

root.mainloop()








