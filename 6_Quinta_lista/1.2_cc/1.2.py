matriz = [ [0,0,0,0], [0,0,0,0],[0,0,0,0],[0,0,0,0] ]
lista=[]

for i in range(0,4):
	for j in range(0,4):
		matriz[i][j] = int(input("Digite o número: "))
		if i==j:
			lista.append(matriz[i][j])
print(lista)