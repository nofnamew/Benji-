#1.Feladat: Bekéretés, és tárolás________________________________________________________________________________
utcak = []
sorokszama = True

with open("utca.txt", encoding="utf-8") as forrasfajl:
    for i in forrasfajl:
        if sorokszama == True:
            help = i.strip().split(' ')
            adosav = {
                "A" : int(help[0]),
                "B" : int(help[1]),
                "C" : int(help[2]),
            }
            sorokszama = False
        else:
            help = i.strip().split(' ') 
            helpdic = {
                "adoszam": help[0],
                "nev": help[1],
                "hazszam": help[2],
                "adotipus": help[3],
                "terulet": int(help[4]),
            }
            utcak.append(helpdic)

#2.Feladat: Telek mennyiseég kiíratás________________________________________________
utcahosz = int(len(utcak))
print("2.feladat:")
print("A mintában ",utcahosz, " telek szerepel.")

#3.Feladat: Egy tulajdonos házának megtalálása  ________________________________________________
print("3.feladat:")
egytulaj = str(input("Egy tulajdonos adószáma:"))
epitmenyek = 0
for i in range(utcahosz):
    if utcak[i]["adoszam"] == egytulaj:
        print(utcak[i]["nev"]," utca ",utcak[i]["hazszam"])
        epitmenyek += 1
if epitmenyek == 0:
    print("Nem szerepel az adatállományban\n")



#4.Feladat: Adószámítás függvénnyel ________________________________________________

def ado(adotipus,terulet):
    if adosav[adotipus] * terulet < 10000:
        return 0
    else: 
        return adosav[adotipus] * terulet 
    
#5.Feladat: adósávak megszámolása ________________________________________________

print("5. Feladat\n")
helpadosav = {
    "A" : 0,
    "B" : 0,
    "C" : 0
}
vegado = {
    "A" : 0,
    "B" : 0,
    "C" : 0
}
for i in range(utcahosz):
    helpadosav[utcak[i]["adotipus"]] += 1
    vegado[utcak[i]["adotipus"]] = vegado[utcak[i]["adotipus"]] + ado(utcak[i]["adotipus"],utcak[i]["terulet"])

print("A sávba ", helpadosav["A"]," telek esik, az adó ",vegado["A"]," Ft.")
print("B sávba ", helpadosav["B"]," telek esik, az adó ",vegado["B"]," Ft.")
print("C sávba ", helpadosav["C"]," telek esik, az adó ",vegado["C"]," Ft.")

#6.feladat:  olyan utcák, ahol többféle ado csoportositás van________________________________________________________________

vegnev = []

for i in range(utcahosz-1):
    if utcak[i]["nev"] == utcak[i+1]["nev"] and utcak[i]["adotipus"] != utcak[i+1]["adotipus"]:
        vegnev.append(utcak[i]["nev"])

vegnev = list(set(vegnev))

for i in range(len(vegnev)):
    print(vegnev[i])

#7.feladat:   ________________________________________________________________

f = open("fizetendo.txt", "w", encoding="utf-8")
for i in range(utcahosz):
    helpado = str(ado(utcak[i]["adotipus"],utcak[i]["terulet"]))
    f.write(utcak[i]["adoszam"])
    f.write(" ")
    f.write(helpado)
    f.write("\n")

f.close()



