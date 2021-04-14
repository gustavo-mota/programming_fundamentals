A = int(input("Digite a quantidade de alunos:"))
P = int(input("Digite a quantidade de provas:"))
alunos = range(1, A+1)
provas = range(1, P+1)
pesos = []
somaAritProvas = []
somaNotas = 0
somaPesos = 0
indicadorProva = 1
for i in range (len(provas)):
    somaAritProvas.append(0)
    aux = int(input("Digite o peso de cada prova respectivamente:"))
    pesos.append(aux)
    somaPesos += pesos[i]
for j in alunos:
    notas = []
    somaNotas = 0
    for k in range (len(provas)):
        nota = float(input("Digita uma nota:"))
        notas.append(nota)
        somaNotas += notas[k]*pesos[k]
        somaAritProvas[k] = somaAritProvas[k] + nota 
    print("A media ponderada do", j, "aluno foi:", (somaNotas/somaPesos))
for l in range(len(provas)):
    print("A média aritmética da classe na prova",indicadorProva ,  "foi:", somaAritProvas[l]/len(provas))
    indicadorProva += 1


        
        
    
    
