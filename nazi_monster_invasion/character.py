import pygame
from pygame.sprite import Sprite

class Character(Sprite):
	
	def __init__(self, settings, screen):
		"""Inicialiaza a espaçonave e define sua posição inicial."""
		super(Character, self).__init__()
		self.screen = screen
		self.settings = settings
		
		#Carrega a imagem do vilão e obtém seu rect
		self.image = pygame.image.load('images/nazi_monster.bmp')
		self.rect = self.image.get_rect()
		
		#Inicia cada novo vilão próximo a parte superior esquerda da tela
		self.rect.x = self.rect.width
		self.rect.y = self.rect.height
		
		#Armazena a posição exata do vilão
		self.x = float(self.rect.x)

	def blitme(self):
		"""Desenha a espaçonave em sua posição atual"""
		self.screen.blit(self.image, self.rect)
