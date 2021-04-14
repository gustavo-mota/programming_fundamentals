#algoritmo item M
#Gustavo Antonio Sousa Paz E Mota
a = float(input("Digite um valor: "))
b = float(input("Digite outro valor: "))
c = float(input("Digite mais outro valor: "))
if (b-c)< a < (b+c) and (a-c)<b<(a+c) and (a-b)<c<(a+b):
    print("Os valores digitados podem pertencer a um triangulo.")
else:
    print("Nao e o caso de os valores digitados pertencerem aos lados de um triangulo.")