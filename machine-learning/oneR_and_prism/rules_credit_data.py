# -*- coding: utf-8 -*-
"""
Created on Sun Apr 12 16:09:17 2020

@author: aasousa
"""

import Orange
import random

#Insere c# para saber a classe
#Insere i# ignora a coluna para tratamento dos dados
base = Orange.data.Table('D:/estudo-machine-learning/estudo-python/machine-learning/dataset/credit_data.csv')

print(base.domain)
print(len(base))

#base_dividida = Orange.data.Table(base.domain, random.sample(base, 500))

base_dividida           = Orange.evaluation.testing.sample(base, n=0.25)
base_treinamento        = base_dividida[1]
base_teste              = base_dividida[0]

print(len(base_treinamento))
print(len(base_teste))

cn2_learner             = Orange.classification.rules.CN2Learner()
classificador           = cn2_learner(base_treinamento)

for regras in classificador.rule_list:
    print(regras)

#É possível aplicar diversos tipos de classificadores para avaliar os modelos
resultado = Orange.evaluation.testing.TestOnTestData(base_treinamento, 
                                                    base_teste, [classificador])

#Apresenta a acuracidade dp resultado
acuracidade = Orange.evaluation.CA(resultado)
print(acuracidade)