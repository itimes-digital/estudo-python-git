"""Classe que realiza o gerenciamento de sons do jogo"""
import pygame
from pygame import mixer
import time

class Sound_Game():
	
	def __init__(self, frequency, size, channels, buffersize):
		mixer.init(frequency, size, channels, buffersize)

	def eternal_song(soundfile, duration_secs):
		"""Play a soundfile for a configurable duration"""
		mixer.music.load(soundfile)
		mixer.music.play(-1)
		time.sleep(duration_secs)
		
	def play_effects(soundfile, duration_secs):
		"""Play a soundfile for a configurable duration"""
		effect = pygame.mixer.Sound(soundfile)
		effect.play()
		time.sleep(duration_secs)
		mixer.music.stop()
		mixer.quit()

# Play for 5 seconds
#play('sound/People_Get_Up_And_Drive_Your_Funky_Soul_Remix.mp3', 20)
#play_effects('sound/explosao_v2.wav', 10)
#play_effects('sound/tiro.mp3', 5)
 

