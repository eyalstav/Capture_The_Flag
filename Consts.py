import pygame
WIN_SIZE = (1000,500)
GRID_ROWS = 50
GRID_COLS = 100
GRID_ROWS_PRESENTED = 25
GRID_COLS_PRESENTED = 50

CELL_SIZE = (WIN_SIZE[0]/GRID_COLS_PRESENTED, WIN_SIZE[1]/GRID_ROWS_PRESENTED)

GRASS_IMG = "bin/grass.png"
MINE_IMG = "bin/mine.png"
EXPLOAD_IMG = "bin/explosion.png"
EXPLOAD_SIZE = (CELL_SIZE[0]*4,CELL_SIZE[1]*4)

START_MSG = "Help me get to this flag!"
LOSE_MSG = "YOU LOST!"
WIN_MSG = "YOU WON!"

SOLDIER_WIDTH = 4
SOLDIER_HEIGHT = 5
SOLDIER_SIZE = (CELL_SIZE[0]*SOLDIER_WIDTH,CELL_SIZE[1]*SOLDIER_HEIGHT)
FLAG_IMG = "bin/flag.png"
FLAG_WIDTH = 4
FLAG_HEIGHT = 6
FLAG_SIZE = (CELL_SIZE[0]*FLAG_WIDTH,CELL_SIZE[1]*FLAG_HEIGHT)

GUARD_IMG = "bin/dino.png"

FIRST_INDX = 0
X_INDEX = 0
Y_INDEX = 1
TICK_LENGTH = 15
MINE_AMOUNT = 5
ROW_INDEX = 0
COL_INDEX = 1

BACKGROUND_COLOR = (20,100,20)
WIN_COLOR = (255,255,255)
LOSE_COLOR = (255,255,255)
END_COLOR = (10,10,10)
START_MSG_COLOR = (0, 0, 0)
NIGHT_GRID_COLOR = (255, 255, 255)
NIGHT_GRID_WIDTH = 1
BOMB_LEN = 3
START_FONT_SIZE = 30
MILISEC_IN_SEC = 1000
KEYBOARD_DICT = {ord('a') : "left", pygame.K_LEFT : "left", ord('d') : 'right', pygame.K_RIGHT : 'right',
            pygame.K_UP : 'up', ord('w') : 'up', ord('s') : 'down', pygame.K_DOWN : "down"}

#teleport
TP_START_ROW = 4
TP_END_ROW = 20
TP_WIDTH = 4
TP_HEIGHT = 2
TP_IMG = "bin/tp2.png"
TP_AMOUNT = 4

MAX_SAVE = 9
MIN_SAVE = 0
DB_PATH = "game_states.csv"

BLANK_GAME_STATES  = {"saved_num" : range(MIN_SAVE, MAX_SAVE + 1), "board": [[[],[]] for i in range(MAX_SAVE + 1)], 'player_loc' : [[] for i in range(MAX_SAVE + 1)]
                      , 'guard_dir_loc' : [[] for i in range(MIN_SAVE, MAX_SAVE + 1)], 'teleports' : [[] for x in range(MIN_SAVE, MAX_SAVE + 1)]}
#intro screen
current_hero = 0
intro_frame = 0

SOLDIER_FOLDER = f"bin/{current_hero}/"


