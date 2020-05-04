# -*- coding: utf-8 -*-
"""
Created on Sun May  3 15:25:17 2020

@author: aasousa
"""

import pandas as pd

base = pd.read_csv('dataset\credit_data.csv')

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

from sklearn.model_selection import cross_val_score

#importação da biblioteca
from sklearn.naive_bayes import GaussianNB

#criação do classificador
classificador = GaussianNB()

resultados = cross_val_score(classificador, previsores, classe, cv = 10)
resultados.mean()
resultados.std() # é bom para validar o desempenho do modelo, se não está havendo overfitting


