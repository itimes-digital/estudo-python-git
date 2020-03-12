"""Criação de jogo de invasão alienígena"""

from settings import Settings
from ship import Ship
from character import Character
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
	character = Character(screen)
	
	bullets = Group()
	
	
	#Inicia o laço principal do jogo
	while True:
		
		#Observa eventos de teclado e de mouse
		gf.check_events(settings, screen, ship, bullets)
		ship.update() #Atualização dos movimentos
		gf.update_bullets(bullets)
		gf.draw_screen(screen, settings)
		gf.update_screen_ship(ship, bullets)
		gf.update_screen_character(character)
		

				
		#Sempre execução final
		gf.update_screen()
		
		
run_game()
