filename = 'C:\\Users\\admin\\Documents\\estudos\\text-file\\guest.txt'

def insertGuest(filename, count, nomeUsuario):
	with open(filename, 'a') as guest:
		guest.write(str(count) + "º Convidado: " + nomeUsuario + "\n")
		
def visualizarGuest(filename):
	with open(filename) as reader:
		for line in reader:
			print(line)
		
quantGuest = 5
count = 1

while count <= quantGuest:
	nome = input("Por favor digite o seu nome para entrar na lista de convidados: ")
	insertGuest(filename, count, nome)
	print("Obrigado por colocar o seu nome em nossa lista VIP!\n")
	count += 1

print("Segue abaixo a lista de convidados:\n ")
visualizarGuest(filename)
	



