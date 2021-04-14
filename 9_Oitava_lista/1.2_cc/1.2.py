n = int(input("Digite quantos serviços deseja analisar: "))
serviços = []
indice = 0
soma_v = 0
maior = 0

while len(serviços) <n:
    registro = {}
    registro['os'] = int(input("Digite o número do serviço: "))
    registro['data'] = str(input("Digite a data: "))
    registro['valor'] = float(input("Digite o valor: "))
    registro['descrição'] = str(input("Digite a descrição: "))
    registro['nome'] = str(input("Digite o nome do cliente: "))
    soma_v += registro['valor']
    if maior < registro['valor']:
        maior = registro['valor']
        indice = len(serviços)
    serviços.append(registro)
media = soma_v/n
print("Média: ",media,
      "\n")
for p in serviços:
    if p['valor'] == maior:
        print("Data: ",p['data'],"Cliente: ",p['nome'],"Descrição: ",p['descrição'])