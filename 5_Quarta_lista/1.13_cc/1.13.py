nomes = ""
ant = 0
nov = 0
y = 0
x = 0
continua = 1
lista = []
print ("Para finalizar a eleicao digite Fim")
while continua == 1:
	nomes = input("Digite o nome do canditado que quer eleger: ")
	if nomes == 'Fim' or nomes == 'fim':
		continua = 0
	else:
		lista.append(nomes)
		
for i in range(0,len(lista)):	
	ant = nov
	nov = lista[i]
	if ant != nov:
		y = x
		x = (lista.count(nov))
		print ("Numero de votacoes no",nov,":",x)
		if x > y:
			campeao = nov
print (campeao,"venceu a eleicao")
		
		
