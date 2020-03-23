"""Criação de jogo de invasão alienígena"""

from settings import Settings
from ship import Ship
from game_stats import GameStats
import game_functions as gf

import pygame #módulo

from pygame.sprite import Group

def run_game():
	#Inicializa o jogo e cria um objeto para a tela
	pygame.init()
	
	running = True
	#speed = 60
	
	settings = Settings()
	screen = pygame.display.set_mode((settings.screen_width, settings.screen_height))
	pygame.display.set_caption("Nazi Invasion")
	"""Cria uma instância para armazenar dados estatísticos do jogo"""
	stats = GameStats(settings)
	clock = pygame.time.Clock()
	#Espaço sideral
	background = [pygame.image.load('images/background_v1.png').convert(),
				pygame.image.load('images/background_v2.png').convert(),
				pygame.image.load('images/background_v3.png').convert(),
				pygame.image.load('images/background_v4.png').convert()]
	
	#Espaçonave
	ship = Ship(settings, screen)
	
	#nazi = Nazi_Monster(settings, screen)
	nazis = Group()
	
	#bullets
	bullets = Group()
	
	#Cria uma frota de vilões
	gf.create_fleet(settings, screen, ship, nazis)

	#Inicia o laço principal do jogo
	while running:
		
		#Observa eventos de teclado e de mouse
		gf.check_events(settings, screen, ship, bullets)
		gf.update_bullets(settings, screen, ship, nazis, bullets)
		gf.update_nazis(settings, stats, screen, ship, nazis, bullets)
		gf.draw_screen(screen, settings, background)
		ship.update(background) #Atualização dos movimentos
		gf.update_screen_ship(ship, bullets)
		gf.update_screen_nazi_monster(nazis, screen)
		

		#pygame.time.set_timer(USEREVENT+1, 500)	
		#Sempre execução final
		gf.update_screen()
		
		#clock.tick(speed)
		
run_game()
