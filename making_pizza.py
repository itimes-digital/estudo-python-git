#Forma de importar módulo e funções
import pizza

pizza.make_pizza(16, 'pepperoni')
pizza.make_pizza(12, 'mushrooms', 'green pappers', 'extra cheese')

#Forma de importar módulo e funções
from pizza import make_pizza

make_pizza(16, 'pepperoni')
make_pizza(12, 'mushrooms', 'green pappers', 'extra cheese')

#Forma de importar módulo e funções com alias
from pizza import make_pizza as mp

mp(16, 'pepperoni')
mp(12, 'mushrooms', 'green pappers', 'extra cheese')

#Forma de importar módulo com alias
import pizza as p 

p.make_pizza(16, 'pepperoni')
p.make_pizza(12, 'mushrooms', 'green pappers', 'extra cheese')

#Forma de importar com todas as funções
from pizza import *

pizza.make_pizza(16, 'pepperoni')
pizza.make_pizza(12, 'mushrooms', 'green pappers', 'extra cheese')
