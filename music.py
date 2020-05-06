import pygame
from pygame import *


pygame.mixer.init()
musics=['music/Ice_Cream_Island.mp3', 'music/boss.mp3']

class MUSIC:
    def __init__(self):
        self.music=pygame.mixer.music.load(musics[0])
        self.jump=pygame.mixer.Sound('music/jump.wav')
        self.item=pygame.mixer.Sound('music/itemget.wav')
        self.boom=pygame.mixer.Sound('music/fireattack.wav')
        self.fire=pygame.mixer.Sound('music/boom.wav')

    def mplay(self,i):
        self.music = pygame.mixer.music.load(musics[i])
        pygame.mixer.music.set_volume(0.35)
        pygame.mixer.music.play(-1)


