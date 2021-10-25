from tkinter import *
from tkinter import Tk

mycolor = '#4acd63'
root = Tk()

ShoppingVar= StringVar()

root.configure(bg=mycolor)
root.title('Rich Supermarket')
root.geometry("1100x700")
root.attributes('-fullscreen', True)

Label(text ="Please Select an Item", bg= mycolor, width="300", height ="2", font=("Calibri",13)).pack()
arugulapic = PhotoImage(file='C:/Users/Rchrd/OneDrive/Desktop/Supermarket Project/AllProducts/Produce/Arugula.gif')
b1= Button(root, image= arugulapic).pack()

asianpic = PhotoImage(file='C:/Users/Rchrd/OneDrive/Desktop/Supermarket Project/AllProducts/Produce/Zucchini.gif')
b2= Button(root, image= asianpic).pack()

basilpic = PhotoImage(file='C:/Users/Rchrd/OneDrive/Desktop/Supermarket Project/AllProducts/Produce/Sweet-Peppers.gif')
b3= Button(root, image= basilpic).pack()

Label(textvariable= ShoppingVar, bg= mycolor, width="300", height ="2", font=("Calibri",13))
b4= Button(root, text="Close", command= root.destroy).pack()
b5= Button(root,text="Check Out").pack()

####WITH SHOPPING VAR I CAN HAVE CONVERT A LIST INTO A STRING AND JUST KEEP UPDAING IT

def AddSelectedItem():
    EnteredBC = input()
    
    e =Entry(root, )
root.mainloop()