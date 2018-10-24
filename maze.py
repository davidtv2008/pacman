import pygame
from tiles import Tiles
from food import Food
from ghost import Ghost
from portal import Portal

class Maze:
    def __init__(self,screen,fileMap,tileImage,tiles,foods,ghosts,portals,routes):
        file = open('resources/maze/maze.txt', 'r')
        lines = file.readlines()

        c = 19
        r = 18

        for line in lines:
            for x in line:
                if x == 'X':
                    tile = Tiles(screen,c,r)
                    tiles.add(tile)
                if x == 'o':
                    food = Food(screen,c,r,'food')
                    foods.add(food)
                if x == 'p':
                    food = Food(screen,c,r,'power')
                    foods.add(food)
                    routes.append((r,c))
                if x == 'c':
                    food = Food(screen,c,r,'cherry')
                    foods.add(food)
                if x == 's':
                    food = Food(screen,c,r,'strawberry')
                    foods.add(food)
                if x == '1':
                    ghost = Ghost(screen,c,r,'blinky','gameplay')
                    ghosts.add(ghost)
                if x == '2':
                    ghost = Ghost(screen,c,r,'pinky','gameplay')
                    ghosts.add(ghost)
                if x == '3':
                    ghost = Ghost(screen,c,r,'cylde','gameplay')
                    ghosts.add(ghost)
                if x == '4':
                    ghost = Ghost(screen,c,r,'inkey','gameplay')
                    ghosts.add(ghost)
                if x == 'y':
                    portal = Portal(screen,c,r,'portal1')
                    portals.append(portal)
                if x == 'z':
                    portal = Portal(screen,c,r,'portal2')
                    portals.append(portal)
                if x == 'a':
                    food = Food(screen,c,r,'food')
                    foods.add(food)
                    routes.append((r,c))
                if x == 'b':
                    routes.append((r,c))
                if x == '\n':
                    r += 18
                c += 19
            c = 19
        file.close()