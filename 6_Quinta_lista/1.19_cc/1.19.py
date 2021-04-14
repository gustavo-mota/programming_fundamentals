matriz = [ [0,0,0,0],[0,0,0,0],[0,0,0,0],[0,0,0,0],[0,0,0,0],[0,0,0,0],[0,0,0,0],[0,0,0,0],[0,0,0,0],[0,0,0,0],[0,0,0,0],[0,0,0,0] ]
sm = 0
ss = 0
st = 0
for i in range(0,12):
    for j in range(0,4):
        matriz[i][j] = int(input("Digite o valor da venda: "))
        st = st + matriz[i][j]

for mês in range(0,12):
    for s in range(0,4):
        sm = sm+matriz[mês][s]
    print("Mês ",mês," vendas: ",sm)
    sm = 0
print("\n")
for semana in range(0,4):
    for r in range(0,12):
        ss = ss+matriz[r][semana]
    print("Semana ",semana," vendeu: ",ss)
print("\n")
print("Total de vendas: ",st)