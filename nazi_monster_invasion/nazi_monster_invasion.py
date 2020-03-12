"""Criação de jogo de invasão alienígena"""

from settings import Settings
from ship import Ship
import game_functions as gf

import pygame #módulo

from pygame.sprite import Group

def run_game():
	#Inicializa o jogo e cria um objeto para a tela
	pygame.init()
	settings = Settings()
	screen = pygame.display.set_mode((settings.screen_width, settings.screen_height))
	pygame.display.set_caption("Alien Invasion")
	ship = Ship(settings, screen)
	#character = Character(settings, screen)
	nazi = Group()
	bullets = Group()
	
	#Cria uma frota de vilões
	gf.create_fleet(settings, screen, ship, nazi)
	
	#Inicia o laço principal do jogo
	while True:
		
		#Observa eventos de teclado e de mouse
		gf.check_events(settings, screen, ship, bullets)
		ship.update() #Atualização dos movimentos
		gf.update_bullets(bullets)
		gf.draw_screen(screen, settings)
		gf.update_screen_ship(ship, bullets)
		gf.update_screen_character(nazi, screen)
		

				
		#Sempre execução final
		gf.update_screen()
		
		
run_game()
