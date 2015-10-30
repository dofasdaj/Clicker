__author__ = 'Smyke'
import pygame,sys
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

setDisplay = pygame.display.set_mode((1100,750))
pygame.display.set_caption("Dragon Clicker")
Dragon_Clicker = True

display_X = 800
display_Y = 400

font = pygame.font.SysFont(None, 25)

class mainLoop:
    def __init__(self):
        punkte = 0
        while Dragon_Clicker:
            print (punkte)
            for event in pygame.event.get():Ä
9                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.MOUSEBUTTONDOWN:
                        punkte += 1

mainLoop()