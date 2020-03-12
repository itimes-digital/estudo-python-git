import sys

import pygame

def check_events(ship):
	"""Responde a eventos de pressionamento de teclas e de mouse"""

	for event in pygame.event.get():
		
		if event.type == pygame.QUIT:
			sys.exit()
		
		elif event.type == pygame.KEYDOWN:
			event_keydown(event, ship)
		
		elif event.type == pygame.KEYUP:
			event_keyup(event, ship)

def event_keydown(event, ship):
	
	event_current = event.key
	
	if event_current == pygame.K_RIGHT:
		#Move a espaçonave para a direita
		ship.moving_right = True
	
	if event_current == pygame.K_LEFT:
		#Move a espaçonave para a esquerda
		ship.moving_left = True
	
	if event_current == pygame.K_UP:
		#Move a espaçonave para cima
		ship.moving_top = True
	
	if event_current == pygame.K_DOWN:
		#Move a espaçonave para baixo
		ship.moving_bottom = True

		
def event_keyup(event, ship):
	if event.key == pygame.K_RIGHT:
		ship.moving_right = False
	
	if event.key == pygame.K_LEFT:
		ship.moving_left = False
	
	if event.key == pygame.K_UP:
		ship.moving_top = False
	
	if event.key == pygame.K_DOWN:
		ship.moving_bottom = False
									
					
def draw_screen(screen, ai_settings):
	#Redesenha a tela a cada passagem pelo laço
	screen.fill(ai_settings.bg_color)

def update_screen():
	#Deixa a tela mais recente visível
	pygame.display.flip()

def update_screen_ship(ship):
	"""Atualiza as imagens na tela e alterna para a nova tela."""
	ship.blitme()

def update_screen_character(character):
	"""Atualiza as imagens na tela e alterna para a nova tela."""
	character.blitme()
	


	
	
