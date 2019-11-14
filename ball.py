import pygame
from constants import Constants


class Ball:
    def __init__(self):
        self.rect = pygame.Rect(400, 15, 15, 15)
        self.left = True
        self.down = True

#>14 <97

    def calculate_top_position(self, player):
        value =abs(self.rect.top - player.rect.top)        
        if (13 <= value <= 98):
            return True
    
    def calculate_left_position(self, player):
        if self.rect.left==(player.rect.left+Constants.PLAYER_WIDTH):
            return True
    
    def calculate_right_position(self,player):
        if self.rect.left==(player.rect.left-Constants.PLAYER_WIDTH):
            return True
    
    def collission_left(self, player):        
        if( self.calculate_left_position(player) and self.calculate_top_position(player)):            
            print(f'ball left =  {self.rect.left}\n player left = {player.rect.left}')
            self.left = False

    def collission_right(self, player):        
        if(self.calculate_right_position(player) and self.calculate_top_position(player)):            
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
        if (self.rect.top > 5 and self.down is False):
            self.rect.top -=1
        
        if(self.rect.top ==5):
            self.down=True

    
    def move_down(self):        
        if (self.rect.top < ((Constants.HEIGHT-self.rect.height)-5) and self.down is True):
            self.rect.top+=1
        if (self.rect.top == (Constants.HEIGHT-self.rect.height)-5):
            self.down=False
    
    def moveLeft(self):        
        if (self.rect.left > 0 and self.left is True):
            self.rect.left = self.rect.left-1
        

    def moveRight(self):                
        if (self.rect.left < (Constants.WIDTH-self.rect.width) and self.left is False):
            self.rect.left = self.rect.left+1

        
            

        
            
            


