# -*- coding: utf-8 -*-
"""
Created on Wed May  6 21:09:29 2020

@author: aasousa

Fórmula da reta da regressão
y = b0 + b1 * x1
"""

import pandas as pd

base = pd.read_csv('dataset/plano_saude.csv')

X = base.iloc[:, 0].values
Y = base.iloc[:, 1].values

import numpy as np

correlacao = np.corrcoef(X, Y)

X = X.reshape(-1, 1)

from sklearn.linear_model import LinearRegression

regressor = LinearRegression()
regressor.fit(X, Y)

# b0
regressor.intercept_

# b1
regressor.coef_

import matplotlib.pyplot as plt

plt.scatter(X, Y)
# X é o valor real
# regressor.predict(X) é o valor previsto a partir de X
plt.plot(X, regressor.predict(X), color = 'red')
plt.title('Regressão Linear Simples')
plt.xlabel('Idade')
plt.ylabel('Custo')

# previsão com várias idades
param_idade = np.asarray([40, 45, 50])
param_idade = param_idade.reshape(-1, 1)

previsao1 = regressor.predict(param_idade)
# processo manual
previsao2 = regressor.intercept_ + regressor.coef_ * 45

score = regressor.score(X, Y)

# Valores residuais são os valores que estejam distante da linha de tendência

from yellowbrick.regressor import ResidualsPlot

visualizador = ResidualsPlot(regressor)
visualizador.fit(X, Y)
visualizador.poof()

