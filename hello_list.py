bicycles = ['trek', 'cannondale', 'redline', 'specialized']
print(bicycles)

print("Segundo elemento da lista : " + bicycles[1])
print("Terceiro elemento da lista (usando metodo title()): " + bicycles[2].title())

ages = [10, 30, 50, 25, 15]
print("Idades : " + str(ages))
print("A idade da quarta posição da lista eh : " + str(ages[3]))

#Ultimo item da lista
print("Última idade da lista (-1) : " + str(ages[-1]))

#Ultimo item da lista
print("Antepenúltima idade da lista (-3) : " + str(ages[-3]))

message = "My first bicycle was a " + bicycles[0].title() + '.'
print(message)

names = ["elvis presley", "james brown", "koko taylor", "tina turner", "diana krall"]
print(names)
print(names[0].title() + ", " + names[1].title() + " and " + names[2].title() + " unfortunately, they are dead!")
print(names[3].title() + " is a great icon and " + names[4].title() + " is great jazz singer with a good soft voice.")

#Trocando valores das listas
print(names)
names[0] = "Big Joe Turner"
print("Nome mudado... " + str(names))
print(names[0] + ", by Grammy Museum is considered the grandfather of Rock´n Roll!")

#Adicionando elementos
names.append("Elvis Presley")
names.append("Al Green")
names.append("George Clinton")
names.append("Laverna Baker")
names.append("Ray Charles")
print("Lista de nomes : " + str(names))

#Listas dentro de outra lista
songs = ["Love me tender", "Please, Please, Please", "The best", "The Look Of Love"]
print("Músicas de alguns artistas : " + str(songs))
names.append(songs)
print("Agregando a lista songs dento de names : " + str(names))
names.append(ages)
print("Agregando a lista ages dento de names : " + str(names))

print("Pegando um valor dentro do array songs e exibindo a música de Diana Krall : " + names[-2][-1])


print("\n Lista total : " + str(names))
print("Removendo o primeira música da lista songs...")
del names[-2][0]
print("Lista de songs atualizada : " + str(names[-2]))

print("\nAntes... " + str(ages))
ages_pop = ages.pop()
print(ages)
print(ages_pop)

print("\nAntes (posição 2)... " + str(ages))
ages_pop = ages.pop(2)
print(ages)
print(ages_pop)

print("\nAntes ... " + str(names))
print("Removendo Elvis Presley...")
names.remove("Elvis Presley")
print(names)

imperadores_romanos = ["Julio Cesar", "Otávio Augusto", "Nero", "Tibério", "Calígula"]
print("\nImperadores Romanos : " + str(imperadores_romanos))
print("Inserindo...")

imperadores_romanos.insert(0, "Tito")
imperadores_romanos.insert(3, "Trajano")
imperadores_romanos.append("Constantino")
print(imperadores_romanos)
print("Trocando Tito de lugar para Otávio Augusto...")

imperador_pop = imperadores_romanos.pop(0)
imperadores_romanos.insert(0, imperadores_romanos[1])
imperadores_romanos[2] = imperador_pop
print("lista organizada : " + str(imperadores_romanos))
print(imperadores_romanos[0] + " é o primeiro Imperador de Roma!")
print(imperadores_romanos[-1] + " é o último Imperador de Roma e considerado o primeiro Papa da igreja!")

print("Retirando o Imperador que colocou fogo em Roma...")
del imperadores_romanos[4]
print("Lista atualizada : " + str(imperadores_romanos))

#Eliminando outras listas internas
print("\n" + str(names))
names.pop(-1)
names.pop(-1)
print(names)

#Ordenando listas
print("\nOrdenando com sort()")
deuses_mitologicos = ["thor", "apolo", "odin", "locke", "zeus", "afrodite", "musa", "artemis"]
print("\nDeuses Mitológicos : " + str(deuses_mitologicos))
deuses_mitologicos.sort()
print(deuses_mitologicos)

print("\nRevertendo a ordem com reverse=True")
deuses_mitologicos.sort(reverse=True)
print(deuses_mitologicos)

deuses_mitologicos = ["thor", "apolo", "odin", "locke", "zeus", "afrodite", "musa", "artemis"]
print("\nDeuses Mitológicos : " + str(deuses_mitologicos))
print("Ordenando listas com sorted()...")
print(sorted(deuses_mitologicos))
print("\nDeuses Mitológicos : " + str(deuses_mitologicos))
print(sorted(deuses_mitologicos))
print("\nDeuses Mitológicos : " + str(deuses_mitologicos))
deuses_mitologicos.reverse()
print("\nDeuses Mitológicos em ordem inversa: " + str(deuses_mitologicos))
print("tamanho da lista eh " + str(len(deuses_mitologicos)))

#===========================//===================================
squares = [value**2 for value in range(1,11)]
print(squares)#itera o range que é de 1 até 10 e eleva ao quadrado cada valor da iteração

squares = []
for value in range(1, 11):
	square = value**3
	squares.append(square)

print("\nResultado : " + str(squares))

print(list(range(8,11,2)))
# ** Dois asteriscos representam exponenciais, portanto, 3**2 = 9
print(3**2)

for value in range(1, 21):
	print(str(value) + " ao qudrado eh : " + str(value ** 2))
	
milhao = list(range(1, 1000001))
valorMin = min(milhao)
valorMax = max(milhao)
print(valorMin)
print(valorMax)
print("Valor total : " + str(sum(milhao)))

print("\n")

#Para número par ou ímpar, sempre o terceiro parâmetro é 2
for value in range(1, 21, 2):
	print(str(value) + " ao qudrado eh : " + str(value ** 2))
	
print("\n")	

for value in range(3, 31, 3):
	print(str(value) + " ao qudrado eh : " + str(value ** 3))
	
valor = [value**2 for value in range(1, 11)]
print("\nResultado da lista via comprehension : " + str(valor))

print("Cópia de lista [:]: " + str(valor[:]))

players = ['charles', 'martina', 'michael', 'florence', 'eli']
print("\n" + str(players))

print("\n[3:]")
for player in players[3:]:
	print(player.title())
	
print("\n[:3]")
for player in players[:3]:
	print(player.title())
