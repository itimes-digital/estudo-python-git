"""Teste de chamada de módulo para restaurantes"""
#from restaurants import * isto é uma abordagem de implementação
#import restaurants também é uma abordagem, desde que seja explícito
#o nome do módulo.nome_da_classe

#from nome_do_módulo import nome_da_classe
from restaurants import Restaurants #Está explícito apenas a classe Restaurants
from restaurants import IceCreamStand

restaurant1 = Restaurants('família mancini', "italiana")
restaurant1.describe_restaurant()
restaurant1.count_clients()
restaurant1.open_restaurant()

restaurant2 = Restaurants('boi na brasa', "churrasco gaúcho")
restaurant2.describe_restaurant()
restaurant2.count_clients()
restaurant2.open_restaurant()
restaurant2.update_count_clients(10)
restaurant2.count_clients()

restaurant3 = Restaurants('boi na brasa', "churrasco gaúcho")
restaurant3.describe_restaurant()
restaurant3.count_clients()
restaurant3.open_restaurant()
restaurant3.update_count_clients(50)
restaurant3.count_clients()
restaurant3.update_count_clients(5)
restaurant3.count_clients()

ice = IceCreamStand()
ice.show_flavors()
