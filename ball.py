import pygame
from constants import Constants


class Ball:
    def __init__(self):
        self.rect = pygame.Rect(400, 150, 15, 15)
        self.left = True
        self.down = True

#>14 <97
    
    def collission_left(self, player):
        if(self.rect.left==(player.rect.left+Constants.PLAYER_WIDTH) and ((self.rect.top-player.rect.top)>=14 or  (self.rect.top-player.rect.top)<=97)):
            print(f'\ncolisao esquerda \nball.left={self.rect.left}\nball.top={self.rect.top}\nplayer.top= {player.rect.top}')
            self.left = False
    def collission_right(self, player):
        if(self.rect.left==(player.rect.left-Constants.PLAYER_WIDTH)):
            print(f'\ncolisao direita \nball.left={self.rect.left}\nball.top={self.rect.top}\nplayer.top= {player.rect.top}')
            self.left = True    


    def move(self):
        if(self.down is True):
            self.move_down()
        else:
            self.move_up()
        
        if(self.left is True):
            self.moveLeft()
        else:
            self.moveRight()
            

    def move_up(self):
        if (self.rect.top > 0 and self.down is False):
            self.rect.top -=1
        
        if(self.rect.top ==0):
            self.down=True

    
    def move_down(self):
        
        if (self.rect.top < (Constants.HEIGHT-self.rect.height) and self.down is True):
            self.rect.top+=1
        if (self.rect.top == (Constants.HEIGHT-self.rect.height)):
            self.down=False


    
    def moveLeft(self):
        # print(f'Left{self.rect.left}')        
        if (self.rect.left > 0 and self.left is True):
            self.rect.left = self.rect.left-1
        

    def moveRight(self):        
        # print(f'Right{self.rect.left}')        
        if (self.rect.left < (Constants.WIDTH-self.rect.width) and self.left is False):
            self.rect.left = self.rect.left+1

        
            

        
            
            


