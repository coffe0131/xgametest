import pygame
#여기에 fire
fire_attack=[pygame.image.load('images/fire.png'),
             pygame.image.load('images/fire.png'),
             pygame.image.load('images/fire.png')]

class Attack:
    def __init__(self,x,y):
        super(Attack, self).__init__()
        self.size = [4,4]
        self.height = 4
        self.speed = 10
        self.x=x
        self.y=y
        self.image_type=[]
        self.rect = pygame.Rect((self.x, self.y), (self.size[0], self.size[1]))
        self.attackcount = 0

    # item에서 불,스파크 아이템 먹으면 해당 스킬 사용 지정
    def attack_type(self, type):
        print(type)
        if type == 1:
            self.image_type=fire_attack


    def update(self):
        self.x += self.speed
        self.rect = pygame.Rect((self.x, self.y), (self.size[0], self.size[1]))
        self.attackcount += 1

    def is_screen_out(self):
        return self.x + self.speed >= 800

    def draw(self,gamePad):
        self.hitbox = ((self.x, self.y),(self.size[0], self.size[1]))
        gamePad.blit(self.image_type[self.attackcount % 3], self.rect)
        pygame.draw.rect(gamePad, (255, 0, 0), self.hitbox, 1)

    def collision(self,item_hitbox):
        
        if self.rect.colliderect(item_hitbox):  #self를 둘러싼 사각형 이미지 박스 - 아이템이랑 부딪히면 true
                return True
        
        return False

