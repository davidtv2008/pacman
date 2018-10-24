import pygame
import sys
from tiles import Tiles
from maze import Maze
import random

def checkEvents(screen,pacman,tiles,ghosts,routes):
    pacman.ghostTimer -= 1
        
    for ghost in ghosts:
        if ghost.ghostType == 'blinky' and pacman.ghostTimer == 1600:
            ghost.movingUp = True
        elif ghost.ghostType == 'pinky' and pacman.ghostTimer == 1000:
            ghost.movingUp = True
        elif ghost.ghostType == 'cylde' and pacman.ghostTimer == 400:
            ghost.movingUp = True
            
    for event in pygame.event.get(): 
        if event.type == pygame.QUIT:
            if pacman.pointsCollected > 0:
                file = open('resources/highScore.txt', 'a+')
                file.write(str(pacman.pointsCollected)+'\r\n')
                file.close()
            sys.exit()
        elif event.type == pygame.KEYDOWN:
            checkKeyDown(event,pacman,tiles,ghosts)
        #elif event.type == pygame.KEYUP:
        #    checkKeyUp(event,pacman,tiles)
        pacman.blitme()
    
    routeNode = 0
    for y,x in routes:
        for ghost in ghosts:
            if ghost.rect.centery == y and ghost.rect.centerx == x:                        
                ghost.movingUp = False
                ghost.movingDown = False
                ghost.movingLeft = False
                ghost.movingRight = False
                print routeNode
                if routeNode == 26:
                    if pacman.rect.centerx < ghost.rect.centerx:
                        ghost.movingLeft = True
                    elif pacman.rect.centerx > ghost.rect.centerx:
                        ghost.movingRight = True
                    elif pacman.rect.centerx >= ghost.rect.centerx:
                        ghost.movingRight = True
                elif routeNode == 25:
                    if pacman.rect.centerx <= ghost.rect.centerx:
                        ghost.movingLeft = True
                    elif pacman.rect.centerx > ghost.rect.centerx:
                        ghost.movingRight = True
                    elif pacman.rect.centery < ghost.rect.centery:
                        ghost.movingUp = True
                    elif pacman.rect.centery > ghost.rect.centery:
                        ghost.movingRight = True
                elif routeNode == 24:
                    if pacman.rect.centerx > ghost.rect.centerx:
                        ghost.movingRight = True
                    elif pacman.rect.centery > ghost.rect.centery:
                        ghost.movingDown = True
                elif routeNode == 31:
                    if pacman.rect.centerx < ghost.rect.centerx:
                        ghost.movingLeft = True
                    elif pacman.rect.centery > ghost.rect.centery:
                        ghost.movingDown = True
                    elif pacman.rect.centery < ghost.rect.centery:
                        ghost.movingUp = True
                    elif pacman.rect.centerx > ghost.rect.centerx:
                        ghost.movingDown = True
                elif routeNode == 30:
                    if pacman.rect.centerx < ghost.rect.centerx:
                        ghost.movingDown = True
                    elif pacman.rect.centery > ghost.rect.centery:
                        ghost.movingDown = True
                    elif pacman.rect.centery < ghost.rect.centery:
                        ghost.movingUp = True
                    elif pacman.rect.centerx > ghost.rect.centerx:
                        ghost.movingRight = True
                elif routeNode == 38:
                    if pacman.rect.centery < ghost.rect.centery:
                        ghost.movingUp = True
                    if pacman.rect.centery > ghost.rect.centery:
                        ghost.movingDown = True
                    elif pacman.rect.centerx > ghost.rect.centerx:
                        ghost.movingRight = True
                    elif pacman.rect.centerx < ghost.rect.centerx:
                        ghost.movingLeft = True
                elif routeNode == 37:
                    if pacman.rect.centerx > ghost.rect.centerx:
                        ghost.movingRight = True
                    elif pacman.rect.centery > ghost.rect.centery:
                        ghost.movingDown = True
                    elif pacman.rect.centery < ghost.rect.centery:
                        ghost.movingRight = True
                elif routeNode == 43:
                    if pacman.rect.centery > ghost.rect.centery:
                        ghost.movingDown = True
                    elif pacman.rect.centerx < ghost.rect.centerx:
                        ghost.movingLeft = True
                    
                elif routeNode == 44:
                    if pacman.rect.centerx > ghost.rect.centerx:
                        ghost.movingDown = True
                    elif pacman.rect.centery > ghost.rect.centery:
                        ghost.movingDown = True
                    elif pacman.rect.centery < ghost.rect.centery:
                        ghost.movingRight = True
                    elif pacman.rect.centerx < ghost.rect.centerx:
                        ghost.movingDown = True
                elif routeNode == 54:
                    if pacman.rect.centery > ghost.rect.centery:
                        ghost.movingDown = True
                    elif pacman.rect.centerx > ghost.rect.centerx:
                        ghost.movingRight = True
                elif routeNode == 53:
                    if pacman.rect.centerx < ghost.rect.centerx:
                        ghost.movingLeft = True
                    elif pacman.rect.centery < ghost.rect.centery:
                        ghost.movingUp = True
                    
                elif routeNode == 63:
                    if pacman.rect.centerx < ghost.rect.centerx:
                        ghost.movingLeft = True
                    elif pacman.rect.centery > ghost.rect.centery:
                        ghost.movingDown = True
                    
                elif routeNode == 64:
                    if pacman.rect.centerx > ghost.rect.centerx:
                        ghost.movingRight = True
                    elif pacman.rect.centery < ghost.rect.centery:
                        ghost.movingUp = True
                elif routeNode == 65:
                    if pacman.rect.centerx > ghost.rect.centerx:
                        ghost.movingRight = True
                    elif pacman.rect.centery < ghost.rect.centery:
                        ghost.movingUp = True
                elif routeNode == 66:
                    if pacman.rect.centerx > ghost.rect.centerx:
                        ghost.movingUp = True
                    elif pacman.rect.centerx > ghost.rect.centerx:
                        ghost.movingRight = True 
                    elif pacman.rect.centery < ghost.rect.centery:
                        ghost.movingUp = True
                    elif pacman.rect.centerx < ghost.rect.centerx:
                        ghost.movingLeft = True
                    
                elif routeNode == 62:
                    if pacman.rect.centery < ghost.rect.centery:
                        ghost.movingLeft = True
                    elif pacman.rect.centerx < ghost.rect.centery:
                        ghost.movingLeft = True
                    elif pacman.rect.centery > ghost.rect.centery:
                        ghost.movingRight = True
                    elif pacman.rect.centerx > ghost.rect.centerx:
                        ghost.movingRight = True
                elif routeNode == 61:
                    if pacman.rect.centery < ghost.rect.centery:
                        ghost.movingUp = True
                    elif pacman.rect.centerx > ghost.rect.centerx:
                        ghost.movingRight = True
                    elif pacman.rect.centery > ghost.rect.centery:
                        ghost.movingUp = True
                elif routeNode == 60:
                    if pacman.rect.centery < ghost.rect.centery:
                        ghost.movingUp = True
                    elif pacman.rect.centerx < ghost.rect.centerx:
                        ghost.movingUp = True
                    elif pacman.rect.centerx < ghost.rect.centerx:
                        ghost.movingLeft = True
                elif routeNode == 50:
                    if pacman.rect.centery > ghost.rect.centery:
                        ghost.movingDown = True
                    elif pacman.rect.centerx < ghost.rect.centerx:
                        ghost.movingLeft = True
                    elif pacman.rect.centerx > ghost.rect.centerx:
                        ghost.movingRight = True
                elif routeNode == 41:
                    if pacman.rect.centery < ghost.rect.centery:
                        ghost.movingUp = True
                    elif pacman.rect.centerx < ghost.rect.centerx:
                        ghost.movingLeft = True
                    elif pacman.rect.centerx > ghost.rect.centerx:
                        ghost.movingRight = True
                    elif pacman.rect.centery > ghost.rect.centery:
                        ghost.movingDown = True
                elif routeNode == 55:
                    if pacman.rect.centery < ghost.rect.centery:
                        ghost.movingUp = True
                    elif pacman.rect.centerx < ghost.rect.centerx:
                        ghost.movingLeft = True
                    elif pacman.rect.centerx > ghost.rect.centerx:
                        ghost.movingRight = True
                    elif pacman.rect.centery > ghost.rect.centery:
                        ghost.movingRight = True
                    elif pacman.rect.centery > ghost.rect.centery:
                        ghost.movingLeft = True
                elif routeNode == 45:
                    if pacman.rect.centerx < ghost.rect.centerx:
                        ghost.movingLeft = True
                    elif pacman.rect.centery > ghost.rect.centery:
                        ghost.movingDown = True
                    elif pacman.rect.centery < ghost.rect.centery:
                        ghost.movingLeft = True
                elif routeNode == 46:
                    if pacman.rect.centerx > ghost.rect.centerx:
                        ghost.movingRight = True
                    elif pacman.rect.centery > ghost.rect.centery:
                        ghost.movingDown = True
                    elif pacman.rect.centery < ghost.rect.centery:
                        ghost.movingUp = True
                elif routeNode == 47:
                    if pacman.rect.centerx > ghost.rect.centerx:
                        ghost.movingRight = True
                    elif pacman.rect.centery > ghost.rect.centery:
                        ghost.movingDown = True
                    elif pacman.rect.centerx < ghost.rect.centerx:
                        ghost.movingLeft = True
                elif routeNode == 48:
                    if pacman.rect.centerx < ghost.rect.centerx:
                        ghost.movingLeft = True
                    elif pacman.rect.centerx > ghost.rect.centerx:
                        ghost.movingRight = True
                    elif pacman.rect.centery < ghost.rect.centery:
                        ghost.movingUp = True
                elif routeNode == 49:
                    if pacman.rect.centery < ghost.rect.centery:
                        ghost.movingUp = True
                    elif pacman.rect.centerx < ghost.rect.centerx:
                        ghost.movingLeft = True
                    elif pacman.rect.centerx > ghost.rect.centerx:
                        ghost.movingRight = True
                elif routeNode == 33:
                    if pacman.rect.centery < ghost.rect.centery:
                        ghost.movingUp = True
                    elif pacman.rect.centerx > ghost.rect.centerx:
                        ghost.movingRight = True
                    elif pacman.rect.centerx < ghost.rect.centerx:
                        ghost.movingLeft = True
                elif routeNode == 40:
                    if pacman.rect.centerx > ghost.rect.centerx:
                        ghost.movingRight = True
                    elif pacman.rect.centery > ghost.rect.centery:
                        ghost.movingDown = True
                    elif pacman.rect.centery < ghost.rect.centery:
                        ghost.movingRight = True
                elif routeNode == 22:
                    if pacman.rect.centery < ghost.rect.centery:
                        ghost.movingUp = True
                    elif pacman.rect.centerx > ghost.rect.centerx:
                        ghost.movingRight = True
                    elif pacman.rect.centery > ghost.rect.centery:
                        ghost.movingDown = True
                elif routeNode == 14:
                    if pacman.rect.centery < ghost.rect.centery:
                        ghost.movingUp = True
                    elif pacman.rect.centerx > ghost.rect.centerx:
                        ghost.movingRight = True
                    elif pacman.rect.centerx < ghost.rect.centerx:
                        ghost.movingLeft = True
                    elif pacman.rect.centery > ghost.rect.centery:
                        ghost.movingDown = True
                elif routeNode == 4:
                    if pacman.rect.centerx > ghost.rect.centerx:
                        ghost.movingRight = True
                    elif pacman.rect.centerx < ghost.rect.centerx:
                        ghost.movingLeft = True
                    elif pacman.rect.centery > ghost.rect.centery:
                        ghost.movingDown = True
                elif routeNode == 3:
                    if pacman.rect.centery > ghost.rect.centery:
                        ghost.movingDown = True
                    elif pacman.rect.centerx > ghost.rect.centerx:
                        ghost.movingRight= True
                elif routeNode == 12:
                    if pacman.rect.centerx < ghost.rect.centerx:
                        ghost.movingLeft = True
                    elif pacman.rect.centerx > ghost.rect.centerx:
                        ghost.movingRight= True
                    elif pacman.rect.centery > ghost.rect.centery:
                        ghost.movingUp = True
                elif routeNode == 11:
                    if pacman.rect.centerx < ghost.rect.centerx:
                        ghost.movingLeft = True
                    elif pacman.rect.centerx > ghost.rect.centerx:
                        ghost.movingRight= True
                    elif pacman.rect.centery < ghost.rect.centery:
                        ghost.movingUp = True
                elif routeNode == 10:
                    if pacman.rect.centerx < ghost.rect.centerx:
                        ghost.movingLeft = True
                    elif pacman.rect.centery > ghost.rect.centery:
                        ghost.movingDown= True
                    elif pacman.rect.centerx > ghost.rect.centerx:
                        ghost.movingRight = True
                elif routeNode == 27:
                    if pacman.rect.centerx > ghost.rect.centerx:
                        ghost.movingRight = True
                    elif pacman.rect.centery < ghost.rect.centery:
                        ghost.movingUp= True
                    elif pacman.rect.centerx < ghost.rect.centerx:
                        ghost.movingLeft = True
                elif routeNode == 28:
                    if pacman.rect.centery > ghost.rect.centery:
                        ghost.movingDown = True
                    elif pacman.rect.centerx < ghost.rect.centerx:
                        ghost.movingLeft= True
                elif routeNode == 32:
                    if pacman.rect.centery > ghost.rect.centery:
                        ghost.movingDown = True
                    elif pacman.rect.centerx > ghost.rect.centerx:
                        ghost.movingRight= True
                    elif pacman.rect.centery < ghost.rect.centery:
                        ghost.movingUp= True
                elif routeNode == 36:
                    if pacman.rect.centery > ghost.rect.centery:
                        ghost.movingDown = True
                    elif pacman.rect.centerx < ghost.rect.centerx:
                        ghost.movingLeft= True
                    elif pacman.rect.centery < ghost.rect.centery:
                        ghost.movingUp= True
                elif routeNode == 42:
                    if pacman.rect.centery < ghost.rect.centery:
                        ghost.movingUp = True
                    elif pacman.rect.centerx < ghost.rect.centerx:
                        ghost.movingLeft= True
                    elif pacman.rect.centerx > ghost.rect.centerx:
                        ghost.movingRight= True
                    elif pacman.rect.centery > ghost.rect.centery:
                        ghost.movingDown= True
                    
                elif routeNode == 52:
                    if pacman.rect.centerx > ghost.rect.centerx:
                        ghost.movingRight = True
                    elif pacman.rect.centery > ghost.rect.centery:
                        ghost.movingDown= True
                    elif pacman.rect.centerx < ghost.rect.centerx:
                        ghost.movingDown = True
                elif routeNode == 51:
                    if pacman.rect.centery > ghost.rect.centery:
                        ghost.movingDown = True
                    elif pacman.rect.centery < ghost.rect.centery:
                        ghost.movingUp = True
                    if pacman.rect.centerx < ghost.rect.centerx:
                        ghost.movingLeft= True
                elif routeNode == 59:
                    if pacman.rect.centerx > ghost.rect.centerx:
                        ghost.movingRight = True
                    elif pacman.rect.centery > ghost.rect.centery:
                        ghost.movingDown= True
                    elif pacman.rect.centerx < ghost.rect.centerx:
                        ghost.movingRight= True
                elif routeNode == 13:
                    if pacman.rect.centerx > ghost.rect.centerx:
                        ghost.movingRight = True
                    elif pacman.rect.centerx < ghost.rect.centerx:
                        ghost.movingLeft= True
                    elif pacman.rect.centery > ghost.rect.centery:
                        ghost.movingDown= True
                elif routeNode == 56:
                    if pacman.rect.centerx < ghost.rect.centerx:
                        ghost.movingLeft = True
                    elif pacman.rect.centery < ghost.rect.centery:
                        ghost.movingUp= True
                    elif pacman.rect.centerx > ghost.rect.centerx:
                        ghost.movingUp= True
                elif routeNode == 67:
                    if pacman.rect.centerx < ghost.rect.centerx:
                        ghost.movingLeft = True
                    elif pacman.rect.centery < ghost.rect.centery:
                        ghost.movingUp= True
                elif routeNode == 9:
                    if pacman.rect.centery > ghost.rect.centery:
                        ghost.movingDown = True
                    elif pacman.rect.centerx < ghost.rect.centerx:
                        ghost.movingLeft= True
                    elif pacman.rect.centerx > ghost.rect.centerx:
                        ghost.movingRight= True
                    elif pacman.rect.centery < ghost.rect.centery:
                        ghost.movingUp= True
                elif routeNode == 17:
                    if pacman.rect.centery > ghost.rect.centery:
                        ghost.movingDown = True
                    elif pacman.rect.centerx < ghost.rect.centerx:
                        ghost.movingLeft= True
                    elif pacman.rect.centery < ghost.rect.centerx:
                        ghost.movingUp= True
                elif routeNode == 39:
                    if pacman.rect.centerx < ghost.rect.centerx:
                        ghost.movingLeft = True
                    elif pacman.rect.centery < ghost.rect.centery:
                        ghost.movingUp= True
                    elif pacman.rect.centerx > ghost.rect.centerx:
                        ghost.movingRight= True
                    
                    
                elif routeNode == 20:
                    if pacman.rect.centerx > ghost.rect.centerx:
                        ghost.movingRight = True
                    elif pacman.rect.centery > ghost.rect.centery:
                        ghost.movingDown= True
                elif routeNode == 58:
                    if pacman.rect.centerx < ghost.rect.centerx:
                        ghost.movingLeft = True
                    elif pacman.rect.centery > ghost.rect.centery:
                        ghost.movingDown= True
                    elif pacman.rect.centery < ghost.rect.centery:
                        ghost.movindLeft = True
                elif routeNode == 21:
                    if pacman.rect.centery < ghost.rect.centery:
                        ghost.movingUp = True
                    elif pacman.rect.centerx < ghost.rect.centerx:
                        ghost.movingLeft= True
                elif routeNode == 35:
                    if pacman.rect.centery < ghost.rect.centery:
                        ghost.movingUp = True
                    elif pacman.rect.centerx > ghost.rect.centerx:
                        ghost.movingRight= True
                    elif pacman.rect.centery > ghost.rect.centery:
                        ghost.movingDown= True
                elif routeNode == 16:
                    if pacman.rect.centery < ghost.rect.centery:
                        ghost.movingUp = True
                    elif pacman.rect.centerx > ghost.rect.centerx:
                        ghost.movingRight= True
                elif routeNode == 8:
                    if pacman.rect.centery < ghost.rect.centery:
                        ghost.movingUp = True
                    elif pacman.rect.centerx > ghost.rect.centerx:
                        ghost.movingRight= True
                    elif pacman.rect.centery > ghost.rect.centery:
                        ghost.movingDown= True
                elif routeNode == 57:
                    if pacman.rect.centery < ghost.rect.centery:
                        ghost.movingUp = True
                    elif pacman.rect.centerx > ghost.rect.centerx:
                        ghost.movingRight= True
                elif routeNode == 18:
                    if pacman.rect.centery < ghost.rect.centery:
                        ghost.movingUp = True
                    elif pacman.rect.centerx > ghost.rect.centerx:
                        ghost.movingRight= True
                    elif pacman.rect.centerx < ghost.rect.centerx:
                        ghost.movingRight = True
                elif routeNode == 19:
                    if pacman.rect.centerx < ghost.rect.centerx:
                        ghost.movingLeft = True
                    elif pacman.rect.centery > ghost.rect.centery:
                        ghost.movingDown= True
                    elif pacman.rect.centerx > ghost.rect.centerx:
                        ghost.movingLeft = True
                elif routeNode == 6:
                    if pacman.rect.centery < ghost.rect.centery:
                        ghost.movingUp = True
                    elif pacman.rect.centery > ghost.rect.centery:
                        ghost.movingDown= True
                elif routeNode == 5:
                    if pacman.rect.centery > ghost.rect.centery:
                        ghost.movingDown = True
                    elif pacman.rect.centerx < ghost.rect.centerx:
                        ghost.movingLeft= True
                elif routeNode == 15:
                    if pacman.rect.centery > ghost.rect.centery:
                        ghost.movingDown = True
                    elif pacman.rect.centerx < ghost.rect.centerx:
                        ghost.movingLeft= True
                    elif pacman.rect.centery < ghost.rect.centery:
                        ghost.movingUp= True
                    
        routeNode += 1

    


