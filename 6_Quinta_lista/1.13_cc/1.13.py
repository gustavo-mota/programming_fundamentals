n = int(input("digite um valor: ")) #dimensões
if n>10 or n<0: #Verifica condições de existência baseado em n
    print("Error")
else:
    simetrica = True
    Matriz = []
    Transposta = []
    #Gerador da matriz
    for s in range(0,n):
        Matriz.append([])
        Transposta.append([])
    #Inclusão dos elementos da matriz linha por linha
    for i in range(0,n):
        for j in range(0,n):
            x = int(input("Digite o valor: "))
            Matriz[i].append(x)
            transposta[i].append(0) #A transposta no momento só possuirá zeros
    #Preenchimento da transposta
    for h in range(0,n):
        for w in range(0,n):
            Transposta[w][h] = Matriz[h][w]
    #comparação entre matriz e transposta dirá se é ou não simétrica
    for r in range(0,n):
        for f in range(0,n):
            if Matriz[r][f] != Transposta[r][f]:
                simetrica = False
    #Vereficação final:
    if simetrica == True:
        print("Simétrica")
    else:
        print("Não simétrica.")
