#algortimo 1.2 CC
continua=True
produto=1
while (continua):
    n = int(input("Digite um algarismo(Digite zero se quiser parar): "))
    if n==0:
        continua=False
    else:
        produto = produto*n
print(produto)