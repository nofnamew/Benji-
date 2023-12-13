from tkinter import * 
import tkinter as tk
from tkinter import messagebox

ablak = Tk()
ablak.geometry("500x500")

szoveg = tk.StringVar()


def adddef():
    szoveghelp = szoveg.get()
    if szoveghelp == "":
        messagebox.showinfo(title="Empty Entry", message="Enter task name")
    else:
        listabox.insert(0, szoveghelp)
        szoveg.set("")


def delldef():
    try:
        if listabox.curselection() == "":
            print("ezaz")
        listabox.delete(listabox.curselection())
    except:
        messagebox.showinfo(title="Cannot Delete", message="No Task Item Selected")


def alldelldef():
    kerdes = messagebox.askquestion("Delete All", "Are you sure?")
    if kerdes == "yes":
        listabox.delete(0,END)
    

def esitdef():
    kerdes = messagebox.askquestion("Exit", "Are you sure?")
    if kerdes == "yes":
        ablak.destroy()



ablak.title("To-Do List")

cim = Label(ablak, text="To-Do List")
cim.place(x = 30, y=30)

enter = Label(ablak, text="Enter task title:")
enter.place(x = 30, y=50)


be = Entry(ablak, textvariable=szoveg,bd = 1, width=24)
be.place(x=30,y=80)


add = Button(ablak, text="Add task", width=20, command=adddef)
add.place(x=30,y=120)

dell = Button(ablak, text="Delete", width=20, command=delldef)
dell.place(x=30,y=150)

alldell = Button(ablak, text="Delete all", width=20, command=alldelldef)
alldell.place(x=30,y=180)

esit = Button(ablak, text="Exit", width=20, command=esitdef)
esit.place(x=30,y=210)


listabox = Listbox(ablak, selectmode="Single")
listabox.place(x=200,y=10)

ablak.mainloop()
