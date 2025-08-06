import tkinter
windows=tkinter.Tk()
windows.title("My App")
windows.geometry("400x500") #not to use * symbol
windows.config(background="light blue")
#windows.congig(bg="yellow")

"""tkinter.Label(text="Firstname:").pack()
tkinter.Label(text="lastname:").pack()
"""

tkinter.Label(text="Firstname:",bg="lightblue",font="dubai 15 bold",fg="red").place(x=0,y=0)
tkinter.Label(text="Lastname:",bg="lightblue",font="dubai 15 bold",fg="red").place(x=0,y=30)



windows.mainloop()   #mainloop helps to get screen and will be last line