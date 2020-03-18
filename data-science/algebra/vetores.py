"""Estudo de algebra linear com python"""

import functools
import math

height_weight_age = [70, #polegadas
					170, #quilos
					40]  #anos

grades = [95, #teste1
		 80,  #teste2
		 75,  #teste3
		 62]  #teste4
		 
def vector_add(v, w):
	"""Soma de elementos correspondentes"""
	return [v_i + w_i for v_i, w_i in zip(v, w)]
			
def vector_subtract(v, w):
	"""subtração de elementos correspondentes"""
	return [v_i - w_i 
			for v_i, w_i in zip(v, w)]
	
print("Vetor A : " + str(height_weight_age))
print("Vetor B : " + str(grades))
print("Soma de vetores : " + str(vector_add(height_weight_age, grades)))
print("Subtração de vetores : " + str(vector_subtract(height_weight_age, grades)))

vectors = [height_weight_age, grades]

print("vectors : " + str(vectors))

def vector_sum(vectors):
	"""Soma todos os elementos correspondentes"""
	
	result = vectors[0]
	for vector in vectors[1:]:
		result = vector_add(result, vector)
	return result
	
	"""Caminho alternativo para realizar a soma"""
	#return functools.reduce(vector_add, vectors)
	

print(vector_sum(vectors))


def scalar_multiply(c, v):
	"""c é um número, v é um vetor"""
	return [c * v_i for v_i in v]	
	
def vector_mean(vectors):
	"""Computar o vetor cujo i-ésimo elemento seja a média dos i-ésimos
	elementos dos vetores inclusos"""
	n = len(vectors)
	return scalar_multiply(1/n, vector_sum(vectors))
	
def dot(v, w):
	"""v_1 * w_1 + ... + v_n * w_n"""
	return sum(v_i * w_i for v_i, w_i in zip(v, w))
	
def sum_of_squares(v):
	"""v_1 * v_1 + ... + v_n * v_n"""
	return dot(v, v)

def magnitude(v):
	return math.sqrt(sum_of_squares(v)) #math.sqrt é a função de raiz quadrada
	
def squared_distance(v, w):
	"""(v_1 - w_1) ** 2 + ... + (v_n - w_n) ** 2"""
	return sum_of_sqwares(vector_subtract(v, w))
	
def distance(v, w):
	return magnitude(vector_subtract(v, w))
	

