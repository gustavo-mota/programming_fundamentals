import math
a = float(input("Digite a cordenada x do centro: "))
b = float(input("Digite a cordenada y do centro: "))
centro = [a,b] 
ponto = []
todos_pontos = []
raio_lista = []
raio_lista2 = []
ant = 0
nov = 0
n = int(input("Escolha as cordenadas de 2 a 99 pontos: "))
if 1 < n < 99:
	for i in range(1,n+1):
		x = float(input("Digite a cordenada x do ponto: "))
		y = float(input("Digite a cordenada y do ponto: "))
		ponto = [x,y]
		todos_pontos.append(ponto)
		raio = math.sqrt(((x-a)**2) + ((y-b)**2))
		raio_lista.append (raio) 
else:
	print ("Numero invalido")
raio_lista.sort()
for i in range(0,len(raio_lista)):	
	ant = nov
	nov = raio_lista[i]
	if ant != nov:
		x = (raio_lista.count(nov))
		raio_lista2.append (nov)
		 
print ("Cordenadas do centro",centro)
print ("Cordenadas dos pontos",todos_pontos)
print ("Possiveis raios: ",raio_lista2)


