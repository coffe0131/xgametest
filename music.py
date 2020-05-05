import pygame
from pygame import *

def mplay(sound):
    pygame.mixer.init()
    pygame.mixer.music.load('music/Ice_Cream_Island.mp3')
    pygame.mixer.music.set_volume(sound)
    pygame.mixer.music.play(-1)



