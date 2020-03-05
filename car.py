class Car():
	"""Classe que representa um carro real"""
	
	def __init__(self, make, model, year):
		self.fabricante = make
		self.modelo = model
		self.ano = year
		self.odometer_reading = 0
		
	def get_descriptive_name(self):
		"""Deveolve um nome descritivo, formatado de modo elegante"""
		long_name = str(self.ano) + ' ' + self.fabricante + ' ' + self.modelo
		return long_name.title() 
	
	def read_odometer(self):
		"""Exibe uma frase que mostra a milhagem do carro."""
		print("This car has " + str(self.odometer_reading) + " miles on it.")
		
	def update_odometer(self, mileage):
		"""
		Define o valor de leitura do hodômetro com o valor especificado
		Rejeita a alteração se for tentativa de definir um valor 
		menor para o hodômetro
		"""
		if mileage >= self.odometer_reading:
			self.odometer_reading = mileage
		else:
			print("You can´t roll back an odometer!")

	def increment_odometer(self, miles):
		"""Soma a quantidade especificada ao valor de leitura do hodômetro"""
		self.odometer_reading += miles
		
my_new_car = Car('audi', 'a4', 2016)
print("\n" + my_new_car.get_descriptive_name())
my_new_car.read_odometer()

your_new_car = Car('ford', 'focus', 2016)
print("\n" + your_new_car.get_descriptive_name())
your_new_car.odometer_reading = 30
your_new_car.read_odometer()

other_new_car = Car('volks', 'fusca', 1975)
print("\n" + other_new_car.get_descriptive_name())
other_new_car.update_odometer(100)
other_new_car.read_odometer()
#else
other_new_car.update_odometer(20)

other_new_car.increment_odometer(35)
other_new_car.read_odometer()
