'''Criar um programa que leia uma matriz ANxN (N < 10) e calcule a respectiva matriz
transposta At.'''
import random
N = int(input("Digite o valor para as linhas e colunas da matriz: "))
#Criação da Matriz e Matriz Transposta
matriz = [0]*N
for i in range(N):
    matriz[i] = [0]*N
matriz_transposta = [0]*N
for j in range(N):
    matriz_transposta[j] = [0]*N

#Preenchimento das Matrizes
for i in range(N):
    for j in range(N):
        matriz[i][j] = random.randint(0,10)
        matriz_transposta[j][i] = matriz[i][j]
        
#Mostra as duas Matrizes
print("Matriz:")
for i in matriz:
    print(i)
print("Matriz Transposta: ")
for j in matriz_transposta:
    print(j)
