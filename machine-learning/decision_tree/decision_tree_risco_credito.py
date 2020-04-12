# -*- coding: utf-8 -*-
"""
Editor Spyder

Este é um arquivo de script temporário.
"""
"""
Cálculo de entropia faz parte do aprendizado de máquina Decision Tree
De acordo com a base de dados, temos esses dados:
    Alto = 6/14
    Moderado = 3/14
    Baixo = 5/14
    
    E(s) = -6/14 * # -pi
    log(6/14; 2) - 3/14 * #log2 - logaritma com base 2
    log(3/14; 2) - 5/14 * 
    log(5/14; 2) = 1,53
    
"""
import pandas as pd

base = pd.read_csv("D:/estudo-machine-learning/estudo-python/machine-learning/dataset/risco_credito.csv")

previsores = base.iloc[:, 0:4].values
classe = base.iloc[:, 4].values

from sklearn.preprocessing import LabelEncoder

labelEncoder = LabelEncoder()

previsores[:, 0] = labelEncoder.fit_transform(previsores[:, 0])
previsores[:, 1] = labelEncoder.fit_transform(previsores[:, 1])
previsores[:, 2] = labelEncoder.fit_transform(previsores[:, 2])
previsores[:, 3] = labelEncoder.fit_transform(previsores[:, 3])

from sklearn.tree import DecisionTreeClassifier, export
from sklearn import tree

#Por default é gini
classificador = DecisionTreeClassifier(criterion="entropy")
classificador.fit(previsores, classe)
print(classificador.feature_importances_)

#Viável a partir da versão 0.22
tree.plot_tree(classificador, filled=True)

#Precisa da ferramenta instalada graphviz para visualizar o gráfico
#http://www.webgraphviz.com/ ferramenta online
#https://dreampuf.github.io/GraphvizOnline ferramenta online
export.export_graphviz(classificador,
                       out_file = 'decision_tree.dot',
                       feature_names = ['historia', 'divida', 'garantias', 'renda'],
                       class_names = ['alto', 'moderado', 'baixo'],
                       filled = True,
                       leaves_parallel = True)

#HITÓRIA BOA, DÍVIDA ALTA, GARANTIAS NENHUMA, RENDA > 35.000
#resultado = classificador.predict([[0, 0, 1, 2]])
# HITÓRIA RUIM, DÍVIDA ALTA, GARANTIAS ADEQUADA, RENDA < 15.000
#HITÓRIA desconhecida, dívida baixa, garantia nenhuma, renda acima_35
resultado = classificador.predict([[0, 0, 1, 2], [2, 0, 0, 0], [1, 1, 1, 2]])

print(classificador.classes_)

