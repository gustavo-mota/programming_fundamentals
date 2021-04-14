#algoritmo 1.21 CC
a=int(input("Digite um valor: "))
b=int(input("digite um segundo valor: "))
i=1
while i<=a and i<=b:
    if a%i==0 and b%1==0:
        mdc=i
    i=i+1
print(i-1)