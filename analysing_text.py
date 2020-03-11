"""Analisando texto"""
filename = 'C:\\Users\\admin\\Documents\\estudos\\text-file\\alice.txt'

word = "Alice"
try:
	with open(filename) as obj_open:
		contents = obj_open.read()
except FileNotFoundError:
	msg = "Sorry, the file " + filename + "does not exist."
	print(msg)
else:
	# Conta o número aproximado de palavras no arquivo
	words = contents.split()
	num_words = len(words)
	print("The file " + filename + " has about " + str(num_words) + " words.")
	count = 0
	for word1 in words:
		if word == word1:
			count += 1
	print("A palavra 'Alice' contêm : " + str(count))
	
