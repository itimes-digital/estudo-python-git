# -*- coding: utf-8 -*-
"""
Created on Wed May  6 23:47:50 2020

@author: aasousa
"""
import pandas as pd

base = pd.read_csv('dataset/house_price.csv')

# Variável independente
X = base.iloc[:, 3:19].values

# Variável dependente
Y = base.iloc[:, 2].values

from sklearn.model_selection import train_test_split

x_treinamento, x_teste, y_treinamento, y_teste = train_test_split(X, 
                                                                  Y,
                                                                  test_size = 0.3,
                                                                  random_state = 0)

from sklearn.linear_model import LinearRegression

regressor = LinearRegression()
regressor.fit(x_treinamento, y_treinamento)

score = regressor.score(x_treinamento, y_treinamento)

previsoes = regressor.predict(x_teste)

from sklearn.metrics import mean_absolute_error

mean_abs_error = mean_absolute_error(y_teste, previsoes)

regressor.score(x_teste, y_teste)

regressor.intercept_

len(regressor.coef_)

regressor.coef_
