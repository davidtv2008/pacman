import pygame
from pygame.sprite import Sprite

class Food(Sprite):
    def __init__(self,screen,x,y,foodType):
        super(Food,self).__init__()

         #get the screen dims
        self.screen = screen
        self.screenRect = self.screen.get_rect()
        self.frame = 0
        self.soundFrequency = 0
        self.soundLimit = 320

        self.foodType = foodType

        #create our food object
        if foodType == 'food':
            self.image = pygame.image.load('resources/images/food.gif')
        elif foodType == 'power':
            self.image = pygame.image.load('resources/images/power.gif')
        elif foodType == 'cherry':
            self.image = pygame.image.load('resources/images/cherry.gif')
        elif foodType == 'strawberry':
            self.image = pygame.image.load('resources/images/strawberry.gif')
        self.rect = self.image.get_rect()
        self.rect.x = self.rect.width
        self.rect.y = self.rect.height
        self.x = float(self.rect.x)
        self.y = float(self.rect.y)
        
        self.rect.centerx = x
        self.rect.bottom = y
        

        self.center = float(self.rect.centerx)

        if self.foodType == 'food':
            self.points = 10
        elif self.foodType =='power':
            self.points = 30
        elif self.foodType == 'cherry' or self.foodType == 'strawberry':
            self.points = 60

        self.blitme()
            
    def update(self):            
        self.blitme()

    def blitme(self):
        self.screen.blit(self.image,self.rect) 

        