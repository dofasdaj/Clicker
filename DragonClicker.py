__author__ = 'Smyke, dofasdaj'
import pygame,sys
import time
import random
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
setDisplay = pygame.display.set_mode((1300, 800))
pygame.display.set_caption("Dragon Clicker")
Dragon_Clicker = True
i = 0
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
RUp1 = False
#font = pygame.font.SysFont(None, 25)
class mainLoop:
    def __init__(self):
        Taste = "Q"
        Taste2 = "E"
        Taste3 = "A"
        Taste4 = "D"
        DisplayGr = (1200, 700)
        ###################
        KosUp1 = 100
        KosUp2 = 200
        KosUp3 = 1000
        KosUp4 = 5000
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
        RUp1 = False
        MaUp1 = False
        MaUp2 = False
        BerUp1 = False
        ####################
        punkte = 0
        LS = 1
        MS = 0
        BS = 0
        Bog = 0
        i = 0
        while Dragon_Clicker:
            sys_font = pygame.font.SysFont(None, 60)
            render = sys_font.render("Nicht Cookie",0,(0,0,0))
            setDisplay.blit(render, (500,10))
            sys_font = pygame.font.SysFont(None, 35)
            sys_font = pygame.font.SysFont(None, 50)
            render = sys_font.render(("Geld:"+str(punkte)),0,(0,0,0))
            setDisplay.blit(render, (30,100))
            render = sys_font.render("Staerke deiner Armee:"+ str(Update),0,(0,0,0))
            setDisplay.blit(render, (30,200))
            render = sys_font.render("Deine Wirtschaft:",0,(0,0,0))
            setDisplay.blit(render, (30,470))
            sys_font = pygame.font.SysFont(None, 30)
            render = sys_font.render("Dein Schwert:"+str(LS),0,(0,0,0))
            setDisplay.blit(render, (30,250))
            render = sys_font.render("Bogenschuetzen:"+str(Bog),0,(0,0,0))
            setDisplay.blit(render, (30,300))
            render = sys_font.render("Magier:"+str(MS),0,(0,0,0))
            setDisplay.blit(render, (30,350))
            render = sys_font.render("Berserker:"+str(BS),0,(0,0,0))
            setDisplay.blit(render, (30,400))
            render = sys_font.render("Dein Schwert:"+" "+str(KosUp1),0,(0,0,0))
            setDisplay.blit(render, (850,40))
            render = sys_font.render("Q"+" "+"zum verbessern.",0,(0,0,0))
            setDisplay.blit(render, (850,80))
            render = sys_font.render("Magier:"+" "+str(KosUp3),0,(0,0,0))
            setDisplay.blit(render, (850,210))
            render = sys_font.render("E"+" "+"zum verbessern.",0,(0,0,0))
            setDisplay.blit(render, (850,250))
            render = sys_font.render("Bogenschuetzen:"+" "+str(KosUp2),0,(0,0,0))
            setDisplay.blit(render, (850,130))
            render = sys_font.render("W"+" "+"zum verbessern",0,(0,0,0))
            setDisplay.blit(render, (850,170))
            render = sys_font.render("Berserker:"+" "+str(KosUp4),0,(0,0,0))
            setDisplay.blit(render, (850,290))
            render = sys_font.render("R"+" "+"zum verbessern",0,(0,0,0))
            setDisplay.blit(render, (850,330))
            
            pygame.display.update()
            bild = pygame.image.load("CookieBild.bmp")
            bild = bild.convert()
            setDisplay.blit(bild, (0,0))
            punkte += 0.03 * Bog
            punkte += 0.1 * MS
            punkte += 0.5 * BS
            #################################
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit
                if event.type == pygame.MOUSEBUTTONDOWN:
                    punkte += 1 * LS                    
                ###################################
                if event.type == KEYDOWN:
                    #Bogenschuetzen
                    if event.key == K_w:
                        if punkte >= 200:
                            punkte -= 200
                            Update += 1
                            KosUp2 = 500
                            time.wait(10)
                            Bog += 1
                    #Schwert
                    if event.key == K_q:
                        if punkte >= 100:
                            punkte -= 100
                            Update += 1
                            time.wait(10)
                            LS += 1
                    #Magier
                    if event.key == K_e:
                        if punkte >= 1000:
                            punkte -= 1000
                            Update += 1
                            KosUp3 = 3000
                            time.wait(10)
                            Taste3 = "S"
                            MS += 1
                    #Berserker
                    if event.key == K_r:
                        if punkte >= 5000 and BerUp1 == False:
                            punkte -= 5000
                            Update += 1
                            KosUp4 = 20000
                            time.wait(10)
                            BS += 1
                    else:
                        print("error")
                    if event.key == K_m:
                        punkte += 500
                        print("Cheater ")
                    #nur feur Entwickler zum Testen
###############################################################                        
mainLoop()
