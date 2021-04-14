def maior(lista):
	maior = vetor[1]
	for i in range(1,n):
		if maior < vetor[i]:
			maior = vetor[i]
	return maior
n = int(input("Digite o tamanho do vetor: "))
vetor = []
for i in range(0,n):
    x = int(input("Digite um numero: "))
    vetor.append(x)
maior_termo = maior(vetor)
print(maior_termo)