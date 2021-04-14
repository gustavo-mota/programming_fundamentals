#algoritmo item H
#Gustavo Antonio Sousa Paz E Mota
x = int(input("Digite o valor que queira achar tabuada: "))
y = x*10
i = 0
lista = []
h = 0
while h != y:
    h = x*i
    i = i + 1
    lista.append(h)

print(lista)