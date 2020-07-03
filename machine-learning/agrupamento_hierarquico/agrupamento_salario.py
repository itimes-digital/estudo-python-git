# -*- coding: utf-8 -*-
"""
Created on Sat May 16 17:08:59 2020

@author: aasousa
"""
import matplotlib.pyplot as plt
from sklearn.cluster import AgglomerativeClustering
import pandas as pd
import numpy as np
from sklearn.preprocessing import StandardScaler

x = [20, 27, 21, 37,46,53,55,47,52,32,39,41,39,48, 48];
y = [1000, 1200, 2900, 1850,900,950,2000,2100,3000,5900,4100,5100,7000,5000,6500];

plt.scatter(x, y)

base_x = pd.DataFrame({'x': x})
base_y = pd.DataFrame({'y': y})

base = base_x.join(base_y)

base = np.asarray(base);

scaler = StandardScaler();
base = scaler.fit_transform(base)

hc = AgglomerativeClustering(n_clusters = 3, 
                             affinity = 'euclidean', 
                             linkage = 'ward')

previsoes = hc.fit_predict(base)

plt.scatter(base[previsoes == 0, 0], base[previsoes == 0, 1], s = 100, c = 'red', label = 'Cluster 1')
plt.scatter(base[previsoes == 1, 0], base[previsoes == 1, 1], s = 100, c = 'blue', label = 'Cluster 2')
plt.scatter(base[previsoes == 2, 0], base[previsoes == 2, 1], s = 100, c = 'green', label = 'Cluster 3')
plt.xlabel('Idade')
plt.ylabel('Salário')
plt.legend()