import pygame
import random
import enemy
padWidth = 1000
padHeight = 500

class BOSS():
    def __init__(self):
        super(BOSS, self).__init__()
        self.image = pygame.image.load('images/m01.png')
        self.size = (100,100)
        self.image = pygame.transform.scale(self.image, self.size)
        self.pos_x = 800
        self.pos_y = 340
        #self.speed = speed
        self.hitbox = (self.pos_x,self.pos_y,self.size[0],self.size[1])
        self.imagecount = 0
        self.monsterimage=[pygame.image.load('images/go1.png'),pygame.image.load('images/m02.png'),pygame.image.load('images/m03.png'),pygame.image.load('images/m04.png')]
        self.A = 0
        self.shootdelay = 0
        self.bossdelay = 0


    def shoot(self, bullets):
        if self.shootdelay % 40 == 0:

            bullet = enemy.MONSTER((self.pos_x,self.pos_y+40),23)
            bullets.add(bullet)
        self.shootdelay+=1

    def update(self):
        if self.shootdelay % 20 == 0:
            if(self.pos_y>130 and self.A ==0):
                self.pos_y-=70
                if self.pos_y==130:
                    self.A = 1
            if(self.pos_y>=130 and self.A==1):
                self.pos_y += 70
                if self.pos_y==340:
                    self.A = 0
            self.pos_x =self.pos_x
        self.bossdelay +=1
        

    def draw(self, gamePad):
        self.hitbox = (self.pos_x, self.pos_y, self.size[0], self.size[1])
        gamePad.blit(self.monsterimage[0], self.hitbox)
        #gamePad.blit(self.image,((self.pos_x, self.pos_y),(self.pos_x+self.size[0],self.pos_y+self.size[1])))