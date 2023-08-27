import pygame
import Game_Field, Guard, Teleport
from Consts import *
from Soldier import soldier

screen = pygame.display.set_mode(WIN_SIZE)
pygame.display.set_caption("Capture The Flag")

grass_obj = pygame.transform.scale(pygame.image.load(GRASS_IMG),CELL_SIZE)
mine_obj = pygame.transform.scale(pygame.image.load(MINE_IMG),(CELL_SIZE[ROW_INDEX]*3,CELL_SIZE[1]))


upper_left_cell = [0,0]
def draw_field(field):
    for i in range(top_left_corner[Y_INDEX], len(field)):
        for j in range(top_left_corner[X_INDEX], len(field[i])):
            if field[i][j]["type"] == "grass":
                relative_loc = (CELL_SIZE[ROW_INDEX]*(j -top_left_corner[X_INDEX]),CELL_SIZE[COL_INDEX]*(i- top_left_corner[Y_INDEX]))
                screen.blit(grass_obj, relative_loc)

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
def draw_mines():
    field = Game_Field.field
    screen.fill((10,10,10))
    draw_grid()
    for y in range(top_left_corner[Y_INDEX], len(field)):
        for x in range(top_left_corner[X_INDEX], len(field[y])):
            if field[y][x]["draw_mine"]:
                relative_loc = (CELL_SIZE[ROW_INDEX]*(x -top_left_corner[X_INDEX]),CELL_SIZE[COL_INDEX]*(y- top_left_corner[Y_INDEX]))
                screen.blit(mine_obj,relative_loc)
    top_left_screen = top_left_corner[X_INDEX] * CELL_SIZE[X_INDEX], top_left_corner[Y_INDEX] * CELL_SIZE[Y_INDEX]
    soldier_relative_loc = find_relative_loc(soldier.x, soldier.y)
    display_from_sheet(soldier, soldier_relative_loc[0], soldier_relative_loc[1], 128, 128, SOLDIER_SIZE)
    screen.blit(Game_Field.flag.image, (Game_Field.flag.x - top_left_screen[X_INDEX], Game_Field.flag.y - top_left_screen[Y_INDEX]))
    guard_relative_location = find_relative_loc(Guard.guard.col, Guard.guard.row, True)
    display_from_sheet(Guard.guard, guard_relative_location[0], guard_relative_location[1], 128, 64, (Guard.guard.w*CELL_SIZE[0], Guard.guard.h*CELL_SIZE[1]))
    draw_tps()
    pygame.display.update()
    pygame.time.wait(MILISEC_IN_SEC*1) #waits 1 sec. 1000 miliseconds in one second



start_font = pygame.font.SysFont('David',  START_FONT_SIZE, True)
def draw_start_msg():
    txt = start_font.render(START_MSG, False, START_MSG_COLOR)
    screen.blit(txt, (SOLDIER_SIZE[ROW_INDEX],20))
    pygame.display.update()
    pygame.time.wait(MILISEC_IN_SEC * 2)


dead_soldier = pygame.transform.rotate(pygame.transform.scale(pygame.image.load(SOLDIER_FOLDER + "death.png"), SOLDIER_SIZE), 20)

explosion = pygame.transform.scale(pygame.image.load(EXPLOAD_IMG), EXPLOAD_SIZE)
def draw_end_screen():
    draw_mines()
    screen.blit(dead_soldier,(soldier.x, soldier.y))
    field = Game_Field.field
    screen.fill(END_COLOR)
    draw_grid()
    for y in range(top_left_corner[Y_INDEX], len(field)):
        for x in range(top_left_corner[X_INDEX], len(field[y])):
            if field[y][x]["draw_mine"]:
                relative_loc = (CELL_SIZE[ROW_INDEX]*(x -top_left_corner[X_INDEX]),CELL_SIZE[COL_INDEX]*(y- top_left_corner[Y_INDEX]))
                screen.blit(mine_obj,relative_loc)
    soldier_loc = find_relative_loc(soldier.x, soldier.y)
    screen.blit(dead_soldier, (soldier_loc[X_INDEX]-SOLDIER_WIDTH/3*CELL_SIZE[0], soldier_loc[Y_INDEX]-SOLDIER_HEIGHT/3*CELL_SIZE[0]))
    screen.blit(explosion,(soldier_loc[X_INDEX],soldier_loc[Y_INDEX]+(CELL_SIZE[1]*SOLDIER_HEIGHT)-explosion.get_height()))
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
    x_val = CELL_SIZE[ROW_INDEX] * (location_pix[ROW_INDEX] - top_left_corner[X_INDEX])
    y_val = CELL_SIZE[COL_INDEX] * (location_pix[COL_INDEX] - top_left_corner[Y_INDEX])
    screen.blit(image_obj, (x_val, y_val))


