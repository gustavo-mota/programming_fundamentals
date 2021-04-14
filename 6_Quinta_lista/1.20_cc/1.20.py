CR_alto = 0

#Criação das Matrizes
matriz = [0]*3
matriz_linhas_alunas = [0]
for j in range(3):
    matriz[j] = [0]*4

#Preenchimento da Matriz
for i in range(3):
    matriz[i][0] = int(input("Digite a matrícula da pessoa %d: " %i))
    matriz[i][1] = int(input("Digite o sexo da pessoa %d (0: Feminino 1: Masculino): " %i))
    matriz[i][2] = int(input("Digite o código do curso da pessoa %d: " %i))
    matriz[i][3] = int(input("Digite o CR da pessoa %d: " %i))
#Recebe o codigo do curso
cod_curso = int(input("Digite o codigo do curso: "))

for i in range(3):
#Verifica as linhas que possuem o mesmo código do curso
    if (matriz[i][2] == cod_curso):
#Verifica se o Sexo da pessoa é Feminino
        if(matriz[i][1] == 0):
#Verifica se o CR dessa pessoa é o maior, se for maior substitui o valor na lista, se for igual so acrescenta
            if(matriz[i][3] > CR_alto):
                CR_alto = matriz[i][3]
                matriz_linhas_alunas[0] = i
            elif(matriz[i][3] == CR_alto):
                CR_alto = matriz[i][3]
                matriz_linhas_alunas.append(i)
#Se não existir nenhum valor na lista, nenhuma menina atende ao requisito para ser sorteada
if len(matriz_linhas_alunas) == 0:
    print("Nenhuma aluna possui o requisito")
#Se existir, printa os valores de acordo com a linha guardada na list
else:
    print("Aluna(s) Vencedora(s): ")
    for linha in matriz_linhas_alunas:
        print("Matrícula da Aluna: %d" %matriz[linha][0])
        print("CR da Aluna: %d" %matriz[linha][3])
