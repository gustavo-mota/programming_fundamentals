def dias(dataA, dataB):
    diaA = int(dataA[0])
    mesA = int(dataA[1])
    anoA = int(dataA[2])
    diaB = int(dataB[0])
    mesB = int(dataB[1])
    anoB = int(dataB[2])
    diass = (((mesB-mesA)*30)+diaB)-diaA + (365*(anoB-anoA))
    if diass >0:
        numero_dias = diass
    elif diass <0:
        numero_dias = 0
    return numero_dias

def juros(dias_passados,valor):
    valor_antigo = valor
    while dias_passados>0:
        valor = valor+((2*valor)/100)
        dias_passados -= 1
    juro = valor - valor_antigo
    return juro
soma =0
contas = []

while len(contas) <15:
    registro = {}
    regsitro['numero'] = int(input("Digit eo numero do documento: "))
    registro['codigo'] = int(input("Digite o código do cliente: "))
    registro['vencimento'] = str(input("Digite entre barras / a data de vencimento para não dar errado: "))
    registro['pagamento'] = str(input("Digite entre barras / a data de pagamento para não dar erro: "))
    registro['valor'] = float(input("Digite o valor: "))
    data1 = registro['pagamento'].split("/")
    data2 = registro['venciemnto'].split("/")
    di = dias(data2,data1)
    registro['juros'] = juros(di,registro['valor'])
    soma += registro['juros']
print("Arrecadado em juros, aproximadamente: ",soma)