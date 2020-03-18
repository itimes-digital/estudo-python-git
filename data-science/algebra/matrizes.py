"""Estudo de algebra linear com python"""

import functools
import math

#Possui duas linhas e três colunas
matriz_A = [[1, 2, 3], 
			[4, 5, 6]]

#Possui três linhas e duas colunas
matriz_B = [[1, 2], 
			[3, 4],
			[5, 6]]
			
print("Tamanho de A : " + str(len(matriz_A)))
print("Tamanho de A na posição [0] : " + str(len(matriz_A[0])))
print("Tamanho de B : " + str(len(matriz_B)))

def shape(A):
	num_rows = len(A)
	num_cols = len(A[0]) if A else 0 #número de elementos na primeira linha
	return num_rows, num_cols
	
print("\nMatriz A : ")
print("[ [1, 2, 3], ")
print("  [4, 5, 6] ]")
print("Matriz A com duas linhas e três colunas.")
print("Cada coluna podemos chamar de vetor.")
print("Portanto, há três vetores com n elementos.")
print("Matriz A : " + str(shape(matriz_A)))

def get_rows(A, i):
	return A[i] #A[i] já é da linha A[i] é linha i-ésimo
	
def get_column(A, j):
	return [A_i[j]  #j-ésimo elemento da linha A_i
			for A_i in A] #para cada linha A_i
			
def make_matrix(num_rows, num_cols, entry_fn):
	"""Retorna a matriz num_rows x num_cols
	cuja entrada (i, j)th é entry_fn(i, j)"""
	return [[entry_fn(i,j)            #dado i, cria uma lista
			for j in range(num_cols)] # [entry_fn(i,0), ...]
			for i in range(num_rows)] #cria uma lista para cada i
			
def is_diagonal(i, j):
	"""1´s na diagonal, 0's nos demais lugares"""
	return 1 if i == j else 0
	
friendships = [(0,1),(0,2),(1,2),(1,3),(2,3),(3,4),
			   (4,5),(5,6),(5,7),(6,8),(7,8),(8,9)]

result = make_matrix(10, 10, is_diagonal)

print(result)

friends_of = [i 
				for i, is_friend in enumerate(friendships[5])
				if is_friend]
				
print("vetor : " + str(friends_of))
				

		

