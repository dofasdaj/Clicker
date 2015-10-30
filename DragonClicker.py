__author__ = 'Smyke, dofasdaj'
import pygame,sys
import time
from pygame import *
pygame.init()

def message_to_screen(msg,red):
    screen_text = font.render(msg, True, red)
    setDisplay.blit(screen_text, [display_X/2, display_Y/2])


red = (255,0,0)
green = (0,255,0)
blue = (0,0,255)
coolBlack = (10,10,10)
coolWhite = (250,250,250)
orange = (250,160,31)

setDisplay = pygame.display.set_mode((1000,940))
pygame.display.set_caption("Dragon Clicker")
Dragon_Clicker = True

display_X = 800
display_Y = 400
UpPerC2 = False
UpPerC3 = False
UpPerC4 = False
UpPerC5 = False
UpPerC6 = False
UpPerC7 = False
UpPerC8 = False
UpPerC9 = False
UpPerC10 = False
UpPerC11 = False
UpPerC12 = False
UpPerC13 = False






font = pygame.font.SysFont(None, 25)

class mainLoop:
    def __init__(self):
        Update = 1
        UpPerC2 = False
        UpPerC3 = False
        UpPerC4 = False
        UpPerC5 = False
        UpPerC6 = False
        UpPerC7 = False
        UpPerC8 = False
        UpPerC9 = False
        UpPerC10 = False
        UpPerC11 = False
        UpPerC12 = False
        UpPerC13 = False
        punkte = 0
        while Dragon_Clicker:
            sys_font = pygame.font.SysFont(None, 60)
            render = sys_font.render("Updatestufe:"+str(Update),0,(0,0,0))
            setDisplay.blit(render, (500,10))
            sys_font = pygame.font.SysFont(None, 60)
            render = sys_font.render(("Punkte:"+str(punkte)),0,(0,0,0))
            setDisplay.blit(render, (30,215))
            pygame.display.update()
            bild = pygame.image.load("CookieBild.bmp")
            bild = bild.convert()
            setDisplay.blit(bild, (0,0))
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit
                if event.type == pygame.MOUSEBUTTONDOWN:
                    if UpPerC2 == True:
                        punkte += 1
                    if UpPerC3 == True:
                        punkte += 2
                    else:
                        punkte += 1
                if event.type == KEYDOWN:
                    if event.key == K_q:
                        if punkte >= 100 and UpPerC2 == False :
                            UpPerC2 = True
                            punkte -= 100
                            Update += 1
                    if event.key == K_w and UpPerC2 == True:
                        if punkte >= 300 and UpPerC3 == False:
                            UpPerC3 = True
                            punkte -= 300
                            Update += 1
                            time.wait(10)
                           
                        else:
                             print("error")
                         

                    if event.key == K_m:
                        punkte += 1000000000
                        print("Cheater ^^")
                        
mainLoop()
