def somar(lista):
	somatorio = 0
	for i in range(0,n):
		somatorio = somatorio + lista[i]
	return somatorio

n = int(input("Digite o tamanho do vetor: "))
vetor = []
for i in range(0,n):
	x = int(input("Digite um valor: "))
	vetor.append(x)
soma = somar(vetor)
print(soma)
