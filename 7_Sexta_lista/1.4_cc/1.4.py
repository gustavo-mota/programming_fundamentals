def multiplica(numero,multi):
	if multi == 0:
		resultado = 0
	elif multi == 1:
		resultado = numero
	else:
		vezes = 0
		while multi!=1:
			multi = multi - 1
			vezes = vezes + numero
		for i in range(0, vezes):
			numero = numero + 1
		resultado = numero
	return resultado

num = int(input("digite um número: "))
multiplicador = int(input("Digite outro número: "))
produto = multiplica(num, multiplicador)
print(produto)
