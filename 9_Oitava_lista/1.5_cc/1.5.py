estilista = []
estação_climática = []
roupa = []
while len(estilista) <5:
    registtroA = {}
    registroA['código'] = int(input("Digite o código do estilista: "))
    registroA['nome'] = str(input("Digite o nome do estilista: "))
    registtroA['salario'] = float(input("Digite o salário: "))
    estilista.append(registtroA)
while len(estação_climática)<4:
    registroB = {}
    registroB['código'] = int(input("Digite o código da estação: "))
    registroB['nome'] = str(input("digit eo nome da estação: "))
    estação_climática.append(registroB)
while len(roupa)<10:
    registroC = {}
    registroC['código'] = int(input("Digite o código da roupa: "))
    registroC['descrição'] = str(input("Digite a descrição da roupa: "))
    registroC['códigoE'] = int(input("Digite o código do estilista: "))
    registroC['códigoEs'] = int(input("Digite o código da estação: "))
    registroC['ano'] = int(input("Digite o ano: "))
    roupa.append(registroC)
Codigo = int(input("Digite o código da estação: "))
for p in roupa:
    if p['códigoEs'] == Codigo:
        print(p)
        for h in estilista:
            if h['código'] == p['códigoE']:
                print(h)