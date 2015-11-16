__author__ = 'Smyke, dofasdaj'
import pygame
import random
from pygame import *
import os

pygame.init()


def message_to_screen(msg, red):
    screen_text = font.render(msg, True, red)
    setDisplay.blit(screen_text, [display_X / 2, display_Y / 2])


whileVaribel = True
Kartenwhile = True

red = (255, 0, 0)
green = (0, 255, 0)
blue = (0, 0, 255)
coolBlack = (10, 10, 10)
coolWhite = (250, 250, 250)
orange = (250, 160, 31)
grey = (100, 100, 100)
DisplayGr = (1200, 700)
setDisplay = pygame.display.set_mode((1300, 800))
pygame.display.set_caption("Dragon Clicker")
Dragon_Clicker = True
i = 0
display_X = 1200
display_Y = 700
font = pygame.font.SysFont(None, 25)


def menue():
    setDisplay.fill(coolWhite)
    mouse = pygame.mouse.get_pos()
    sys_font = pygame.font.SysFont(None, 80)
    render = sys_font.render("Level 1", 0, red)
    setDisplay.blit(render, (540, 20))
    pygame.draw.rect(setDisplay, (238,213,183), [1100,600,200,200])
    pygame.draw.rect(setDisplay, (238,213,183), [0,600,200,200])
    sys_font = pygame.font.SysFont(None, 40)
    render = sys_font.render("Press ESC to quit", 0, red)
    setDisplay.blit(render, (500, 600))
    render = sys_font.render("Karte", 0, coolBlack)
    setDisplay.blit(render, (1160, 650))
    render = sys_font.render("Spiel", 0, coolBlack)
    if 1100+200 > mouse[0] > 150 and 600+200 > mouse[1] > 600 :
        blabla = pygame.image.load("Karte.png")
        setDisplay.blit(blabla,(0,0))
    setDisplay.blit(render, (60, 650))
    pygame.display.update()
def karten():
    setDisplay.fill(coolWhite)
    sys_font = pygame.font.SysFont(None, 80)
    render = sys_font.render("Das ist die Karte", 0, red)
    setDisplay.blit(render, (450, 20))
    bild = pygame.image.load("Karte.png")
    bild = bild.convert()
    setDisplay.blit(bild, (0, 0))
    pygame.display.update()
    
