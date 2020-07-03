# -*- coding: utf-8 -*-
"""
Created on Thu May 14 20:46:42 2020

@author: aasousa
"""
import matplotlib.pyplot as plt
import pandas as pd
from sklearn.cluster import KMeans
from sklearn.preprocessing import StandardScaler

base = pd.read_csv('dataset/credit_card_clients.csv', header = 1)

base['BILL_TOTAL'] = base['BILL_AMT1'] + base['BILL_AMT2'] + base['BILL_AMT3']+ base['BILL_AMT4']+ base['BILL_AMT5']+ base['BILL_AMT6']

x = base.iloc[:,[1,25]].values

scaler = StandardScaler()
x = scaler.fit_transform(x)

wcss = []

for i in range(1, 11):
    kmeans = KMeans(n_clusters = i, random_state = 0)
    kmeans.fit(x)
    wcss.append(kmeans.inertia_)
    
plt.plot(range(1, 11), wcss)
plt.xlabel('Número de clusters')
plt.ylabel('WCSS')

