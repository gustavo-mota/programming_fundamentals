def inverte(lista):
	lista.reverse()
	return lista

n = int(input("Digite quantos elementos há no vetor: "))
vetor = []

for i in range(0,n):
    x = input("Digite o elemento: ")
    vetor.append(x)
inverte(vetor)
print(vetor)