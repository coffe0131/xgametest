import pygame
import map
import boss
import attack
import items
char1_l=[pygame.image.load('images/l01.png'),
         pygame.image.load('images/l02.png'),
         pygame.image.load('images/l03.png'),
         pygame.image.load('images/l04.png'),
         pygame.image.load('images/l05.png')]
char1_r=[pygame.image.load('images/r01.png'),
         pygame.image.load('images/r02.png'),
         pygame.image.load('images/r03.png'),
         pygame.image.load('images/r04.png'),
         pygame.image.load('images/r05.png')]


class kirby():
    def __init__(self):
        super(kirby, self).__init__()
        self.image = pygame.image.load('images/r01.png')
        self.size = (50,50)
        self.image = pygame.transform.scale(self.image,self.size)
        print(self.image.get_rect())
        self.isJump = False
        self.pos_x = 50
        self.pos_y = 370
        self.vel = 5
        self.left = False
        self.right = False
        self.jumpCount = 10
        self.walkCount = 0
        self.ishalf = False
        self.rect = pygame.Rect((self.pos_x,self.pos_y),(self.size[0],self.size[1]))
        self.eat_item=''
        self.heart = 3

    def walk(self, ground):
        if self.walkCount +1 >= 12:
                self.walkCount = 0
        if self.left:
            if self.pos_x>20:
                self.change_pos(-self.vel,0)
            self.image_load(0)
            self.walkCount += 1
        elif self.right:
            if self.pos_x > 350:
                self.ishalf = True
            else:
                self.ishalf = False
                self.change_pos(self.vel,0)
            self.image_load(1)
            self.walkCount += 1
        else:
            self.image_load(2)

    def update(self):
        if self.isJump == True:
            if self.jumpCount >=-10:
                neg = 1
                if self.jumpCount <0:
                    neg = -1
                self.pos_y -=(self.jumpCount**2)*0.5*neg
                self.jumpCount -=1
            else:
                self.isJump = False
                self.jumpCount = 10

    def change_pos(self,x,y):
        self.pos_x = self.pos_x +x
        self.pos_y = self.pos_y +y
        self.rect = pygame.Rect(((self.pos_x,self.pos_y),(self.pos_x+self.size[0],self.pos_y+self.size[1])))

    def draw(self,gamePad):
        self.rect = pygame.Rect((self.pos_x+5, self.pos_y+20),(self.size[0]+7,self.size[1]+7))
        #pygame.draw.rect(gamePad,(255,0,0),self.rect,2) #사각형 테두리
        gamePad.blit(self.image, self.rect)

    def image_load(self, stat): 
        walkLeft = [pygame.image.load('images/'+self.eat_item+'l0'+str(i)+'.png') for i in range(1,6)]
        walkRight = [pygame.image.load('images/'+self.eat_item+'r0'+str(i)+'.png') for i in range(1,6)]
        
        if stat == 0:
            self.image = walkLeft[self.walkCount%5]
        elif stat == 1:
            self.image = walkRight[self.walkCount%5]
        elif stat == 2:
            self.image = pygame.image.load('images/'+self.eat_item+'r01.png')
        


    def collision(self,item_hitbox):
        if self.rect.colliderect(item_hitbox):  #self를 둘러싼 사각형 이미지 박스 - 아이템이랑 부딪히면 true
                return True
        return False

    def hit(self, bullets):
        hits = pygame.sprite.spritecollide(self,bullets,True)
        if hits:
            self.heart -= 1