def checkKeyUp(event,pacman,tiles):
    ''''''
    if event.key == pygame.K_RIGHT:
        pacman.movingRight = False
    if event.key == pygame.K_LEFT:
        pacman.movingLeft = False
    if event.key == pygame.K_UP:
        pacman.movingUp = False
    if event.key == pygame.K_DOWN:
        pacman.movingDown = False



def checkKeyDown(event,pacman,tiles,ghosts):
    if event.key == pygame.K_RIGHT:
        pacman.movingRight = True
        pacman.movingLeft = False
        pacman.movingUp = False
        pacman.movingDown = False
    elif event.key == pygame.K_LEFT:
        pacman.movingLeft = True
        pacman.movingRight = False
        pacman.movingDown = False
        pacman.movingUp = False
        
    elif event.key == pygame.K_UP:
        pacman.movingUp = True
        pacman.movingDown = False
        pacman.movingRight = False
        pacman.movingLeft = False

        
    elif event.key == pygame.K_DOWN:
        pacman.movingDown = True
        pacman.movingUp = False
        pacman.movingLeft = False
        pacman.movingRight = False
        
    elif event.key == pygame.K_q:
        sys.exit()

def checkPortalCollisions(screen,pacman,portals):
    if pacman.rect.left > portals[0].rect.right and pacman.rect.centery > portals[0].rect.top and pacman.rect.centery < portals[0].rect.bottom:
        pacman.rect.centerx = portals[1].rect.centerx
        pacman.rect.centery = portals[1].rect.centery
    elif pacman.rect.right < portals[1].rect.left and pacman.rect.centery > portals[1].rect.top and pacman.rect.centery < portals[1].rect.bottom:
        pacman.rect.centerx = portals[0].rect.centerx
        pacman.rect.centery = portals[0].rect.centery
    elif pacman.rect.right < screen.get_rect().left and pacman.rect.centery > portals[0].rect.bottom and pacman.rect.centery < portals[1].rect.top:
        pacman.rect.centerx = screen.get_rect().right
    elif pacman.rect.left > screen.get_rect().right and pacman.rect.centery > portals[0].rect.bottom and pacman.rect.centery < portals[1].rect.top:
        pacman.rect.centerx = screen.get_rect().left
    

