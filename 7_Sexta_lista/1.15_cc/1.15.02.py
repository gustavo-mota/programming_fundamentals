def teste(termo):
    letras = [ "a",'b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']
    numero = [1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,25,26]
    palavra_original = []
    palavra_invertida = []
    for i in range(0,len(termo)):
        for s in range(0,len(letras)):
            if palavra[i] == letras[s]:
                y = numero[s]
                palavra_original.append(y)

    palavra_original.reverse()
    palavra_invertida = palavra_original[:]
    palavra_original.reverse()

    poli = True

    for b in range(0,len(palavra_original)):
        if palavra_original[b]!=palavra_invertida[b]:
            poli=False
    return poli

palavra = str(input("Digite a palavra sem acentuação e entre aspas, todas minusculas: "))
vero = False
vero = teste(palavra)
if vero==True:
    print("Ela é palíndromo.")
elif vero==False:
    print("Ela não é palíndromo.")