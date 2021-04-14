matrizA = [ [0,0],[0,0],[0,0]]
matrizB = [ [0,0,0,0,0],[0,0,0,0,0]]
matrizC = [ [0,0,0,0,0],[0,0,0,0,0],[0,0,0,0,0]]

for i in range(0,3):
    for j in range(0,5):
        matrizA[i][j] = int(input("Digite o elemento: "))

for s in range(0,2):
    for r in range(0,5):
        matrizB[s][r] = int(input("Digite o elemento: "))

for h in range(0,3):
    for d in range(0,5):
        n = matrizA[h][1]*matrizB[1][d] + matrizA[h][2]*matrizB[2][d]
        matrizC[h][d] = n
        print(matrizC[h][d], end=" ")
    print("\n")