def checkWallCollisions(pacman,tiles,ghosts):
        collision = pygame.sprite.spritecollideany(pacman,tiles)
        
        if collision:
            
            if pacman.movingRight and pacman.movingUp:
                pacman.movingRight = False
                pacman.movingUp = False
                
                pacman.rect.right -= pacman.speed *2
                pacman.rect.top += pacman.speed *2
                
            if pacman.movingRight and pacman.movingDown:
                pacman.movingRight = False
                pacman.movingDown = False
                
                pacman.rect.centerx -= pacman.speed *2
                pacman.rect.centery -= pacman.speed *2

            if pacman.movingRight:
                pacman.movingRight = False
                
                pacman.rect.centerx -= pacman.speed *2

            
            if pacman.movingLeft and pacman.movingUp:
                pacman.movingLeft = False
                pacman.movingUp = False
                
                pacman.rect.centerx += pacman.speed *2
                pacman.rect.centery += pacman.speed*2
                
            if pacman.movingLeft and pacman.movingDown:
                pacman.movingLeft = False
                pacman.movingDown = False
                
                pacman.rect.centerx += pacman.speed*2
                pacman.rect.centery -= pacman.speed*2

            if pacman.movingLeft:
                pacman.movingLeft = False
                
                pacman.rect.centerx += pacman.speed*2
            
                
            if pacman.movingUp:
                pacman.movingUp = False
                
                pacman.rect.centery += pacman.speed*2
                
            if pacman.movingDown:
                pacman.movingDown = False
                
                pacman.rect.centery -= pacman.speed*2
                
        
        '''collisions1 = pygame.sprite.groupcollide(ghosts, tiles, False,False)
        if collisions1:
            for ghost in collisions1:
                checkGhostMovement(ghost)
        '''
                
        
