ant = 10000
nov = 10000
continua = 1
lista = []
lista2 = []
print ("Digite um valor maior que 1000 para sair da selecao dos elementos da lista")
while continua==1:
	n = int(input("Digite um valor n: "))	
	if n>=1000:
		lista.sort()
		continua = 0
	else:
		lista += [n]
			
		
print ("Aqui esta a lista: ",lista)
for i in range(0,len(lista)):	
	ant = nov
	nov = lista[i]
	if ant != nov:
		x = (lista.count(nov))
		if x != 1:
			print ("Repeticoes do numero",nov,":",x)
		lista2 += [nov]  
print ("Aqui esta a lista sem repeticoes:", lista2)





