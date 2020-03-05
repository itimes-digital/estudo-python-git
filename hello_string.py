mesage = "Hello Python World!"
print(mesage)

mesage = "Hello Python Crash Course World!"
print(mesage)

message_new = "Novo teste no terminal"
print(message_new)

l_novo_teste = "Novo?"
print(l_novo_teste)

string_1 = 'I told my friend, "Python is my favorite language!"'
print(string_1)

string_2 = "The language 'Python', is named after the great Monty Python, not the snake"
print(string_2)

string_3 = "One of Python's strengths is its diverse and supportive community."
print(string_3)

name = "ada lovelace is from same family from Linda Lovelace?"
print(name.title())

name = 'Ada loveLace'
print(name.upper())
print(name.lower())

name = 'aDa loVeLAcE is grEaT!'
print(name)
name = name.lower()
print(name.title())

first_name = "ada"
last_name = "lovelace"
full_name = first_name + " " + last_name
print(full_name)
message_final = "concatenacao : Hello, " + full_name.title() + " algorithm mother!"
print(message_final)

new_message = "Dizem que um programador poliglota deve saber escrever em: \tJAVA, \t.Net, \tJavascript, \tR, \tJulia \tou Python"
print(new_message)

new_message = "Mas acho que um programador poliglota deve saber escrever em: \nJAVA, \nR, \nJulia \nou Python"
print(new_message)

new_message = "[Tabulação] Mas acho que um programador poliglota deve saber escrever em: \nLinguagens -> \n\tJAVA, \n\tR, \n\tJulia \n\tou Python"
print(new_message)

new_word = '            python      '
print("palavra com espaco : " + new_word)

print("palavra sem espaco (strip()): " + new_word.strip())
print("palavra sem espaco direto (rstrip()): " + new_word.rstrip())
print("palavra sem espaco esquerdo (lstrip()): " + new_word.lstrip())

message = "One of Python's strengths is its diverse community."
print(message)

texto = "Isto é apenas um teste para python!"
print(texto)
print(len(texto))

texto = texto.replace('apenas', '')
print(texto)

print("Existem " + str(texto.count('e')) + " letras 'e'.")

encontrado = texto.find('m')
print("Encontrado a posição da letra m : " + str(encontrado))
print(texto[encontrado])

array_texto = texto.split()
print(array_texto)

#Apenas a primeira letra maiúscula
print("\nApenas a primeira letra maiúscula")
print(texto.lower().capitalize())









