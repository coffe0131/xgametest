import pygame

#pygame.init()


class BACKGROUND:
    def __init__(self):
        self.screen = pygame.display.set_mode((1000,500))
        self.white = (255,255,255)
        self.background_width=944
        self.background1=pygame.image.load('images/realbackground.png')
        print(self.background1.get_rect())
        self.background1 = pygame.transform.scale(self.background1,(1000,500))
        self.background2=self.background1.copy()
        self.background1_x = 0
        self.background2_x = self.background_width
        

    def background_rotate(self, stat = 0):
        if stat == 1:
            self.background1_x -= 5            #맵이동
            self.background2_x -= 5              #맵이동
        if self.background1_x <= -(self.background_width):
            self.background1_x = self.background_width
        if self.background2_x <= -(self.background_width):
            self.background2_x = self.background_width
        self.screen.blit(self.background1,(self.background1_x,0))   
        self.screen.blit(self.background2,(self.background2_x,0))

