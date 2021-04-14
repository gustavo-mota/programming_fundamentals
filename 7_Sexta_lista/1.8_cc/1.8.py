def fibo(ordem):
	x = 1
	y = 1
	i = 1
	while i<= ordem-2:
		num = x + y
		y = x
		x = num
		i = i + 1
	return num



ordem = int(input("Digite qual o n-nésimo valor de fibonacci : "))
numero = fibo(ordem)
print(numero)