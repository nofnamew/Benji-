import math

forrasfajl = open("jelado.txt")

def eltelt(sorok1,sorok2):
    return abs((int(sorok2[0]) - int(sorok1[0])) * 3600 + (int(sorok2[1]) - int(sorok1[1])) * 60 + (int(sorok2[2]) - int(sorok1[2])))


sorok = []

o =  0

for i in forrasfajl:
    help = i.split(' ') 
    sorok.append(help)
    o += 1

print("1.feladat:\n")
sorszam = int(input("Adj meg egy sorszámot:"))
print("\n x: ",sorok[sorszam-1][-2],"\n y: ",sorok[sorszam-1][-1])
print("------------------\n")
print("4.feladat:\n")
kulonbseg = eltelt(sorok[0], sorok[-1])

osszosszora = kulonbseg // 3600
osszosszperc = (kulonbseg % 3600) // 60
osszosszmp = kulonbseg  % 60

print("osszosszora: ",osszosszora)
print("osszosszperc: ",osszosszperc)
print("osszosszmp: ",osszosszmp)

print("5.feladat:\n")

forrasfajl.close() 