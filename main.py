import pygame, sys
from pygame.locals import *
from pygame import quit, key
from player import Player
from constants import Constants
from ball import Ball

def main():    
    pygame.init()

    DISPLAY=pygame.display.set_mode((Constants.WIDTH,Constants.HEIGHT),0,32)

    WHITE=(255,255,255)
    BLACK=(0,0,255)

    ball = Ball()
    player1 = Player(5)
    player2 = Player( (Constants.WIDTH-Constants.PLAYER_WIDTH)-5)

    DISPLAY.fill(BLACK)
    
    
    pygame.draw.rect(DISPLAY,WHITE,player1)
    pygame.draw.rect(DISPLAY,WHITE,player2)
    pygame.draw.rect(DISPLAY,WHITE,ball)


    def moveBall():
        pygame.draw.rect(DISPLAY,BLACK,ball)
        
        ball.collission_left(player1)
        ball.collission_right(player2)
        ball.move()
        pygame.draw.rect(DISPLAY,WHITE,ball)


    def check_player1(keys):
        if keys[K_s]:                        
            pygame.draw.rect(DISPLAY,BLACK,player1)          
            player1.movDown()           
            pygame.draw.rect(DISPLAY,WHITE,player1)  
        if keys[K_w]:                       
            pygame.draw.rect(DISPLAY,BLACK,player1)          
            player1.moveUp()         
            pygame.draw.rect(DISPLAY,WHITE,player1)  

    def check_player2(keys):
        if keys[K_DOWN]:                       
            pygame.draw.rect(DISPLAY,BLACK,player2)          
            player2.movDown()           
            pygame.draw.rect(DISPLAY,WHITE,player2)  
        if keys[K_UP]:                 
            pygame.draw.rect(DISPLAY,BLACK,player2)          
            player2.moveUp()
            pygame.draw.rect(DISPLAY,WHITE,player2) 
        

    clock=pygame.time.Clock()


    while True:       
        clock.tick(500) 
        pygame.display.update()
        
        keys = key.get_pressed() 
        moveBall()
        check_player1(keys)
        check_player2(keys)
        if keys[K_ESCAPE]:
            pygame.quit()
            sys.exit()       
        if keys[K_o]:
            print(f'\n ball.top={ball.rect.top}\n player.top={player1.rect.top}\n')
            
        for e in pygame.event.get():            
            pass

    

    




            


main()
