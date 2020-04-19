# -*- coding: utf-8 -*-
"""
Created on Mon Mar 30 21:37:11 2020

@author: admin
"""
import pandas as pd

base = pd.read_csv('D:/estudo-machine-learning/estudo-python/machine-learning/dataset/census.csv')

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
from sklearn.svm import SVC

#criação do classificador
classificador = SVC(kernel='linear', 
                    random_state=1)
classificador.fit(previsores_treinamento, classe_treinamento)
previsoes = classificador.predict(previsores_teste)

from sklearn.metrics import confusion_matrix, accuracy_score
precisao = accuracy_score(classe_teste, previsoes)
matriz = confusion_matrix(classe_teste, previsoes)

import collections 
#Válido para compreender qual o percentual esperado de acuracidade e determinar
#qual classificador é melhor para tal problema 
print(collections.Counter(classe_teste))
