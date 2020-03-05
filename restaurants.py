class Restaurants():
	"""Restaurante italino"""
	def __init__(self, restaurant_name, cuisine_type):
		"""Inicia os tributos da classe"""
		self.restaurant_name = restaurant_name
		self.cuisine_type = cuisine_type
		self.number_served = 0
		
	def describe_restaurant(self):
		print("\nO restaurante " + self.restaurant_name.title() + 
			" é estilo clássico com música ao vivo " + 
			"e oferecendo o que há de melhor da cozinha " + 
			self.cuisine_type + ".")
			
	def open_restaurant(self):
		print("O restaurante " + self.restaurant_name.title() + 
		" funciona de terça à domingo das 15h até 02h.")
	
	def count_clients(self):
		print(str(self.number_served) + " clientes atendidos!")
		
	def update_count_clients(self, number_clients):
		print("Entrou novos clientes...")
		self.number_served += number_clients

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
