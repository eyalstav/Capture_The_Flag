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
        self.alive = True
        self.direction = None

    def update_field(self):
        start_x = int(self.x / CELL_SIZE[0])
        start_y = int(self.y / CELL_SIZE[1])
        for i in range(int(SOLDIER_SIZE[0] / CELL_SIZE[0])-1):
            for j in range(int(SOLDIER_SIZE[1] / CELL_SIZE[0])-1):
                field[int(start_y+j)][int(start_x+i)]["soldier"] = True
                if field[int(start_y+j)][int(start_x+i)]["mine"] == True:
                    self.alive = False
                    print("You Died!")


    def move(self):
        direction = self.direction
        if not direction:
            return
        if direction == "up":
            self.y -= CELL_SIZE[1]
            if self.y < 0: self.y = 0
            self.update_field()
        elif direction == "down":
            self.y += CELL_SIZE[1]
            if self.y > WIN_SIZE[1]-SOLDIER_SIZE[1]: self.y = WIN_SIZE[1]-SOLDIER_SIZE[1]
            self.update_field()
        elif direction == "left":
            self.x -= CELL_SIZE[0]
            if self.x < 0: self.x = 0
            self.update_field()
        elif direction == "right":
            self.x += CELL_SIZE[0]
            if self.x > WIN_SIZE[0] - SOLDIER_SIZE[0]: self.x = WIN_SIZE[0] - SOLDIER_SIZE[0]
            self.update_field()

soldier = Soldier()