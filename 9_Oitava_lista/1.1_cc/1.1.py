dados = []
soma_salario = 0
soma_filhos = 0
maior_salario = 0
contador = 0
while len(dados)<=20:
    pesquisa = {}
    pesquisa['salario'] = float(input("Digite o salário: "))
    pesquisa['idade'] = int(input("Digite sua idade: "))
    pesquisa['filhos'] = int(input("Digite o número de filhos: "))
    pesquisa['sexo'] = int(input('Digite o número correspondente ao sexo(1 para masculino, 2 feminino): '))
    if pesquisa['salario'] > maior_salario:
        maior_salario = pesquisa['salario']
    soma_salario += pesquisa['salario']
    soma_filhos += pesquisa['filhos']
    if pesquisa['sexo'] == 2 and pesquisa['salario'] >=10000:
        contador += 1
    dados.append(pesquisa)
media_salario = soma_salario/20
media_filhos = soma_filhos/20
print("Média salarial é de: ",media_salario,"\n","Média de filhos: ",media_filhos,"\n","Maior salário: ",
      maior_salario,"\n","Mulheres que ganham mais que dez mil(contabilizado apenas as que registraram corretamente): ", contador)
