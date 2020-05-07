# -*- coding: utf-8 -*-
"""
Created on Mon May  4 20:42:20 2020

@author: aasousa
"""
import pandas as pd
import pickle
import numpy as np
from sklearn.impute import SimpleImputer
from sklearn.preprocessing import StandardScaler

base = pd.read_csv('dataset/credit_data.csv')
base.loc[base.age < 0, 'age'] = 40.92
 
previsores = base.iloc[:, 1:4].values
classe = base.iloc[:, 4].values

imputer = SimpleImputer(missing_values=np.nan, strategy='mean')# , axis=0
imputer = imputer.fit(previsores[:, 1:4])
previsores[:, 1:4] = imputer.transform(previsores[:, 1:4])

scaler = StandardScaler()
previsores = scaler.fit_transform(previsores)

svm = pickle.load(open('modelo_treinado/svm_finalizado.sav', 'rb'))
random_forest = pickle.load(open('modelo_treinado/random_forest_finalizado.sav', 'rb'))
mlp = pickle.load(open('modelo_treinado/mlp_finalizado.sav', 'rb'))

resultado_svm = svm.score(previsores, classe)
resultado_random_forest = random_forest.score(previsores, classe)
resultado_mlp = mlp.score(previsores, classe)

novo_registro_para_avaliacao = [[50000, 40, 5000]]
novo_registro_para_avaliacao = np.asarray(novo_registro_para_avaliacao)
# muda a ordem horizontal para vertical
novo_registro_para_avaliacao = novo_registro_para_avaliacao.reshape(-1, 1)
novo_registro_para_avaliacao = scaler.fit_transform(novo_registro_para_avaliacao)
# muda a ordem vertical para horizontal
novo_registro_para_avaliacao = novo_registro_para_avaliacao.reshape(-1, 3)

resposta_svm = svm.predict(novo_registro_para_avaliacao)
resposta_random_forest = random_forest.predict(novo_registro_para_avaliacao)
resposta_mlp = mlp.predict(novo_registro_para_avaliacao)


