propinas = []
proprinas_repetidas = []
x = int(input("Deseja inserir pagamento(0: Não. Qualquer numero: Sim)?"))
if x!=0:
    propina = {}
    propina['nome'] = str(input("Insira o nome do sujeito: "))
    propina['data'] = str(input("Insira a data: "))
    propina['descrição'] = str(input("Insira a descrição: "))
    propina['partido'] = str(input('Insira o nome do partido: '))
    propina['pagamento'] = float(input("Insira o valor da propina: "))
    propinas.append(propina)
x = int(input("Deseja inserir pagamento(0: Não. Qualquer numero: Sim)?"))
while x!=0:
    propina = {}
    propina['nome'] = str(input("Insira o nome do sujeito: "))
    propina['data'] = str(input("Insira a data: "))
    propina['descrição'] = str(input("Insira a descrição: "))
    partido = str(input('Insira o nome do partido: '))
    n_existe = True
    for p in propinas:
        if p['partido'] == partido:
            n_existe = False
            pagamento = float(input("Insira o pagamento: "))
            p['pagamento'] += pagamento
            propina['partido'] = partido
            propina['pagamento'] = pagamento
            proprinas_repetidas.append(propina)
    if n_existe:
        propina['partido'] = partido
        propina['pagamento'] = float(input("Insira o pagamento: "))
        propinas.append(propina)
    x = int(input("Deseja inserir pagamento(0: Não. Qualquer numero: Sim)?"))
maior = 0
for s in propinas:
    if s['pagamento'] >maior:
        maior = s['pagamento']
print(maior)
print(propinas)
for x in propinas:
    if x['pagamento'] == maior:
        print('MAior receptor:',x)