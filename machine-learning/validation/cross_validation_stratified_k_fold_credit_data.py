# -*- coding: utf-8 -*-
"""
Created on Sun May  3 15:40:26 2020

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
from sklearn.tree import DecisionTreeClassifier
from sklearn.ensemble import RandomForestClassifier
import numpy as np
from sklearn.model_selection import StratifiedKFold
from sklearn.metrics import accuracy_score


resultados_30_testes = []

for i in range(30):
    # pegará os previsores e fará o split/divisão dos dados
    k_fold = StratifiedKFold(n_splits = 10,
                             shuffle = True, # parâmetro em conjunto com random_state
                             random_state = i)
    
    resultados_rodada = []
    for indice_treinamento, indice_teste in k_fold.split(previsores,
                                                         np.zeros(shape=(previsores.shape[0], 1 ))):
     
        #criação do classificador
        #classificador = GaussianNB()    
        #classificador = DecisionTreeClassifier()   
        classificador = RandomForestClassifier()  
        classificador.fit(previsores[indice_treinamento], classe[indice_treinamento])
        previsoes = classificador.predict(previsores[indice_teste])
        precisao  = accuracy_score(classe[indice_teste], previsoes)
        resultados_rodada.append(precisao)
        
    resultados_rodada = np.asarray(resultados_rodada)
    media = resultados_rodada.mean()
    resultados_30_testes.append(media)

resultados_30_testes = np.asarray(resultados_30_testes)

for x in range(resultados_30_testes.size):
    print(str(resultados_30_testes[x]).replace('.', ','))



