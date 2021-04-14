#algoritmo 1.18 CC
a=int(input('digite um valor: '))
b=int(input("digite outro valor: "))
j=2
primos=True
while j<a or j<b:
    if a%j==0 and b%j==0:
        primos=False
    j=j+1
if primos==True:
    print("São primos entre si.")
else:
    print("Não são primos entre si.")