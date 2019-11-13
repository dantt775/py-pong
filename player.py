import pygame
from constants import Constants

class Player:
    def __init__(self, left):
        self.rect = pygame.Rect(
                        left,
                        Constants.PLAYER_INITIAL_TOP,
                        Constants.PLAYER_WIDTH,
                        Constants.PLAYER_HEIGHT
                    )
    
    def moveUp(self):        
        if (self.rect.top > 5):#check screen limits
            self.rect.top=self.rect.top-1        

    def movDown(self):
        if (self.rect.top < (Constants.HEIGHT-self.rect.height)-5): #check screen limits
            self.rect.top=self.rect.top+1