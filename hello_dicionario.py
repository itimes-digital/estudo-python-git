alien_0 = {'color': 'green', 'points': 5}
print(alien_0['color'])
print(alien_0['points'])
new_points = alien_0['points']
print("You just earned " + str(new_points) + " points!")

alien_0['x_position'] = 0
alien_0['y_position'] = 25
print(alien_0)

alien_1 = {}
alien_1['color'] = 'green'
alien_1['points'] = 5
print(alien_1)

print('The alien is ' + alien_0['color'] + '.')

alien_0['color'] = 'yellow'
print(alien_0)
print('The alien is now ' + alien_0['color'] + '.')

#=======================//=================================
print('\n')
alien_0 = {'x_position': 0, 'y_position': 25, 'speed': 'fast'}
print('Original x-position: ' + str(alien_0['x_position']))

#Move o alienígena para a direita
#Determina a distância que o alienígena deve ser deslocar de acordo com sua
#velocidade atual
if alien_0['speed'] == 'slow':
	x_increment = 1
elif alien_0['speed'] == 'medium':
	x_increment = 2
else:
	#Este deve ser um alienígena
	x_increment = 3
	
#A nova posição é a posição antiga somada ao incremento
alien_0['x_position'] = alien_0['x_position'] + x_increment

print('New x-position : ' + str(alien_0['x_position']))

print(alien_1)
del alien_1['points']
print(alien_1)
#==============================//=================================
favorite_languages = {
	'jen': 'python', 
	'sarah': 'c', 
	'edward': 'ruby', 
	'phil': 'python'
	}
print(favorite_languages)
print("\n Sarah's favorite language is " + 
	favorite_languages['sarah'].title() + 
	".")
print('\n')
pessoa = {'nome' : 'Kool Herc', 
		'cidade': 'Nova York', 
		'profissão': 'DJ',
		'período': 'anos 70'}
estilos = {'1': 'rock', 
		'2': 'hip-hop', 
		'3':'jazz', 
		'4': 'funk', 
		'5':'blues', 
		'6':'pop'}
		
pessoa['estilos'] = estilos
print(pessoa)
print('\nO ' + 
	pessoa['profissão'] + 
	" " +  
	pessoa['nome'] + 
	' é considerado o percursor do ' + 
	pessoa['estilos']['2'].upper() + 
	'.')
	
print('Ele iniciou sua carreira nos ' + 
	pessoa['período'] + 
	' na cidade de ' +
	pessoa['cidade'] + 
	'.')
#============================//====================================
for key, value in pessoa.items():
	print('\nKey: ' + key)
	print('Value: ' + str(value))
	if key == 'estilos':
		print('\n' + str(key))
		for key2, value2 in pessoa['estilos'].items():
			print('\nKey: ' + key2)
			print('Value: ' + value2)

print('\n')
for name in favorite_languages.keys():#Ou for name in favorite_languages:
	print(name.title())

print('\n')
for value in favorite_languages.values():
	print(value.title())
	
print('\n')
print(favorite_languages)
friends = ['sarah', 'phil']
print(friends)
print('\n')
for name in favorite_languages.keys():
	print(name.title())
	if name in friends:
		print(" Hi " + name.title() + 
		", I see your favorite language is " + 
		favorite_languages[name].title() + "!")
		
print("\n")
for name in sorted(favorite_languages.keys()):
	print(name.title() + ", think you for taking the poll.")
	
print('\nUnicidade de objeto na lista...')
#Similar ao Set do java que aceita apenas um única instância
for language in set(favorite_languages.values()):
	print(language.title())
