# -*- coding: utf-8 -*-
"""
Estudo de machine learning

"""

import pandas as pd

base = pd.read_csv('dataset\credit_data.csv')
base.describe()

#Busca as informações de acordo com uma condição
base.loc[base['age'] < 0]

#apagar a coluna e tribui nela mesma, péssima ideia
base.drop('age', 1, inplace=True)

#apagar os registros com problema
base.drop(base[base.age < 0].index, inplace=True)

#Preencher os valores manualmente
#Preencher os valores com a média
base.mean()
base['age'].mean()
base['age'][base.age > 0].mean() #retirar do calculo os valores negativos

#ajuste de valores inconsistentes
base.loc[base.age < 0, 'age'] = 40.92

#Verificar os valores null
pd.isnull(base['age'])

#Indentifica quais são os valores da coluna age estão null
base.loc[pd.isnull(base['age'])]

#extração de colunas 1, 2 e 3 essenciais para a análise
previsores = base.iloc[:,1:4].values

#extração de coluna 4 essenciais para a classificação
classe = base.iloc[:,4].values

from sklearn.preprocessing import Imputer

#Eliminar valores faltantes colocando o valor da média
imputer = Imputer(missing_values='NaN', strategy='mean', axis=0)
imputer = imputer.fit(previsores[:, 1:4])
previsores[:, 1:4] = imputer.transform(previsores[:, 1:4])

from sklearn.preprocessing import StandardScaler

#Mudar o escalonamento dos dados para calcular espaço euclidiano
scaler = StandardScaler()
previsores = scaler.fit_transform(previsores)





