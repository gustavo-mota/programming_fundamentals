#Algoritmo item O
#Gustavo Antonio Sousa Paz E Mota
a = float(input("Digite um valor: "))
b = float(input("Digite outro valor: "))
c = float(input("Digite mais outro valor: "))
if (b-c)< a < (b+c) and (a-c)<b<(a+c) and (a-b)<c<(a+b):
    if a**2>b**2+c**2 or b**2>a**2+c**2 or c**2>b**2+a**2:
        print("Obtuso")
    elif a**2<b**2+c**2 or b**2<a**2+c**2 or c**2<b**2+a**2:
        print("Acutângulo")
    else:
       print("Triângulo retângulo.")
else:
    print("Nao e o caso de os valores digitados pertencerem aos lados de um triangulo.")