n = int(input("Digite um número: "))
matriz = [  ]
linha = [  ]
oposta = [  ]
antisimetrica=True
for h in range(0,n):
    linha.append(0)
for d in range(0,n):
    matriz.append(linha)
    oposta.append(linha)

for i in range(0,n):
    for j in range(0,n):
        matriz[i][j] = int(input('Digite o valor: '))
        oposta[j][i] = matriz[i][j] * (-1)

for s in range(0,n):
    for r in range(0,n):
        if matriz[s][r] != oposta[s][r]:
            antisimetrica=False
if antisimetrica==True:
    print("È antisimétrica")
else:
    print("Não é")