"""Construção de gráficos de linha com matplotlib"""
from matplotlib import pyplot as plt

variance = [1,2,4,8,16,32,64,128,256]
bias_squared = [256,128,64,32,16,8,4,2,1]

#Exemplo: [(1, 256), (2, 128), (4, 64) ...]
dados_combinados = zip(variance, bias_squared)

total_error = [x + y for x, y in dados_combinados]
xs = [i for i, _ in enumerate(variance)]

#podemos fazer múltiplas chamadas para plt.plot
#para mostrar múltiplias séries no mesmo gráfico

#linha verde sólida
plt.plot(xs, variance, 'g-', label='variance')
#linha com linha de ponto tracejado vermelho
plt.plot(xs, bias_squared, 'r-.', label='bias^2')
#linha com pontilhado azul
plt.plot(xs, total_error, 'b:', label='total error')

#porque atributos rótulos para cada série
#podemos obter uma legenda gratuita
#loc=9 significa "top center"
plt.legend(loc=9)
plt.xlabel("complexidade do modelo")
plt.title("Compromisso entre Polarização e Variância")
plt.show()


