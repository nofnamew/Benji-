#1.Feladat: 
print("1. feladat")
fajlnev = str(input("Adja meg a bemeneti fájl nevét! "))
sor = int(input("Adja meg egy sor számát! ")) - 1
oszlop = int(input("Adja meg egy oszlop számát! ")) - 1

#2 feladat

tablazat = []
lepesek = []
with open(fajlnev, 'r') as fajl:
    for adtsor in fajl:
        adatsor = adtsor.strip().split()
        ertekek = [int(adat) for adat in adatsor]
        if len(ertekek) == 9:
            tablazat.append(ertekek)
        else:
            lepesek.append(ertekek)

#3 feladat

if tablazat[sor][oszlop] == 0:
    print("Az adot helyet még nem töltötték ki.")
else: 
    print(tablazat[sor][oszlop])
    print("A hely a(z) ",3 * (sor // 3) + (oszlop // 3) + 1," résztáblázathoz tartozik.")

#4 feladat
hossz = len(tablazat)
print(hossz)
