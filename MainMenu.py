import pygame
import sys
from pygame.sprite import Sprite
from pacman import Pacman
from ghost import Ghost
from food import Food

class MainMenu(Sprite):
    
    def __init__(self,screen):

        super(MainMenu,self).__init__()

        #create some attributes and setup text for main menu
        #"SPACE" text
        self.textColor1 = (255,255,255)
        self.font1 = pygame.font.SysFont(None, 100)

        self.pacman = Pacman(screen,'intro')
        self.ghost1 = Ghost(screen,10,10,'blinky','intro')
        self.ghost2 = Ghost(screen,10,10,'pinky','intro')
        self.ghost3 = Ghost(screen,10,10,'cylde','intro')
        self.ghost4 = Ghost(screen,10,10,'inkey','intro')
        
        
        self.screen = screen

        #"INVADERS" text
        self.textColor2 = (255,255,255)
        self.font2 = pygame.font.SysFont(None,100)

        #create my actual text for the title and set its color and background color
        self.title1 = self.font1.render("PA", True, self.textColor1, (0,0,0))
        self.title1Rect = self.title1.get_rect()
        self.title1Rect.centerx = screen.get_rect().centerx - 100
        self.title1Rect.centery = screen.get_rect().top + 50
        
        self.imageTitle= pygame.image.load('resources/images/pacmanRight1.gif')
        self.imageTitle = pygame.transform.scale(self.imageTitle,(70,70))
        self.imageTitleRect = self.imageTitle.get_rect()
        self.imageTitleRect.centery = self.title1Rect.centery + 10
        self.imageTitleRect.centerx = self.title1Rect.centerx + 80

        self.title2 = self.font2.render("MAN",True,self.textColor2,(0,0,0))
        self.title2Rect = self.title2.get_rect()
        self.title2Rect.centery = self.title1Rect.centery
        self.title2Rect.centerx = self.imageTitleRect.centerx + 120

        self.introduction = self.font2.render('BLINKY',True,self.textColor2,(0,0,0))
        self.introductionRect = self.introduction.get_rect()
        self.introductionRect.centery = self.title2Rect.centery + 260
        self.introductionRect.centerx = self.title2Rect.centerx - 80
        
        
        #play button to start game
        self.start = self.font2.render("Play Game", True, self.textColor2, (0,0,0))
        self.startRect = self.start.get_rect()
        self.startRect.centery = screen.get_rect().bottom - 200
        self.startRect.centerx = screen.get_rect().centerx
        self.rect = pygame.Rect(self.startRect.left,self.startRect.top, self.startRect.width, self.startRect.height)
        self.play = False

        #highscores button to start game
        self.highScore = self.font2.render("Highest Score", True, self.textColor2, (0,0,0))
        self.highRect = self.highScore.get_rect()
        self.highRect.centery = screen.get_rect().bottom - 120
        self.highRect.centerx = screen.get_rect().centerx
        self.highrect = pygame.Rect(self.highRect.left,self.highRect.top, self.highRect.width, self.highRect.height)
        self.score = False
        self.scores = []
        self.highestScore = 0

        self.addAll()
        

    def addAll(self):
        self.addGameObject(self.screen,self.title1,self.title1Rect)
        self.addGameObject(self.screen,self.imageTitle,self.imageTitleRect)
        self.addGameObject(self.screen,self.title2,self.title2Rect)
        self.addGameObject(self.screen,self.start,self.startRect)
        self.addGameObject(self.screen,self.highScore,self.highRect)
    
    def wait(self):
        while self.play == False:
            for event in pygame.event.get():
                if event.type==pygame.QUIT:
                    sys.exit()
                elif event.type ==pygame.MOUSEBUTTONDOWN:
                    mouse_x,mouse_y = pygame.mouse.get_pos()
                    self.check_play_button(mouse_x,mouse_y)
                    self.check_score_button(mouse_x,mouse_y)
            self.screen.fill((0,0,0))

            if self.ghost4.rect.left > self.screen.get_rect().right + 60:
                self.ghost4.movingRight = False
                self.ghost3.movingRight = False
                self.ghost2.movingRight = False
                self.ghost1.movingRight = False
                self.pacman.movingRight = False

                self.ghost4.movingLeft = True
                self.ghost3.movingLeft = True
                self.ghost2.movingLeft = True
                self.ghost1.movingLeft = True
                self.pacman.movingLeft = True
            
            if self.pacman.rect.right < self.screen.get_rect().left - 60:
                self.ghost4.movingLeft = False
                self.ghost3.movingLeft = False
                self.ghost2.movingLeft = False
                self.ghost1.movingLeft = False
                self.pacman.movingLeft = False

                self.ghost1.movingRight = True
                if self.ghost1.movingRight:
                    self.introduction = self.font2.render('BLINKY',True,(186,32,42),(0,0,0))
                    self.screen.blit(self.introduction,self.introductionRect)
        

            if self.pacman.rect.right < self.screen.get_rect().left - 60 and self.ghost1.rect.left > self.screen.get_rect().right + 60:
                self.ghost1.movingRight = False
                self.ghost2.movingRight = True

                if self.ghost2.movingRight:
                    self.introduction = self.font2.render('PINKY   ',True,(241,103,132),(0,0,0))
                    self.screen.blit(self.introduction,self.introductionRect)
        
                
            if self.pacman.rect.right < self.screen.get_rect().left - 60 and self.ghost2.rect.left > self.screen.get_rect().right + 60:
                self.ghost2.movingRight = False
                self.ghost3.movingRight = True
                if self.ghost3.movingRight:
                    self.introduction = self.font2.render('INKEY   ',True,(0,173,232),(0,0,0))
                    self.screen.blit(self.introduction,self.introductionRect)
            
            if self.pacman.rect.right < self.screen.get_rect().left - 60 and self.ghost3.rect.left > self.screen.get_rect().right + 60:
                self.ghost3.movingRight = False
                self.ghost4.movingRight = True
                if self.ghost4.movingRight:
                    self.introduction = self.font2.render('CLYDE   ',True,(247,147,82),(0,0,0))
                    self.screen.blit(self.introduction,self.introductionRect)
            
            if self.pacman.rect.right < self.screen.get_rect().left - 60 and self.ghost4.rect.left > self.screen.get_rect().right + 60:
                self.ghost4.movingRight = False   
        
            self.pacman.update()
            self.ghost1.update()
            self.ghost2.update()
            self.ghost3.update()
            self.ghost4.update()
            
            self.addAll()

            pygame.display.flip()    

    def displayHighScore(self):
        file = open('resources/highScore.txt', 'r')
        f1 = file.readlines()
        for x in f1:
            self.scores.append(int(x))
        file.close()

        if len(self.scores) == 0:
            print("no scores to show")
        elif len(self.scores) == 1:
            self.highestScore = self.scores[0]
        elif len(self.scores) > 1:
            i = 0
            self.highestScore = self.scores[0]
            while i < len(self.scores):
                if self.highestScore < self.scores[i+1]:
                    self.highestScore = self.scores[i+1]
                i += 1
                if i == len(self.scores)-1:
                    break
        open('resources/highScore.txt', 'w').close()
        file = open('resources/highScore.txt','w')
        file.write(str(self.highestScore)+'\r\n')

        self.hs = self.font2.render(str(self.highestScore),True,self.textColor2,(0,0,0))
        self.hsRect = self.hs.get_rect()
        self.hsRect.center = (self.screen.get_rect().centerx, self.highRect.bottom + 30)
        self.addGameObject(self.screen,self.hs,self.hsRect)
               

    def check_play_button(self,mouse_x,mouse_y):
        """Start a new game when the player click Play."""
        button_clicked = self.rect.collidepoint(mouse_x,mouse_y)

        if button_clicked:
            self.play = True
        
    def check_score_button(self,mouse_x,mouse_y):
        """Start a new game when the player click Play."""
        button_clicked = self.highrect.collidepoint(mouse_x,mouse_y)

        if button_clicked:
            self.displayHighScore()


    def addGameObject(self,screen,object,xy):
        #print(len(object))
        screen.blit(object,xy)  