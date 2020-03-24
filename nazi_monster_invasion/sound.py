"""Classe que realiza o gerenciamento de sons do jogo"""
import pygame
import pygame.mixer

class Sound():
	
	def __init__(self, frequency, size, channels, buffersize, devicename):
		pygame.mixer.pre_init(frequency, size, channels, buffersize, devicename)

	def set_song(self, nr_channel, sound):
		pygame.mixer.Channel(nr_channel).play(self.mixer.Sound(sound))
		pygame.mixer.music.play(0)
		pygame.mixer.music.set_volume(0.5)

	def eternal_song(self, nr_channel, sound):
		pygame.mixer.Channel(nr_channel).play(pygame.mixer.Sound(sound))
		pygame.mixer.music.play(-1)
