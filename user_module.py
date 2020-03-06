"""Ajustando as classes e seus módulos"""
class User():
	"""Classe que representa o usuário"""
	
	def __init__(self, 
				first_name, 
				last_name,
				age,
				adress,
				phone):
		self.first_name = first_name
		self.last_name = last_name
		self.age = age
		self.adress = adress
		self.phone = phone
		self.login_attempts = 0
		
	def describe_user(self):
		print("\n" + self.first_name.title() + " " + self.last_name.title() + 
			" tem " + str(self.age) + " anos de idade e vive em " + 
			self.adress.title() + " e seu telefone de contato é " + 
			self.phone + ".")
			
	def greet_user(self):
		print("Olá " + self.first_name.title() + ", tudo bem?")
		
	def increment_login_attempts(self):
		self.login_attempts += 1
		
	def reset_login_attempts(self):
		self.login_attempts = 0	
		print("Login resetado...")
		
	def show_login_attempts(self):
		print("Qt. logins : " + str(self.login_attempts))
		
		
