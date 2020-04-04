# -*- coding: utf-8 -*-
"""
Created on Fri Apr  3 21:56:15 2020

@author: admin
"""

import pandas as pd

base = pd.read_csv('dataset\credit_data.csv')

#ajuste de valores inconsistentes
base.loc[base.age < 0, 'age'] = 40.92

#extração de colunas 1, 2 e 3 essenciais para a análise
previsores = base.iloc[:, 1:4].values

#extração de coluna 4 essenciais para a classificação
classe = base.iloc[:, 4].values

from sklearn.preprocessing import Imputer

#Eliminar valores faltantes colocando o valor da média
imputer = Imputer(missing_values='NaN', strategy='mean', axis=0)
imputer = imputer.fit(previsores[:, 1:4])
previsores[:, 1:4] = imputer.transform(previsores[:, 1:4])

from sklearn.preprocessing import StandardScaler

#Mudar o escalonamento dos dados para calcular espaço euclidiano
scaler = StandardScaler()
previsores = scaler.fit_transform(previsores)


#Gerar uma amostra de treinamento - previsores e classe
#Gerar uma amostra de teste - previsores e classe
from sklearn.cross_validation import train_test_split
#Proporção de 25%
previsores_treinamento, previsores_teste, classe_treinamento, classe_teste = train_test_split(previsores, 
                                classe, 
                                test_size=0.25,
                                random_state=0)


