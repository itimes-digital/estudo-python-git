# -*- coding: utf-8 -*-
"""
Created on Sun May 17 11:49:38 2020

@author: aasousa
"""
from sklearn.cluster import DBSCAN
import pandas as pd
from sklearn.preprocessing import StandardScaler
import matplotlib.pyplot as plt
import numpy as np

base = pd.read_csv('dataset/credit_card_clients.csv', header = 1)

base['BILL_TOTAL'] = base['BILL_AMT1'] + base['BILL_AMT2'] + base['BILL_AMT3']+ base['BILL_AMT4']+ base['BILL_AMT5']+ base['BILL_AMT6']

x = base.iloc[:,[1,25]].values
scaler = StandardScaler();
x = scaler.fit_transform(x);

dbscan = DBSCAN(eps = 0.37, min_samples = 4)
previsoes = dbscan.fit_predict(x)

# retorna a contagem de itens unicos
unicos, quantidade = np.unique(previsoes, return_counts = True)

plt.scatter(x[previsoes == 0, 0], x[previsoes == 0, 1], s = 100, c = 'red', label = 'Cluster 1')
plt.scatter(x[previsoes == 1, 0], x[previsoes == 1, 1], s = 100, c = 'orange' , label = 'Cluster 2')
plt.scatter(x[previsoes == 2, 0], x[previsoes == 2, 1], s = 100, c = 'green', label = 'Cluster 3')
plt.xlabel('Limite')
plt.ylabel('Gastos')
plt.legend()

lista_clientes = np.column_stack((base, previsoes))
lista_clientes = lista_clientes[lista_clientes[:, 26].argsort()]

