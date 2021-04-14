def converter(x,lista):
    while x != 0:
        y = int(x % 2)
        x = int(x/2)
        lista.append(y)
    lista.reverse()
    return lista

n = int(input("Digite um numero: "))
binario=[]
converter(n,binario)
print(binario)