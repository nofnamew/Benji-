import tkinter
from tkinter import *
from PIL import Image, ImageTk
import tkinter
from tkinter import font

#ablak
ablak = Tk()
ablak.geometry("500x500")



#hero img
hero = PhotoImage(file="C:\\Users\\home\\Desktop\\Programozás\\Pton\\fun\\hero2.gif")
herosize = hero.subsample(10, 10)



#framek
koszon = Frame(ablak)
fo = Frame(ablak)
gameover = Frame(ablak)
koszon.pack(fill='both', expand=1)
fo.pack_forget()
gameover.pack_forget()

#def-ek

def animation():
    print("qwe")


def maindef():
    fo.pack(fill='both', expand=1)
    koszon.pack_forget()
    gameover.pack_forget()



#felvétel és elhelyezés
font1 = font.Font(family='Georgia', size='22', weight='bold')
start = Button(koszon, text="Start",command=maindef)
Sl = Label(koszon, text="S", font=font1)
Nl = Label(koszon, text="N", font=font1)
Al = Label(koszon, text="A", font=font1)
Kl = Label(koszon, text="K", font=font1)
El = Label(koszon, text="E", font=font1)
herokep = Label(fo,image=herosize)



herokep.place(x=140,y=100)
Sl.place(x=140,y=100)
Nl.place(x=180,y=100)
Al.place(x=220,y=100)
Kl.place(x=260,y=100)
El.place(x=300,y=100)
start.place(x=200,y=200)





ablak.after_idle(animation)
ablak.mainloop()