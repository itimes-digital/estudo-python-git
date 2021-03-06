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


class IceCreamStand(Restaurants):
	"""Classe filha ou subclasse de restaurantes"""
	def __init__(self):
		super()
		self.flavors = ['chocolate', 'morango', 'abacaxi', 'creme']
		
	def show_flavors(self):
		print("Em nossa sorveteria temos esses sabores : " + str(self.flavors))
	


