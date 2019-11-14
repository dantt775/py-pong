from constants import Constants
class MoveHelper:
    def __init__(self, rect):
        self.rect = rect



    def move_left(self):               
        self.rect.left = self.rect.left-1

    def move_right(self):
        self.rect.left = self.rect.left+1


    def move_up(self):      
        if (self.rect.top > 5):
            self.rect.top -=1       
    
    def move_down(self):
        if (self.rect.top < (Constants.HEIGHT-self.rect.height)-5):
            self.rect.top+=1
        
        

