import random

import pygame
from Consts import *


def generate_mines():
    mine_locations = []
    for i in range(MINE_AMOUNT):
        while True:
            x = random.randint(0, int(GRID_COLS / 3)-1) * 3
            y =  random.randint(0, GRID_ROWS - 1)
            if (x<4 and y<6):
                continue
            if (x>=GRID_COLS-FLAG_WIDTH-3 and y >= GRID_ROWS-FLAG_HEIGHT):
                continue
            break
        mine_locations.append([y,x])
    return mine_locations
mines = generate_mines()
def create_field():
    output = []

    for row in range(GRID_ROWS):
        r = []
        for col in range(GRID_COLS):
            r.append({"type": random.choice(["normal","grass"]),"mine":False,"soldier":False, "draw_mine":False})
        output.append(r)

    for mine in mines:
        output[mine[0]][mine[1]]["draw_mine"] = True
        for i in range(3):
            output[mine[0]][mine[1]+i]["mine"] = True


    return output
field = create_field()
class Flag:
    def __init__(self, location,size):
        '''
        this method initializes the flag
        :param location: tuple/list flags (x, y) coords
        :param size: tuple/list- flag's length and height
        '''
        self.image = pygame.image.load(FLAG_IMG)
        self.image = pygame.transform.scale(self.image, FLAG_SIZE)
        self.size = size
        self.location = tuple(location)
        self.x = location[0] * CELL_SIZE[0]
        self.y = location[1] * CELL_SIZE[1]

        self.update_field()

    def update_field(self):
        start_y = self.location[0]
        start_x = self.location[1]

        for i in range(FLAG_HEIGHT):
            for j in range(FLAG_WIDTH):
                field[start_x+i][start_y+j]["flag"] = True


    def is_stepped_on(self, soldier):
        xp = int(soldier.x/CELL_SIZE[0]) + SOLDIER_WIDTH-1
        yp = int(soldier.y/CELL_SIZE[1]) + SOLDIER_HEIGHT-1
        if xp > GRID_COLS-FLAG_WIDTH and yp > GRID_ROWS-FLAG_HEIGHT:
            return True
        return False

flag = Flag((len(field[0]) - FLAG_WIDTH, len(field) - FLAG_HEIGHT), (FLAG_WIDTH, FLAG_HEIGHT))




