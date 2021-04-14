#Escreva um programa que leia uma matriz A3x3 e calcule o seu determinante.
import random
soma_diagonal_principal = 0
soma_diagonal_secundaria = 0

#Criação da Matriz
matriz = [0]*3
for i in range(3):
    matriz[i] = [0]*3

#Preenchimento da Matriz
for i in range(3):
    for j in range(3):
        matriz[i][j] = random.randint(0,10)
print("Matriz: ")
for i in matriz:
    print(i)
matriz_determinante = matriz
#Criação da Matriz nova para calcular a Determinante
for i in range(3):
    for j in range(2):
        matriz_determinante[i].append(matriz[i][j])
print("Matriz Determinante: ")
for i in matriz_determinante:
    print(i)
    
#Cálculo da Soma da Diagonal Principal
produto = 1
for i in range(3):
    for j in range(3):
        produto = produto * matriz_determinante[j][j+i]
    soma_diagonal_principal = soma_diagonal_principal + produto 
    produto = 1

print("Valor da soma da Diagonal Principal:",soma_diagonal_principal)

#Cálculo da Soma da Diagonal Secundaria
for i in range(3):
    for j in range(3):
        produto = produto * matriz_determinante[j][4-(j+i)]
    soma_diagonal_secundaria = soma_diagonal_secundaria + produto
    produto = 1
print("Valor da soma da Diagonal Secundaria:", soma_diagonal_secundaria)
print("O Valor da Determinante é:",soma_diagonal_principal - soma_diagonal_secundaria)
