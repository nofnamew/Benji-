import random

tabla = [[0,0,0,0],
         [0,0,0,0],
         [0,0,0,0],
         [0,0,0,0],
         ]

def keveres():
    global randomx
    global randomy
    global randomx2
    global randomy2
    randomx = random.randint(0,3)
    randomy = random.randint(0,3)

    tabla[randomy][randomx] = 2

    randomx2 = random.randint(0,3)
    randomy2 = random.randint(0,3)

    if randomx2 != randomx and randomy != randomy2:
        randomx2 = random.randint(0,3)
        randomy2 = random.randint(0,3)

    tabla[randomy2][randomx2] = 2

def elhely():
    randomx = random.randint(0,3)
    randomy = random.randint(0,3)

    if tabla[randomy][randomx] == 0:
        tabla[randomy][randomx] = 2
    else:
        randomx = random.randint(0,3)
        randomy = random.randint(0,3)
        tabla[randomy][randomx] = 2


veg = "I"
lefutott = 0

while veg != "N":
    if lefutott == 0:
        keveres()
        lefutott += 1
    else:
        for i in range(4):
            print(tabla[i])
        mozgas = input("Fel(w)\nLe(s)\nBalra(a)\nJobbra(d)")
        if mozgas == "N":
            veg == "N"
        if mozgas == "w":

            for o in range(3) :

                for i in range(4) :

                    if tabla[3-o][i] != 0 and tabla[3-o][i] == tabla[3-o-1][i]:

                        tabla[3-o-1][i] = tabla[3-o-1][i] * 2
                        tabla[3-o][i] = 0

                    elif tabla[3-o][i] != 0 and tabla[3-o-1][i] == 0:

                        tabla[3-o-1][i] = tabla[3-o][i]
                        tabla[3-o][i] = 0

        if mozgas == "s":

            for o in range(3) :

                for i in range(4) :

                    if tabla[o][i] != 0 and tabla[o][i] == tabla[o+1][i]:

                        tabla[o+1][i] = tabla[o+1][i] * 2
                        tabla[o][i] = 0

                    elif tabla[o][i] != 0 and tabla[o+1][i] == 0:

                        tabla[o+1][i] = tabla[o][i]
                        tabla[o][i] = 0

        if mozgas == "d":

            for i in range(3) :

                for o in range(4) :

                    if tabla[o][i] != 0 and tabla[o][i] == tabla[o][i+1]:

                        tabla[o][i+1] = tabla[o][i+1] * 2
                        tabla[o][i] = 0

                    elif tabla[o][i] != 0 and tabla[o][i+1] == 0:

                        tabla[o][i+1] = tabla[o][i]
                        tabla[o][i] = 0

        if mozgas == "a":
            for i in reversed(range(1,4)) :

                for o in reversed(range(0,4)) :

                    if tabla[o][i] != 0 and tabla[o][i-1] == tabla[o][i]:

                        tabla[o][i-1] = tabla[o][i-1] * 2
                        tabla[o][i] = 0

                    elif tabla[o][i] != 0 and tabla[o][i-1] == 0:

                        tabla[o][i-1] = tabla[o][i]
                        tabla[o][i] = 0
        
        elhely()
    

        


