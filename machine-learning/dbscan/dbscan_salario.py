# -*- coding: utf-8 -*-
"""
Created on Sun May 17 11:34:19 2020

@author: aasousa
"""
import matplotlib.pyplot as plt
import pandas as pd
import numpy as np
from sklearn.preprocessing import StandardScaler
from sklearn.cluster import DBSCAN

x = [20, 27, 21, 37,46,53,55,47,52,32,39,41,39,48, 48];
y = [1000, 1200, 2900, 1850,900,950,2000,2100,3000,5900,4100,5100,7000,5000,6500];

plt.scatter(x, y)

base = pd.DataFrame({'x': x}).join(pd.DataFrame({'y': y}))

base = np.asarray(base);

scaler = StandardScaler();
base = scaler.fit_transform(base)

dbscan = DBSCAN(eps = 0.95, min_samples = 3);
dbscan.fit(base)
previsoes = dbscan.labels_

cores = ['g.','r.', 'b.'];
for i in range(len(base)):
    plt.plot(base[i][0], base[i][1], cores[previsoes[i]], markersize = 15);

