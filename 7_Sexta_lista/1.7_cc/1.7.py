def combinar(lista):
	for i in range(51,61):
		for j in range(41,51):
			for k in range(31,41):
				for l in range(21,31):
					for m in range(11,21):
						for n in range(1,11):
							x = [[i],[j],[k],[l],[m],[n]]
							lista.append(x)
	return lista


combinacoes = []
combinar(combinacoes)
print(combinacoes)