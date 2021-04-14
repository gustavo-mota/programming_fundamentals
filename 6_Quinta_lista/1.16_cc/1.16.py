matriz=[ [0,0,0], [0,0,0],[0,0,0] ]
matrix=[ [0,0,0], [0,0,0],[0,0,0] ]

for i in range(0,3):
	for j in range(0,3):
		matriz[i][j] = int(input("Insira o valor do elemento: "))
		if i==0:
			matrix[j][i+2] = matriz[i][j]
		elif i==1:
			matrix[j][i] = matriz[i][j]
		elif i==2:
			matrix[j][i-2] = matriz[i][j]

for s in range(0,3):
	for r in range(0,3):
		print(matrix[s][r], end=" ")
	print("\n")
