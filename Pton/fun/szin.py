from tkinter import *
from tkinter import font
from tkinter import messagebox
import random
import tkinter as tk
from PIL import Image, ImageTk, ImageSequence 

ablak = Tk()
ablak.title("Color Picker 2000")
hatter = PhotoImage(file= "C:\\Users\\home\\Desktop\\Programozás\\Pton\\fun\\rgbg.gif")



ablak.geometry("900x580")

foablak = Frame(ablak)
fokoszont = Frame(ablak)
label1 = Label(fokoszont, image = hatter) 
label1.place(x = 0, y = 0) 
fokoszont.pack(fill='both', expand=1)
foablak.pack_forget()

kormehet = True
pont = 0
bestpont = 0

def szintrans(rgb):
    r, g, b = rgb
    return f'#{r:02x}{g:02x}{b:02x}' 

def kocka1def():
    global pont
    if melyikkocka == 0:
        pont += 1
        pontmutat.configure(text=pont)
    else:
        vesztet()
    rendomszindef()

def kocka2def():
    global pont
    if melyikkocka == 1:
        pont += 1
        pontmutat.configure(text=pont)
    else:
        vesztet()
    rendomszindef()

def kocka3def():
    global pont
    if melyikkocka == 2:
        pont += 1
        pontmutat.configure(text=pont)
    else:
        vesztet()
    rendomszindef()

def kocka4def():
    global pont
    if melyikkocka == 3:
        pont += 1
        pontmutat.configure(text=pont)
    else:
        vesztet()
    rendomszindef()

def nehezsegdef():
    global nehezlistertek
    nehezlist = {"Könnyű":40,
                 "Közepes": 30,
                 "Nehéz": 20
                 }
    nehezlistertek = random.choice(list(nehezlist.items()))
    return nehezlistertek[1]

def rendomszindef():
    global kockadoboz
    global melyikkocka 
    piros = random.randint(0,255)
    kek = random.randint(0,255)
    zold = random.randint(0,255)
    szinek = [piros, kek, zold]
    szinekcopy = [piros, kek, zold]
    melyikszin = random.randint(0,2)
    melyikkocka = random.randint(0,3)
    for i in range(4):
        if melyikkocka == i:
            szinekcopy[melyikszin] = abs(szinek[melyikszin] - nehezsegdef())
            kockadoboz[i].configure(bg=szintrans((szinekcopy[0],szinekcopy[1],szinekcopy[2])))
        else:
            kockadoboz[i].configure(bg=szintrans((szinek[0],szinek[1],szinek[2])))
    nehezsegmutat.configure(text=nehezlistertek[0])

def kezdesdef():
    foablak.pack(fill='both', expand=1)
    fokoszont.pack_forget()
    rendomszindef()
    
def vegdef():
    ablak.destroy()

def vesztet():
    global pont
    global bestpont
    valasz = messagebox.askquestion("Vesztetél","Akarod még folytatni?")
    if valasz == "yes":
        if pont > bestpont:
            bestpont = pont
            bestpontmutat.configure(text=bestpont)
        pont = 0
        pontmutat.configure(text=pont)
    else:
        vegdef()



idoperc = str(0)
idomp = str(0)
font1 = font.Font(family='Georgia', size='22', weight='bold')

koszontes = Label(fokoszont, text="Color picker 2000(pro max 100 % danger)", font=font1)
kezdes = Button(fokoszont, text="Start", command = kezdesdef,width=15)
kilepes = Button(fokoszont, text="Quit", command = vegdef,width=15)

kocka1 = Button(foablak, command = kocka1def,width=35, height=15)
kocka2 = Button(foablak, command = kocka2def,width=35, height=15)
kocka3 = Button(foablak, command = kocka3def,width=35, height=15)
kocka4 = Button(foablak, command = kocka4def,width=35, height=15)
pontmutat = Label(foablak,text=pont,font = font1)
best = Label(foablak,text="Best:",font = font1)
bestpontmutat = Label(foablak,text=bestpont,font = font1)
idomutat = Label(foablak,text=idomp,font = font1)
nehezsegmutat = Label(foablak,text="-",font = font1)


kockadoboz = [kocka1,kocka2,kocka3,kocka4]

kockadoboz[0].place(x=150,y=50)
kockadoboz[1].place(x=400,y=50)
kockadoboz[2].place(x=150,y=280)
kockadoboz[3].place(x=400,y=280)


idomutat.place(x=700,y=20)
nehezsegmutat.place(x=700,y=20)
pontmutat.place(x=20,y=20)
best.place(x=10,y=80)
bestpontmutat.place(x=20,y=120)
koszontes.place(x=100,y=180)
kezdes.place(x=250,y=350)
kilepes.place(x=400,y=350)

ablak.mainloop()