import pygame
WIN_SIZE = (1000,500)
GRID_ROWS = 25
GRID_COLS = 50

CELL_SIZE = (WIN_SIZE[0]/GRID_COLS, WIN_SIZE[1]/GRID_ROWS)

GRASS_IMG = "bin/grass.png"
MINE_IMG = "bin/mine.png"
EXPLOAD_IMG = "bin/explosion.png"
EXPLOAD_SIZE = (CELL_SIZE[0]*4,CELL_SIZE[1]*4)

START_MSG = "WELCOME TO THE GAME! Have Fun!"
LOSE_MSG = "YOU LOST!"
WIN_MSG = "YOU WON!"

SOLDIER_IMG = "bin/soldier.png"
NIGHT_SOLDIER_IMG = "bin/soldier_night.png"
DEAD_SOLDIER_IMG = "bin/injury.png"
SOLDIER_WIDTH = 4
SOLDIER_HEIGHT = 6
SOLDIER_SIZE = (CELL_SIZE[0]*4,CELL_SIZE[1]*6)
FLAG_IMG = "bin/flag.png"
FLAG_WIDTH = 4
FLAG_HEIGHT = 6
FLAG_SIZE = (CELL_SIZE[0]*FLAG_WIDTH,CELL_SIZE[1]*FLAG_HEIGHT)

FIRST_INDX = 0
X_INDEX = 0
Y_INDEX = 1

MINE_AMOUNT = 50

KEYBOARD_DICT = {ord('a') : "left", pygame.K_LEFT : "left", ord('d') : 'right', pygame.K_RIGHT : 'right',
            pygame.K_UP : 'up', ord('w') : 'up', ord('s') : 'down', pygame.K_DOWN : "down"}