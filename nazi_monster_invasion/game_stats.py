class GameStats():

	def __init__(self, settings):
		"""Inicializa os dados estatísticos"""
		self.settings = settings
		self.reset_stats()
		
	def reset_stats(self):
		"""Inicializa os dados estatísticos que podem mudar durante o jogo"""
		self.ships_left = self.settings.ship_limit	
	
