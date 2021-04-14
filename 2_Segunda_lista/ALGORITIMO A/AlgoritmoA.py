print("1 para media, 2 para subtracao do maior pelo menor, 3 para multiplicao e 4 para divisao")
f = int(input("Digite a operacao desejada: "))
if f >= 5:
	print("ERROR. Digite valores validos")
else:
	n1 = float(input("Digite o primeiro valor: "))
	n2 = float(input("Digite o segundo valor: "))
	if f == 1:
		n3 = (n1+n2)/2
		print("Operacao media:",n3)
	elif f == 2:
		if n1 > n2:
			n3 = n1-n2
			print("A subtracao do maior pelo menor foi:", n3)
		elif n2 > n1:
			n3 = n2-n1
			print("A subtracao do maior pelo menor foi:", n3)
		else:
			print("Os dois sao iguais: zero")
	elif f == 3:
		n3 = n1*n2
		print("O produto entre os dois valores foi:", n3)
	elif f == 4:
		if n2 == 0:
			print("O denominador nao pode ser zero")
		elif n2 != 0:
			n3 = n1/n2
			print("O resultado foi:", n3)
