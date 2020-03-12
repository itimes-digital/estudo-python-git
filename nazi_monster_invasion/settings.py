"""Classe de configurações do jogo"""
class Settings():
	"""Uma classe para armazenar todas as configurações da Invasão Alienígena"""
	
	def __init__(self):
		"""Incializa as configurações do jogo"""
		
		#Configurações da tela
		self.screen_width 				= 1200
		self.screen_height 				= 600
		self.bg_color 					= (0, 0, 0)
		
		#Configurações da nave
		self.ship_speed_factor 			= 1.5
		self.ship_jump_speed_factor 	= 10
		
		#Configurações do tiro
		self.bullet_speed_factor 		= 1
		self.bullet_width 				= 3
		self.bullet_height 				= 15
		self.bullet_color 				= 60, 60, 60
		self.bullets_allowed 			= 3
		
		
		
