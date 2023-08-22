import random

import pygame

import Screen
from Consts import *


def create_field():
    output = []
    for row in range(GRID_ROWS):
        r = []
        for col in range(GRID_COLS):
            r.append(
                {"type": random.choice(["normal", "grass"]), "mine": bool(random.getrandbits(1)), "soldier": False,"flag": False})

        output.append(r)
    return output


def edge_pixel_list(location, pix_size):
    edge_list = []
    for y_loc in range(int(location[Y_INDEX]), int(location[Y_INDEX]) + int(pix_size[Y_INDEX])):
        # test if all the line should be checked or only the right and left edge
        if y_loc == int(location[Y_INDEX]) or y_loc == pix_size[Y_INDEX] - 1:
            for x_loc in range(int(location[X_INDEX]), int(location[X_INDEX]) + int(pix_size[X_INDEX])):
                edge_list.append((x_loc, y_loc))
        else:
            # check only right and left edges of the picture
            for x_loc in [location[X_INDEX], location[X_INDEX] + pix_size[X_INDEX] - 1]:
                edge_list.append((x_loc, y_loc))
    return edge_list


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
        print(location)
        self.x = location[0] * CELL_SIZE[0]
        self.y = location[1] * CELL_SIZE[1]

        self.update_field()

    def draw(self):
        Screen.draw_obj(self.image, self.location)

    def update_field(self):
        print(field)
        print(len(field), len(field[0]))
        start_y = self.location[0]
        start_x = self.location[1]

        for i in range(FLAG_HEIGHT):
            for j in range(FLAG_WIDTH):
                field[start_x+i][start_y+j]["flag"] = True

        print(field)


    def is_stepped_on(self, soldier):
        soldier_edge = edge_pixel_list((int(soldier.y / CELL_SIZE[1]), int(soldier.x / CELL_SIZE[0])), (int(soldier.h / CELL_SIZE[1]), int(soldier.w / CELL_SIZE[0])))
        flag_edge = edge_pixel_list(self.location, self.size)
        for flag_pix in flag_edge:
            for soldier_pix in soldier_edge:
                if soldier_pix == flag_pix:
                    return True
        return False

field = create_field()
flag = Flag((len(field[0]) - FLAG_WIDTH, len(field) - FLAG_HEIGHT), (FLAG_WIDTH, FLAG_HEIGHT))
