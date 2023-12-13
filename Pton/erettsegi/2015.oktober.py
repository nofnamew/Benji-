import random

#1.feladat
def dobas():
    szam = random.randint(0,1)
    if szam == 0:
        return "F"
    else:
        return "I"
    
print("1.feladat")
print("A pénzfeldobás eredménye: ",dobas())

#2.feladat
print("2.feladat")
valos = dobas()
tipp = input("Tippeljen! (F/I) = ")
print("A tipp ", tipp, " volt, a dobás eredménye ", valos," volt")
if tipp == valos :
    print("Ön eltalálta")
else: 
    print("Ön nem találta el")

#3.feladat
print("3.feladat")
with open("talalatok.txt", encoding="utf-8") as f:
    szam = 0
    for sor in f:
        szam += 1
print("A kísérlet", szam," dobásból állt.")

#4.feladat

print("4.feladat")
fszam = 0
with open("talalatok.txt", encoding ="utf-8") as f:
    for sor in f:
        helpsor = f.readline().strip("\n")
        if helpsor == "F":
            fszam += 1
           
print(fszam)
print(f"A kísérlet során a fej relatív gyakorísága {round(fszam/szam*100, 2)}% volt")


#5.feladat

print("5.feladat")

helpszam = 0
helpstr = ''

with open("talalatok.txt", encoding ="utf-8") as f:
    for i in f:
        if len(helpstr) == 3 and helpstr == "FFI":
            helpszam += 1

        if len(helpstr) == 4:
            helpstr = helpstr[1:] + i.strip()
            if helpstr == 'IFFI':
                helpszam += 1
        else:
            helpstr += i.strip()

    if helpstr[1:] == 'IFF':
        helpszam += 1
print(f'A kísérlet során a összesen {helpszam} alkalommal dobtak pontosan két fejet egymás után.')

#6
print("6.feladat")

helpstr = ""

with open("talalatok.txt", encoding ="utf-8") as f:
    for i in f:
        pass