class MainLoop:
    def __init__(self):
        Kartenwhile = False
        Karte = False
        # Name
        # Diamante
        # Quests#
        TxQ1 = False
        TxQ2 = False
        RevoltTx = False
        ##########
        ###################
        KosUp1 = 100
        KosUp2 = 200
        KosUp3 = 1000
        KosUp4 = 5000
        KosUp5 = 20000
        KosUp7 = 100000
        KosUp6 = 1000000
        KosUp8 = 500000
        Update = 1
        punkte = 0
        AnWaS = 0
        Einwohner = 0
        WaS = 1
        LS = 1
        MS = 0
        BS = 0
        HS = 0
        Bog = 0
        SiMi = 0
        MiSt = 0
        GSS = 1
        GS = 0
        KS = 0
        BauH = 0
        klick = 0
        SmAn = 0
        SmSt = 600
        UnZ = HS * 3000
        RevoltRi = 100000 - UnZ

        i = random.randrange(5000)
        MiSt += SiMi
        Up1M = 1
        q = random.randrange(3)
        r = random.randrange(RevoltRi)

        if punkte >= 1000000:
            Up1M += 1

        while Dragon_Clicker:
            punkterausch = True
            Menu = False
            Kartenwhile = False
            Karte = False
            
            if punkterausch == True:
                UnZ = HS * 500
                RevoltRi = 100000 - UnZ
                if r != 1:
                    r = random.randrange(RevoltRi)
                Armeestaercke = Bog
                Armeestaercke += LS
                Armeestaercke += MS
                Armeestaercke += BS
                Armeestaercke += KS
                Armeestaercke += HS
                Einwohner += Armeestaercke / 10000

                Di = random.randrange(SmSt)
                if Di == 1:
                    SmAn += 1
                # sterben der Truppen
                Bog -= 0.0001
                MS -= 0.000008
                BS -= 0.0000008
                KS -= 0.0000001
                if KS <= 0:
                    KS = 0
                if MS <= 0:
                    MS = 0
                if BS <= 0:
                    BS = 0
                if Bog <= 0:
                    Bog = 0

                if klick >= 6000:
                    TxQ2 = True
                    BS += 10
                    KS += 2
                    MS += 25
                    Bog += 50
                    klick = 0
                # Quest

                if r == 1:
                    HS - HS
                    punkte *= 0.75
                    Bog *= 0.75
                    MS *= 0.75
                    BS *= 0.75
                    KS *= 0.75
                    RevoltTx = True
                    RevoltRi += 10000
                    r = random.randrange(RevoltRi)
                    q = random.randrange(3)
                if r > 1:
                    r = random.randrange(RevoltRi)

                if r <= 0:
                    r = random.randrange(RevoltRi)
                if i == 1:
                    TxQ1 = True
                    Bog += 10
                    time.wait(10)
                    i = random.randrange(10000)
                    q = random.randrange(3)

                if i > 1:
                    i = random.randrange(10000)

                if i <= 0:
                    i = random.randrange(10000)
                if RevoltTx:
                    TxQ2 = False
                    TxQ1 = False
                    RevoltTx = False
                    if q == 0:
                        sys_font = pygame.font.SysFont(None, 40)
                        render = sys_font.render("Revolte!!!", 0, blue)
                        setDisplay.blit(render, (500, 600))

                    if q == 1:
                        sys_font = pygame.font.SysFont(None, 40)
                        render = sys_font.render("Revolte!!!", 0, green)
                        setDisplay.blit(render, (500, 600))
                    if q == 2:
                        sys_font = pygame.font.SysFont(None, 40)
                        render = sys_font.render("Revolte!!!", 0, red)
                        setDisplay.blit(render, (500, 600))
                if TxQ2:
                    TxQ1 = False
                    RevoltTx = False
                    if q == 0:
                        sys_font = pygame.font.SysFont(None, 40)
                        render = sys_font.render("Eine Horde Krieger schliesst sich dir an", 0, blue)
                        setDisplay.blit(render, (500, 600))

                    if q == 1:
                        sys_font = pygame.font.SysFont(None, 40)
                        render = sys_font.render("Eine Horde Krieger schliesst sich dir an", 0, green)
                        setDisplay.blit(render, (500, 600))
                    if q == 2:
                        sys_font = pygame.font.SysFont(None, 40)
                        render = sys_font.render("Eine Horde Krieger schliesst sich dir an", 0, red)
                        setDisplay.blit(render, (500, 600))
                if TxQ1:
                    TxQ2 = False
                    RevoltTx = False
                    if q == 0:
                        sys_font = pygame.font.SysFont(None, 40)
                        render = sys_font.render("Eine Horde Bogenschuetzen schliesst sich dir an", 0, blue)
                        setDisplay.blit(render, (500, 600))

                    if q == 1:
                        sys_font = pygame.font.SysFont(None, 40)
                        render = sys_font.render("Eine Horde Bogenschuetzen schliesst sich dir an", 0, green)
                        setDisplay.blit(render, (500, 600))
                    if q == 2:
                        sys_font = pygame.font.SysFont(None, 40)
                        render = sys_font.render("Eine Horde Bogenschuetzen schliesst sich dir an", 0, red)
                        setDisplay.blit(render, (500, 600))

                sys_font = pygame.font.SysFont(None, 50)
                render = sys_font.render(("Geld:" + " " + str(round(punkte)) + "$"), 0, (0, 0, 0))
                setDisplay.blit(render, (100, 5))
                render = sys_font.render(("Diamanten:" + " " + str(round(SmAn))), 0, (0, 0, 0))
                setDisplay.blit(render, (550, 0))
                render = sys_font.render(("Obdachlose Einwohner:" + " " + str(round(Einwohner))), 0, (0, 0, 0))
                setDisplay.blit(render, (40, 600))
                sys_font = pygame.font.SysFont(None, 40)
                render = sys_font.render("Staerke " + "deine" + " Armee:", 0, (0, 0, 0))
                setDisplay.blit(render, (30, 50))
                render = sys_font.render("Deine Wirtschaft:", 0, (0, 0, 0))
                setDisplay.blit(render, (30, 235))
                sys_font = pygame.font.SysFont(None, 30)
                render = sys_font.render("Dein Schwert:" + str(LS), 0, (0, 0, 0))
                setDisplay.blit(render, (30, 90))
                render = sys_font.render("Bogenschuetzen:" + str(round(Bog)), 0, (0, 0, 0))
                setDisplay.blit(render, (30, 120))
                render = sys_font.render("Horde:" + str(round(HS)), 0, (0, 0, 0))
                setDisplay.blit(render, (250, 90))
                render = sys_font.render("Magier:" + str(round(MS)), 0, (0, 0, 0))
                setDisplay.blit(render, (30, 150))
                render = sys_font.render("Berserker:" + str(round(BS)), 0, (0, 0, 0))
                setDisplay.blit(render, (30, 180))
                render = sys_font.render("Katapult:" + str(round(KS)), 0, (0, 0, 0))
                setDisplay.blit(render, (30, 210))
                render = sys_font.render("Minen:" + str(SiMi), 0, (0, 0, 0))
                setDisplay.blit(render, (30, 265))
                render = sys_font.render("Goldschmied:" + str(GS), 0, (0, 0, 0))
                setDisplay.blit(render, (30, 295))
                render = sys_font.render("Waffenschmied:" + str(AnWaS), 0, (0, 0, 0))
                setDisplay.blit(render, (30, 330))
                render = sys_font.render("Bauernhaeuser:" + str(BauH), 0, (0, 0, 0))
                setDisplay.blit(render, (30, 365))
                render = sys_font.render("Dein Schwert:" + " " + str(KosUp1), 0, (255, 0, 0))
                setDisplay.blit(render, (850, 30))
                render = sys_font.render("Q" + " " + "zum verbessern.", 0, (255, 0, 0))
                setDisplay.blit(render, (850, 60))
                render = sys_font.render("Horde:" + " " + "1 Ob.Ein.", 0, (255, 0, 0))
                setDisplay.blit(render, (1100, 30))
                render = sys_font.render("1" + " " + "zum verbessern.", 0, (255, 0, 0))
                setDisplay.blit(render, (1100, 60))
                render = sys_font.render("Bauern:" + " " + "1 Horde", 0, (255, 0, 0))
                setDisplay.blit(render, (1100, 90))
                render = sys_font.render("2" + " " + "zum verbessern.", 0, (255, 0, 0))
                setDisplay.blit(render, (1100, 120))
                render = sys_font.render("Magier:" + " " + str(KosUp3), 0, (255, 0, 0))
                setDisplay.blit(render, (850, 150))
                render = sys_font.render("E" + " " + "zum verbessern.", 0, (255, 0, 0))
                setDisplay.blit(render, (850, 180))
                render = sys_font.render("Bogenschuetzen:" + " " + str(KosUp2), 0, (255, 0, 0))
                setDisplay.blit(render, (850, 90))
                render = sys_font.render("W" + " " + "zum verbessern", 0, (255, 0, 0))
                setDisplay.blit(render, (850, 120))
                render = sys_font.render("Berserker:" + " " + str(KosUp4), 0, (255, 0, 0))
                setDisplay.blit(render, (850, 210))
                render = sys_font.render("R" + " " + "zum verbessern", 0, (255, 0, 0))
                setDisplay.blit(render, (850, 240))
                render = sys_font.render("Katapult:" + " " + str(KosUp8), 0, (255, 0, 0))
                setDisplay.blit(render, (850, 270))
                render = sys_font.render("T" + " " + "zum verbessern", 0, (255, 0, 0))
                setDisplay.blit(render, (850, 300))
                render = sys_font.render("Mine:" + " " + str(KosUp5), 0, (255, 255, 0))
                setDisplay.blit(render, (850, 330))
                render = sys_font.render("A" + " " + "zum bauen", 0, (255, 255, 0))
                setDisplay.blit(render, (850, 360))
                render = sys_font.render("Waffenschmied:" + " " + str(KosUp6), 0, (0, 255, 0))
                setDisplay.blit(render, (850, 450))
                render = sys_font.render("D" + " " + "zum bauen", 0, (0, 255, 0))
                setDisplay.blit(render, (850, 480))
                render = sys_font.render("Bauernhaus:" + " " + "10 Ob.Ein.", 0, (0, 255, 0))
                setDisplay.blit(render, (850, 510))
                render = sys_font.render("F" + " " + "zum bauen", 0, (0, 255, 0))
                setDisplay.blit(render, (850, 540))
                render = sys_font.render("Goldschmied:" + " " + str(KosUp7), 0, (0, 255, 0))
                setDisplay.blit(render, (850, 390))
                render = sys_font.render("S" + " " + "zum bauen", 0, (0, 255, 0))
                setDisplay.blit(render, (850, 420))
                render = sys_font.render("ESC" + " " + "zum Menu", 0, (0, 0, 0))
                setDisplay.blit(render, (1000, 650))
                pygame.display.update()
                bild = pygame.image.load("DinoDrache.png")
                bild = bild.convert()
                setDisplay.blit(bild, (0, 0))
                # ToDo
                punkte += 0.1 * round(HS) * WaS * ((BauH / 10) + 1)
                punkte += 0.03 * round(Bog) * WaS * ((BauH / 10) + 1)
                punkte += 0.1 * round(MS) * WaS * ((BauH / 10) + 1)
                punkte += 0.6 * round(BS) * WaS * ((BauH / 10) + 1)
                punkte += punkte * ((MiSt * (BauH / 10 + 1)) * GSS)
                punkte += 7 * round(KS) * WaS

                if punkte >= 1000000:
                    Up1M = 2
                #################################
                for event in pygame.event.get():
                    if event.type == pygame.QUIT:
                        pygame.quit()
                        exit()


                    if event.type == pygame.MOUSEBUTTONDOWN:
                        punkte += 1 * LS * WaS * Up1M
                        klick += 1
                    ###################################
                    if event.type == KEYDOWN:
                        # ToDo
                        # Horde
                        if event.key == K_1:
                            if round(Einwohner) >= 1:
                                Einwohner -= 1
                                HS += 1
                        # Bauern
                        if event.key == K_2:
                            if HS >= 1:
                                HS -= 1
                                Einwohner += 1
                        # Bogenschuetzen
                        if event.key == K_w:
                            if punkte >= 200:
                                punkte -= 200
                                Update += 1
                                time.wait(10)
                                Bog += 1
                        # Schwert
                        if event.key == K_q:
                            if punkte >= 100:
                                punkte -= 100
                                Update += 1
                                time.wait(10)
                                LS += 1
                        # Magier
                        if event.key == K_e:
                            if punkte >= 1000:
                                punkte -= 1000
                                Update += 1
                                time.wait(10)
                                MS += 1
                        # Berserker
                        if event.key == K_r:
                            if punkte >= 5000:
                                punkte -= 5000
                                Update += 1
                                time.wait(10)
                                BS += 1
                        # Katapul
                        if event.key == K_t:
                            if punkte >= 50000:
                                punkte -= 50000
                                Update += 1
                                time.wait(10)
                                KS += 1
                        # Minen
                        if event.key == K_a:
                            if punkte >= 20000:
                                punkte -= 20000
                                time.wait(10)
                                SiMi += 1
                                MiSt += 0.0001
                        # Waffenschmied
                        if event.key == K_d:
                            if punkte >= 1000000:
                                punkte -= 1000000
                                time.wait(10)
                                WaS += 0.7
                                AnWaS += 1
                        # Goldschmied
                        if event.key == K_s:
                            if punkte >= 100000:
                                punkte -= 100000
                                time.wait(10)
                                GSS += 0.7
                                GS += 1
                        # Bauernhaus
                        if event.key == K_f:
                            if Einwohner >= round(10):
                                Einwohner -= 10
                                time.wait(10)
                                BauH += 1


                        #MENUE
                        if event.key == pygame.K_ESCAPE:
                            Menu = True
                        

                            # Troll
                            # if event.key == K_l:
                            # if punkte >= 1000000000:
                            # punkte -= 1000000000
                            # time.wait(10)
                            # print("Gehe nach drausen!!!")
                            # print("Du spielst dieses Spiel schon zulange")
                            # time.wait(10000000000000000000000000000000000000000000)
                            # nur feur Entwickler zum Testen
            if Menu:
                whileVaribel = True
                while whileVaribel:
                    menue()
                    for event in pygame.event.get():
                        if event.type == pygame.QUIT:
                            pygame.quit()
                            exit()
                            ###################################
                        if event.type == KEYDOWN:
                            if event.key == K_w:
                                Karte = True
                                whileVaribel = False
                            if event.key == pygame.K_ESCAPE:
                                punkterausch = True
                                whileVaribel = False
                            if event.key == K_s:
                                datenstrom = open("Speichern.txt","w")
                                datenstrom.write("Hallo")
                                datenstrom.close()
                            

            
            if Karte == True:
                Kartenwhile = True
                while Kartenwhile:
                    karten()
                    for event in pygame.event.get():
                        if event.type == pygame.QUIT:
                            pygame.quit()
                            exit()
                            ###################################
                        if event.type == KEYDOWN:
                            if event.key == pygame.K_ESCAPE:
                                punkterausch = True
                                Kartenwhile = False

###############################################################

MainLoop()
