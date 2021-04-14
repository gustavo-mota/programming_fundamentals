import math
continua = 1
lista = []
x = 0
y = 0
print ("Digite um valor quebrado para sair da selecao de elementos")
while continua==1:
	n = float(input("Digite um valor n: "))	
	if n>int(n):
		continua = 0
	else:
		lista += [n]
for i in range(0,len(lista)):
	x = x + lista[i]	
media = x/len(lista)
for i in range(0,len(lista)):
	y = y + ((lista[i]-media)**2)
variancia = y/len(lista)
desviopadrao = math.sqrt(variancia) 
print("Aqui esta sua lista",lista)
print("Aqui esta a media da lista: ",media)
print("Aqui esta a variancia da lista: ",variancia)
print("Aqui esta o desvio padrao da lista: ",desviopadrao)
	

