import pygame
from pygame import*
from pygame.locals import*
import keyboard
import playgame

import random
import sys
from time import sleep

width,height = 500,500
screen = pygame.display.set_mode((width,height))
pygame.display.set_caption('kerby')

def play(screen):
    pygame.init()
    menu_main = 0 #0은 메인메뮤, 1은 option, 2는 back
    pygame.display.update()

    font = pygame.font.Font("images/Maplestory Bold.ttf", 50)
    #font2 = pygame.font.Font("font/Maplestory Light.ttf", 40)
    start_button = font.render("START", True, (0, 255, 0))
    start_rect = start_button.get_rect(x=180,y=200)
    
    option_button = font.render('OPTION', True,(0,255,0)) 
    option_rect = start_button.get_rect(x=160,y=120)

    cursor = pygame.image.load("images/cursor.jpg").convert()
    cursor.set_colorkey((0,255,0))

    running=True #화ccccccccc면이 계속 켜져있게 해줌

    while running :
        target = pygame.mouse.get_pos()
        key_event = pygame.key.get_pressed()
        if menu_main == 0:       
            S_background = pygame.transform.scale(pygame.image.load("images/back.png"),(500,500))
            screen.blit(S_background, (0, 0))
            screen.blit(start_button, start_rect)
            screen.blit(option_button, option_rect)
            screen.blit(cursor, target)

        elif menu_main == 1:
            option=pygame.image.load("images/as.jpg").convert()
            pygame.transform.scale(option,(500,500))
            screen.blit(option, (0, 0))
        

        for event in pygame.event.get():
            if start_rect.collidepoint(pygame.mouse.get_pos()): ##start에 마우스가 올려져 있을 때
                if event.type == MOUSEBUTTONDOWN:  
                    g = playgame.game()
                    result = g.start()
                    if result ==0:
                        print("GAME OVER")
                    else:
                        print("CLEAR")
            if option_rect.collidepoint(pygame.mouse.get_pos()): 
                if event.type == MOUSEBUTTONDOWN:
                    menu_main = 1           
            if event.type == pygame.KEYDOWN:
                if (key_event == pygame.K_ESCAPE) :  #ESE 누르면 종료
                    running = False
        pygame.display.update()
    pygame.quit()


if __name__ == "__main__":
    play(screen)
        