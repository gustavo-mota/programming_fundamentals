#algoritmo 1.05 sem uso de lista: CC
continua=True
maior=1
p=1
n = int(input("Digite um valor para o comparativo(digite zero se desejar parar): "))
while (continua):
    if n==0:
        continua=False
        print(maior)
    else:
        if p>n:
            maior=p
        else:
            maior=n
        p=n
        n=int(input("Digite um valor para o comparativo: "))

#print("Maior valor:", max(lista))
#maior =2, p=2,n=2// n=3,maior=3,p=3//n=1,