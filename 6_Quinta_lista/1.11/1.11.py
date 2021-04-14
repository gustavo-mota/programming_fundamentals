
matriz = {}
cofator = {}
inversa = {}
det = []

som = 1
sub = 1
cont = 0
detMatriz = 0

for i in range(1, 4):
    for j in range(1, 4):
        matriz[(i, j)] = int(input(" "))

for i in range(1, 4):
    for j in range(1, 4):
        for k in range(1, 4):
            for l in range(1, 4):
                if i != k and j != l:
                    if cont == 0:
                        som *= matriz[k, l]
                        cont += 2
                    else:
                        sub *= matriz[k, l]
                        cont -= 1
        cont = 0
        cofator[(i, j)] = ((-1)**(j+i))*(som - sub)
        if i == 2:
            det.append(cofator[(i, j)] * matriz[(i, j)])
        som = 1
        sub = 1

for k in range(3):
    detMatriz += det[k]

if detMatriz == 0:
    print("A matriz não possui inversa!")
else:
    for i in range(1, 4):
        for j in range(1, 4):
            inversa[(i, j)] = cofator[(j, i)]*(1/detMatriz)

    print("\nA matriz inversa é:")

    for k in range(1, 4):
        for l in range(1, 4):
            print(inversa[(k, l)], end=" ")
        print(end="\n")
