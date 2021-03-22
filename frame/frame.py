from tkinter import *
from PIL import ImageTk, Image


root = Tk()

# title
root.title('Images Insertion')
# icon images
# png icons does not support somoetimes
root.iconbitmap('E:/images/global.ico')

'''
#Adding frame in the program
frame = LabelFrame(root, text="My Frame", padx=5, pady=5)
frame.pack(padx=10,pady=10)
'''

# padx and pady outside inside of the frame
#frame = LabelFrame(root, text="My Frame", padx=50, pady=50)
#frame.pack(padx=10,pady=10)

#2. can remove the text from frame
frame = LabelFrame(root, padx=50, pady=50)
frame.pack(padx=10,pady=10)

#Adding button inside the frame
'''
button = Button(frame, text="Don't Click")
button.pack()
'''
button1 = Button(frame, text="Click this")
button1.grid(row=0, column=0)
button2 = Button(frame, text="Do not Click")
button2.grid(row=1, column=1)



root.mainloop()