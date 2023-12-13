import tkinter as tk
from tkinter import *
from tkinter import messagebox
from tkinter.ttk import *
import tkinter
import random
import time


ablak = Tk()
ablak.geometry("500x300")
ablak.configure(bg="#ffff00")


def randomszam():
    szam = random.randint(1,3)
    return szam

def ujradef():
    global eredmeny 
    global valasz
    eredmeny = int(randomszam())
    valasz = 0

def vizsgalat():
    if eredmeny == valasz:
        jelenes.configure(text="Döntetlen!")
        ablak.after(2000, ures)
        ujra = messagebox.askquestion("Döntetlen", "Szeretnél újat kezdeni")
        if ujra == "yes":
            ujradef()
        else:
            ablak.destroy()

    elif (eredmeny == 3 and valasz == 2) or (eredmeny == 1 and valasz == 3) or (eredmeny == 2 and valasz == 1):
        jelenes.configure(text="Vesztettél!!!")
        ablak.after(2000, ures)
        ujra = messagebox.askquestion("Vesztettél:(", "Szeretnél újat kezdeni")
        if ujra == "yes":
            ujradef()
        else:
            ablak.destroy()

    elif (eredmeny == 1 and valasz == 2) or (eredmeny == 2 and valasz == 3) or (eredmeny == 3 and valasz == 1):
        jelenes.configure(text="Nyertél!!!")
        ablak.after(2000, ures)
        ujra = messagebox.askquestion("Nyertél!!!", "Szeretnél újat kezdeni")
        if ujra == "yes":
            ujradef()
        else:
            ablak.destroy()

def ures():
    jelenes.configure(text="")

def kodef():
    global valasz
    valasz = 1
    jelenes.configure(text="1")
    ablak.after(2000, ures)
    vizsgalat()


def papirdef():
    global valasz
    valasz = 2
    jelenes.configure(text="2")
    ablak.after(2000, ures)
    vizsgalat()


def ollodef():
    global valasz
    valasz = 3
    jelenes.configure(text="3")
    ablak.after(2000, ures)
    vizsgalat()


ujradef()
jelenes = Label(ablak, text="",anchor="center",width=30)
jelenes.place(x=150 ,y=75)
kokep = PhotoImage(file = "C:\\Users\\home\\Desktop\\Programozás\\Pton\\fun\\kpo\\ko1.gif")
kokep1 = kokep.subsample(2,2)
papirkep = PhotoImage(file = "C:\\Users\\home\\Desktop\\Programozás\\Pton\\fun\\kpo\\papir.gif")
papirkep1 = papirkep.subsample(2,2)
ollokep = PhotoImage(file = "C:\\Users\\home\\Desktop\\Programozás\\Pton\\fun\\kpo\\ollo.gif")
ollokep1 = ollokep.subsample(2,2)

ko = Button(ablak, text="ko" ,width=20,image = kokep1,command=kodef)

papir = Button(ablak, text="papir",width=20,image = papirkep1,command=papirdef)

ollo = Button(ablak, text="ollo",width=20,image = ollokep1,command=ollodef)

ko.place(x = 25 , y = 150)
papir.place(x= 175, y=150)
ollo.place(x= 325, y=150)


ablak.mainloop()
