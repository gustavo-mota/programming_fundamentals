matriz = [ [0,0,0], [0,0,0],[0,0,0] ]
vetor=[]
soma=0
for i in range(0,3):
	for j in range(0,3):
		matriz[i][j] = int(input("Digite o valor do elemento: "))
		soma = soma + matriz[i][j]
	vetor.append(soma)
	soma = 0
for j in range(0, len(vetor)):
	print(vetor[j], end=" ")