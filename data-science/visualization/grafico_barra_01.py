"""Construção de gráficos de barra com matplotlib"""
from matplotlib import pyplot as plt

movies = ["Annie Hall", "Ben-Hur", "Casablanca", "Gandhi", "West Side Story"]
num_oscars = [5, 11, 3, 8, 10]

#Barras possuem o tamanho padrão de 0.8, então adicionamos 0.1 às
#coordenadas à esquerda para que cada barra seja centralizada

xs = [i + 0.1 for i, _ in enumerate(movies)]

#As barras do gráfico com as coordenadas x à esquerda [xs], alturas
#[num_oscars]
plt.bar(xs, num_oscars)

plt.ylabel("# de Premiações")
plt.title("Meus Filmes Favoritos")

#Nomeia o eixo x com nomes de filmes na barra central
plt.xticks([i + 0.5 for i, _ in enumerate(movies)], movies)

plt.show()
