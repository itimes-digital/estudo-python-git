# -*- coding: utf-8 -*-
"""
Created on Sun May 17 14:13:52 2020

@author: aasousa
"""
import pandas as pd
import matplotlib.pyplot as plt

base = pd.read_csv('dataset/credit_data.csv')

base = base.dropna()

# outliers idade
plt.boxplot(base.iloc[:, 2], showfliers = True)

base_outliers_age = base[(base.age < -20)]

# outliers loan
plt.boxplot(base.iloc[:, 3], showfliers = True)
base_outliers_loan = base[(base.loan > 13300)]