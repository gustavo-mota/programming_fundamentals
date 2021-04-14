string = str(input("Digite o nome sem espaços no fim: "))
sobre = []
novo_nome = []
for i in string:
    novo_nome.append(i)
x = len(novo_nome) - 1
while x > 0:
    if ord(novo_nome[x]) == 32:
        break
    else:
        if ord(novo_nome[x]) >= 97 and ord(novo_nome[x]) <= 122:
            novo_nome[x] = chr(ord(novo_nome[x]) - 32)
        sobre.append(novo_nome[x])
        novo_nome.pop()
        x -= 1
sobre.reverse( )
sobre.append(",")
for s in sobre:
    print(s,end="")
for i in novo_nome:
    print(i,end="")