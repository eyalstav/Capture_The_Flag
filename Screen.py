import pygame
from Consts import *
from Soldier import *


screen = pygame.display.set_mode(WIN_SIZE)
pygame.display.set_caption("Capture The Flag")

grass_obj = pygame.transform.scale(pygame.image.load(GRASS_IMG),CELL_SIZE)
mine_obj = pygame.transform.scale(pygame.image.load(MINE_IMG),(CELL_SIZE[0]*3,CELL_SIZE[1]))

def draw_field(field:list[list]):
    for i in range(len(field)):
        for j in range(len(field[i])):
            if field[i][j]["type"] == "grass":
                screen.blit(grass_obj,(CELL_SIZE[0]*j,CELL_SIZE[1]*i))

def draw_mines(field:list[list]):
    screen.fill((10,10,10))
    for i in range(len(field)):
        for j in range(len(field[i])):
            if field[i][j]["draw_mine"]:
                screen.blit(mine_obj,(CELL_SIZE[0]*j,CELL_SIZE[1]*i))
    pygame.display.update()
    pygame.time.wait(1000*1) #1 sec

font=pygame.font.SysFont('timesnewroman',  60)
def draw_lose_msg():
    lose_txt = font.render(LOSE_MSG,False,(20,20,20))
    screen.blit(lose_txt, (WIN_SIZE[0]/2-lose_txt.get_width()/2,WIN_SIZE[1]/2-lose_txt.get_height()/2))
    pygame.display.update()
    pygame.time.wait(1000*3)




def draw(field:list[list]):
    screen.fill((20,100,20))

    draw_field(field)

    screen.blit(soldier.img, (soldier.x,soldier.y))

    pygame.display.flip()
    pass

