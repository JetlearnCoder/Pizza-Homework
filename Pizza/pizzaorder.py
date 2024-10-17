from tkinter import *
from tkinter.ttk import *
#combobox is defined inside ttk

window = Tk()
window.geometry("600x300")
window.title("Pizza Order")

favpizza = Label(window, text = "Select your favourite pizza:")
quantity = Label(window, text = "Enter Quantity:")
welcome = Label(window,text = "Welcome to Pizza Hut")

pizzatype = StringVar()

combofood = Combobox(window,textvariable = pizzatype)
combofood["values"] = ["Pepperoni Pizza","Cheese Pizza","Cheesy pizza","Vegan Pizza"]
"""quantiitycombo = Combobox(window,textvariable = amount)"""
    
rS = Radiobutton(window,text = "S",)
rM = Radiobutton(window,text = "M",)
rL = Radiobutton(window,text = "L",)


favpizza.place(x = 30, y = 100)
quantity.place(x = 30, y = 160)
welcome.place(x = 250, y = 30)
combofood.place(x = 260, y = 100)
"""quantity.place(x = 260, y = 200)"""

window.mainloop()