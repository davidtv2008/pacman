import pygame
import sys
from pacman import Pacman
from pygame.sprite import Group
from maze import Maze
from MainMenu import MainMenu
import time
import events as e

def App():

    pygame.mixer.pre_init(22050, -16, 2, 512)
    pygame.mixer.init()

    pygame.mixer.Channel(0).play(pygame.mixer.Sound('resources/sounds/pacman_beginning.wav'))
    pygame.init()


    screen = pygame.display.set_mode((890,1020))

    mainMenu = MainMenu(screen)
    mainMenu.wait()

    #create my pacman character
    pacman = Pacman(screen,'gameplay')

    
    #create group to hold all tiles, and create actual tiles
    portals = []
    tiles = Group()
    foods = Group()
    ghosts = Group()

    routes = []

    ghostCounter = 1000
    
    maze = Maze(screen,'resources/maze/maze.txt','resources/images/tile.gif',tiles,foods,ghosts,portals,routes)

    while True:
        e.checkEvents(screen,pacman,tiles,ghosts,routes)
        screen.fill((0,0,0))
        e.checkWallCollisions(pacman,tiles,ghosts)
        e.checkFoodCollisions(screen,pacman,foods,ghosts)
        e.checkPortalCollisions(screen,pacman,portals)
        e.checkGhostCollision(screen,pacman,foods,ghosts)
        pacman.update()
        tiles.update()
        foods.update()
        ghosts.update()
        portals[0].update()
        portals[1].update()
        pygame.display.flip()

    print time.time()

App()