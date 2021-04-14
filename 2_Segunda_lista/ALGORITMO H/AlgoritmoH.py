#Algoritmo item H
#Gustavo Antonio sousa Paz E mota
idade = int(input("Digite a sua idade: "))
peso  = float(input("Digite seu peso: "))
if idade <= 20:
    if peso<=60:
        print("Grupo de risco 9.")
    elif 60<peso<=90:
        print("Grupo de risco 8.")
    elif peso>90:
        print("Grupo de risco 7.")
elif 20<idade<=50:
    if peso <= 60:
        print("Grupo de risco 6.")
    elif 60 < peso <= 90:
        print("Grupo de risco 5.")
    elif peso > 90:
        print("Grupo de risco 4.")
elif idade>50:
    if peso <= 60:
        print("Grupo de risco 3.")
    elif 60 < peso <= 90:
        print("Grupo de risco 2.")
    elif peso > 90:
        print("Grupo de risco 1.")