import pygame
import player, map, enemy,attack,items,startmenu,random
import music
padWidth = 1000
padHeight = 500

class game:
    def __init__(self):
        self.gamePad = pygame.display.set_mode((padWidth,padHeight))
        pygame.display.set_caption('Kirby')
        #curby = pygame.image.load("images/fighter.png").convert_alpha()
        self.clock = pygame.time.Clock()
        self.user = player.kirby()
        self.ground = map.BACKGROUND()
        self.game_state=True
        self.attacks=[]
        self.f_s_acctack=attack.Attack(self.user.pos_x+40,self.user.pos_y+20) #atteck class객체를 받아옴(x좌표,y좌표)
        self.item_eat=0 
        self.moncount = 1
        self.monsterheight = [(1000,400),(1000,200)]
        self.mon = enemy.MONSTER((1000,400),10)
        self.itemuse = 0
        self.heart = 3
        self.score = 0
        self.itempresent = 0
        self.item = items.ITEM()
        
    def itemmake(self):
        self.item = items.ITEM()
    def itemcall(self):
        if self.item.pos_x <=400 and self.itempresent==1:
            self.itempresent=0 
        self.item.update()
        self.item.draw(self.gamePad)  #아이템 출력
        self.itemuse = 1

        if self.user.collision(self.item.hitbox):  #커비랑 아이템이랑 충돌했을때 돌아감.
            self.item.pos_y += padHeight   #아이템이 화면에서 안보이고
            self.f_s_acctack.attack_type(type=1) #fire스킬**로 설정해줌
            self.user.eat_item = 'f' #이미지 받아올때 이미지 이름이 f이다.
            self.item_eat +=1  #

    def start(self):
        #crashed = False
        #mon = enemy.MONSTER()
        #item = items.ITEM()
        while self.game_state:
            if(self.moncount > 30):
                return 0
            if(self.heart < 1):
                return 0
            if(self.score >= 100):
                return 1
            self.events()
            if self.user.ishalf == True:
                self.ground.background_rotate(1)   #화면움직이는것 조정해줌
            self.ground.background_rotate()  #배경 업데이트

            self.user.walk(self.ground) #유저 업데이트
            self.user.update() #유저 점프
            self.user.draw(self.gamePad) #화면에 유저모습 출력

            if self.user.collision(self.mon.hitbox):  #커비랑 몬스터랑 충돌했을때 돌아감.
                self.mon.pos_x -= padWidth  
                self.heart -=1
                print("heart is ",self.heart)

            if self.mon.pos_x <= 0:
                if(self.moncount <10):
                    self.mon = enemy.MONSTER(random.choice(self.monsterheight),10)   #몬스터가 화면에서 없어지면 새 몬스터 출발
                if(10<=self.moncount<20):
                    if(self.moncount==10):
                        self.mon = enemy.MONSTER((1000,200),20)
                    if(self.moncount==11):
                        self.mon = enemy.MONSTER((1000,200),20)
                    if(self.moncount==12):
                        self.mon = enemy.MONSTER((1000,200),20)
                    else:
                        self.mon = enemy.MONSTER(random.choice(self.monsterheight),20)   #몬스터가 화면에서 없어지면 새 몬스터 출발
                if(20<=self.moncount):
                    if(self.moncount==20):
                        self.mon = enemy.MONSTER((1000,200),30)
                    if(self.moncount==21):
                        self.mon = enemy.MONSTER((1000,200),30)
                    if(self.moncount==23):
                        self.mon = enemy.MONSTER((1000,200),20)
                    else:
                        self.mon = enemy.MONSTER(random.choice(self.monsterheight),30)   #몬스터가 화면에서 없어지면 새 몬스터 출발
                self.moncount +=1
                print(self.moncount)

            self.mon.update()    #몬스터 상태 업데이트
            self.mon.draw(self.gamePad)  #화면에 몬스터 모습 출력

            if(self.itempresent==1):
                self.itemcall()
            if(self.moncount == 1 and self.itempresent == 0): 
                self.itemmake() #하나 만들기
                self.itempresent=1 #현재사용중으로 바꿔준다.
                self.itemcall()
            if(self.moncount == 11 and self.itempresent == 0):
                print("LEVEL UP")
                self.itemmake() #하나 만들기
                self.itempresent=1 #현재사용중으로 바꿔준다.
                self.itemcall()
            if(self.moncount == 21 and self.itempresent == 0):
                print("LEVEL UP")
                self.itemmake() #하나 만들기
                self.itempresent=1 #현재사용중으로 바꿔준다.
                self.itemcall()

            self.item.update()
            self.item.draw(self.gamePad)
            
            if self.itemuse == 1:
                if self.f_s_acctack.collision(self.mon.hitbox):  #불꽃이랑 몬스터랑 충돌했을때 돌아감.
                    self.mon.pos_x -= padWidth 
                    self.f_s_acctack.x+= padWidth
                    self.score +=5*self.item_eat
                    print("score is ",self.score)
                    #self.attacks.remove(i)
                    #self.f_s_acctack.y -= padHeight 
            
                for i in self.attacks:      #이 함수가 없으면 불꽃이 안생김
                    i.update()
                    i.draw(self.gamePad)
                    if i.x > padWidth: self.attacks.remove(i)           
            pygame.display.update()
            self.clock.tick(30)
        if heart<1:
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
                if self.item_eat != 0: #item을 먹으면 불꽃
                    if len(self.attacks)  < 1:
                        # self.attacks.append(attack.Attack(self.user.pos_x + 40, self.user.pos_y + 20))
                        self.f_s_acctack.x=self.user.pos_x + 37
                        self.f_s_acctack.y=self.user.pos_y + 30
                        self.attacks.append(self.f_s_acctack)
                else: pass

