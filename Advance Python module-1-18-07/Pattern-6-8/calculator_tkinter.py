import tkinter
calc=tkinter.Tk()
calc.title("Calculator")
calc.geometry("500x600")
calc.config(bg="skyblue")

#value entrty:
tkinter.Label(text="Value_1:",bg="black",fg="white",font="dubai 15 italic").grid(row=0,column=0,sticky="w")
tkinter.Label(text="Value_2:",bg="black",fg="white",font="dubai 15 italic").grid(row=1,column=0,sticky="w")

#entry value:
v1=tkinter.Entry(font="dubai 12 italic")
v1.grid(row=0,column=1,sticky="w")
v2=tkinter.Entry(font="dubai 12 italic")
v2.grid(row=1,column=1,sticky="w")

#button:
def addition():
    print("Addition:",int(v1.get())+int(v2.get()))

def subtraction():
    print("Subtraction:",int(v2.get())-int(v2.get()))

def multiply():
    print("Multiply:",int(v1.get())*int(v2.get()))

def division():
    print("Division:",int(v1.get())/int(v2.get()))

"""tkinter.Checkbutton(text="Add",bg="black",fg="white",font="dubai 12 bold").grid(row=5,column=0,sticky="w")
tkinter.Checkbutton(text="Sub",bg="black",fg="white",font="dubai 12 bold").grid(row=6,column=1,sticky="w")
tkinter.Checkbutton(text="Mul",bg="black",fg="white",font="dubai 12 bold").grid(row=7,column=2,sticky="w")
tkinter.Checkbutton(text="Div",bg="black",fg="white",font="dubai 12 bold").grid(row=8,column=3,sticky="w")
"""

tkinter.Button(text="Add",font="dubai 15 bold",command=addition).place(x=50,y=100)
tkinter.Button(text="Sub",font="dubai 15 bold",command=subtraction).place(x=120,y=100)
tkinter.Button(text="Mul",font="dubai 15 bold",command=multiply).place(x=190,y=100)
tkinter.Button(text="Div",font="dubai 15 bold",command=division).place(x=260,y=100)


calc.mainloop()