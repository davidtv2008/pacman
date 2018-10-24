import pygame
from pygame.sprite import Sprite

class Ghost(Sprite):
    def __init__(self,screen,x,y,ghostType,window):
        super(Ghost,self,).__init__()

        self.speed = 1
        self.window = window
        self.frame = 0
        if window == 'gameplay':
            self.speed = 1
            self.movingRight = False
            self.movingUp = False
        else:
            self.movingRight = True
            self.movingUp = False

        #get the screen dims
        self.screen = screen
        self.screenRect = self.screen.get_rect()
        self.frame = 0
        self.soundFrequency = 5
        self.soundLimit = 3000

        self.ghostType = ghostType
        self.weak = False
        self.weakTime = 0

        self.movingLeft = False
        self.movingDown = False
        self.ghostName = ghostType

        self.points = 100

        #create our food object
        if ghostType == 'blinky':
            self.image = pygame.image.load('resources/images/redGhostRight.gif')
            self.movingUp = False
        elif ghostType == 'pinky':
            self.image = pygame.image.load('resources/images/pinkGhostRight.gif')
            self.movingUp = False
        elif ghostType == 'cylde':
            self.image = pygame.image.load('resources/images/blueGhostRight.gif')
            self.movingUp = False 
        elif ghostType == 'inkey':
            self.image = pygame.image.load('resources/images/orangeGhostRight.gif')
            self.movingUp = True
        self.rect = self.image.get_rect()
        self.rect.x = self.rect.width
        self.rect.y = self.rect.height
        self.x = float(self.rect.x)
        self.y = float(self.rect.y)
        
        self.rect.centerx = x
        self.rect.centery = y

        if window == 'intro':
            if ghostType == 'blinky':
                self.rect.centerx = self.screenRect.left - 80
                self.rect.centery = self.screenRect.centery
            elif ghostType == 'pinky':
                self.rect.centerx = self.screenRect.left - 140
                self.rect.centery = self.screenRect.centery
            elif ghostType == 'cylde':
                self.rect.centerx = self.screenRect.left - 200
                self.rect.centery = self.screenRect.centery
            elif ghostType == 'inkey':
                self.rect.centerx = self.screenRect.left - 260
                self.rect.centery = self.screenRect.centery

        
        self.center = float(self.rect.centerx)
        #self.image= pygame.transform.scale(self.image,(20,20))
        
        
        self.blitme()
    
    def update(self):
        self.frame += 1
        self.soundFrequency += 1

        if self.weakTime <= 0:
            self.weak = False
            if self.ghostType == 'blinky':
                self.image = pygame.image.load('resources/images/redGhostRight.gif')
            elif self.ghostType == 'pinky':
                self.image = pygame.image.load('resources/images/pinkGhostRight.gif')
            elif self.ghostType == 'cylde':
                self.image = pygame.image.load('resources/images/blueGhostRight.gif')
            elif self.ghostType == 'inkey':
                self.image = pygame.image.load('resources/images/orangeGhostRight.gif')
            if self.movingRight:
                self.rect.centerx += self.speed
                if self.ghostType == 'blinky':
                    self.image = pygame.image.load('resources/images/redGhostRight.gif')
                elif self.ghostType == 'pinky':
                    self.image = pygame.image.load('resources/images/pinkGhostRight.gif')
                elif self.ghostType == 'cylde':
                    self.image = pygame.image.load('resources/images/blueGhostRight.gif')
                elif self.ghostType == 'inkey':
                    self.image = pygame.image.load('resources/images/orangeGhostRight.gif')
            elif self.movingLeft:
                self.rect.centerx -= self.speed
                if self.ghostType == 'blinky':
                    if self.window == 'intro':
                        self.image = pygame.image.load('resources/images/scaredGhost.gif')
                    else:
                        self.image = pygame.image.load('resources/images/redGhostLeft.gif')
                elif self.ghostType == 'pinky':
                    if self.window == 'intro':
                        self.image = pygame.image.load('resources/images/scaredGhost.gif')
                    else:
                        self.image = pygame.image.load('resources/images/pinkGhostLeft.gif')
                elif self.ghostType == 'cylde':
                    if self.window == 'intro':
                        self.image = pygame.image.load('resources/images/scaredGhost.gif')
                    else:
                        self.image = pygame.image.load('resources/images/blueGhostLeft.gif')
                elif self.ghostType == 'inkey':
                    if self.window == 'intro':
                        self.image = pygame.image.load('resources/images/scaredGhost.gif')
                    else:
                        self.image = pygame.image.load('resources/images/orangeGhostLeft.gif')
            elif self.movingUp:
                self.rect.centery -= self.speed
                if self.ghostType == 'blinky':
                    self.image = pygame.image.load('resources/images/redGhostUp.gif')
                elif self.ghostType == 'pinky':
                    self.image = pygame.image.load('resources/images/pinkGhostUp.gif')
                elif self.ghostType == 'cylde':
                    self.image = pygame.image.load('resources/images/blueGhostUp.gif')
                elif self.ghostType == 'inkey':
                    self.image = pygame.image.load('resources/images/orangeGhostUp.gif')
            elif self.movingDown:
                self.rect.centery += self.speed
                if self.ghostType == 'blinky':
                    self.image = pygame.image.load('resources/images/redGhostDown.gif')
                elif self.ghostType == 'pinky':
                    self.image = pygame.image.load('resources/images/pinkGhostDown.gif')
                elif self.ghostType == 'cylde':
                    self.image = pygame.image.load('resources/images/blueGhostDown.gif')
                elif self.ghostType == 'inkey':
                    self.image = pygame.image.load('resources/images/orangeGhostDown.gif')
        elif self.weakTime > 0:
            self.image = pygame.image.load('resources/images/scaredGhost.gif')
            self.weak = True
            self.weakTime -= 1
            if self.weakTime < 500:
                if self.weakTime%10 == 0:
                    self.image = pygame.image.load('resources/images/scaredGhost2.gif')    

        #self.image= pygame.transform.scale(self.image,(30,30))
            
        self.blitme()

    def blitme(self):
        self.screen.blit(self.image,self.rect) 