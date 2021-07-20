#Algoritmo item C
salario = float(input("Digite o valor do salario: "))
vendas = float(input("Digite o valor da vendas: "))
comissao = vendas*0.04
salario_final = comissao+salario
print("A comissao eh:", comissao)
print("O salario a pagar eh:", salario_final)