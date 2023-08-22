import random

import pygame

from Consts import *

def create_field():
    output = []
    for row in range(GRID_ROWS):
        r = []
        for col in range(GRID_COLS):
            r.append({"type": random.choice(["normal","grass"]),"mine":bool(random.getrandbits(1)),"soldier":False})

        output.append(r)
    return output

def edge_pixel_list(location, pix_size):
    edge_list = []
    for y_loc in range(location[Y_INDEX], location[Y_INDEX] + pix_size[Y_INDEX]):
        # test if all the line should be checked or only the right and left edge
        if y_loc == FIRST_INDX or y_loc == pix_size[Y_INDEX] - 1:
            for x_loc in range(location[X_INDEX], location[X_INDEX] + pix_size[X_INDEX]):
                edge_list.append((x_loc, y_loc))
        else:
            # check only right and left edges of the picture
            for x_loc in [location[X_INDEX], location[X_INDEX] + pix_size[X_INDEX] - 1]:
                edge_list.append((x_loc, y_loc))
    return edge_list

class Flag:
    image = pygame.image.load(FLAG_IMG)
    image = pygame.transform.scale(image,FLAG_SIZE)

    def __init__(self, location, size):
        '''
        this method initializes the flag
        :param location: tuple/list flags (x, y) coords
        :param size: tuple/list- flag's length and height
        '''
        self.size = tuple(size)
        self.location = tuple(location)

    def is_stepped_on(self, soldier):
        soldier_edge = edge_pixel_list([soldier.x, soldier.y], [soldier.w,soldier.h])
        flag_edge = edge_pixel_list(self.location, self.size)
        for flag_pix in flag_edge:
            for soldier_pix in soldier_edge:
                if soldier_pix == flag_pix:
                    return True
        return False





field = create_field()




