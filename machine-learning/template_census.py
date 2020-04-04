# -*- coding: utf-8 -*-
"""
Created on Mon Mar 30 21:37:11 2020

@author: admin
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
oneHotEncoder = OneHotEncoder(categorical_features=[1,3,5,6,7,8,9,13])
previsores = oneHotEncoder.fit_transform(previsores).toarray()

#Transforma variável categórica em números
labelEncoder_classe = LabelEncoder()
classe = labelEncoder_classe.fit_transform(classe)

from sklearn.preprocessing import StandardScaler

scaler = StandardScaler()

previsores = scaler.fit_transform(previsores)

#Gerar uma amostra de treinamento - previsores e classe
#Gerar uma amostra de teste - previsores e classe
from sklearn.cross_validation import train_test_split
#Proporção de 25%
previsores_treinamento, previsores_teste, classe_treinamento, classe_teste = train_test_split(previsores, 
                                classe, 
                                test_size=0.15,
                                random_state=0)


