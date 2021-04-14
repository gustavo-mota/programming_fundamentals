n=int(input("Digite quantos termos deseja na lista: "))
lista=[]
lista2=[]
if n>20:
    print("Error, o valor excede a quantidade mínima suportada.")
else:
    for i in range(1,n+1):
        x=int(input("Digite um valor para a sua lista: "))
        lista.append(x)
    k=int(input("Digite um indice: "))
    if k>n-1:
        print("Error, o índice é superior ao número de elementos da lista.")
    else:
        print(lista[k])
        for i in range(1,len(lista)):
            lista2.append(min(lista))
            lista.remove(min(lista))
        print(lista2[k])
        for i in range(1,len(lista2)):
            s=0
            vezes=0
            while s<len(lista2):
                if i==lista2[s]:
                     vezes=vezes+1
                s=s+1
            print("O número,",lista2[i],"repete",vezes,"vezes.")