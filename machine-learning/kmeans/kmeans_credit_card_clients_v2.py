# -*- coding: utf-8 -*-
"""
Created on Thu May 14 20:46:42 2020

@author: aasousa
"""
import matplotlib.pyplot as plt
import pandas as pd
from sklearn.cluster import KMeans
from sklearn.preprocessing import StandardScaler
import numpy as np

base = pd.read_csv('dataset/credit_card_clients.csv', header = 1)

base['BILL_TOTAL'] = base['BILL_AMT1'] + base['BILL_AMT2'] + base['BILL_AMT3']+ base['BILL_AMT4']+ base['BILL_AMT5']+ base['BILL_AMT6']

x = base.iloc[:,[1,2,3,4,5,25]].values

scaler = StandardScaler()
x = scaler.fit_transform(x)

wcss = []
# Calcula quantos cluster podem ser usados
for i in range(1, 11):
    kmeans = KMeans(n_clusters = i, random_state = 0)
    kmeans.fit(x)
    wcss.append(kmeans.inertia_)
    
plt.plot(range(1, 11), wcss)
plt.xlabel('Número de clusters')
plt.ylabel('WCSS')

kmeans = KMeans(n_clusters = 4, random_state = 0);
previsoes = kmeans.fit_predict(x)

plt.scatter(x[previsoes == 0, 0], x[previsoes == 0, 1], s = 100, c = 'red', label = 'Cluster 1')
plt.scatter(x[previsoes == 1, 0], x[previsoes == 1, 1], s = 100, c = 'orange' , label = 'Cluster 2')
plt.scatter(x[previsoes == 2, 0], x[previsoes == 2, 1], s = 100, c = 'green', label = 'Cluster 3')
plt.scatter(x[previsoes == 3, 0], x[previsoes == 3, 1], s = 100, c = 'blue', label = 'Cluster 4')
plt.xlabel('Limite')
plt.ylabel('Gastos')
plt.legend()

lista_clientes = np.column_stack((base, previsoes))
lista_clientes = lista_clientes[lista_clientes[:, 26].argsort()]
