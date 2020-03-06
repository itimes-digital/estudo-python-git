"""Módulo de perfil de usuário"""
from user_module import User

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

