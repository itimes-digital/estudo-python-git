import sys
from bullet import Bullet
from key import Key
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
		
	if event_current == Key.K_Q.value:#Letra Q
		#Cria um novo projétil e o adiciona ao grupo de projéteis
		fire_bullet(settings, screen, ship, bullets, Key.K_Q.value)

	if event_current == Key.K_W.value:#Letra W
		#Cria um novo projétil e o adiciona ao grupo de projéteis
		fire_bullet(settings, screen, ship, bullets, Key.K_W.value)

		
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

def update_screen_character(character):
	"""Atualiza as imagens na tela e alterna para a nova tela."""
	character.blitme()
	
def update_screen_character_up(character):
	"""Atualiza as imagens na tela e alterna para a nova tela."""
	character.up()
	
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
	


	
	
