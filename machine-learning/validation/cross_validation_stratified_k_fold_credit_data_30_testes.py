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
import numpy as np

#a = np.zeros(5)
#previsores.shape
#previsores.shape[0]
#b = np.zeros(shape=(previsores.shape[0], 1))

from sklearn.model_selection import StratifiedKFold
from sklearn.metrics import accuracy_score, confusion_matrix

# pegará os previsores e fará o split/divisão dos dados
k_fold = StratifiedKFold(n_splits = 10,
                         shuffle = True, # parâmetro em conjunto com random_state
                         random_state = 30)

resultados = []
matrizes = []
for indice_treinamento, indice_teste in k_fold.split(previsores,
                                                     np.zeros(shape=(previsores.shape[0], 1 ))):
    #print('Indice treinamento: ', indice_treinamento, 'Índice teste: ', indice_teste)
    #criação do classificador
    classificador = GaussianNB()    
    classificador.fit(previsores[indice_treinamento], classe[indice_treinamento])
    previsoes = classificador.predict(previsores[indice_teste])
    precisao  = accuracy_score(classe[indice_teste], previsoes)
    matrizes.append(confusion_matrix(classe[indice_teste], previsoes))
    resultados.append(precisao)


matriz_final = np.mean(matrizes, axis = 0)
resultados = np.asarray(resultados)
resultados.std() # é bom para validar o desempenho do modelo, se não está havendo overfitting
resultados.mean()


