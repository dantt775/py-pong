import pygame, sys
from pygame.locals import *
from pygame import quit, key

def main():
    pygame.init()

    DISPLAY=pygame.display.set_mode((800,600),0,32)

    WHITE=(255,255,255)
    BLACK=(0,0,255)

    DISPLAY.fill(BLACK)
    player_one = pygame.Rect(10,150,15,200)
    player_two = pygame.Rect(775,150.0,15,200)
    
    pygame.draw.rect(DISPLAY,WHITE,player_one)
    pygame.draw.rect(DISPLAY,WHITE,player_two)

    # while True:
    #     for event in pygame.event.get():
    #         keys = key.get_pressed()
    #         pygame.display.update()
    #         keys = key.get_pressed() 
    #         if keys[K_DOWN]:             
    #             pygame.draw.rect(DISPLAY,BLACK,player_one)          
    #             player_one.top = player_one.top+0.1             
    #             pygame.draw.rect(DISPLAY,WHITE,player_one)  
    #             pygame.display.update()
    #         if keys[K_UP]:             
    #             pygame.draw.rect(DISPLAY,BLACK,player_one)          
    #             player_one.top = player_one.top-0.1             
    #             pygame.draw.rect(DISPLAY,WHITE,player_one)
    #             pygame.display.update()
    #     pygame.display.update()

    while True:        
        pygame.display.update()
        keys = key.get_pressed() 
        if keys[K_DOWN]:           
            print('down')  
            pygame.draw.rect(DISPLAY,BLACK,player_one)          
            player_one.top = player_one.top+1             
            pygame.draw.rect(DISPLAY,WHITE,player_one)  
        if keys[K_UP]:     
            print('up')          
            pygame.draw.rect(DISPLAY,BLACK,player_one)          
            player_one.top = player_one.top-1             
            pygame.draw.rect(DISPLAY,WHITE,player_one)                              
        for e in pygame.event.get():
            if e.type==QUIT:
                pygame.quit()
                sys.exit()
            print('pass')
            pass
            


main()