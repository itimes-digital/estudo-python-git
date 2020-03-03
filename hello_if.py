cars = ['audit', 'bmw', 'subaru', 'toyota']

for car in cars:
	if car == 'bmw':
		print(car.upper())
	else:
		print(car.title())
		
cars[0] = 'bmw'

print(cars[0] == 'bmw')
print(cars[0] == 'Bmw'.lower())
print(cars[0].title() == 'Bmw')

print(cars[0].title() != 'Bmw')

age = 18
if age != 18:
	print(True)
else:
	print(False)
	
if age != 20:
	print(True)
else:
	print(False)

if (age >= 17) and (age < 20) or (age < 18):
	print(True)
else:
	print(False)
	
	
if 'toyota' in cars:
	print('Toyota está na lista')
else:
	print('Carro não encontrado!')
	
if 'focus' in cars:
	print('Toyota está na lista')
else:
	print('Carro não encontrado!')

carro = 'focus'
if carro not in cars:
	print(carro + ' : Carro não encontrado!')
else:
	print('Carro encontrado!')

age = 18
if age < 4:
	print('Your admission cost is $0')
elif age < 18:
	print('Your admission cost is $5')
else:
	print('Your admission cost is $10')

lista_vazia = ['oi']
#Vazia retorn false
if lista_vazia:
	print('Tamanho : ' + str(len(lista_vazia)))
else:
	print('Tamanho (vazia): ' + str(len(lista_vazia)))
