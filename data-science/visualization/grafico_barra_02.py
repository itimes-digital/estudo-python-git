"""Construção de gráficos de barra com matplotlib"""
from matplotlib import pyplot as plt
from collections import Counter

grades = [83,95,91,87,70,0,85,82,100,67,73,77,0]
decile = lambda grade: grade // 10 * 10
histogram = Counter(decile(grade) for grade in grades)

#move cada barra para a esquerda
#dá para cada barra sua altura correta
#dá para cada barra a largura de 8
plt.bar([x - 0.1 for x in histogram.keys()], 
		histogram.values(),
		8)
		
#eixo x de -5 até 105
#eixo y de 0 até 5
plt.axis([-5, 105, 0, 5])

#rótulos do eixo x em 0, 10, ..., 100
plt.xticks([10 * i for i in range(11)])
plt.xlabel("Decil")
plt.ylabel("# de Alunos")
plt.title("Distribuição das Notas de Teste 1")
plt.show()
