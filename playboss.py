import pygame
import player, map, enemy,attack,items,startmenu,random
import boss
from time import sleep
import music
padWidth = 1000
padHeight = 500
#font = pygame.font.Font("font/Maplestory Bold.ttf", 50)


class game:
    def __init__(self):
        self.gamePad = pygame.display.set_mode((padWidth,padHeight))
        pygame.display.set_caption('Kirby')
        #curby = pygame.image.load("images/fighter.png").convert_alpha()
        self.font = pygame.font.Font("font/Maplestory Bold.ttf", 50)
        self.clock = pygame.time.Clock()
        self.user = player.kirby()
        self.ground = map.BACKGROUND()
        self.game_state=True
        self.attacks=[]
        self.f_s_acctack=attack.Attack(self.user.pos_x+40,self.user.pos_y+20,20) #atteck class객체를 받아옴(x좌표,y좌표)
        self.item_eat=0 
        self.itemuse = 1
        self.score = 0
        self.itempresent = 0
        self.item = items.ITEM()
        self.levelup = self.font.render("LEVELUP",1,(255,0,0))
        self.levelupcount = 11
        self.bossM = boss.BOSS()
        self.bossheart = 3
        self.bullets = pygame.sprite.Group()
        
    

    def start(self):
        self.f_s_acctack.attack_type(type=1) #fire스킬**로 설정해줌
        self.user.eat_item = 'f' #이미지 받아올때 이미지 이름이 f이다.
        self.item_eat +=1  #
        self.levelupcount = 10
        times = 500
        i = 0
        while i in range(100):
            bosstext = self.font.render("BOSS STAGE",1,(50,50,50))
            print(bosstext)
            bosstext2 = self.font.render("YOU HAVE TO HEAT BOSS 3 TIMES",1,(50,50,50))
            print(bosstext)
            self.gamePad.blit(bosstext,(50,50))
            self.gamePad.blit(bosstext2,(750,0))
            i+=1

        while self.game_state:
            if(times <= 0):
                return 0
                print("TIME OUT")
            if(self.user.heart < 1):
                return 0
                print("GAME OVER")
            if(self.bossheart <= 0):
                print("CLEAR")
                return 1
            
            self.events()
            if self.user.ishalf == True:
                self.ground.background_rotate(1)   #화면움직이는것 조정해줌
            self.ground.background_rotate()  #배경 업데이트

            self.user.walk(self.ground) #유저 업데이트
            self.user.update() #유저 점프
            self.user.draw(self.gamePad) #화면에 유저모습 출력
            self.bossM.shoot(self.bullets)
            self.user.hit(self.bullets)
            self.bullets.update()

            timeout = self.font.render("Time : %d"%(times),1,(50,50,50))
            text2 = self.font.render("Heart : %d"%(self.user.heart),1,(50,50,50))
            times = times -1
            self.gamePad.blit(text2,(0,0))
            self.gamePad.blit(timeout,(750,0))
            self.bossM.update()    
            self.bossM.draw(self.gamePad)
            self.bullets.draw(self.gamePad)

            """if self.user.collision(self.bossM.bullets):  #커비랑 몬스터랑 충돌했을때 돌아감.
                ##불렛으로 고쳐야함
                self.bossM.bullets.pos_x -= padWidth  
                self.user.heart -=1
                print("heart is ",self.user.heart)"""

            if self.itemuse == 1:
                if self.f_s_acctack.collision(self.bossM.hitbox):  #불꽃이랑 몬스터랑 충돌했을때 돌아감.
                    self.bossheart -=1
                    self.f_s_acctack.x+= padWidth
                    print("bossheart is ",self.bossheart)
            
                for i in self.attacks:      #이 함수가 없으면 불꽃이 안생김
                    i.update()
                    i.draw(self.gamePad)
                    if i.x > padWidth: self.attacks.remove(i)           
            pygame.display.update()
            self.clock.tick(30)
        if self.user.heart<1:
            return 0
        else:
            return 1

    def events(self):
        for event in pygame.event.get():
            if event.type in [pygame.QUIT]:
                pygame.quit()

            key_event = pygame.key.get_pressed()

            if event.type == pygame.K_ESCAPE:
                if key_event[pygame.K_ESCAPE]:
                    self.game_state = False
            if event.type == pygame.KEYDOWN:
                if key_event[pygame.K_LEFT] and self.user.pos_x > self.user.vel:
                    self.user.left = True
                elif key_event[pygame.K_RIGHT] and self.user.pos_x < 500 - self.user.size[0] - self.user.vel:
                    self.user.right = True
            elif event.type == pygame.KEYUP:
                if event.key == pygame.K_RIGHT:
                    self.user.ishalf = False
                    self.user.right = False
                elif event.key == pygame.K_LEFT:
                    self.user.left = False
            if not (self.user.isJump):
                if key_event[pygame.K_SPACE]:
                    self.user.isJump = True
                    self.user.walkCount = 0
                    
            if key_event[pygame.K_a]: #key a를 누르면 불꽃 나감
                        # self.attacks.append(attack.Attack(self.user.pos_x + 40, self.user.pos_y + 20))
                self.f_s_acctack.x=self.user.pos_x + 37
                self.f_s_acctack.y=self.user.pos_y + 30
                self.attacks.append(self.f_s_acctack)
