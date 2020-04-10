# -*- coding: utf-8 -*-
"""
Created on Fri Apr  3 21:56:15 2020

@author: admin
"""

import pandas as pd

base = pd.read_csv('D:/estudo-machine-learning/estudo-python/machine-learning/dataset/credit_data.csv')


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


#Gerar uma amostra de treinamento - previsores e classe
#Gerar uma amostra de teste - previsores e classe
from sklearn.model_selection import train_test_split
#Proporção de 25%
previsores_treinamento, previsores_teste, classe_treinamento, classe_teste = train_test_split(previsores, 
                                classe, 
                                test_size=0.25,
                                random_state=0)

from sklearn.naive_bayes import GaussianNB

classificador  = GaussianNB()

#Criação de tabelas de probabilidades - tabela naive bayes
classificador.fit(previsores_treinamento, classe_treinamento)

previsoes = classificador.predict(previsores_teste)

"""
Serve para comparar algoritmos e analisar o nível de precisão do cálculo
A sua aplicabilidade serve também para analisar quão o modelo está sendo preciso,
isto é, efetivo, assertivo, próximo do ideal ou esperado de acordo com a classe 
de teste.
"""
from sklearn.metrics import confusion_matrix, accuracy_score

precisao = accuracy_score(classe_teste, previsoes)

"""
Mostra a relação de erros e acertos esperado para a quantidade de classes definidas
Um dos meios para compreender melhor o resultado do seu modelo
"""
matrix = confusion_matrix(classe_teste, previsoes)


