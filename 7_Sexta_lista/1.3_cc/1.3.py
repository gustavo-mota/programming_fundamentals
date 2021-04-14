def somatorio(numero,soma):
	i = 1
	while i <=soma:
		numero = numero + 1
		i = i +1
	return numero
num = int(input("Digite um número: "))
somador = int(input("Digite um número: "))
soma = somatorio(num, somador)
print(soma)
