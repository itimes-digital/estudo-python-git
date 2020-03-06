minha_lista = [1, 3, 5, 7, 9]

def pesquisa_binaria(lista, item):
	baixo = 0
	alto = len(lista) - 1
	item = abs(item)
	count = 1;
	while baixo <= alto:
		print("Passos : " + str(count))
		meio = str(((baixo + alto) / 2))
		meio = int(meio[:meio.index(".")])
		chute = lista[meio]
		if chute == item:
			return meio
		if chute > item:
			alto = meio - 1
		else:
			baixo = meio + 1
		count += 1
	return None


print("posição : " + str(pesquisa_binaria(minha_lista, 9)))
print('\n')
print("posição : " + str(pesquisa_binaria(minha_lista, -2)))


