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
"""
#age,workclass,final-weight,education,education-num,marital-status,occupation,
#relationship,race,sex,capital-gain,capital-loos,hour-per-week,native-country,income
#Criar variáveis dummy para melhor uso dos dados
from sklearn.preprocessing import OneHotEncoder
from sklearn.compose import ColumnTransformer

column_transform = ColumnTransformer([("encoder", 
                         OneHotEncoder(), 
                        [1,3,5,6,7,8,9,13])],    
                       remainder = 'passthrough')

previsores = column_transform.fit_transform(previsores).toarray()

#Versão anterior
#oneHotEncoder = OneHotEncoder([1,3,5,6,7,8,9,13])
#previsores = oneHotEncoder.fit_transform(previsores).toarray()


#Transforma variável categórica em números
labelEncoder_classe = LabelEncoder()
classe = labelEncoder_classe.fit_transform(classe)
"""
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


