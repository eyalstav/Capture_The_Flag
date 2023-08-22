import pygame

import Game_Field
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

def draw_grid():
    blockSize = int(CELL_SIZE[0]) #Set the size of the grid block
    for x in range(0, int(WIN_SIZE[0]), blockSize):
        for y in range(0, int(WIN_SIZE[1]), blockSize):
            rect = pygame.Rect(x, y, blockSize, blockSize)
            pygame.draw.rect(screen, (255,255,255), rect, 1)

night_soldier_img = pygame.transform.scale(pygame.image.load(NIGHT_SOLDIER_IMG), SOLDIER_SIZE)
def draw_mines():
    field = Game_Field.field
    screen.fill((10,10,10))
    draw_grid()
    for y in range(len(field)):
        for x in range(len(field[y])):
            if field[y][x]["draw_mine"]:
                screen.blit(mine_obj,(CELL_SIZE[0]*x,CELL_SIZE[1]*y))
    screen.blit(night_soldier_img, (soldier.x, soldier.y))
    pygame.display.update()
    pygame.time.wait(1000*1) #1 sec

start_font = pygame.font.SysFont('Aerial',  20)
def draw_start_msg():
    txt = start_font.render(START_MSG, False, (255, 255, 255))
    screen.blit(txt, (SOLDIER_SIZE[0],20))
    pygame.display.update()
    pygame.time.wait(1000 * 2)

dead_soldier = pygame.transform.scale(pygame.image.load(DEAD_SOLDIER_IMG), SOLDIER_SIZE)
explosion = pygame.transform.scale(pygame.image.load(EXPLOAD_IMG), EXPLOAD_SIZE)
def draw_end_screen():
    draw_mines()
    screen.blit(dead_soldier,(soldier.x, soldier.y))
    field = Game_Field.field
    screen.fill((10,10,10))
    draw_grid()
    for y in range(len(field)):
        for x in range(len(field[y])):
            if field[y][x]["draw_mine"]:
                screen.blit(mine_obj,(CELL_SIZE[0]*x,CELL_SIZE[1]*y))
    screen.blit(dead_soldier, (soldier.x, soldier.y))
    screen.blit(explosion,(soldier.x,soldier.y+CELL_SIZE[1]))
    pygame.display.update()


font=pygame.font.SysFont('timesnewroman',  60)
def draw_lose_msg():
    draw_end_screen()
    lose_txt = font.render(LOSE_MSG,False,(255,255,255))
    screen.blit(lose_txt, (WIN_SIZE[0]/2-lose_txt.get_width()/2,WIN_SIZE[1]/2-lose_txt.get_height()/2))
    pygame.display.update()
    pygame.time.wait(1000*3)

def draw_win_msg():
    win_txt = font.render(WIN_MSG, False, (20, 20, 20))
    screen.blit(win_txt, (WIN_SIZE[0] / 2 - win_txt.get_width() / 2, WIN_SIZE[1] / 2 - win_txt.get_height() / 2))
    pygame.display.update()
    pygame.time.wait(1000 * 3)

def draw_obj(image_obj, location_pix):
    x_val = CELL_SIZE[0] * location_pix[0]
    y_val = CELL_SIZE[1] * location_pix[1]
    screen.blit(image_obj, (x_val, y_val))




def draw(field:list[list]):
    screen.fill((20,100,20))

    draw_field(field)

    screen.blit(soldier.img, (soldier.x,soldier.y))
    screen.blit(Game_Field.flag.image, (Game_Field.flag.y, Game_Field.flag.x))
    screen.blit(Soldier.soldier.img, (Soldier.soldier.x, Soldier.soldier.y))


    pygame.display.flip()
    pass
