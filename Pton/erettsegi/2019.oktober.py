import random

utasok = []
#1
with open("utasok.txt","r") as f:
    for i in f:
        utasok.append(i.strip().split())


#2
print("2.feladat")
print("A buszra ",len(utasok)," utas akart felszálni")

#3
print("3.feladat")
lejart = 0

for i in range(len(utasok)):
    if (int(utasok[i][1][0:8]) > int(utasok[i][4]) and int(utasok[i][4]) != 0 and int(utasok[i][4]) > 10) or (int(utasok[i][4]) == 0):
        lejart += 1

print("A buszra ",lejart," utas nem szállhatott fel")

#4
print("4.feladat")
legnagyobb = 0
megal = 0
sorszamhelp = 0
for i in range(len(utasok)-1):
    if int(utasok[i][0]) == int(utasok[i+1][0]):
        legnagyobb += 1
    else:
        if legnagyobb > megal:
            megal = legnagyobb + 1
            sorszamhelp = int(utasok[i][0])
        legnagyobb = 0

print("A legtöbb utas (",megal,"fő) a ",sorszamhelp,". megállóban próbált felszálni")

#5
print("5.feladat")
ingyen = 0
kedvezmeny = 0
for i in range(len(utasok)):
    if (utasok[i][3] == "NYP" or utasok[i][3] == "RVS" or utasok[i][3] == "GYK") and (not((int(utasok[i][1][0:8]) > int(utasok[i][4]) and int(utasok[i][4]) != 0 and int(utasok[i][4]) > 10) or (int(utasok[i][4]) == 0))):
        ingyen += 1
    elif (utasok[i][3] == "TAB" or utasok[i][3] == "NYB") and (not((int(utasok[i][1][0:8]) > int(utasok[i][4]) and int(utasok[i][4]) != 0 and int(utasok[i][4]) > 10) or (int(utasok[i][4]) == 0))):
        kedvezmeny += 1

print("Ingyenesen utazók száma: ",ingyen," Fő\n","A kedvezményesen utazók száma: ",kedvezmeny," Fő")

#6
def napokszama(e1,h1,n1,e2,h2,n2):
    h1 = (h1 + 9) % 12
    e1 = e1 - h1 // 10
    d1 = 365*e1 + e1 // 4 - e1 // 100 + e1 // 400 + (h1*306 + 5) // 10 + n1 - 1
    h2 = (h2 + 9) % 12
    e2 = e2 - h2 // 10
    d2 = 365*e2 + e2 // 4 - e2 // 100 + e2 // 400 + (h2*306 + 5) // 10 + n2 - 1
    napokszama = d2-d1 

    return napokszama


#7
kiirat = []
fi = open("figyelmeztetes.txt", "w")
fi.write("")
fi.close
for i in range(len(utasok)):
    e1 = int(utasok[i][1][0:4])
    h1 = int(utasok[i][1][4:6])
    n1 = int(utasok[i][1][6:8])
    if int(utasok[i][4]) > 11:
        e2 = int(utasok[i][4][0:4])
        h2 = int(utasok[i][4][4:6])
        n2 = int(utasok[i][4][6:8])
        if napokszama(e1,h1,n1,e2,h2,n2) <= 3:
            helpsor = utasok[i][4][0:4] + "-" + utasok[i][4][4:6] + "-" + utasok[i][4][6:8]
            fi = open("figyelmeztetes.txt", "a")
            fi.write(utasok[i][2])
            fi.write(" ")
            fi.write(helpsor)
            fi.write("\n")
            fi.close


