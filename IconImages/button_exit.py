from tkinter import *
#from tkinter import Image

root = Tk()

# title
root.title('Images Insertion')

# icon images
# png icons does not support somoetimes
root.iconbitmap('E:/images/global.ico')

'''
filen = r'E:/images/medicine.png'
img = Image.open(filen)
img.save('icon.ico',format = 'ICO', sizes=[(32,32)])
'''


# Button quit option

button_quit = Button(root, text="Exit", command=root.quit)
button_quit.pack()


root.mainloop()