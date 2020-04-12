# -*- coding: utf-8 -*-
"""
Created on Sun Apr 12 17:00:25 2020

@author: aasousa
"""
import Orange

base = Orange.data.Table("D:/estudo-machine-learning/estudo-python/machine-learning/dataset/credit_data.csv")
print(base.domain)

base_dividida = Orange.evaluation.testing.sample(base, n=0.25)

base_treinamento = base_dividida[1]
base_teste = base_dividida[0]
print(len(base_treinamento))
print(len(base_teste))

#Este algoritmo classifica os dados pela maioria apresentada, isto é,
#dados com maior relevância
#Base line classifier
classificador = Orange.classification.MajorityLearner()
resultado = Orange.evaluation.testing.TestOnTestData(base_treinamento, 
                                                     base_teste, 
                                                     [classificador])

print(Orange.evaluation.CA(resultado))

from collections import Counter

print(Counter(str(d.get_class()) for d in base_teste))



