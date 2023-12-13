from tkinter import *
import random

HOSSZ = 700
MAGAS = 700
SPEED = 50
UR = 50
SPACESIZE = 50
BODY = 3
KIGYOSZIN = "#000000"
KAJASZIN = "#00ff00" 
HATTER = "#669999"


class Snake:
    pass

class Kaja:
    def __init__(self):
        x = random.randint(0,(HOSSZ/SPACESIZE-1)) * SPACESIZE
        x = random.randint(0,(MAGAS/SPACESIZE-1)) * SPACESIZE

        self.coordinates = [x,y]

        ter.create_oval(x,y,x + SPACESIZE,)
def kov():
    pass

def iranyvaltoz(ujirany):
    pass

def vege():
    pass

ablak = Tk()
ablak.title("Snék Gém")
ablak.resizable(False,False)

score = 0
direction = "down"

pontmutat = Label(ablak, text="Pont:{}".format(score),font=("consolas", 40))
pontmutat.pack()

ter = Canvas(ablak,bg=HATTER,width=HOSSZ,height=MAGAS)
ter.pack()

ablak.update()

ablak_hossz = ablak.winfo_width()
ablak_magas = ablak.winfo_height()
kep_hossz = ablak.winfo_screenwidth()
kep_magas = ablak.winfo_screenheight()

x = int((kep_hossz/2) - (ablak_hossz/2))
y = int((kep_magas/2) - (ablak_magas/2))

ablak.geometry(f"{ablak_hossz}x{ablak_magas}+{x}+{y}")


kigyo = Snake()
kaja = Kaja()


ablak.mainloop()