matriz = [ [0,0,0,0],[0,0,0,0],[0,0,0,0],[0,0,0,0] ]
for i in range(0,4):
    for j in range(0,4):
        matriz[i][j] = int(input("Digite o valor da venda: "))
for s in range(0,4):
    for r in range(0,4):
        if s!=r:
            print(matriz[s][r],end=" ")
    print("\n")