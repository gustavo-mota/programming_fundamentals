def multiplica(multiplicado, multiplicador):
	i = 1
	resultado = multiplicado
	while i < multiplicador:
		resultado = resultado + multiplicado
		i = i + 1
	return resultado
num = int(input("Digite um número: "))
multi = int(input("Digite o outro: "))
produto = multiplica(num, multi)
print(produto)
