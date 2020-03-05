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
	
user1 = User('anderson', 'de sousa', 40, 'são paulo', '11 969-696-696')
user1.describe_user()
user1.greet_user()

user2 = User('bruno', 'mars', 34, 'los angeles, estados unidos', '11 969-969-696-696')
user2.describe_user()
user2.greet_user()

user3 = User('jay', 'z', 50, 'los angeles, estados unidos', '11 111-111-696-696')
user3.describe_user()
user3.show_login_attempts()
user3.greet_user()
print("Realizando vários logins...")
tentativas = 9
login_realizado = 0

while login_realizado < tentativas:
	user3.increment_login_attempts()
	login_realizado += 1
	
login_realizado = 0
user3.show_login_attempts()
user3.reset_login_attempts()
user3.show_login_attempts()

class Privileges():
	"""Classe com o objetivo de gerenciar os privilégios dos usuários"""
	
	def __init__(self):
		self.privileges = ['can add post', 'can dele post', 'can ban user']
		
	def show_privileges(self):
		print("O perfil administrador têm esses privilégios : " + str(self.privileges))
	


class Admin(User):
	"""Classe filha de User"""
	
	def __init__(self):
		self.privileges = Privileges()
		
ad = Admin()
ad.privileges.show_privileges()
