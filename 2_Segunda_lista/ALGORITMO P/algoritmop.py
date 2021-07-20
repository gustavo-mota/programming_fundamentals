#Algoritmo item P
a = int(input("Digite o primeiro valor: "))
b = int(input("Digite o segundo valor: "))
c = int(input("Digite o terceiro valor: "))
if a==b==c or b==c or a==c or a==b:
    print("Nao e triangulo retangulo.")
elif (b-c)< a < (b+c) and (a-c)<b<(a+c) and (a-b)<c<(a+b):
    if a>=b>=c or a>=c>=b:
        if a**2 == b**2 + c**2:
            print("eh triangulo retangulo")
    elif b>=c>=a or b>=a>c :
        if b**2 == a**2+c**2:
            print("Eh triangulo retangulo.")
    elif c>=a>=b or c>=b>=a:
        if c**2 == a**2 + b**2:
            print("Eh um triangulo retangulo")
    else:
        print("Nao e triangulo retangulo")
else:
    print("Nao e triangulo")
