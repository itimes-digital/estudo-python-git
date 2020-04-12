# -*- coding: utf-8 -*-
"""
Created on Sun Apr 12 15:31:57 2020

@author: aasousa
"""
import Orange

base = Orange.data.Table('D:/estudo-machine-learning/estudo-python/machine-learning/dataset/risco_credito.csv')

print(base.domain)

#Algoritmo de 1989
cn2_learner = Orange.classification.rules.CN2Learner()

"""
Na massa de dados é necessário especificar a classe discreta, para isso, 
é só colocar c# junto com o valor da coluna correspondente, no caso, c#risco
"""
classificador = cn2_learner(base)

for regras in classificador.rule_list:
    print(regras)
    
# HITÓRIA BOA, DÍVIDA ALTA, GARANTIAS NENHUMA, RENDA > 35.000
# HITÓRIA RUIM, DÍVIDA ALTA, GARANTIAS ADEQUADA, RENDA < 15.000
    
resultado = classificador([['boa', 'alta', 'nenhuma', 'acima_35'],
                           ['ruim', 'alta', 'adequada', '0_15']])
#Resultado da posição 0 é IF historia==boa AND renda!=15_35 THEN risco=baixo 
#Resultado da posição 1 é IF renda==0_15 THEN risco=alto 
for i in resultado:
    print(base.domain.class_var.values[i])
