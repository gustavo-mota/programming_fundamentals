string = str(input("Digite a palavra: "))
nova_palavra = []
for i in string:
    if ord(i)>=65 and ord(i)<=90:
        nova_palavra.append(chr(ord(i)+32))
    elif ord(i)>=97 and ord(i)<=122:
        nova_palavra.append(chr(ord(i)-32))
    else:
        nova_palavra.append(i)
for s in nova_palavra:
    print(s,end="")