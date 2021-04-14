contas = []
x = 7
while x!=0:
    print("1-)Crédito\n2-)Débito\n3-)transferir\n4-)Consultar saldo\n5-)Criar conta\n6-)Remover conta")
    x = int(input(">>> "))
    if x==1: #Crédito OK
        numero = str(input("Insira o número da conta a ter valor creditado: "))
        if len(contas) == 0:
            print("Conta não encontrada")
        else:
            existe = False
            for y in contas:
                if y['numero'] == numero:
                    existe = True
                    print("Conta encontrada!")
                    credito = float(input("insira o valor a ser adicionado: "))
                    y['valor'] += credito
            if existe ==  False:
                print("Conta não encontrada")
    elif x==2: #Debitar OK
        numero = str(input("Insira o número da conta a ter valor creditado: "))
        if len(contas) == 0:
            print("Conta não encontrada")
        else:
            existe = False
            for z in contas:
                if z['numero'] == numero:
                    existe = True
                    print('COnta encontrada')
                    debito = float(input("Insira o valor a retirar: "))
                    if z['valor'] < debito:
                        print("Saldo insuficiente")
                    else:
                        z['valor'] -= debito
            if existe == False:
                print("COnta não encontrada")
    elif x==3:
        if len(contas) <2:
            print("Não há contas salvas para a operação")
        else:
            numero1 = str(input("Insira a conta para se ter valor extraido: "))
            existe = False
            for cc in contas:
                if cc['numero'] == numero1:
                    existe = True
                    remover = float(input('Insira o valor a ser extraído: '))
                    if cc['valor'] < remover:
                        print("Saldo insuficiente")
                    else: #não sabe se a conta dois existe, mas se não existir, lá na frente, se concerta
                        cc['valor'] -= remover
            if existe:
                numero2 = str(input("insira a conta para se ter valor transferido: "))
                existe = False
                for k in contas:
                    if k['numero'] == numero2:
                        existe = True
                        print("COnta encontrada")
                        k['valor'] += remover
                if existe == False:
                    print("COnta não encontrada")
                    for e in contas:
                        if e['numero'] == numero1:
                            e['valor'] += remover
            else:
                print("Conta não encontrada")
    elif x==4: #Print conta OK
        numero = str(input("Insira o número da conta para verficar o saldo: "))
        if len(contas)==0:
            print("Não há contas salvas!")
        else:
            existe = False
            for m in contas:
                if m['numero'] == numero:
                    existe = True
                    print("Conta encontrada!")
                    print(m)
            if existe==False:
                print("Conta não encontrada")
    elif x==5: #Criar conta OK #Problema: Crise de chaves
        conta = {}
        numero = str(input("Insira o número da conta a adicionar: "))
        if len(contas) == 0: #Vetor contas vazio: primeira conta cria
            conta['numero'] = numero
            conta['valor'] = 0
            contas.append(conta)
            print("Conta criada!")
        else:
            existe = False
            for p in contas:
                if p['numero'] == numero:
                    existe = True
            if existe:
                print("Número de conta já existente.")
            else: #A conta de fato não existe
                conta['numero'] = numero
                conta['valor'] = 0
                contas.append(conta)
                print("Conta criada!")
    elif x==6: #Remover conta
        numero = str(input("Insira o número da conta a ser removida: "))
        if len(contas)==0:
            print("Não há contas")
        else:
            existe = False #Problema: vetor vazio
            for h in contas:
                if h['numero'] == numero:
                    existe = True
                    contas.remove(h)
                    print("Conta apagada com suceso.")
            if existe==False:
                print("Conta não encontrada")
    else:
        print("Operação inválida.")
    x = int(input("Deseja continuar(0: não. Qualquer número: sim."))