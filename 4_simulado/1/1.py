#Algoritmo 1
soma=0
cont=1
den=1
while cont<=20:
    i=1
    fat = 1
    while i<=cont:
        fat=fat*i
        i=i+1
    if cont%2==0:
        soma-=fat/den
    else:
        soma+=fat/den
    den=(den*2)+1
    cont+=1
print(soma)