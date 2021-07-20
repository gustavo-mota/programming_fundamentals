#algoritmo item n
a = float(input("Digite um valor: "))
b = float(input("Digite um valor: "))
c = float(input("Digite um valor"))
if (b-c)< a < (b+c) and (a-c)<b<(a+c) and (a-b)<c<(a+b):
    if a==b==c:
        print('Triangulo equilatero')
    elif a==b!=c or b==c!=a or a==c!=b:
        print("Triangulo isosceles")
    else:
        ("Triangulo escaleno.")
else:
    print("nao e um triangulo.")