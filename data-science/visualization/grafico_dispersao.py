"""Construção de gráficos de linha com matplotlib"""
from matplotlib import pyplot as plt

friends 	= [70,65,72,63,71,64,60,64,67]
minutes 	= [175,170,205,120,220,130,105,145,190]
labels 		= ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i']

plt.scatter(friends, minutes)

for label, friend_count, minute_count in zip(labels, friends, minutes):
	plt.annotate(label, 
	xy=(friend_count, minute_count), 
	xytext=(5, -5), #Coloca o rótulo com sua posição mas compensa um pouco
	textcoords='offset points')

#Definição dos eixos da escala onde o eixo x inicia com 58 e vai até 74
#Já no eixo y inicia em 80 e vai até 240
#Assim a visualização fica mais legível, pois esta
#configuração tem que estar de acordo com os dados 
#apresentados no gráfico
plt.axis([58, 74, 80, 240])

plt.title("Minutos Diários vc. Números de Amigos")
plt.xlabel("# de amigos")
plt.ylabel("minutos diários passados no site")
plt.show()

"""
Desta forma os dados não são apresentados adequadamente, pois
não há uma definição da escala de valores. O matplotlib define
automaticamente.

test_1_grades = [99,90,85,97,80]
test_2_grades = [100,85,60,90,70]

plt.scatter(test_1_grades, test_2_grades)
plt.title("Os eixos não são compatíveis")
plt.xlabel("nota do teste 2")
plt.ylabel("nota do teste 1")
plt.show()
"""
