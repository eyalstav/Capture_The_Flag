import pygame
import Game_Field, Guard, Teleport
from Consts import *
from Soldier import soldier

screen = pygame.display.set_mode(WIN_SIZE)
pygame.display.set_caption("Capture The Flag")

grass_obj = pygame.transform.scale(pygame.image.load(GRASS_IMG),CELL_SIZE)
mine_obj = pygame.transform.scale(pygame.image.load(MINE_IMG),(CELL_SIZE[ROW_INDEX]*3,CELL_SIZE[1]))

def draw_field(field):
    for i in range(len(field)):
        for j in range(len(field[i])):
            if field[i][j]["type"] == "grass":
                screen.blit(grass_obj,(CELL_SIZE[ROW_INDEX]*j,CELL_SIZE[COL_INDEX]*i))

def draw_grid():
    '''
    draws the grid bright while players views the mines
    '''
    blockSize = int(CELL_SIZE[0]) #Set the size of the grid block
    for x in range(0, int(WIN_SIZE[0]), blockSize):
        for y in range(0, int(WIN_SIZE[1]), blockSize):
            rect = pygame.Rect(x, y, blockSize, blockSize)
            pygame.draw.rect(screen, NIGHT_GRID_COLOR, rect, NIGHT_GRID_WIDTH)

'''
the method below draws the mines and presents the night soldier
'''
night_soldier_img = pygame.transform.scale(pygame.image.load("bin/Swordsman/night.png"), SOLDIER_SIZE)
def draw_mines():
    field = Game_Field.field
    screen.fill((10,10,10))
    draw_grid()
    for y in range(len(field)):
        for x in range(len(field[y])):
            if field[y][x]["draw_mine"]:
                screen.blit(mine_obj,(CELL_SIZE[ROW_INDEX]*x,CELL_SIZE[COL_INDEX]*y))
    screen.blit(night_soldier_img, (soldier.x, soldier.y))
    screen.blit(Game_Field.flag.image, (Game_Field.flag.y, Game_Field.flag.x))
    screen.blit(Guard.guard.img, (Guard.guard.col*CELL_SIZE[0], Guard.guard.row*CELL_SIZE[1]))
    draw_tps()
    pygame.display.update()
    pygame.time.wait(MILISEC_IN_SEC*1) #waits 1 sec. 1000 miliseconds in one second


start_font = pygame.font.SysFont('Aerial',  START_FONT_SIZE)
def draw_start_msg():
    txt = start_font.render(START_MSG, False, START_MSG_COLOR)
    screen.blit(txt, (SOLDIER_SIZE[ROW_INDEX],20))
    pygame.display.update()
    pygame.time.wait(MILISEC_IN_SEC * 2)


dead_soldier = pygame.transform.rotate(pygame.transform.scale(pygame.image.load("bin/Swordsman/death.png"), SOLDIER_SIZE),20)

explosion = pygame.transform.scale(pygame.image.load(EXPLOAD_IMG), EXPLOAD_SIZE)
def draw_end_screen():
    draw_mines()
    screen.blit(dead_soldier,(soldier.x, soldier.y))
    field = Game_Field.field
    screen.fill(END_COLOR)
    draw_grid()
    for y in range(len(field)):
        for x in range(len(field[y])):
            if field[y][x]["draw_mine"]:
                screen.blit(mine_obj,(CELL_SIZE[ROW_INDEX]*x,CELL_SIZE[COL_INDEX]*y))
    screen.blit(dead_soldier, (soldier.x-SOLDIER_WIDTH/3*CELL_SIZE[0], soldier.y-SOLDIER_HEIGHT/3*CELL_SIZE[0]))
    screen.blit(explosion,(soldier.x,soldier.y+(CELL_SIZE[1]*SOLDIER_HEIGHT)-explosion.get_height()))
    pygame.display.update()


font=pygame.font.SysFont('timesnewroman',  60)
def draw_lose_msg():
    draw_end_screen()
    lose_txt = font.render(LOSE_MSG,False,LOSE_COLOR)
    screen.blit(lose_txt, (WIN_SIZE[0]/2-lose_txt.get_width()/2,WIN_SIZE[1]/2-lose_txt.get_height()/2))
    pygame.display.update()
    pygame.time.wait(1000*3)

def draw_win_msg():
    win_txt = font.render(WIN_MSG, False, WIN_COLOR)
    screen.blit(win_txt, (WIN_SIZE[0] / 2 - win_txt.get_width() / 2, WIN_SIZE[1] / 2 - win_txt.get_height() / 2))
    pygame.display.update()
    pygame.time.wait(1000 * 3)


def draw_obj(image_obj, location_pix):
    x_val = CELL_SIZE[ROW_INDEX] * location_pix[ROW_INDEX]
    y_val = CELL_SIZE[COL_INDEX] * location_pix[COL_INDEX]
    screen.blit(image_obj, (x_val, y_val))


def draw_tps():
    for tp in Teleport.tps:
        screen.blit(tp.img,(tp.x1*CELL_SIZE[0], tp.y1*CELL_SIZE[1]))
        screen.blit(tp.img, (tp.x2 * CELL_SIZE[0], tp.y2 * CELL_SIZE[1]))

def display_from_sheet(obj,x,y, sw, sh, size):
    image = pygame.Surface((sw,sh)).convert_alpha()
    image.blit(obj.sprite_sheet,(0,0), ((obj.frame*sw),0,sw,sh))
    image = pygame.transform.scale(image,size)
    image.set_colorkey((0,0,0))
    screen.blit(image,(x,y))

    obj.frame += 1
    if obj.sprite_sheet.get_width()/sw <= obj.frame:
        obj.frame = 0

def draw(field):
    screen.fill(BACKGROUND_COLOR)

    draw_field(field)

    draw_obj(Game_Field.flag.image, Game_Field.flag.location)
    #screen.blit(soldier.img, (soldier.x, soldier.y))
    screen.blit(Game_Field.flag.image, (Game_Field.flag.y, Game_Field.flag.x))
    screen.blit(Guard.guard.img, (Guard.guard.col*CELL_SIZE[0], Guard.guard.row*CELL_SIZE[1]))

    display_from_sheet(soldier, soldier.x, soldier.y, 128, 128, SOLDIER_SIZE)

    pygame.display.flip()
    pass

