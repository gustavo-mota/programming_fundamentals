#Algoritmo item G
#Gustavo Antonio Sousa Paz E Mota
idade = int(input("Qual a sua idade? Digite: "))
if 5<= idade <= 7:
    print("Categoria Infanto")
elif 8 <= idade <= 10:
    print("Categoria Infanto-Juvenil")
elif 11<=idade<=15:
    print("Categoria Juvenil")
elif 16<=idade<=30:
    print("Categoria Adulto")
elif idade>30:
    print("Categoria Master")
else:
    print("Idade inválida.Idades aceitaveis apenas a maiores ou iguais a cinco anos.")