import pygame.image
from Consts import *
from Game_Field import field
class Soldier:
    def __init__(self):
        self.x = 0
        self.y = 0
        self.img = pygame.image.load(SOLDIER_IMG)
        self.img = pygame.transform.scale(self.img,SOLDIER_SIZE)
        self.w = self.img.get_width()
        self.h = self.img.get_height()

    def update_field(self):
        start_x = self.x / CELL_SIZE[0]
        start_y = self.y / CELL_SIZE[1]
        for i in range(SOLDIER_SIZE[0] / CELL_SIZE[0]):
            for j in range(SOLDIER_SIZE[1] / CELL_SIZE[1]):
                field[start_x+(i*CELL_SIZE[0])][start_y+(j*CELL_SIZE[1])]["soldier"] = True

    def move(self, direction):
        if direction == "up":
            self.y -= CELL_SIZE[1]
            if self.y < 0: self.y = 0

        if direction == "down":
            self.y += CELL_SIZE[1]
            if self.y > WIN_SIZE[1]-SOLDIER_SIZE[1]: self.y = WIN_SIZE[1]-SOLDIER_SIZE[1]
        if direction == "left":
            self.x -= CELL_SIZE[0]
            if self.x < 0: self.x = 0
        if direction == "right":
            self.x += CELL_SIZE[0]
            if self.x > WIN_SIZE[0] - SOLDIER_SIZE[0]: self.x = WIN_SIZE[0] - SOLDIER_SIZE[0]

soldier = Soldier()