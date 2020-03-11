"""Realizando leitura de arquivos"""
filename = 'C:\\Users\\admin\\Documents\\estudos\\text-file\\programming.txt'

"""
-> 'r' é modo de leitura, a omissão o Python só permite leitura
-> 'w' é modo de escrita, elimina o que já foi escrito em open apaga o arquivo
-> 'a' é modo de concatenação
-> 'r+' é modo de escrita e leitura
"""


with open(filename, 'w') as file_object:
	file_object.write("Estou programando em Python...\n")
	file_object.write("Estou programando em Java...\n")
	file_object.write("Estou programando em R...\n")
	file_object.write("Estou estudando data science!\n")

with open(filename) as file_object_open:
	for line in file_object_open:
		print(line)

with open(filename, 'a') as file_object_concat:
	file_object_concat.write("I also love finding meaning in large datasets.\n")
	file_object_concat.write("I love creating apps that can run in a browser.\n")
	
with open(filename) as file_object_open:
	for line in file_object_open:
		print(line)
	


		

