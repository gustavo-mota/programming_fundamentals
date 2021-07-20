#Algoritmo item L
print("Programa que testa se determinado numero e ou nao divisivel por um segundo numero")
n1 = int(input("Digite o primeiro valor: "))
n2 = int(input("Digite o segundo valor: "))
r = n1%n2
if r ==0:
	print("E divisivel")
else:
	print("Nao e divisivel")
