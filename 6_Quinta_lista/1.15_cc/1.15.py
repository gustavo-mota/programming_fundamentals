soma_dp = 0
soma_ds = 0
soma_l1 = 0
soma_l2 = 0
soma_l3 = 0
soma_c1 = 0
soma_c2 = 0
soma_c3 = 0

#Criação da Matriz
matriz = [0]*3
for i in range(3):
    matriz[i] = [0]*3

#Preenchimento da Matriz
for i in range(3):
    for j in range(3):
        matriz[i][j] = int(input("Digite um número: "))
#Calculo da soma da Diagonal Principal
        if (i == j):
            soma_dp = matriz[i][j] + soma_dp
#Cálculo da soma da Diagonal Secundária
    soma_ds = matriz[i][4-(i+j)] + soma_ds
#Cálculo da soma das linhas e das colunas
for j in range(3):
    soma_l1 = matriz[0][j] + soma_l1
    soma_l2 = matriz[1][j] + soma_l2
    soma_l3 = matriz[2][j] + soma_l3
    soma_c1 = matriz[j][0] + soma_c1
    soma_c2 = matriz[j][1] + soma_c2
    soma_c3 = matriz[j][2] + soma_c3
#Printa a Matriz
for i in matriz:
    print(i)
#Verifica se todas as somas são iguais
if (soma_l1 == soma_l2 and soma_l2 == soma_l3 and soma_l3 == soma_dp and soma_dp == soma_ds and soma_ds == soma_c1 and soma_c1 == soma_c2 and soma_c2 == soma_c3):
    print("É um quadrado mágico")
else:
    print("Não é um quadrado mágico")
