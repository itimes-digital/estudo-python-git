"""Criação de jogo de invasão alienígena"""

from settings import Settings
from ship import Ship
from character import Character
import game_functions as gf

import pygame #módulo

def run_game():
	#Inicializa o jogo e cria um objeto para a tela
	pygame.init()
	settings = Settings()
	screen = pygame.display.set_mode((settings.screen_width, settings.screen_height))
	pygame.display.set_caption("Alien Invasion")
	ship = Ship(settings, screen)
	character = Character(screen)
	
	font = pygame.font.Font('freesansbold.ttf', 32) 
	
	
	#Inicia o laço principal do jogo
	while True:
		
		#Observa eventos de teclado e de mouse
		gf.check_events(ship)
		ship.update() #Atualização dos movimentos
		gf.draw_screen(screen, settings)
		gf.update_screen_ship(ship)
		gf.update_screen_character(character)
		
		#Sempre execução final
		gf.update_screen()
		
		
run_game()
