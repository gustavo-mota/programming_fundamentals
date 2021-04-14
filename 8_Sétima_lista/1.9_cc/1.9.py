senha = input("Digite a senha: ")
if len(senha) <8 or len(senha)>15:
    print("Erro. Tamanho inválido.")
else:
    lista_senha = []
    for a in senha:
        lista_senha.append(ord(a))
    print(lista_senha)
    ascii_minusculas = [97,98,99,100,101,102,103,104,105,106,107,108,109,110,111,112,113,114,115,116,117,118,119,120,121,122]
    ascii_maiusculas = [65,66,67,68,69,70,71,72,73,74,75,76,77,78,79,80,81,82,83,84,85,86,87,88,89,90]
    numeros = [48,49,50,51,52,53,54,55,56,57]
    minus_válida = False
    mai_válida = False
    digi_válida = False
    for i in lista_senha:
        for maiuscula in ascii_maiusculas:
            if i == maiuscula:
                mai_válida = True
        for minuscula in ascii_minusculas:
            if i==minuscula:
                minus_válida = True
        for numeral in numeros:
            if i ==numeral:
                digi_válida = True
    if minus_válida and mai_válida and digi_válida:
                print("Senha válida.")
    else:
        print("Senha inválida.")