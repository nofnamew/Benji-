from collections import Counter

#1
tanc = {}
adatok = []
tancok = []
with open("tancrend.txt","r") as f:
    for i in f:
        adatok.append(i.strip())
        if len(adatok) == 3:
            tanc["nev"] = adatok[0]
            tanc["lany"] = adatok[1]
            tanc["fiu"] = adatok[2]
            tancok.append(tanc)
            tanc = {}
            adatok = []

hosz = len(tancok)
#2
print("2.feladat")
print(f"Az első a(z) {tancok[0]['nev']} volt, az utolsó a(z) {tancok[-1]['nev']}")

#3
print("3.feladat")
helpossz = 0
for i in range(hosz):
    if tancok[i]['nev'] == "samba": 
        helpossz += 1


print(f"Összesen {helpossz} an mutattak be sambát")

#4
print("4.feladat")
print("Vilma szerepelt ezekben a táncokba:")
for i in range(hosz):
    if tancok[i]['lany'] == "Vilma": 
        print(tancok[i]['nev'])

#5
print("5.feladat")

vilmatanc = input("Adjon meg egy táncot")

helpossz = 0

for i in range(hosz):
    if tancok[i]['lany'] == "Vilma" and tancok[i]['nev'] == vilmatanc: 
        print(f"{tancok[i]['fiu']} mutatta be Vilmával")
        helpossz += 1
if helpossz == 0:
    print(f"A {vilmatanc} nem volt bemutatva Vilma által")

#6
print("6.feladat")

helplistlany = []
helplistfiu = []

for i in range(hosz):
    helplistlany.append(tancok[i]['lany'])
    helplistfiu.append(tancok[i]['fiu'])

listlany = list(set(helplistlany))
listfiu = list(set(helplistfiu))



with open("szereplok.txt","w",encoding="utf-8") as f:
    f.write("Lanyok: ")
    for i in range(len(listlany)):
        f.write(listlany[i])
        if i != len(listlany) - 1:
            f.write(", ")

    f.write("\n")
    f.write("Fiuk: ")
    for i in range(len(listfiu)):
        f.write(listfiu[i])
        if i != len(listfiu) - 1:
            f.write(", ")


#7
helpmax = 0
helphely = 0
lanyok = Counter(helplistlany)
fiuk = Counter(helplistfiu)

helplanyok = list(lanyok.keys())
helpszamlanyok = list(lanyok.values())


helpfiuk = list(fiuk.keys())
helpszamfiuk = list(fiuk.values())
print("A legtöbbet szerepelt lányok:")
for i in range(len(helplanyok)):
    if helpszamlanyok[i] > helpmax:
        helphely = i
        helpmax = helpszamlanyok[i]

for i in range(len(helplanyok)):
    if helpszamlanyok[i] == helpszamlanyok[helphely]:
        print(f"{helplanyok[i]}")


print("A legtöbbet szerepelt fiuk:")
for i in range(len(helpfiuk)):
    if helpszamfiuk[i] > helpmax:
        helphely = i
        helpmax = helpszamfiuk[i]

for i in range(len(helpfiuk)):
    if helpszamfiuk[i] == helpszamfiuk[helphely]:
        print(f"{helpfiuk[i]}")