import sys
from bullet import Bullet
from key import Key
from nazi_monster import Nazi_Monster
import pygame
import pygame.mixer
from random import randint
from time import sleep

def check_events(settings, screen, ship, bullets, sound):
	"""Responde a eventos de pressionamento de teclas e de mouse"""

	for event in pygame.event.get():
		
		if event.type == pygame.QUIT:
			sys.exit()
		
		elif event.type == pygame.KEYDOWN:
			event_keydown(event, settings, screen, ship, bullets, sound)
		
		elif event.type == pygame.KEYUP:
			event_keyup(event, ship)

def event_keydown(event, settings, screen, ship, bullets, sound):
	
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
		sound.set_song(1, 'sound/zapsplat_cartoon_rocket_launch_missle.mp3')
		fire_bullet(settings, screen, ship, bullets, None)
		
	if event_current == pygame.K_v:#Letra V
		#Cria um novo projétil e o adiciona ao grupo de projéteis
		fire_bullet(settings, screen, ship, bullets, Key.K_V.value)

	if event_current == pygame.K_b:#Letra B
		#Cria um novo projétil e o adiciona ao grupo de projéteis
		fire_bullet(settings, screen, ship, bullets, Key.K_B.value)
		
	if event_current == pygame.K_a:#Letra L
		#Cria um novo projétil e o adiciona ao grupo de projéteis
		fire_bullet(settings, screen, ship, bullets, Key.K_A.value)
	
	if event_current == pygame.K_s:#Letra L
		#Cria um novo projétil e o adiciona ao grupo de projéteis
		fire_bullet(settings, screen, ship, bullets, Key.K_S.value)
		
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
									
					
def draw_screen(screen, settings, background):
	#Redesenha a tela a cada passagem pelo laço
	#
	screen.fill(settings.bg_color)
	screen.blit(background[0], (0,0))
	

def update_screen():
	#Deixa a tela mais recente visível
	pygame.display.flip()

def update_screen_ship(ship, bullets):
	"""Atualiza as imagens na tela e alterna para a nova tela."""
	
	for bullet in bullets.sprites():
		bullet.draw_bullet()
		
	ship.blitme()


def update_screen_nazi_monster(nazi, screen):
	"""Atualiza as imagens na tela e alterna para a nova tela."""
	nazi.draw(screen)
	#character.blitme()
	
	
def update_bullets(settings, screen, ship, nazis, bullets, sound):
	"""Atualiza a posição dos projéteis e se livra ds projéteis antigos"""
	#Atualiza as posições dos projéteis
	bullets.update()
	
	#Livra-se dos projéteis que desapareceram
	for bullet in bullets.copy():
		if bullet.rect.bottom <= 0:
			bullets.remove(bullet)
		if bullet.rect.right >= 1200:
			bullets.remove(bullet)
		if bullet.rect.left <= -600:
			bullets.remove(bullet)
			
	check_bullet_nazi_collisions(settings, screen, ship, nazis, bullets, sound)
	
def check_bullet_nazi_collisions(settings, screen, ship, nazis, bullets, sound):
	"""Responde a colisões entre projéteis e nazis"""
	#Remove qualquer projétil e nazi que tenham colidido
	
	collisions = pygame.sprite.groupcollide(bullets, nazis, True, True) 
	
	if len(collisions) == 0:
		sound.set_song(2, 'sound/audio_hero_ExplosionSmall_DIGIJ02_24_351.mp3')
	
	if len(nazis) == 0:
		"""Destrói os projéteis existentes e cria uma nova frota"""
		bullets.empty()
		nazis.empty()
		create_fleet(settings, screen, ship, nazis)		
			
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
	nazi 			= Nazi_Monster(settings, screen)
	number_nazi_x 	= get_number_nazis_x(settings, nazi.rect.width)
	number_rows 	= get_number_rows(settings, 
									ship.rect.height, 
									nazi.rect.height)
	
	#Cria a primeira linha de nazis
	for row_number in range(number_rows):
		for nazi_number in range(number_nazi_x):
			create_nazi(settings, screen, nazis, nazi_number, row_number)
		
def get_number_nazis_x(settings, nazi_width):
	"""Determina o número de nazis que cabem em uma linha"""

	available_space_x 	= settings.screen_width - (2 * nazi_width)
	number_nazis_x 		= int(available_space_x / (2 * nazi_width))
	return number_nazis_x

def create_nazi(settings, screen, nazis, nazi_number, row_number):
	#Cria um nazi e o posiciona na linha
	nazi 				= Nazi_Monster(settings, screen)
	nazi_width 			= nazi.rect.width
	nazi.x 				= nazi_width + (randint(0, 2) * nazi_width * nazi_number)
	nazi.rect.x 		= nazi.x + 10
	nazi.rect.y 		= nazi.rect.height + (2 * nazi.rect.height * row_number)
	nazis.add(nazi)
	
	
def get_number_rows(settings, ship_height, nazi_height):
	"""Determine o número de linhas com nazis que cabem na tela"""

	available_space_y 	= (settings.screen_height - (4 * nazi_height) - ship_height)

	number_rows = int(available_space_y / (4 * nazi_height))
	return number_rows
	
def scroll_background(screen, background, a, b):
	
	for i in range(4):
		screen.blit(background[i], (a, b))
		
def update_nazis(settings, stats, screen, ship, nazis, bullets):
	"""
	Verifica se a frota está em uma das bordas e então
	atualiza as posições de todos os nazis da frota"""
	check_fleet_edges(settings, nazis)
	nazis.update()
	
	if pygame.sprite.spritecollideany(ship, nazis):
		#print("Ohhh nooooo... Ship hit!!!")
		ship_hit(settings, stats, screen, ship, nazis, bullets)
	
	#Verifica se há algum nazi que atingiu a parte inferior da tela
	check_nazis_botton(settings, stats, screen, ship, nazis, bullets)
	
def check_fleet_edges(settings, nazis):
	"""responde apropriadamente se algum nazis alcançou uma borda"""
	for nazi in nazis.sprites():
		if nazi.check_edges():
			change_fleet_direction(settings, nazis)
			break
			
def change_fleet_direction(settings, nazis):
	"""Faz toda a frota descer e muda a sua direção"""
	for nazi in nazis.sprites():
		nazi.rect.y += settings.fleet_drop_speed
	settings.fleet_direction *= -1
	

def ship_hit(settings, stats, screen, ship, nazis, bullets):
	"""Responde ao fato de a espaçonave ter sido atingida por um nazi"""
	#Decrementa ships_left
	stats.ships_left -= 1
	
	#Esvazia a lista de alienígenas e de projéteis
	nazis.empty()
	bullets.empty()
	
	#Cria uma nova frota e centraliza e espaçonave
	create_fleet(settings, screen, ship, nazis)
	ship.center_ship()
	
	#Faz uma pausa
	sleep(0.5)	
	
def check_nazis_botton(settings, stats, screen, ship, nazis, bullets):
	"""Verifica se algum nazi alcançou a parte inferior da tela"""
	screen_rect = screen.get_rect()
	for nazi in nazis.sprites():
		if nazi.rect.bottom >= screen_rect.bottom:
			#Trata esse caso do mesmo modo que é feito quando
			#a espaçonave é atingida
			ship_hit(settings, stats, screen, ship, nazis, bullets)
			break
