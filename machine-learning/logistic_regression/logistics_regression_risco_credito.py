# -*- coding: utf-8 -*-
"""
Created on Wed Apr 15 22:08:04 2020

@author: aasousa
"""# -*- coding: utf-8 -*-

import pandas as pd

base = pd.read_csv("D:/estudo-machine-learning/estudo-python/machine-learning/dataset/risco_credito_v2.csv")

previsores = base.iloc[:, 0:4].values
classe = base.iloc[:, 4].values

from sklearn.preprocessing import LabelEncoder

labelEncoder = LabelEncoder()

previsores[:, 0] = labelEncoder.fit_transform(previsores[:, 0])
previsores[:, 1] = labelEncoder.fit_transform(previsores[:, 1])
previsores[:, 2] = labelEncoder.fit_transform(previsores[:, 2])
previsores[:, 3] = labelEncoder.fit_transform(previsores[:, 3])


from sklearn.linear_model import LogisticRegression

classificador = LogisticRegression()

classificador.fit(previsores, classe)

#B0 = [-0.52358972]
print(classificador.intercept_)

#B1...Bn são os coeficientes dos parâmetros gerados pelo algoritmo
#[[-0.65034407  0.25428474 -0.45375558  1.17384764]]
print(classificador.coef_)

#HITÓRIA BOA, DÍVIDA ALTA, GARANTIAS NENHUMA, RENDA > 35.000
# HITÓRIA RUIM, DÍVIDA ALTA, GARANTIAS ADEQUADA, RENDA < 15.000
resultado = classificador.predict([[0, 0, 1, 2], [3, 0, 0, 0]])
resultado2 = classificador.predict_proba([[0, 0, 1, 2], [3, 0, 0, 0]])
print(resultado)
print(resultado2)




