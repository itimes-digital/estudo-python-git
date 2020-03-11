"""Testando a gravação e leitura de arquivos"""

def visualizarCadastro(filename):
	with open(filename, 'r') as crudR:
		for line in crudR:
			print(line)

	
def inserirValor(filename, valorAlterado):
	with open(filename, 'w') as crud:
		crud.write("Nome: " + valorAlterado[0] + ".\n")
		crud.write("Nascimento: " + valorAlterado[1] + ".\n")
		crud.write("Cidade: " + valorAlterado[2] + ".\n")
		crud.write("Profissão: " + valorAlterado[3] + ".\n")
		crud.write("Empresa: " + valorAlterado[4] + ".\n")
	
def atualizaValor(filename, valorAlterado, indice):
	conj = [1, 2, 3, 4, 5]
	count = 0
	with open(filename, 'r') as crudR:
		for line in crudR:
			conj[count] = line
			count += 1
			
	with open(filename, 'w') as crudW:
		conj[indice] = valorAlterado
		for linha in conj:
			crudW.write(linha)


filename = 'C:\\Users\\admin\\Documents\\estudos\\text-file\\crud.txt'

respostas = [1,2,3,4,5]

respostas [0] = input("0 - Qual o seu nome completo? ")
respostas [1] = input("1 - Qual a sua data de nascimento (ddmmyyyy)? ")
respostas [2] = input("2 - Qual a sua cidade? ")
respostas [3] = input("3 - Qual a sua profissão? ")
respostas [4] = input("4 - Qual a empresa que você trabalha? ")

inserirValor(filename, respostas)

print("\nCadastro finalizado! Veja abaixo o que digitou:")

visualizarCadastro(filename)

proximoPasso = input("Deseja alterar seu cadastro?\nDigite S-Sim ou N-Não: ")

if proximoPasso == "S":
	proximoPasso = input("Qual informação deseja atualizar?\n" + 
					"Digite:\n " + 
					"0 - Para Nome\n " + 
					"1 - Para Data de Nascimento\n " + 
					"2 - Para Cidade\n " + 
					"3 - Para Profissão\n " + 
					"4 - Para Empresa que trabalha\n " +  
					"9 - Para sair! -> ")
	valorAlterado = ""
	proximoPasso = int(proximoPasso)
	print("\n")
	if proximoPasso == 0:
		valorAlterado = input("Atualize o seu nome: ")
		atualizaValor(filename, "Nome: " + valorAlterado + "\n", proximoPasso)
	elif proximoPasso == 1:
		valorAlterado = input("Atualize a sua data de nascimento: ")
		atualizaValor(filename, "Data: " + valorAlterado + "\n", proximoPasso)
	elif proximoPasso == 2:
		valorAlterado = input("Atualize a sua cidade: ")
		atualizaValor(filename, "Cidade: " + valorAlterado + "\n", proximoPasso)
	elif proximoPasso == 3:
		valorAlterado = input("Atualize a sua profissão: ")
		atualizaValor(filename, "Profissão: " + valorAlterado + "\n", proximoPasso)
	elif proximoPasso == 4:
		valorAlterado = input("Atualize a empresa que você trabalha: ")
		atualizaValor(filename, "Empresa: " + valorAlterado + "\n", proximoPasso)
	else:
		print("Obrigado.")	
	
	print("=====Veja seu cadastro final:=====\n")
	visualizarCadastro(filename)
else:
	print("Obrigado.")
	


