# -*- coding: utf-8 -*-
"""
Created on Sun May 17 14:35:50 2020

@author: aasousa
"""
import pandas as pd
from pyod.models.knn import KNN

base = pd.read_csv('dataset/credit_data.csv')

base = base.dropna()

detector = KNN();

detector.fit(base.iloc[:, 1:4])

previsoes = detector.labels_

confianca_previsoes = detector.decision_scores_

outliers = []

for i in range(len(previsoes)):
    #print(previsoes[i])
    if previsoes[i] == 1:
        outliers.append(i)
        
# lista de outliers
lista_outliers = base.iloc[outliers, :]



