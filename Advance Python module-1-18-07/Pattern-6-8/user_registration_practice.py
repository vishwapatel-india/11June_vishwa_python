import tkinter
from tkinter import ttk
user=tkinter.Tk()
user.title("My Store")
user.geometry("500x600")
user.config(bg="maroon")

#pack practice for label
"""tkinter.Label(text="Name:").pack()
tkinter.Label(text="Surname:").pack()
"""

tkinter.Label(text="Product Details",bg="black",fg="white",font="dubai 18 italic").grid(row=0,column=3,sticky="w")

#label with place
"""tkinter.Label(text="Product name",bg="black",fg="white",font="dubai 18 italic").place(x=0,y=30)
tkinter.Label(text="Brand Name",bg="black",fg="white",font="dubai 18 italic").place(x=0,y=30)
"""
#label with grid
tkinter.Label(text="Product name",bg="black",fg="white",font="dubai 15 italic").grid(row=1,column=0,sticky="w")
tkinter.Label(text="Brand name",bg="black",fg="white",font="dubai 15 italic").grid(row=2,column=0,sticky="w")

#entry in above
pnm=tkinter.Entry(text="constantia 12 bold")
pnm.grid(row=1,column=1,sticky="w")
bnm=tkinter.Entry(text="constantia 12 bold")
bnm.grid(row=2,column=1,sticky="w")

tkinter.Radiobutton(value=0,text="Face Care",font="constantia 12 bold",bg="black",fg="white").grid(row=6,column=0,sticky="w")
tkinter.Radiobutton(value=1,text="Hair care",font="constantia 12 bold",bg="black",fg="white").grid(row=6,column=1,sticky="w")
tkinter.Radiobutton(value=2,text="Accesories",font="constantia 12 bold",bg="black",fg="white").grid(row=6,column=2,sticky="w")

tkinter.Checkbutton(text="Loreal",font="constantia 12 bold",bg="black",fg="white").grid(row=8,column=0,sticky="w")
tkinter.Checkbutton(text="Maybelline",font="constantia 12 bold",bg="black",fg="white").grid(row=8,column=1,sticky="w")
tkinter.Checkbutton(text="Renee'",font="constantia 12 bold",bg="black",fg="white").grid(row=8,column=2,sticky="w")

City=["Rajkot","Ahmedabad","Surat","Baroda","Jamnagar"]
ttk.Combobox(values="City").grid(row=9,column=0,sticky="w")

def btnclick():
    print("Product name:".pnm.get())
    print("Brand name:".bnm.get())

tkinter.Button(text="Submit",font='Constantia 18 bold',command=btnclick).place(x=190,y=290)



user.mainloop()
