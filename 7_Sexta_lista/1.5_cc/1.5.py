def multiplica(numero, multi):
    if numero < 0: #para que a multiplicação funcione, ambos valores devem ser positivos.
        numero = numero * -1
    if multi < 0: # esse if e o anterior asseguram que os valores sejam como requisitado
        multi = multi * -1
    if multi == 0 or numero == 0: #A partir desse if, a multiplicação será determinada
        resultado = 0
    elif multi == 1:
        resultado = numero
    elif numero == 1:
        resultado = multi
    else:
        vezes = 0
        while multi != 1: #descobrir quantos incremento será
            multi -= 1
            vezes = vezes + numero
        for i in range(0, vezes):
            numero = numero + 1
        resultado = numero
    return resultado


def sinal(valor1, valor2, result):
    if valor1 < 0 and valor2 > 0:
        result = result * -1
    elif valor1 > 0 and valor2 < 0:
        result = result * -1
    return result


num = int(input("digite um numero: "))
multiplicador = int(input("digite outro numero: "))
multiplicacao = multiplica(num, multiplicador)
produto = sinal(num, multiplicador, multiplicacao)
print(produto)
