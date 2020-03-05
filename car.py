"""Uma classe que pode ser usada para representar um carro"""
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
		
	def fill_gas_thank(self):
		"""Carros elétricos não teêmm tanques de gasolina."""
		print("This car need a gas tank!")
		

