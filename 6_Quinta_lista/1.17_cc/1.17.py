matriz=[ [0,0,0],[0,0,0],[0,0,0] ]
matrix=[ [0,0,0],[0,0,0],[0,0,0] ]
matric=[ [0,0,0],[0,0,0],[0,0,0] ]

for i in range(0,3):
	for j in range(0,3):
		matriz[i][j]=int(input("Digite o valor do elemento: "))
		if i==0:
			matrix[j][i+2] = matriz[i][j]
		if i==1:
			matrix[j][i] = matriz[i][j]
		if i==2:
			matrix[j][i-2] = matriz[i][j]


for t in range(0,3):
	for u in range(0,3):
		if t==0:
			matric[u][t+2] = matrix[t][u]
		if t==1:
			matric[u][t] = matrix[t][u]
		if t==2:
			matric[u][t-2] = matrix[t][u]


for s in range(0,3):
	for r in range(0,3):
		print(matric[s][r], end=" ")
	print("\n")

