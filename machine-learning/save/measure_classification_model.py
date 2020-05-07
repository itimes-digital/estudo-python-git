# -*- coding: utf-8 -*-
"""
Created on Mon May  4 21:34:27 2020

@author: aasousa
"""
import pandas as pd
import pickle
import numpy as np
from sklearn.impute import SimpleImputer
from sklearn.preprocessing import StandardScaler

scaler = StandardScaler()

svm = pickle.load(open('modelo_treinado/svm_finalizado.sav', 'rb'))
random_forest = pickle.load(open('modelo_treinado/random_forest_finalizado.sav', 'rb'))
mlp = pickle.load(open('modelo_treinado/mlp_finalizado.sav', 'rb'))


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

paga = 0
nao_paga = 0

if resposta_svm[0] == 1:
    paga += 1
else:
    nao_paga += 1
    
if resposta_random_forest[0] == 1:
    paga += 1
else:
    nao_paga += 1
    
if resposta_mlp[0] == 1:
    paga += 1
else:
    nao_paga += 1
    
if paga > nao_paga:
    print('Cliente pagará o empréstimo')
elif paga == nao_paga:
    print('Resultado empatado')
else:
    print('Cliente não pagará o empréstimo')




