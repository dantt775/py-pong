import pygame
from constants import Constants


class Ball:
    def __init__(self):
        self.rect = pygame.Rect(400, 150, 15, 15)
        self.left = True
        self.down = True


    def move(self):

        if(self.down is True):
            self.move_down()
        else:
            self.move_Up()

        
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
        print(self.rect.top)
        if (self.rect.top < 585 and self.down is True):
            self.rect.top+=1
        if (self.rect.top == 585):
            self.down=False


    
    def moveLeft(self):
        # print(f'Left{self.rect.left}')        
        if (self.rect.left > 5 and self.left is True):
            self.rect.left = self.rect.left-1

        if (self.rect.left == 5):
            self.left=False

    def moveRight(self):        
        # print(f'Right{self.rect.left}')        
        if (self.rect.left < 785 and self.left is False):
            self.rect.left = self.rect.left+1

        if (self.rect.left == 785):
            self.left=True
            

        
            
            


