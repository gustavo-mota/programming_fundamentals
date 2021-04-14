matriz = [ [0,0,0,0], [0,0,0,0], [0,0,0,0], [0,0,0,0] ]

for i in range(0,4):
	for j in range(0,4):
		matriz[i][j] = int(input("Digite o valor do elemento: "))
x = 3
y = 0

for s in range(0,4):
	for r in range(0,4):
		if s==y and r==x:
			del matriz[s][r]
	x=x-1
	y=y+1
	print("\n")

for h in range(0,4):
	print(matriz[h],"\n")