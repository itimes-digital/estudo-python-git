class Dog():
	"""Uma tentativa simples de modelar um cachorro"""
	
	def __init__(self, name, age):
		"""Inicializa os atributos name e age"""
		self.name = name
		self.age = age
		
	def sit(self):
		"""Simula um cachorro sentenado em resporta a um comando"""
		print(self.name.title() + " is now sitting.")
	
	def roll_over(self):
		"""Simula um cachorro rolando em resposta a um cachorro."""
		print(self.name.title() + " rolled over!")
		
	def latir(self):
		"""Simula um cachorro rolando em resposta a um cachorro."""
		return self.name.title() + " esta latindo!"
		
my_dog = Dog('willie', 6)

print("My dog's name is " + my_dog.name.title() + ".")
print("My dog is " + str(my_dog.age) + " years old.")

my_dog.sit()
my_dog.roll_over()
print(my_dog.latir())


your_dog = Dog('lassie', 10)

print("My dog's name is " + your_dog.name.title() + ".")
print("My dog is " + str(your_dog.age) + " years old.")

your_dog.sit()
your_dog.roll_over()
print(your_dog.latir())
