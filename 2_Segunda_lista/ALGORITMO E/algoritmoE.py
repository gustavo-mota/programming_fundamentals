#Algoritmo item E
#Gustavo antonio sousa Paz e Mota
investimento = float(input("Digite o valor do investimento: "))
tipo = str(input("Digite o tipo de investimento(P para poupança e F para fundo de renda fixa):"))
if tipo == "P":
    investimento = (investimento*0.1)+investimento
    print("Valor corrigido:", investimento)
elif tipo == "F":
    investimento = (investimento*0.15)+investimento
    print("Valor corrigido:", investimento)
else:
    print("Digite corretamente qual o tipo de investimento.")