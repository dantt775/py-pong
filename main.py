import pygame, sys
from pygame.locals import *
from pygame import quit, key
from player import Player
from constants import Constants

def main():    
    pygame.init()

    DISPLAY=pygame.display.set_mode((Constants.WIDTH,Constants.HEIGHT),0,32)

    WHITE=(255,255,255)
    BLACK=(0,0,255)

    player1 = Player(10)
    player2 = Player(775)

    DISPLAY.fill(BLACK)
    
    
    pygame.draw.rect(DISPLAY,WHITE,player1)
    pygame.draw.rect(DISPLAY,WHITE,player2)


    def checkPlayerOne(keys):
        if keys[K_s]:                        
            pygame.draw.rect(DISPLAY,BLACK,player1)          
            player1.movDown()           
            pygame.draw.rect(DISPLAY,WHITE,player1)  
        if keys[K_w]:                       
            pygame.draw.rect(DISPLAY,BLACK,player1)          
            player1.moveUp()         
            pygame.draw.rect(DISPLAY,WHITE,player1)  

    def checkPlayerTwo(keys):
        if keys[K_DOWN]:                       
            pygame.draw.rect(DISPLAY,BLACK,player2)          
            player2.movDown()           
            pygame.draw.rect(DISPLAY,WHITE,player2)  
        if keys[K_UP]:                 
            pygame.draw.rect(DISPLAY,BLACK,player2)          
            player2.moveUp()
            pygame.draw.rect(DISPLAY,WHITE,player2) 




    while True:        
        pygame.display.update()
        keys = key.get_pressed() 
        checkPlayerOne(keys)
        checkPlayerTwo(keys)
        if keys[K_ESCAPE]:
            pygame.quit()
            sys.exit()                         
        for e in pygame.event.get():            
            pass
            


main()
