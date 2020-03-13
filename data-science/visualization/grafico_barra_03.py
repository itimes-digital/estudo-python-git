"""Construção de gráficos de barra com matplotlib"""
from matplotlib import pyplot as plt

mentions = [500, 505]
years = [2013, 2014]

plt.bar([x + 0.4 for x in [2012.6, 2013.6]], mentions, 0.8)
plt.xticks(years)
plt.ylabel("# de vezes que ouvimos alguém dizer 'data science'")

#Se você não fizer isso, matplotlib nomeará o eixo x de 0, 1
#E então adiciona a +2.013e3 para fora do canto (matplotlib feito!)
plt.ticklabel_format(useOffset=False)

#Enganar o eixo y mostra apenas a parte acima de 500
#plt.axis([2012.5,2014.5,499,506])
#plt.title("Olhe o 'Grande' Aumento!")

#Alternativas de iniciar os valores no eixo y
plt.axis([2012.5,2014.5,0,550])
plt.title("Não Tão Grande Agora!")
plt.show()

