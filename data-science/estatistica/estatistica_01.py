"""
Histograma
Tendência central
"""

from matplotlib import pyplot as plt
import collections
from random import randint

def mean(x):
	return sum(x) / len(x)
	
def median(v):
	"""enconra o valor mais oa meio de v"""
	n = len(v)
	sorted_v = sorted(v)
	mid_point = n // 2
	
	if n % 2 == 1:
		#se for ímpar, retorna o valor do meio
		return sorted_v[mid_point]
	else:
		#se for par, retorna a média dos valores do meio
		lo = mid_point - 1 #pega uma posição anterior
		hi = mid_point     #pega uma posição posterior
		return (sorted_v[lo] + sorted_v[hi]) / 2

def quantile(x, p):
	"""retorna o valor percentual p-ésimmo em x"""
	p_index = int(p * len(x))
	return sorted(x)[p_index]
	
def mode(x):
	"""retorna uma lista, pode haver mais de uma moda"""
	counts = collections.Counter(x)
	max_count = max(counts.values())
	return [x_i for x_i, count in counts.items()
			if count == max_count]

#amplitude já possui significado em Python, então usaremos um nome diferente
def data_range(x):
	return max(x) - min(x)
	
# Uma única barra / a divisão ficará fracionada 10 // 2 = 5.0
# Uma única barra // a divisão ficará inteira 10 // 2 = 5
print(10 // 2)

num_friends = []

for x in range(100):
	num_friends.append(randint(1, 10))

for x in range(100):
	num_friends.append(randint(1, 20))
	
for x in range(100):
	num_friends.append(randint(1, 50))

num_friends.append(100)
num_friends_sorted 	= sorted(num_friends) # ordenar a lista
print(num_friends_sorted) 

print(mean(num_friends_sorted)) #Média
print(median(num_friends_sorted)) #Mediana
print(quantile(num_friends_sorted, 0.10)) #1º Quantile
print(quantile(num_friends_sorted, 0.25)) #2º Quantile
print(quantile(num_friends_sorted, 0.75)) #3º Quantile
print(quantile(num_friends_sorted, 0.90)) #4º Quantile
print("moda : " + str(mode(num_friends_sorted))) #Moda
print("range dos dados : " + str(data_range(num_friends_sorted)))


num_points 				= len(num_friends_sorted)
print("quantidade : " + str(num_points)) # quantidade
largest_value 			= max(num_friends_sorted) #maior valor
smallest_value 			= min(num_friends_sorted) #menor valor
smallest_value 			= num_friends_sorted[0]
second_smallest_value 	= num_friends_sorted[1]
second_largest_value 	= num_friends_sorted[-2]


print(smallest_value)
print(second_smallest_value)
print(second_largest_value)

friend_counts 	= collections.Counter(num_friends_sorted)
xs 				= range(101) #o valor maior é 100
ys 				= [friend_counts[x] for x in xs] #a altura é somente # de amigos
plt.bar(xs, ys)
plt.axis([0, 101, 0, 25])
plt.title("Histograma da Contagem de Amigos")
plt.xlabel("# de amigos")
plt.ylabel("# de pessoas")
plt.show()



