import math

"""Lista ordenada para realizar busca binária,
obrigatoriamente a lista deve estar ordenada!"""
minha_lista = ['Aaron',
'Abel',
'Abelardo',
'Abigail',
'Abner',
'Abrahão',
'Abraão',
'Abrão',
'Abílio',
'Ada',
'Adalberto',
'Adalgisa',
'Adam',
'Adauto',
'Adela',
'Adelaide',
'Adelberto',
'Adelina',
'Ademar',
'Adhemar',
'Adolfo',
'Adolpho',
'Adoniram',
'Adrian',
'Adriana',
'Adriane',
'Adrianne',
'Adriano',
'Adriel',
'Adriene',
'Adrienne',
'Adão',
'Adèle',
'Adélia',
'Adônis',
'Afif',
'Afonso',
'Agatha',
'Agenor',
'Agnaldo',
'Agnes',
'Agostinho',
'Aguinaldo',
'Aiko',
'Aimar',
'Aimée',
'Airton',
'Ajit',
'Akahana',
'Akako',
'Akiva',
'Alan',
'Alana',
'Alane',
'Alanna',
'Alanne',
'Alaíde',
'Alba',
'Alberta',
'Albertina',
'Alberto',
'Alceu',
'Alcides',
'Alcione',
'Alcyone',
'Alda',
'Aldaberto',
'Aldine',
'Aldo',
'Alec',
'Alecsandra',
'Alegra',
'Alejandra',
'Aleksandra',
'Alessandra',
'Alessandro',
'Alex',
'Alexa',
'Alexandra',
'Alexandre',
'Alfonso',
'Alfredo',
'Ali',
'Alice',
'Alicia',
'Aline',
'Alisha',
'Alissa',
'Allegra',
'Alma',
'Alonso',
'Aloísio',
'Aluísio',
'Alzira',
'Aléxis',
'Amadeu',
'Amadeus',
'Amaia',
'Amanda',
'Amar',
'Amara',
'Amarílis',
'Amauri',
'Amaury',
'Amedeo',
'Amir',
'Amisha',
'Amita',
'Amiti',
'Amos',
'Amy',
'Amália',
'Amélia',
'Amélie',
'América',
'Américo',
'Amílcar',
'Ana',
'Anabela',
'Anahy',
'Aída',
'Aílton',
'B.B King',
'Big Mama Thorton',
'Billie Holliday',
'James Brown',
'Koko Taylor',
'Laverna Baker',
'Madonna',
'Tina Turner',
'Ágata',
'Álvaro']
			
print(len(minha_lista))

def pesquisa_binaria(lista, item):
	baixo = 0
	alto = len(lista) - 1
	retorno = None
	passos = 1
	while baixo <= alto:
		print("Passos : " + str(passos))
		meio = str(((baixo + alto) / 2))
		meio = int(meio[:meio.index(".")])
		chute = lista[meio]
		if chute == item:
			retorno = meio
			break
		if chute > item:
			alto = meio - 1
		else:
			baixo = meio + 1
		passos += 1

	print("Big O -> Tempo gasto (Log2) " + str(math.log2(passos)))
	return retorno

param_pesquisa = 'Aaron'
print("posição : " + str(pesquisa_binaria(minha_lista, param_pesquisa)) + 
" para encontrar " + param_pesquisa)

print('\n')

param_pesquisa = 'Álvaro'
print("posição : " + str(pesquisa_binaria(minha_lista, param_pesquisa)) + 
" para encontrar " + param_pesquisa)

print('\n')

param_pesquisa = 'Alceu'
print("posição : " + str(pesquisa_binaria(minha_lista, param_pesquisa)) + 
" para encontrar " + param_pesquisa)


