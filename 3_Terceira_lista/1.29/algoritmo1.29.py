#algoritmo 1.29 CC
s=0
n=int(input("Digite um valor: "))
numerador=1
soma1=0
soma2=0
denominador=n
while denominador>1:
    s=numerador/denominador
    denominador=denominador-1
    numerador=numerador+1
    soma1=soma1+s
while denominador<n:
    s=denominador/numerador
    denominador=denominador+1
    numerador=numerador-1
    soma2=soma2+s
print(soma1+soma2)