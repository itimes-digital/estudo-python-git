import sys
from bullet import Bullet
from key import Key
from character import Character
import pygame

def check_events(settings, screen, ship, bullets):
	"""Responde a eventos de pressionamento de teclas e de mouse"""

	for event in pygame.event.get():
		
		if event.type == pygame.QUIT:
			sys.exit()
		
		elif event.type == pygame.KEYDOWN:
			event_keydown(event, settings, screen, ship, bullets)
		
		elif event.type == pygame.KEYUP:
			event_keyup(event, ship)

def event_keydown(event, settings, screen, ship, bullets):
	
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
	
	if event_current == pygame.K_SPACE:
		#Cria um novo projétil e o adiciona ao grupo de projéteis
		fire_bullet(settings, screen, ship, bullets, None)
		
	if event_current == pygame.K_v:#Letra V
		#Cria um novo projétil e o adiciona ao grupo de projéteis
		fire_bullet(settings, screen, ship, bullets, Key.K_V.value)

	if event_current == pygame.K_b:#Letra B
		#Cria um novo projétil e o adiciona ao grupo de projéteis
		fire_bullet(settings, screen, ship, bullets, Key.K_B.value)
		
	if event_current == pygame.K_q:#Letra Q
		sys.exit()

		
def event_keyup(event, ship):
	if event.key == pygame.K_RIGHT:
		ship.moving_right = False
	
	if event.key == pygame.K_LEFT:
		ship.moving_left = False
	
	if event.key == pygame.K_UP:
		ship.moving_top = False
	
	if event.key == pygame.K_DOWN:
		ship.moving_bottom = False
									
					
def draw_screen(screen, settings):
	#Redesenha a tela a cada passagem pelo laço
	screen.fill(settings.bg_color)

def update_screen():
	#Deixa a tela mais recente visível
	pygame.display.flip()

def update_screen_ship(ship, bullets):
	"""Atualiza as imagens na tela e alterna para a nova tela."""
	
	for bullet in bullets.sprites():
		bullet.draw_bullet()
		
	ship.blitme()

def update_screen_character(character, screen):
	"""Atualiza as imagens na tela e alterna para a nova tela."""
	character.draw(screen)
	#haracter.blitme()
	
	
def update_bullets(bullets):
	"""Atualiza a posição dos projéteis e se livra ds projéteis antigos"""
	#Atualiza as posições dos projéteis
	bullets.update()
	
	#Livra-se dos projéteis que desapareceram
	for bullet in bullets.copy():
		if bullet.rect.bottom <= 0:
			bullets.remove(bullet) 
			
def fire_bullet(settings, screen, ship, bullets, enumKey):
	"""Dispara um projétil se o limite ainda não foi alcançado"""
	#Cria um novo projétil e o adiciona ao grupo de projéteis
	if len(bullets) < settings.bullets_allowed:
		new_bullet = Bullet(settings, screen, ship, enumKey)
		bullets.add(new_bullet)
		
def create_fleet(settings, screen, ship, nazis):
	"""Cria uma frota completa de monstrinhos nazistas"""
	#Cria um nazi e calcula o número de nazis em uma linha
	#O espaçamento entre os nazis é igual à largura de um nazi
	nazi = Character(settings, screen)
	number_nazi_x = get_number_nazis_x(settings, nazi.rect.width)
	number_rows = get_number_rows(settings, 
								ship.rect.height, 
								nazi.rect.height)
	
	#Cria a primeira linha de nazis
	for row_number in range(number_rows):
		for nazi_number in range(number_nazi_x):
			create_nazi(settings, screen, nazis, nazi_number, row_number)
		
def get_number_nazis_x(settings, nazi_width):
	"""Determina o número de nazis que cabem em uma linha"""
	available_space_x 	= settings.screen_width - 2 * nazi_width
	number_nazis_x 		= int(available_space_x / (2 * nazi_width))
	return number_nazis_x

def create_nazi(settings, screen, nazis, nazi_number, row_number):
	#Cria um nazi e o posiciona na linha
	nazi 				= Character(settings, screen)
	nazi_width 			= nazi.rect.width
	nazi.x 				= nazi_width + 2 * nazi_width * nazi_number
	nazi.rect.x 		= nazi.x
	nazi.rect.y 		= nazi.rect.height + 2 * nazi.rect.height * row_number
	nazis.add(nazi)
	
	
def get_number_rows(settings, ship_height, nazi_height):
	"""Determine o número de linhas com nazis que cabem na tela"""
	available_space_y = (settings.screen_height - (3 * nazi_height) - ship_height)

	number_rows = int(available_space_y / (2 * nazi_height))
	return number_rows
	


	
	
