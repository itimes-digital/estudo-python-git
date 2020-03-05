def describe_pet(pet_name, animal_type='dog'):
	"""Exibe informações sobre um animal de estimação"""
	print("\nI have a " + animal_type + ".")
	print("My " + animal_type + "'s name is " + pet_name.title() + ".")
	
describe_pet('harry', 'hamster')
describe_pet('snoop', 'dog')
describe_pet('tom', 'cat')
describe_pet('jerry', 'rat')
describe_pet('roger', 'rabbit')

#Argumentos nomeados
print("\nCom argumentos nomeados posso inverter a ordem da implementação")
print("Declaração inicial da função : describe_pet(pet_name, animal_type='dog')")
print("describe_pet(animal_type='rabbit', pet_name='bugs bunny')")
describe_pet(animal_type="rabbit", pet_name="bugs bunny")

#Valores default
print("\nValores default")
print("Declaração inicial da função : describe_pet(pet_name, animal_type='dog')")
describe_pet(animal_type="rabbit", pet_name="bugs bunny")
describe_pet(pet_name="lassy")
describe_pet("lassy")

def make_shirt(tamanho="grande", texto_estampa="Eu amo Python!"):
	"""Exibe o tamanho da camisa e o texto da estampa"""
	print("O tamanho da camisa é " + tamanho + " e o texto da estampa é '" + texto_estampa + "'.")
	
make_shirt()
make_shirt("pequena", "Hoje é hoje, amanhã é outro dia, pois não é bem isso, é quase isso.")
make_shirt(tamanho="média")

def descrive_city(cidade, pais="Islândia"):
	"""Descreve o nome da cidade e o nome do país"""
	print("A cidade " + cidade + " está localizada no(a) " + pais)
	
descrive_city("Kópavogur")
descrive_city("Mosfellsbær")
descrive_city("Reykjanesbær")
descrive_city("São Paulo", "Brasil")

def get_formatted_name(last_name, first_name='jimi'):
	"""Devolve um nome completo formatado de modo elegante"""
	full_name = first_name + " " + last_name
	return full_name.title()

musician = get_formatted_name('hendrix')
print('\n'+ musician)
musician = get_formatted_name('page')
print(musician)
musician = get_formatted_name('presley', 'elvis')
print(musician)

name1 = 'Elvis Aaron Presley'
name2 = 'Big Joe Turner'
vogais = ['a', 'e', 'i', 'o', 'u']

def just_vowels(text):
	num = 0
	resultado = []
	while num < len(text):
		if text.lower()[num] in vogais:
			resultado.append(text[num])
		num += 1
	return resultado

print("\n" + str(name1))	
result = just_vowels(name1)	
print(result)
print("\n" + str(name2))	
result = just_vowels(name2)	
print(result)

lista_musicos = ['James Brown', "Oscar Peterson", 'Jerry Lee Lewis']
print('\nAntes da execução : ' + str(lista_musicos))
def remove_item_lista(lista):
	"""Eliminando itens de uma lista"""
	lista.append('Grandmaster Flash')
	return lista


resultado_final = remove_item_lista(lista_musicos)
print('Lista Original Alterada : ' + str(lista_musicos))
print('Novo resultado : ' + str(resultado_final))
print("Resultado da lista como parâmetro normal (Inserção de dados): " + str(len(resultado_final)))

lista_musicos = ['James Brown', "Oscar Peterson", 'Jerry Lee Lewis']
resultado_final = remove_item_lista(lista_musicos[:])
print('\nLista Original : ' + str(lista_musicos))
print('Novo resultado : ' + str(resultado_final))
print("Resultado da lista como cópia no parâmetro [:] : " + str(len(resultado_final)))

#Passa por parâmetros diversos valores
def send_param(*params):
	"""Diversos parametros"""
	for valor in params:
		if valor == 'rock':
			print('Elvis is ' + valor)
		elif valor == 'jazz':
			print('Billie Holiday is ' + valor)
		elif valor == 'blues':
			print('Big Mama Thorton is ' + valor)
		else:
			print('Tupac is ' + valor) 
	
send_param('rock', 'jazz', 'blues', 'hip-hop')

print('\n')
def build_profile(first, last, **user_info):
	"""Contrói um dicionário contendo tudo que sabemos sobre um usuário"""
	profile = {}
	profile['first_name'] = first
	profile['last_name'] = last

	for key, value in user_info.items():
		profile[key] = value
	return profile
	
user_profile = build_profile('albert', 'einstein',
								location='princeton',
								field='physics')
print(user_profile)
