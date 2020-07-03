# -*- coding: utf-8 -*-
"""
Created on Sun May 17 14:24:23 2020

@author: aasousa
"""
import pandas as pd
import matplotlib.pyplot as plt

base = pd.read_csv('dataset/credit_data.csv')

base = base.dropna()

# ================= Uma Variável ================= 

# income x age
plt.scatter(base.iloc[:, 1], base.iloc[:, 2])

# income x loan
plt.scatter(base.iloc[:, 1], base.iloc[:, 3])

# age x loan
plt.scatter(base.iloc[:, 2], base.iloc[:, 3])

# média das idade
base.loc[base.age < 0, 'age'] = 42.92

# income x age
plt.scatter(base.iloc[:, 1], base.iloc[:, 2])

# age x loan
plt.scatter(base.iloc[:, 2], base.iloc[:, 3])


base_census = pd.read_csv('dataset/census.csv')

# ================= Duas Variáveis ================= 

# age x final weight
plt.scatter(base_census.iloc[:, 0], base_census.iloc[:, 2])

