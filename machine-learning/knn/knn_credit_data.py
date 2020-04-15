# -*- coding: utf-8 -*-
"""
Created on Tue Apr 14 19:27:00 2020

@author: aasousa
"""


import pandas as pd

base = pd.read_csv('D:/estudo-machine-learning/estudo-python/machine-learning/dataset/credit_data.csv')

#ajuste de valores inconsistentes
base.loc[base.age < 0, 'age'] = 40.92

#extração de colunas 1, 2 e 3 essenciais para a análise
previsores = base.iloc[:, 1:4].values

#extração de coluna 4 essenciais para a classificação
classe = base.iloc[:, 4].values

import numpy as np
from sklearn.impute import SimpleImputer

#Eliminar valores faltantes colocando o valor da média
imputer = SimpleImputer(missing_values=np.nan, strategy='mean')# , axis=0
imputer = imputer.fit(previsores[:, 1:4])
previsores[:, 1:4] = imputer.transform(previsores[:, 1:4])

from sklearn.preprocessing import StandardScaler

#Mudar o escalonamento dos dados para calcular espaço euclidiano
scaler = StandardScaler()
previsores = scaler.fit_transform(previsores)


#Gerar uma amostra de treinamento - previsores e classe
#Gerar uma amostra de teste - previsores e classe
from sklearn.model_selection import train_test_split
#Proporção de 25%
previsores_treinamento, previsores_teste, classe_treinamento, classe_teste = train_test_split(previsores, 
                                classe, 
                                test_size=0.25,
                                random_state=0)

#importação da biblioteca
from sklearn.neighbors import KNeighborsClassifier
#criação do classificador
classificador = KNeighborsClassifier(n_neighbors = 5,
                                     metric = "minkowski",
                                     p = 2)

classificador.fit(previsores_treinamento, classe_treinamento)
previsoes = classificador.predict(previsores_teste)

from sklearn.metrics import confusion_matrix, accuracy_score
precisao = accuracy_score(classe_teste, previsoes)
matriz = confusion_matrix(classe_teste, previsoes)

import collections 
#Válido para compreender qual o percentual esperado de acuracidade e determinar
#qual classificador é melhor para tal problema 
print(collections.Counter(classe_teste))



