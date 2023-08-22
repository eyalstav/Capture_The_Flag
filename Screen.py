import pygame
from Consts import *
from Soldier import *


screen = pygame.display.set_mode(WIN_SIZE)
pygame.display.set_caption("Capture The Flag")

grass_obj = pygame.transform.scale(pygame.image.load(GRASS_IMG),CELL_SIZE)

def draw_field(field:list[list]):
    for i in range(len(field)):
        for j in range(len(field[i])):
            if field[i][j]["type"] == "grass":
                screen.blit(grass_obj,(CELL_SIZE[0]*i,CELL_SIZE[1]*j))

def draw_mines(field:list[list]):
    screen.fill((10,10,10))
    for i in range(len(field)):
        for j in range(len(field[i])):
            if field[i][j]["mine"]:
                screen.blit(grass_obj,(CELL_SIZE[0]*i,CELL_SIZE[1]*j))
    pygame.time.wait(1000*1) #1 sec



def draw(field:list[list]):
    screen.fill((20,100,20))

    draw_field(field)

    screen.blit(soldier.img, (soldier.x,soldier.y))

    pygame.display.flip()
    pass

