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
DisplayGr = (1200, 700)
setDisplay = pygame.display.set_mode((1200, 700))
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
        Taste = "Q"
        Taste2 = "E"
        DisplayGr = (1200, 700)
        ###################
        KosUp1 = 100
        KosUp2 = 200
        Update = 1
        ###################
        PerSec1 = False
        PerSec2 = False
        ###################
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
        ####################
        punkte = 0
        while Dragon_Clicker:
            sys_font = pygame.font.SysFont(None, 60)
            render = sys_font.render("Updatestufe:"+str(Update),0,(0,0,0))
            setDisplay.blit(render, (500,10))
            sys_font = pygame.font.SysFont(None, 30)
            render = sys_font.render("Kosten fuers Klick-Update:"+" "+str(KosUp1),0,(0,0,0))
            setDisplay.blit(render, (900,40))
            sys_font = pygame.font.SysFont(None, 30)
            render = sys_font.render("Druecke"+" "+str(Taste)+" "+"zum verbessern",0,(0,0,0))
            setDisplay.blit(render, (900,80))
            sys_font = pygame.font.SysFont(None, 30)
            render = sys_font.render("Kosten fuers Sec-Update:"+" "+str(KosUp2),0,(0,0,0))
            setDisplay.blit(render, (900,130))
            sys_font = pygame.font.SysFont(None, 50)
            sys_font = pygame.font.SysFont(None, 30)
            render = sys_font.render("Dreucke"+" "+str(Taste2)+" "+"zum verbessern",0,(0,0,0))
            setDisplay.blit(render, (900,170))
            render = sys_font.render(("Punkte:"+str(punkte)),0,(0,0,0))
            setDisplay.blit(render, (30,215))
            pygame.display.update()
            bild = pygame.image.load("CookieBild.bmp")
            bild = bild.convert()
            setDisplay.blit(bild, (0,0))
            if PerSec1 == True:
                punkte += 0.02
            if PerSec2 == True:
                punkte += 0.04
            #################################
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit
                if event.type == pygame.MOUSEBUTTONDOWN:
                    if UpPerC2 == True:
                        punkte += 1
                    if UpPerC3 == True:
                        punkte += 3
                    if UpPerC4 == True:
                        punkte += 4
                    else:
                        punkte += 1
                ###################################
                if event.type == KEYDOWN:
                    if event.key == K_e and PerSec1 == False:
                        if punkte >= 200:
                            punkte -= 200
                            Update+= 1
                            KosUp2 = 500
                            Taste2 = "R"
                            time.wait(10)
                            PerSec1 = True
                    if event.key == K_r:
                        if punkte >= 500 and PerSec2 == False:
                            punkte -= 500
                            Update += 1
                            KosUp2 = 1000
                            Taste2 = "E"
                            time.wait(10)
                            PerSec2 = True
                    if event.key == K_q:
                        if punkte >= 100 and UpPerC2 == False :
                            UpPerC2 = True
                            punkte -= 100
                            Update += 1
                            KosUp1 = 250
                            Taste = "W"
                            time.wait(10)
                    if event.key == K_w and UpPerC2 == True:
                        if punkte >= 250 and UpPerC3 == False:
                            UpPerC3 = True
                            punkte -= 250
                            Update += 1
                            KosUp1 = 500
                            time.wait(10)
                            Taste = "Q"
                    if event.key == K_q and UpPerC3 == True:
                        if punkte >= 500 and UpPerC4 == False:
                            UpPerC4 = True
                            punkte -= 500
                            Update += 1
                            KosUp1 = 1000
                            time.wait(10)
                            Taste = "W"
                    if event.key == K_w and UpPerC5 == False:
                        if punkte >= 1000 and UpPerC5 == False:
                            UpPerC3 = True
                            punkte -= 1000
                            Update += 1
                            KosUp1 = 1000
                            time.wait(10)
                            Taste = "Q"
                    
                        else:
                             print("error")
                         

                    if event.key == K_m:
                        punkte += 500
                        print("Cheater ")
                    #nur feur Entwickler zum Testen
###############################################################                        
mainLoop()
