def fibonacci(lista, ordem):
	x = 1
	y = 1
	lista.append(x)
	lista.append(y)
	for i in range(2,ordem):
		num = x + y
		y  = x
		x = num
		lista.append(num)
	return lista


vetor = []
ordem = int(input("Digite quantos valores de fibonacci deseja: "))
fibonacci(vetor,ordem)
print(vetor)