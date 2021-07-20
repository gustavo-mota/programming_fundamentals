#Algoritmo item B

salario = float(input("Digite o salario: "))
if salario > 900:
	print("Nao tera aumento")
else:
	salario = (salario*0.3)+salario
	print("Salario com reajuste:", salario)