def checkGhostMovement(ghost):

    num = random.randint(1,3)
        
    if ghost.movingUp:
        ghost.movingUp = False
        ghost.movingDown = False
        ghost.movindRight = False
        ghost.movingLeft = False
        ghost.rect.centery += ghost.speed
        if num == 1:
            ghost.movingRight = False
            ghost.movingLeft = True
            ghost.movingDown = False
        elif num == 2:
            ghost.movingLeft = False
            ghost.movingRight = True
            ghost.movingDown = False
        elif num == 3:
            ghost.movingLeft = False
            ghost.movingRight = False
            ghost.movingDown = True
    if ghost.movingRight:
        ghost.movingRight = False
        ghost.movingUp = False
        ghost.movingDown = False
        ghost.movingLeft = False
        ghost.rect.centerx -= ghost.speed
        if num == 1:
            ghost.movingUp = True
            ghost.movingDown = False
            ghost.movingLeft = False
        elif num == 2:
            ghost.movingUp = False
            ghost.movingDown = True
            ghost.movingLeft = False
        elif num == 3:
            ghost.movingUp = False
            ghost.movingDown = False
            ghost.movingLeft = True
    if ghost.movingLeft:
        ghost.movingRight = False
        ghost.movingUp = False
        ghost.movingDown = False
        ghost.movingLeft = False
        ghost.rect.centerx += ghost.speed
        if num == 1:
            ghost.movingRight = True
            ghost.movingUp = False
            ghost.movingDown = False
        if num == 2:
            ghost.movingRight = False
            ghost.movingUp = True
            ghost.movingDown = False
        if num == 3:
            ghost.movingRight = False
            ghost.movingUp = False
            ghost.movingDown = True
    if ghost.movingDown:
        ghost.movingRight = False
        ghost.movingUp = False
        ghost.movingDown = False
        ghost.movingLeft = False
        ghost.rect.centery -= ghost.speed
        if num == 1:
            ghost.movingRight = True
            ghost.movingUp = False
            ghost.movingLeft= False
        if num == 2:
            ghost.movingRight = False
            ghost.movingUp = True
            ghost.movingLeft = False
        if num == 3:
            ghost.movingRight = False
            ghost.movingUp = False
            ghost.movingLeft = True
    
        
