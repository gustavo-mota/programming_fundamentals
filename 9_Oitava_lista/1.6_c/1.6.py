print("1- Cadastrar tombo,\n,"
      "2- Cadastrar obra,\n"
      "3- Pesquisar por ano,\n"
      "4- Pesquisar por autor,\n"
      "5- Pesquisar por editora,\n"
      "6- Encerrar.")
operação=0
while operação!=6:
    obras = []
    tombos =[]
    operação = int(input("Digite qual operação deseja: "))
    if operação >6:
        print("Erro. Comando inválido.")
    elif operação <0:
        print("Erro. Comando inválido.")
    elif operação==1:  #registrar tombo
        if len(tombos)==20:
            print("Tamanho excedido.") #Existem apenas 20
        else:
            tombo ={}
            tombo['numero']=int(input("Digite o número do tombo: "))
            tombo['nome'] = str(input("Digite o nome da obra: ")) #tamanho máximo de obrars 3
            tombo['autor'] = str(input("Digite o nome do autor: "))
            tombo['editora']= str(input("Digite o nome da eidtora: "))
            tombo['ano'] = int(input("Digite o ano: "))
            tombos.append(tombo)
    elif operação==2:
        obra = {}
        obra['numero'] = int(input("Digite o número do tombo: ")) #máximo de 3 obras por tombo
        obra['exemplar'] = int(input("Digite o número do exemplar: "))
        obra['data'] = str(input("Digite a data de comprad : "))
        obras.append(obra)
    elif operação==3:
        ano = int(input("Digite  o ano: "))
        achado = False
        for h in tombos:
            if h['ano'] == ano:
                achado = True
                c = h['numero']
                for j in obras:
                    if c == j['numero']:
                        print(j)
        if achado == False:
            print("Obra não encontrada.")
    elif operação==4:
        autor = str(input("Digite o nome do autor: "))
        achado = False
        for p in tombos:
            if p['autor'] == autor:
                achado = True
                x = p['numero']
                for q in obras:
                    if x == q['numero']:
                        print(q)
        if achado == False:
            print("Autor não encontrado.")
    elif operação==5:
        editora = str(input("Digite a editora que quer pesquisar: "))
        achado = False
        for d in tombos:
            if d['editora'] == editora:
                achado = True
                w = d['numero']
                for u in obras:
                    if w == u['numero']:
                        print(u)
        if achado == False:
            print("Editora não achada.")