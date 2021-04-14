produtos = []
produtos_orden = []
while len(produtos) <10:
    registro = {}
    registro['código'] = int(input("Digite o código: "))
    registro['descrição'] = str(input("digite a descrição: "))
    registro['valor'] = float(input("Digite o valor: "))
    registro['quantidade']  =int(input("Digite a quantidade: "))
    produtos.append(registro)
produ_cop = produtos[:]
for p in produtos:
    maior = p['código']
    for k in produ_cop: #descobre o maior
        if maior < k['código']:
            maior = k['código']
    for s in produ_cop:
        if maior == s['código']:
            produtos_orden.append(s)
            produ_cop.remove(s)
x = produ_cop[0] #tinha um problema que o ultimo ficava esquecido, isso é pra conssertar
produtos_orden.append(x)
produtos_orden.reverse() #antes era crescente a orden, agora não mais
print(produtos_orden)