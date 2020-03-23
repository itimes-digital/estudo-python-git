import pygame
from pygame.sprite import Sprite

class Nazi_Monster(Sprite):
	
	def __init__(self, settings, screen):
		"""Inicialiaza a espaçonave e define sua posição inicial."""
		super(Nazi_Monster, self).__init__()
		self.screen = screen
		self.settings = settings
		
		#Carrega a imagem do vilão e obtém seu rect
		self.image = pygame.image.load('images/nazi_monster_v2.png')
		self.rect = self.image.get_rect()
		
		#Inicia cada novo vilão próximo a parte superior esquerda da tela
		self.rect.x = self.rect.width
		self.rect.y = self.rect.height
		
		#Armazena a posição exata do vilão
		self.x = float(self.rect.x)

	def blitme(self):
		"""Desenha a espaçonave em sua posição atual"""
		self.screen.blit(self.image, self.rect)
		
	def update(self):
		"""Move o nazi para a direita ou para esquerda"""
		self.x += (self.settings.nazi_speed_factor *
					self.settings.fleet_direction)
		self.rect.x = self.x
		
	def check_edges(self):
		"""Devolve True se o alienígena estiver na borda da tela"""
		screen_rect = self.screen.get_rect()
		if self.rect.right >= screen_rect.right:
			return True
		elif self.rect.left <= 0:
			return True
