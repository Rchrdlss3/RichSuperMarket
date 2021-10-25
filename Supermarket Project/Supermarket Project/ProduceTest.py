from tkinter import *
from tkinter import Tk

mycolor = '#4acd63'
root = Tk()

root.configure(bg=mycolor)
root.title('Rich Supermarket')
root.geometry("1100x700")


arugulapic = PhotoImage(file='C:/Users/Rchrd/OneDrive/Desktop/Supermarket Project/AllProducts/Produce/Arugula.png')
Button(root, image= arugulapic).pack()

asianpic = PhotoImage(file='C:/Users/Rchrd/OneDrive/Desktop/Supermarket Project/AllProducts/Produce/Asian Greens.png')
Button(root, image= asianpic).pack()

basilpic = PhotoImage(file='C:/Users/Rchrd/OneDrive/Desktop/Supermarket Project/AllProducts/Produce/Basil.png')
Button(root, image= basilpic).pack()

root.mainloop()