def draw_tps():
    for tp in Teleport.tps:
        screen.blit(tp.img,((tp.x1 - top_left_corner[X_INDEX])*CELL_SIZE[0], (tp.y1 - top_left_corner[Y_INDEX])*CELL_SIZE[1]))
        screen.blit(tp.img,((tp.x2 - top_left_corner[X_INDEX])*CELL_SIZE[0], (tp.y2 - top_left_corner[Y_INDEX])*CELL_SIZE[1]))


def display_from_sheet(obj,x,y, sw, sh, size):
    image = pygame.Surface((sw/2,sh*3/4)).convert_alpha()
    image.blit(obj.sprite_sheet,(0,0), ((obj.frame*sw)+sw/4,sh/4,sw/2,sh*3/4))
    image = pygame.transform.scale(image,size)
    image.set_colorkey((0,0,0))
    screen.blit(image,(x,y))

    obj.frame += 1
    if obj.sprite_sheet.get_width()/sw <= obj.frame:
        obj.frame = 0

top_left_corner = [0, 0]
def find_up_left_corner(soldier):
    soldier_row = soldier.y / CELL_SIZE[1]
    soldier_col = soldier.x / CELL_SIZE[0]
    corner_row = soldier_row - GRID_ROWS_PRESENTED /2 + soldier.h /(CELL_SIZE[1] *2)
    corner_col= soldier_col - GRID_COLS_PRESENTED /2 + soldier.w /(CELL_SIZE[0] *2)
    if corner_col < 0:
        corner_col = 0
    elif corner_col > GRID_COLS - GRID_COLS_PRESENTED:
        corner_col =  GRID_COLS - GRID_COLS_PRESENTED
    if corner_row < 0:
        corner_row = 0
    elif corner_row > GRID_ROWS - GRID_ROWS_PRESENTED:
        corner_row =  GRID_ROWS - GRID_ROWS_PRESENTED
    return int(corner_col), int(corner_row)

def find_relative_loc(col, row, convert=False):
    if convert:
        col *= CELL_SIZE[X_INDEX]
        row *= CELL_SIZE[Y_INDEX]
    return col - top_left_corner[X_INDEX] * CELL_SIZE[X_INDEX], row - top_left_corner[Y_INDEX] * CELL_SIZE[Y_INDEX]



def draw(field):
    global top_left_corner
    screen.fill(BACKGROUND_COLOR)
    top_left_corner = find_up_left_corner(soldier)

    draw_field(field)
    draw_tps()
    draw_obj(Game_Field.flag.image, Game_Field.flag.location)
    screen.blit(Game_Field.flag.image, (Game_Field.flag.y, Game_Field.flag.x))
    soldier_relative_loc = find_relative_loc(soldier.x, soldier.y)
    display_from_sheet(soldier, soldier_relative_loc[0], soldier_relative_loc[1], 128, 128, SOLDIER_SIZE)
    guard_relative_location = find_relative_loc(Guard.guard.col, Guard.guard.row, True)
    display_from_sheet(Guard.guard, guard_relative_location[0], guard_relative_location[1], 128, 64, (Guard.guard.w*CELL_SIZE[0], Guard.guard.h*CELL_SIZE[1]))

    pygame.display.flip()
    pass

