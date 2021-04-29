from tkinter import *
from PIL import ImageTk, Image
import numpy as np
import matplotlib.pyplot as plt

root = Tk()
root.title('GRAPH')
root.iconbitmap('E:/images/global.ico')
root.geometry('400x200')

def graph():
    house_prices = np.random.normal(200000, 25000, 5000)
    plt.hist(house_prices)
    plt.show()

my_button = Button(root, text="Graph it", command=graph).pack()




mainloop()

