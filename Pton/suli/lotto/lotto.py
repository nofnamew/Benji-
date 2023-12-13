

def maxfinder():

    max = dic[0]

    helpsor = 0 

    for i in range(100):
        if dic[i] >= max:
            max = dic[i]
            helpsor = i

    dic[helpsor] = 0

    return str(helpsor)



f = open("Lottó.txt", "r")


dic = {

}

for i in range(100):
    dic[i] = 0




for fullLine in f:
    sepFullLine = fullLine.split(';')

    for i in range(5):
        help = int(sepFullLine[i + 11])
        dic[help] += 1

print(dic)

placeNum = int(input("Szám: "))

d = open("Nyeroszam.txt", "w")
d.close()

for i in range(placeNum):
   helpveg = maxfinder()
   print(helpveg)
   d = open("Nyeroszam.txt", "a")
   d.write(str(i+1))
   d.write(":")
   d.write(helpveg)
   d.write("\n")
   d.close()
   

