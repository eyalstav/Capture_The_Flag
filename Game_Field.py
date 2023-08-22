import random

import pygame
from Consts import *


def generate_mines():
    mine_locations = []
    for i in range(MINE_AMOUNT):
        while True:
            x = random.randint(0, int(GRID_COLS / BOMB_LEN) - 1) * BOMB_LEN
            y = random.randint(0, GRID_ROWS - 1)
            if (x < SOLDIER_WIDTH and y < SOLDIER_HEIGHT) or (x >= GRID_COLS - FLAG_WIDTH - BOMB_LEN and y >= GRID_ROWS - FLAG_HEIGHT):
                continue
            break
        mine_locations.append([y, x])
    return mine_locations


mines = generate_mines()


def create_field():
    output = []

    for row in range(GRID_ROWS):
        r = []
        for col in range(GRID_COLS):
            r.append({"type": random.choice(["normal", "grass"]), "mine": False, "draw_mine": False})
        output.append(r)

    for mine in mines:
        output[mine[ROW_INDEX]][mine[COL_INDEX]]["draw_mine"] = True
        for i in range(BOMB_LEN):
            output[mine[ROW_INDEX]][mine[COL_INDEX] + i]["mine"] = True
    return output


field = create_field()


class Flag:
    def __init__(self, location, size):
        '''
        this method initializes the flag
        :param location: tuple/list flags (x, y) coords
        :param size: tuple/list- flag's length and height
        '''
        self.image = pygame.image.load(FLAG_IMG)
        self.image = pygame.transform.scale(self.image, FLAG_SIZE)
        self.size = size
        self.location = tuple(location)
        self.x = location[ROW_INDEX] * CELL_SIZE[ROW_INDEX]
        self.y = location[COL_INDEX] * CELL_SIZE[COL_INDEX]

        self.update_field()

    def update_field(self):
        start_y = self.location[ROW_INDEX]
        start_x = self.location[COL_INDEX]

        for i in range(FLAG_HEIGHT):
            for j in range(FLAG_WIDTH):
                field[start_x + i][start_y + j]["flag"] = True

    def is_stepped_on(self, soldier):
        xp = int(soldier.x / CELL_SIZE[ROW_INDEX]) + SOLDIER_WIDTH - 1
        yp = int(soldier.y / CELL_SIZE[COL_INDEX]) + SOLDIER_HEIGHT - 1
        return xp > GRID_COLS - FLAG_WIDTH and yp > GRID_ROWS - FLAG_HEIGHT


flag = Flag((len(field[ROW_INDEX]) - FLAG_WIDTH, len(field) - FLAG_HEIGHT), (FLAG_WIDTH, FLAG_HEIGHT))

class Guard:
    def __init__(self):
        self.h = 2
        self.w = 1
        self.row = random.randint(SOLDIER_WIDTH, GRID_ROWS - self.w*2)
        self.col = random.randint(0, GRID_COLS - self.h*2)
        self.img = pygame.transform.scale(pygame.image.load(GUARD_IMG),(self.w*CELL_SIZE[0]*4 ,self.h*CELL_SIZE[1]*2))
        self.d = 1

    def move(self):
        self.col += self.d
        if self.col >= GRID_COLS-1:
            self.col -= self.d
            self.d *= -1
            self.img = pygame.transform.flip(self.img,True,False)
        if self.col < 0:
            self.col -= self.d
            self.d *= -1
            self.img = pygame.transform.flip(self.img, True, False)


guard = Guard()