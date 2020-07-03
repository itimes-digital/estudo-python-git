# -*- coding: utf-8 -*-
"""
Created on Sat May 16 17:35:18 2020

@author: aasousa
"""
from scipy.cluster.hierarchy import dendrogram, linkage
from sklearn.cluster import AgglomerativeClustering
import pandas as pd
from sklearn.preprocessing import StandardScaler


base = pd.read_csv('dataset/credit_card_clients.csv', header = 1)

base['BILL_TOTAL'] = base['BILL_AMT1'] + base['BILL_AMT2'] + base['BILL_AMT3']+ base['BILL_AMT4']+ base['BILL_AMT5']+ base['BILL_AMT6']

x = base.iloc[:,[1,25]].values
scaler = StandardScaler();
x = scaler.fit_transform(x);

dendrograma = dendrogram(linkage(x, method = 'ward'))

hc = AgglomerativeClustering(n_clusters = 3, 
                             affinity = 'euclidean',
                             linkage = 'ward')
previsoes = hc.fit_predict(x)