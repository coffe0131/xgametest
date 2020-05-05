import pygame
import random
padWidth = 1000
padHeight = 500

class MONSTER():
    def __init__(self,height,speed):
        super(MONSTER, self).__init__()
        self.image = pygame.image.load('images/m01.png')
        self.size = (70,70)
        self.image = pygame.transform.scale(self.image, self.size)
        self.pos_x = height[0]
        self.pos_y = height[1]
        self.speed = speed
        self.hitbox = (self.pos_x,self.pos_y,self.size[0],self.size[1])
        self.imagecount = 0
        self.monsterimage=[pygame.image.load('images/m01.png'),pygame.image.load('images/m02.png'),pygame.image.load('images/m03.png'),pygame.image.load('images/m04.png')]


    def update(self):
        self.pos_x -= self.speed
        

    def draw(self, gamePad):
        self.hitbox = (self.pos_x, self.pos_y, self.size[0]+self.speed, self.size[1]+self.speed)
        pygame.draw.rect(gamePad, (255, 0, 0), self.hitbox, 1) #사각형 테두리
        gamePad.blit(self.monsterimage[self.imagecount%4], self.hitbox)
        self.imagecount +=1
        #gamePad.blit(self.image,((self.pos_x, self.pos_y),(self.pos_x+self.size[0],self.pos_y+self.size[1])))