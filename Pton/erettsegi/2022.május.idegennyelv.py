
#1
meresek = {}
kezdet = []
veg = []

def valt(o,p,mp,mmp):
    return o + (p / 60) + (mp + (mmp / 1000)) / 3600

with open("meresek.txt") as f:
    for i in f:
        sor = i.split()
        meresek[sor[0]] = [valt(int(sor[1]),int(sor[2]),int(sor[3]),int(sor[4])), valt(int(sor[5]),int(sor[6]),int(sor[7]),int(sor[8]))]


#2  
print("2.feladat")  
print(f"A mérés során {len(meresek)} jármű adatait rögzítették")

#3
print("3.feladat")  
helpveg = 0
for i in meresek:
    if meresek[i][1] < 9:
        helpveg += 1
print(f"9 óra előtt {helpveg} jármű haladt el a végponti mérőnél")
#4