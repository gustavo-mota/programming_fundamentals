matriz = [ [0,0,0,0],[0,0,0,0],[0,0,0,0],[0,0,0,0] ]
for i in range(0,4):
    for j in range(0,4):
        matriz[i][j] = int(input('Digite o valor do elemento: '))
x = 3
y = 0
for s in range(0,4):
    print(matriz[y][x], end=" ")
    x -= 1
    y +=1
