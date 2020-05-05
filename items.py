import pygame,random
padWidth = 1000
padHeight = 500


class ITEM():
    def __init__(self):
        super(ITEM, self).__init__()
        self.image = pygame.image.load('images/fire1.png')
        self.size = (25,25)
        self.image = pygame.transform.scale(self.image, self.size)
        self.pos_x = 1000
        self.pos_y = 250
        self.speed = 5
        self.hitbox = (self.pos_x,self.pos_y,self.size[0],self.size[1])

    def update(self):
        self.pos_x -= self.speed

    def draw(self, gamePad):
        self.hitbox = (self.pos_x, self.pos_y, self.size[0]+self.speed, self.size[1]+self.speed)
        gamePad.blit(self.image, self.hitbox)
        #((self.pos_x, self.pos_y),(self.size[0],self.pos_y+self.size[1]))