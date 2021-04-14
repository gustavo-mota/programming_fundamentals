#Criação da Matriz
matriz = [0] * 6
for j in range(6):
    matriz[j] = [0]*3

#Preenchimento da Matriz
for i in range(6):
    for j in range(3):
        numero = int(input("Digite um valor: "))
        matriz[i][j] = numero
        
#Verifica o Maior e o Menor número da Matriz
        if (i == 0 and j == 0):
            numero_maior = matriz[i][j]
            numero_menor = matriz[i][j]
        if (numero > numero_maior):
            numero_maior = numero
        elif (numero < numero_menor):
            numero_menor = numero
            
#Printa Matriz e Maior e Menor números
print("Matriz: ")
for i in matriz:
    print(i)
    
print("O maior número da matriz é: ",numero_maior)
print("O menor número da matriz é: ",numero_menor)
