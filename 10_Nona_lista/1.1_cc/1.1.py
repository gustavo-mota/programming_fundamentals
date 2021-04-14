contas = {}
for i in range(0,3):
    conta = str(input("Insira o número da ocnta a ser criada: "))
    contas[conta] = 0
print(contas)
x = 6
while x!=0:
    print("1-)Crédito\n2-)Débito\n3-)transferir\n4-)Consultar saldo\n")
    x = int(input(">>> "))
    if x == 1:
        nome = str(input("Insira o número da conta: "))
        existe = False
        for p in contas: #Verifica existência da conta isnerida
            if p==nome:
                existe = True #Fim da verificação
        if existe: #Existe, efetua operação
            credita = float(input("Insira o valor a creditar: "))
            contas[nome] += credita
        else: #Não existe, notifica e encerra
            print("Conta não encontrada. Tente outra vez")

    elif x == 2:
        nome = str(input("Digite o número da conta para realizar débito: "))
        existe2 = False
        for q in contas:
            if q == nome:
                existe2 = True
        if existe2:
            debito = float(input("Insira o valor a debitar: "))
            if contas[nome] < debito:
                print("Desculpe. Saldo insuficiente para esse valor de débito. Tente outra hora")
            else:
                contas[nome] -= debito
        else:
            print("Conta não encontrada. Tente novamente")
    elif x==3:
        nome1 = str(input("Insira o numero da conta para se subtrair o valor: "))
        existe = False
        for s in contas:
            if s==nome1:
                existe = True
        if existe == False:
            print("Conta não encontrada. Tente outra hora.")
        else:
            nome2 = str(input("Insira o numero da conta que receberá o valor: "))
            if nome1==nome2:
                print("Mesma conta inserida. Operação inválida.")
            else:
                existe = True
                for h in contas:
                    if h == nome2:
                        existe = True
                if existe == False:
                    print("Conta não encontrada. Tente outro momento")
                else:
                    retira = float(input("insira o valor para subtrair: "))
                    if contas[nome1] < retira:
                        print("Saldo insuficiente. Tente outro instante")
                    else:
                        contas[nome1] -= retira
                        print(contas[nome1]) #descartar
                        contas[nome2] += retira #Soma de contas
    elif x == 4:
        nome = str(input('insira o número da conta para consultar saldo: '))
        existe = False
        for l in contas:
            if l == nome:
                existe = True
        if existe:
            print(contas[nome])
        else:
            print("Conta não encontrada. Tente com paciência")
    else:
        print("Função inválida. Tente noutra hora")
    x = int(input("Deseja continuar(0: não. Qualquer número: sim."))