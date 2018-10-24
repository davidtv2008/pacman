import pygame
import sys
from pygame.sprite import Sprite
import pygame.font

class Pacman(Sprite):
    def __init__(self,screen,window):
        super(Pacman,self).__init__()

        self.speed = 1
        self.window = window
        if window == 'gameplay':
            self.speed = 1
        
         #get the screen dims
        self.screen = screen
        self.screenRect = self.screen.get_rect()
        self.frame = 0
        self.soundFrequency = 0
        self.soundLimit = 320

        self.ghostTimer = 1999
        
        #create our pacman character
        self.image = pygame.image.load('resources/images/pacman.gif')
        self.rect = self.image.get_rect()
        self.rect.x = self.rect.width
        self.rect.y = self.rect.height
        self.x = float(self.rect.x)
        self.y = float(self.rect.y)

        self.movingRight = False
        self.movingLeft = False
        self.movingUp = False
        self.movingDown = False

        self.ghostSpawnTime = [0,0,0,0]


        if window == 'gameplay':
            self.rect.centerx = self.screenRect.centerx
            self.rect.top = self.screenRect.bottom - 340
        elif window == 'intro':
            self.rect.centerx = self.screenRect.left
            self.rect.centery = self.screenRect.centery
            self.movingRight = True

        self.center = float(self.rect.centerx)

        self.collision = False

        self.pointsCollected = 0
        self.lives = 2

        self.font = pygame.font.SysFont(None, 48)

        self.livesImage = pygame.image.load('resources/images/pacmanLeft1.gif')
        
        self.livesLeftImages = []
        self.fruitEaten = []
        
        for x in range(self.lives):
            self.livesLeftImages.append(self.livesImage)

        
        self.blitme()
            
    def update(self):
            
        self.frame += 1
        self.soundFrequency += 1

        if self.movingRight:
            self.rect.centerx += self.speed
            if self.frame == 30:
                self.image = pygame.image.load('resources/images/pacmanRight1.gif')
            if self.frame == 60:
                self.image = pygame.image.load('resources/images/pacmanRight2.gif')
            if self.frame == 90:
                self.image = pygame.image.load('resources/images/pacman.gif')
                self.frame = 0
        if self.movingLeft:
            self.rect.centerx -= self.speed
            if self.frame == 30:
                self.image = pygame.image.load('resources/images/pacmanLeft1.gif')
            if self.frame == 60:
                self.image = pygame.image.load('resources/images/pacmanLeft2.gif')
            if self.frame == 90:
                self.image = pygame.image.load('resources/images/pacman.gif')
                self.frame = 0
        if self.movingUp:
            self.rect.centery -= self.speed
            if self.frame == 30:
                self.image = pygame.image.load('resources/images/pacmanUp1.gif')
            if self.frame == 60:
                self.image = pygame.image.load('resources/images/pacmanUp2.gif')
            if self.frame == 90:
                self.image = pygame.image.load('resources/images/pacman.gif')
                self.frame = 0 
        if self.movingDown:
            self.rect.centery += self.speed
            if self.frame == 30:
                self.image = pygame.image.load('resources/images/pacmanDown1.gif')
            if self.frame == 60:
                self.image = pygame.image.load('resources/images/pacmanDown2.gif')
            if self.frame == 90:
                self.image = pygame.image.load('resources/images/pacman.gif')
                self.frame = 0
        if self.frame >= 90:
            self.frame = 0
        
        self.blitme()
        if self.window == 'gameplay':
            self.score()
            self.showLives()
            self.showFoodsCollected()

    def showFoodsCollected(self):
        if len(self.fruitEaten) > 0:
            spacing = 0
            for x in self.fruitEaten:
                foodImg = x
                foodImgRect = foodImg.get_rect()
                foodImgRect.right = self.screenRect.right - 20 + spacing
                foodImgRect.bottom = self.screenRect.bottom -60
                self.screen.blit(foodImg,foodImgRect)
                spacing -= 42    
        

    def score(self):
        """Turn the score into a rendered image."""
        roundedScore = int(round(self.pointsCollected, -1))
        scoreStr = "{:,}".format(roundedScore)
        self.scoreImage = self.font.render("SCORE " + scoreStr, True, (255,228,0),(0,0,0))
            
        # Display the score at the top right of the screen.
        self.scoreRect = self.scoreImage.get_rect()
        self.scoreRect.left = self.screenRect.left + 40
        self.scoreRect.bottom = self.screenRect.bottom -60

        self.screen.blit(self.scoreImage, self.scoreRect)

    def showLives(self):
        self.livesFont = self.font.render("LIVES",True,(255,228,0),(0,0,0))
        self.livesRect = self.livesFont.get_rect()
        self.livesRect.right = self.screenRect.right - 300
        self.livesRect.bottom = self.screenRect.bottom -60
        self.screen.blit(self.livesFont,self.livesRect)    
        
        #self.screen.blit(self.livesImage,self.livesImageRect)

        
    def blitme(self):
        #print self.rect.centerx
        self.screen.blit(self.image,self.rect)

        if self.window == 'gameplay':
            placement = 0
            for x in self.livesLeftImages:
                self.livesImageRect = x.get_rect()
                self.livesImageRect.right = self.screenRect.right - 250 + placement
                self.livesImageRect.bottom = self.screenRect.bottom - 60
                placement += 30
                self.screen.blit(x,self.livesImageRect)
            