import pygame
from pygame import*
from pygame.locals import*
import keyboard
import playgame
import music

music.mplay(0.3)
pygame.init()
width,height = 500,500
#start이미지, option 이미지, cursor 이미지
image=[pygame.transform.scale(pygame.image.load("images/back.png"),(500,500)),
       pygame.image.load("images/as.jpg"),
       pygame.image.load("images/cursor.png"),
       pygame.transform.scale(pygame.image.load("images/gameover.png"),(1000,400)),
       pygame.image.load("images/w1.png"),
       pygame.image.load("images/clear.jpg")]

font1 = pygame.font.Font("font/Maplestory Bold.ttf", 50)
font2 = pygame.font.Font("font/Maplestory Light.ttf", 80)
st_op_buttons=[font1.render("START", True, (0, 255, 0)),
               font1.render('OPTION', True,(0,255,0)),
               pygame.transform.scale(pygame.image.load("images/continue.png"),(200,80)),
               pygame.transform.scale(pygame.image.load("images/quit.png"),(200,80)),
               font2.render("CLEAR !",True,(0,255,0))]

st_op_rect=[st_op_buttons[0].get_rect(x=200,y=300),
            st_op_buttons[1].get_rect(x=160,y=120),
            st_op_buttons[2].get_rect(x=400,y=220),
            st_op_buttons[3].get_rect(x=400,y=280),
            st_op_buttons[4].get_rect(x=400,y=100)]

class StartMenu():
    def __init__(self):
        self.screen = pygame.display.set_mode((width,height))
        self.menu_state = "start" #
        # self.button = st_op_buttons[0]
        # self.rect = st_op_rect[0]
        self.gameruning=True #화면 유지
        self.key_event = pygame.key.get_pressed()
        self.cursor=image[2]

    def screens(self):
        pygame.display.set_caption('kerby')
        self.cursor.set_colorkey((0, 255, 0))
        while self.gameruning:
            target = pygame.mouse.get_pos()
            if self.menu_state=="start":
                self.screen.blit(image[0],(0,0))
                self.screen.blit(st_op_buttons[0], st_op_rect[0])
                self.screen.blit(st_op_buttons[1], st_op_rect[1])
                self.screen.blit(self.cursor, target)
            else:
                self.screen.blit(image[1], (0, 0))
            self.events()
            pygame.display.update()
        pygame.quit()

    def restart(self):
        pygame.init()
        pygame.display.set_caption('kerby')
        self.cursor.set_colorkey((0, 255, 0))
        while self.gameruning == False:
            target = pygame.mouse.get_pos()
            self.screen = pygame.display.set_mode((1000, 400))
            self.screen.blit(image[3], (0, 0))
            self.screen.blit(st_op_buttons[2], st_op_rect[2])
            self.screen.blit(st_op_buttons[3], st_op_rect[3])
            self.screen.blit(self.cursor, target)
            self.events()
            pygame.display.update()
        pygame.quit()

    def clear(self):
        pygame.init()
        pygame.display.set_caption('kerby')
        self.cursor.set_colorkey((0, 255, 0))
        while self.gameruning == False:
            target = pygame.mouse.get_pos()
            self.screen = pygame.display.set_mode((1000, 400))
            self.screen.blit(image[5], (0, 0))
            self.screen.blit(image[4], (0, 0))
            self.screen.blit(st_op_buttons[2], st_op_rect[2])
            self.screen.blit(st_op_buttons[3], st_op_rect[3])
            self.screen.blit(st_op_buttons[4], st_op_rect[4])
            self.screen.blit(self.cursor, target)
            self.events()
            pygame.display.update()
        pygame.quit()



    def events(self):
        for event in pygame.event.get():
            if event.type in [pygame.QUIT]:
                pygame.quit()
            if st_op_rect[0].collidepoint(pygame.mouse.get_pos()): ##start에 마우스가 올려져 있을 때
                if event.type == MOUSEBUTTONDOWN:
                    g = playgame.game()
                    g.start()
                    if g.start():
                        self.gameruning = False
                        print("CLEAR")
                        g.game_state = True
                        g.boss_start()
                        # if g.boss_start():
                            #self.clear()
                            #print("CLEAR")
                        # else:
                            #self.restart()                
                    else:
                        self.gameruning = False
                        print("GAME OVER")
                        self.restart()
            if st_op_rect[1].collidepoint(pygame.mouse.get_pos()):
                if event.type == MOUSEBUTTONDOWN:
                    self.menu_state="option"
            if st_op_rect[2].collidepoint(pygame.mouse.get_pos()):
                if event.type == MOUSEBUTTONDOWN:
                    g = playgame.game()
                    g.start()
                    if g.start():
                        print("CLEAR")
                        
                    else:
                        self.gameruning = False
                        print("GAME OVER")
            if st_op_rect[3].collidepoint(pygame.mouse.get_pos()):
                if event.type == MOUSEBUTTONDOWN:
                    pygame.quit()




if __name__ == "__main__":
    st=StartMenu()
    st.screens()