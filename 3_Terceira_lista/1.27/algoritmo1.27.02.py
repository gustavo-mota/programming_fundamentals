#algoritmo 1.27
n=int(input("Digite um valor: "))
h=0
denominador=1
while denominador<=n:
    h=h+1/denominador
    denominador=denominador+1

print(h)