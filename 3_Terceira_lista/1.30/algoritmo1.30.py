#algoritmo 1.30 CC
denominador=2
i=1
resultado=0
x=1
while i<=100:
    if i%2==0:
        x=x+(1/denominador)
        resultado=resultado+x
    else:
        x=x-(1/denominador)
        resultado=resultado+x
    i=i+1
    denominador=denominador+2
print("Resultado e:", x)