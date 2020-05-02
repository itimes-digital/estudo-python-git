# -*- coding: utf-8 -*-
"""
Created on Fri May  1 21:12:45 2020

@author: aasousa
"""
from pybrain.structure import FeedForwardNetwork
from pybrain.structure import LinearLayer, SigmoidLayer, BiasUnit
from pybrain.structure import FullConnection

# criação da rede

rede = FeedForwardNetwork()

# criando as camadas da rede
camadaEntrada = LinearLayer(2) # com quantidade de neurônios
camadaOculta = SigmoidLayer(3) # camada oculta com a função sigmoid
camadaSaida = SigmoidLayer(1) # camada de saída com a função sigmoid

bias_camada_oculta = BiasUnit()
bias_camada_saida = BiasUnit()

# adicionado as camadas dentro da rede neural
rede.addModule(camadaEntrada)
rede.addModule(camadaOculta)
rede.addModule(camadaSaida)
rede.addModule(bias_camada_oculta)
rede.addModule(bias_camada_saida)

# realizando a conexão com as camadas da rede
entradaOculta = FullConnection(camadaEntrada, camadaOculta)
ocultaSaida = FullConnection(camadaOculta, camadaSaida)
biasOculta = FullConnection(bias_camada_oculta, camadaOculta)
biasSaida = FullConnection(bias_camada_saida, camadaSaida)

# Criação e ligação das camadas para a montagem da rede neural
rede.sortModules()

# estrutura da rede
print(rede)

# resultado dos pesos de cada neurônio
print(entradaOculta.params)

# pesos da camada oculta para a camada de saída
print(ocultaSaida.params)

# pesos da bias para a camada oculta 
print(biasOculta.params)

# peso da bias da saida da camada de saída
print(biasSaida.params)