string = str(input("Digite: "))
letra = str(input("Digite a letra: "))
L1 = letra
if ord(letra)>=97 and ord(letra)<=122:
    L2 = chr(ord(letra)-32)
elif ord(letra)>= 65 and ord(letra)<=90:
    L2 = chr(ord(letra)+32)
else:
    print("Erro.")
strings = []
for i in string:
    strings.append(i)
for s in strings:
    if s == L1:
        strings.remove(s)
    elif s == L2:
        strings.remove(s)
for n in strings:
    print(n,end="")

