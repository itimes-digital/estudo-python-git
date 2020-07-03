# -*- coding: utf-8 -*-
"""
Created on Thu May 14 19:49:25 2020

@author: aasousa
"""
import numpy as np
import matplotlib.pyplot as plt
from sklearn.cluster import KMeans
import pandas as pd
from sklearn.preprocessing import StandardScaler

x = [20, 27, 21, 37,46,53,55,47,52,32,39,41,39,48, 48];
y = [1000, 1200, 2900, 1850,900,950,2000,2100,3000,5900,4100,5100,7000,5000,6500];

plt.scatter(x, y);

x_1 = pd.DataFrame({"x": x})
y_1 = pd.DataFrame({"y": y})

x_1 = x_1.join(y_1)

base = np.asarray(x_1)

scaler = StandardScaler()

base = scaler.fit_transform(base)

kMeans = KMeans(n_clusters = 3)
kMeans.fit(base)

centroides = kMeans.cluster_centers_
rotulos = kMeans.labels_

cores = ['g.', 'r.', 'b.']

for i in range(len(x)):
    plt.plot(base[i][0], base[i][1], cores[rotulos[i]], markersize = 15)
    
plt.scatter(centroides[:,0], centroides[:, 1], marker = 'x')

