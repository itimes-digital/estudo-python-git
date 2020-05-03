# -*- coding: utf-8 -*-
"""
Created on Sat May  2 17:09:36 2020

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


#Gerar uma amostra de treinamento - previsores e classe
#Gerar uma amostra de teste - previsores e classe
from sklearn.model_selection import train_test_split
#Proporção de 25%
previsores_treinamento, previsores_teste, classe_treinamento, classe_teste = train_test_split(previsores, 
                                classe, 
                                test_size=0.25,
                                random_state=0)

#importação da biblioteca
import keras
from keras.models import Sequential 
from keras.layers import Dense # entradas conectadas a todos os neurônios

#criação do classificador
classificador = Sequential()
classificador.add(Dense(units = 2,
                        activation = 'relu',
                        input_dim = 3))
classificador.add(Dense(units = 2, 
                  activation = 'relu'))
classificador.add(Dense(units = 1, activation = 'sigmoid')) #retorna uma probabilidade

classificador.compile(optimizer = 'adam', # descida do gradiente estocástico
                      loss = 'binary_crossentropy', 
                      metrics = ['accuracy'])
classificador.fit(previsores_treinamento, 
                  classe_treinamento, 
                  batch_size = 10, #atualização dos pesos após 10 elementos
                  nb_epoch = 100)

previsoes = classificador.predict(previsores_teste)
previsoes = (previsoes > 0.5)

from sklearn.metrics import confusion_matrix, accuracy_score
precisao = accuracy_score(classe_teste, previsoes)
matriz = confusion_matrix(classe_teste, previsoes)

