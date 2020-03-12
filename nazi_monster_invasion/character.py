import pygame

class Character():
	
	def __init__(self, screen):
		"""Inicialiaza a espaçonave e define sua posição inicial."""
		self.screen = screen
		
		#Carrega a imagem da espaçonave e obtém seu rect
		self.image = pygame.image.load('images/nazi_monster.bmp')
		self.rect = self.image.get_rect()
		self.screen_rect = screen.get_rect()
		
		#Inicia cada nova espaçonave na parte inferior central da tela
		self.rect.centerx = self.screen_rect.centerx
		self.rect.centery = self.screen_rect.centery

	def blitme(self):
		"""Desenha a espaçonave em sua posição atual"""
		self.screen.blit(self.image, self.rect)
