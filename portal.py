import pygame

class Portal():
    def __init__(self,screen,x,y,portal):
        
        #get the screen dims
        self.screen = screen
        self.screenRect = self.screen.get_rect()
        self.frame = 0
        self.soundFrequency = 0
        self.soundLimit = 320

        self.portal = portal

        #create our food object
        if portal == 'portal1':
            self.image = pygame.image.load('resources/images/portalTop.gif')
            self.image = pygame.transform.scale(self.image,(55,65))
        elif portal == 'portal2':
            self.image = pygame.image.load('resources/images/portalBottom.gif')
            self.image = pygame.transform.scale(self.image,(55,85))
    
        self.rect = self.image.get_rect()
        self.rect.x = self.rect.width
        self.rect.y = self.rect.height
        self.x = float(self.rect.x)
        self.y = float(self.rect.y)
        
        self.rect.centerx = x
        self.rect.bottom = y + 17
        
        self.center = float(self.rect.centerx)
        
        self.blitme()
    
    def update(self):            
        self.blitme()

    def blitme(self):
        self.screen.blit(self.image,self.rect) 


