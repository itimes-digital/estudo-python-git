import pygame

class Ship():
	
	def __init__(self, ai_settings, screen):
		"""Inicialiaza a espaçonave e define sua posição inicial."""
		self.screen 		= screen
		self.ai_settings 	= ai_settings
		#Carrega a imagem da espaçonave e obtém seu rect
		self.image 			= pygame.image.load('images/ship.bmp')
		self.rect 			= self.image.get_rect()
		self.screen_rect 	= screen.get_rect()
		self.center 		= float(self.rect.centerx)
		
		#Inicia cada nova espaçonave na parte inferior central da tela
		self.rect.centerx 	= self.screen_rect.centerx
		self.rect.centery 	= self.screen_rect.centery
		self.rect.bottom 	= self.screen_rect.bottom
		
		#Flags de movimento
		self.moving_right 	= False
		self.moving_left 	= False
		self.moving_top 	= False
		self.moving_bottom 	= False
		
	def update(self):
		"""Atualiza a posição da espaçonave de acordo com a flag de movimento"""
		if self.moving_right and self.rect.right < self.screen_rect.right:
			self.center += self.ai_settings.ship_speed_factor
		
		if self.moving_left and self.rect.left > 0:
			self.center -= self.ai_settings.ship_speed_factor
		
		if self.moving_top and self.rect.top > self.screen_rect.top:
			self.rect.top -= self.ai_settings.ship_speed_factor
		
		if self.moving_bottom and self.rect.bottom < self.screen_rect.bottom:
			self.rect.top += self.ai_settings.ship_speed_factor
			
		#Atualiza o objeto rect de acordo com self.center
		self.rect.centerx = self.center
			
	def update_jump():
		"""Atualiza a posição da espaçonave de acordo com a flag de movimento"""
		if self.moving_right:
			self.rect.centerx += self.ai_settings.ship_speed_factor
		elif self.moving_left:
			self.rect.centerx -= self.ai_settings.ship_speed_factor
			
	def blitme(self):
		"""Desenha a espaçonave em sua posição atual"""
		self.screen.blit(self.image, self.rect)

