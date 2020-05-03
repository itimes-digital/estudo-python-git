# -*- coding: utf-8 -*-
"""
Created on Sat May  2 19:22:54 2020

@author: aasousa
"""
import pandas as pd

base = pd.read_csv('dataset\census.csv')

#Pega todas as linhas até a coluna 13
previsores = base.iloc[:, 0:14].values

classe = base.iloc[:, 14].values

from sklearn.preprocessing import LabelEncoder, OneHotEncoder

#Transforma variável categórica em números
labelEncoder_previsores = LabelEncoder()

#Os dois pontos : significa todas as linhas
#Valores entre os dois pontos 0:5 são todas as colunas 1, 2, 3 e 4
#labels = labelEncoder_previsores.fit_transform(previsores[:,1])

#Implementando a transformação em números e atribuindo
previsores[:, 1] = labelEncoder_previsores.fit_transform(previsores[:,1])
previsores[:, 3] = labelEncoder_previsores.fit_transform(previsores[:,3])
previsores[:, 5] = labelEncoder_previsores.fit_transform(previsores[:,5])
previsores[:, 6] = labelEncoder_previsores.fit_transform(previsores[:,6])
previsores[:, 7] = labelEncoder_previsores.fit_transform(previsores[:,7])
previsores[:, 8] = labelEncoder_previsores.fit_transform(previsores[:,8])
previsores[:, 9] = labelEncoder_previsores.fit_transform(previsores[:,9])
previsores[:, 13] = labelEncoder_previsores.fit_transform(previsores[:,13])

#Criar variáveis dummy para melhor uso dos dados

from sklearn.compose import ColumnTransformer

column_transform = ColumnTransformer([("encoder", 
                         OneHotEncoder(), 
                        [1,3,5,6,7,8,9,13])],    
                       remainder = 'passthrough')

previsores = column_transform.fit_transform(previsores).toarray()

#Transforma variável categórica em números
labelEncoder_classe = LabelEncoder()
classe = labelEncoder_classe.fit_transform(classe)

from sklearn.preprocessing import StandardScaler

scaler = StandardScaler()

previsores = scaler.fit_transform(previsores)

#Gerar uma amostra de treinamento - previsores e classe
#Gerar uma amostra de teste - previsores e classe
from sklearn.model_selection import train_test_split
#Proporção de 25%
previsores_treinamento, previsores_teste, classe_treinamento, classe_teste = train_test_split(previsores, 
                                classe, 
                                test_size=0.15,
                                random_state=0)

#importação da biblioteca
import keras
from keras.models import Sequential
from keras.layers import Dense

#criação do classificador
classificador = Sequential()
# units é a quantidade de neurônios
# activation é o tipo de função de ativação a ser aplicado nos neurônios e pesos
# input_dim é a quantidade de entradas, atributos ou colunas do dataset
classificador.add(Dense(units = 60, activation = 'relu', input_dim = 108))
classificador.add(Dense(units = 60, activation = 'relu'))
classificador.add(Dense(units = 1, activation = 'sigmoid')) # função binária
classificador.compile(optimizer = 'adam', 
                     loss = 'binary_crossentropy', 
                     metrics = ['accuracy'])

# Treinar o modelo
classificador.fit(previsores_treinamento, 
                  classe_treinamento, 
                  batch_size = 10, # ajusta os pesos de cada 10 registros
                  epochs = 100) # o ajuste será rodado 100 vezes
 
previsoes = classificador.predict(previsores_teste)
previsoes = (previsoes > 0.5)

from sklearn.metrics import confusion_matrix, accuracy_score
precisao = accuracy_score(classe_teste, previsoes)
matriz = confusion_matrix(classe_teste, previsoes)