def checkFoodCollisions(screen,pacman,foods,ghosts):
    collisions = pygame.sprite.spritecollide(pacman, foods, True)
    
    if collisions:
        for food in collisions:
            pygame.mixer.Channel(1).play(pygame.mixer.Sound('resources/sounds/pacman_chomp.wav'))
            pacman.pointsCollected += food.points
            if food.foodType == 'cherry':
                pacman.fruitEaten.append(pygame.image.load('resources/images/cherry.gif'))
            elif food.foodType == 'strawberry':
                pacman.fruitEaten.append(pygame.image.load('resources/images/strawberry.gif'))
            elif food.foodType == 'power':
                weakGhost(ghosts)

def checkGhostCollision(screen,pacman,foods,ghosts):    
    collisions1 = pygame.sprite.spritecollide(pacman, ghosts, False)

    if collisions1:
        for ghost in collisions1:
            if ghost.weak == False:
                #print ghost.ghostName
                pacman.rect.centerx = screen.get_rect().centerx
                pacman.rect.top = screen.get_rect().bottom - 340
                #print 'pacman died'
                pacman.lives -=1
                if pacman.lives < 0:
                    print 'game over'
                else:
                    pacman.livesLeftImages.pop()
    
    collisions2 = pygame.sprite.spritecollide(pacman,ghosts,True)

    if collisions2:
        for ghost in collisions2:
            if ghost.weak:
                pacman.pointsCollected += ghost.points
                print len(ghosts)
                if len(ghosts) == 3:
                    pacman.ghostSpawnTime[0] = 700
                elif len(ghosts) == 2:
                    pacman.ghostSpawnTime[1] = 700
                elif len(ghosts) == 1:
                    pacman.ghostSpawnTime[2] = 700
                elif len(ghosts) == 0:
                    pacman.ghostSpawnTime[3] = 700
    


        
def weakGhost(ghosts):
    for g in ghosts:
        g.weak = True
        g.weakTime = 2000
        print g.movingUp
        print g.movingDown
        print g.movingLeft
        print g.movingRight