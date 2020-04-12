# -*- coding: utf-8 -*-
"""
Editor Spyder

Este é um arquivo de script temporário.
"""
import pandas as pd

base = pd.read_csv("D:/estudo-machine-learning/estudo-python/machine-learning/dataset/risco_credito.csv")

previsores = base.iloc[:, 0:4].values
classe = base.iloc[:, 4].values

from sklearn.preprocessing import LabelEncoder

labelEncoder = LabelEncoder()

previsores[:, 0] = labelEncoder.fit_transform(previsores[:, 0])
previsores[:, 1] = labelEncoder.fit_transform(previsores[:, 1])
previsores[:, 2] = labelEncoder.fit_transform(previsores[:, 2])
previsores[:, 3] = labelEncoder.fit_transform(previsores[:, 3])

from sklearn.naive_bayes import GaussianNB

classificador = GaussianNB()
classificador.fit(previsores, classe)

# HITÓRIA BOA, DÍVIDA ALTA, GARANTIAS NENHUMA, RENDA > 35.000
# HITÓRIA RUIM, DÍVIDA ALTA, GARANTIAS ADEQUADA, RENDA < 15.000
resultado = classificador.predict([[0, 0, 1, 2], [3,0,0,0]])

print(classificador.classes_)
print(classificador.class_count_)
print(classificador.class_prior_)