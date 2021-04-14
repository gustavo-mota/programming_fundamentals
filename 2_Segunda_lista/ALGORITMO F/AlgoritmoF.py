#Algoritmo item F
#Gustavo Antonio Sousa Paz E Mota
altura = float(input("Digite sua altura: "))
sexo = str(input("Digite seu gênero (H para homem e M para mulher, letras maicúsculas): "))
if sexo == "H":
    pesoideal = (72.7*altura)-58
    print("Seu peso ideal eh", pesoideal)
elif sexo == "M":
    pesoideal = (62.1*altura)-44.7
    print("Seu peso ideal eh:", pesoideal)
else:
    print("Caractere inválido.")