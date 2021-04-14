contas = []
x = 7
while x!=0:
    print("1-)Crédito\n2-)Débito\n3-)transferir\n4-)Consultar saldo\n5-)Criar conta\n6-)Remover conta")
    x = int(input(">>> "))
    if x==1: #OK
        numero = str(input("Insira o número da conta: "))
        existe = False
        for p in contas: #Verifica existência da conta isnerida
            if p[0]==numero:
                existe = True #Fim da verificação
                credita = float(input("Insira o valor a creditar: "))
                p[1] += credita
        if existe==False: #Não existe, notifica e encerra
            print("Conta não encontrada. Tente outra vez")
    elif x==2: #OK
        numero = str(input("Digite o número da conta para realizar débito: "))
        existe = False
        for q in contas:
            if q[0] == numero:
                existe = True
                debito = float(input("Insira o valor a debitar: "))
                if q[1] < debito:
                    print("Desculpe. Saldo insuficiente para esse valor de débito. Tente outra hora")
                else:
                    q[1] -= debito
        if existe==False:
            print("Conta não encontrada. Tente novamente")
    elif x==3:
        numero1 = str(input("Insira o numero da conta para se subtrair o valor: "))
        existe = False
        for s in contas:
            if s[0] == numero1:
                existe = True
                numero2 = str(input("Insira o numero da conta que receberá o valor: "))
                if numero1 == numero2:
                    print("Mesma conta inserida. Operação inválida.")
                else:
                    existe = True
                    for h in contas:
                        if h[0] == numero2:
                            existe = True
                            retira = float(input("insira o valor para subtrair: "))
                            if s[1] < retira:
                                print("Saldo insuficiente. Tente outro instante")
                            else:
                                s[1] -= retira
                                h[1] += retira  # Soma de contas
                            '''if contas[nome1] < retira:
                                print("Saldo insuficiente. Tente outro instante")
                            else:
                                contas[nome1] -= retira
                                contas[nome2] += retira  # Soma de contas'''
                    if existe == False:
                        print("Conta não encontrada. Tente outro momento")
        if existe == False:
            print("Conta não encontrada. Tente outra hora.")
    elif x==4: #OK
        numero = str(input('insira o número da conta para consultar saldo: '))
        indice = 0
        existe = False
        for l in contas:
            if l[0] == numero:
                existe = True
                print(l)
        if existe==False:
            print("Conta não encontrada. Tente com paciência")
    elif x==5: #OK
        conta = []
        numero = str(input("Insira o número da conta a ser criada: "))
        existe = False
        for u in contas:
            if u[0] == numero:
                existe = True
        if existe:
            print("A conta já existe. Tente depois")
        else:
            conta.append(numero)
            saldo = 0
            conta.append(saldo)
            contas.append(conta)
    elif x==6: #OK
        numero = str(input("Insira o número da conta a ser removida: "))
        existe = False
        for f in contas:
            if f[0] == numero:
                existe = True
                contas.remove(f)
        if existe==False:
            print("Conta não encontrada. Tente no mais tardar")
    else:
        print("Função inválida. Tente noutra hora")
    x = int(input("Deseja continuar(0: não. Qualquer número: sim."))