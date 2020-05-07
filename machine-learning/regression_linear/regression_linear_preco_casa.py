# -*- coding: utf-8 -*-
"""
Created on Wed May  6 23:06:41 2020

@author: aasousa
"""

import pandas as pd

base = pd.read_csv('dataset/house_price.csv')

X = base.iloc[:, 5:6].values
Y = base.iloc[:, 2].values

from sklearn.model_selection import train_test_split

x_treinamento, x_teste, y_treinamento, y_teste = train_test_split(X, Y, 
                                                    test_size = 0.3, 
                                                    random_state = 0)

from sklearn.linear_model import LinearRegression

regressor = LinearRegression()
regressor.fit(x_treinamento, y_treinamento)

score = regressor.score(x_treinamento, y_treinamento)

import matplotlib.pyplot as plt

plt.scatter(x_treinamento, y_treinamento)
plt.plot(x_treinamento, regressor.predict(x_treinamento), color = 'red')

previsoes = regressor.predict(x_teste)

resultado = abs(y_teste - previsoes)
resultado.mean()

from sklearn.metrics import mean_absolute_error, mean_squared_error

mean_abs_error = mean_absolute_error(y_teste, previsoes)
mean_sq_error = mean_squared_error(y_teste, previsoes)

plt.scatter(x_teste, y_teste)
plt.plot(x_teste, regressor.predict(x_teste), color = 'red')

regressor.score(x_teste, y_teste)






