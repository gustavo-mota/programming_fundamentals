#algoritmo item L
#Gustavo Antonio Sousa Paz E Mota
horas = int(input("Digite o numero de horas trabalhadas: "))
salario = float(input("DIgite o valor do slario minimo vigente: "))
horas2 = int(input("Digite o numero de horas extras trabalhadas: "))
salario_bruto = (0.125*salario)*horas
het = (0.25*salario)*horas2 #horas extras rendimento
salario_final = salario_bruto+het
print("Salario a pagar: ", salario_final)