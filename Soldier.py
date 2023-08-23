import pygame.image
from Consts import *
from Game_Field import field
from Guard import guard


class Soldier:
    def __init__(self):
        self.x = 0
        self.y = 0
        self.sprite_sheet = pygame.image.load("bin/Swordsman/Idle.png")
        self.frame = 0
        self.w = SOLDIER_SIZE[0]
        self.h = SOLDIER_SIZE[1]
        self.alive = True
        self.direction = None

    def check_dead(self):
        start_x = int(self.x / CELL_SIZE[0])
        start_y = int(self.y / CELL_SIZE[1])
        for i in range(int(SOLDIER_SIZE[0] / CELL_SIZE[0])):
            for j in range(int(SOLDIER_SIZE[1] / CELL_SIZE[0])):
                if 1 <= i <= SOLDIER_WIDTH-2 and j == int(SOLDIER_SIZE[1] / CELL_SIZE[0]) - 1:
                    if field[int(start_y + j)][int(start_x + i)]["mine"]:
                        self.alive = False
                if 1 <= i <= SOLDIER_WIDTH - 2 and int(SOLDIER_SIZE[1] / CELL_SIZE[0]) - 3 <= j <= int(SOLDIER_SIZE[1] / CELL_SIZE[0]) - 1:
                    if guard.row <= int(start_y + j) <= guard.row + guard.h and guard.col <= int(
                            start_x + i) <= guard.col + guard.w:
                        self.alive = False

    def move(self):
        direction = self.direction
        if not direction:
            self.sprite_sheet = pygame.image.load("bin/Swordsman/Idle.png")
            return

        if direction == "up":
            self.y -= CELL_SIZE[1]
            if self.y < 0: self.y = 0
            self.check_dead()
        elif direction == "down":
            self.y += CELL_SIZE[1]
            if self.y > CELL_SIZE[1] * GRID_ROWS - SOLDIER_SIZE[1]: self.y = CELL_SIZE[1] * GRID_ROWS - SOLDIER_SIZE[1]
            self.check_dead()
        elif direction == "left":
            self.x -= CELL_SIZE[0]
            if self.x < 0: self.x = 0
            self.check_dead()
            self.sprite_sheet = pygame.transform.flip(pygame.image.load("bin/Swordsman/Walk.png"),1,0)
        elif direction == "right":
            self.x += CELL_SIZE[0]
            if self.x > CELL_SIZE[0] * GRID_COLS - SOLDIER_SIZE[0]: self.x = CELL_SIZE[0] * GRID_COLS - SOLDIER_SIZE[0]
            self.check_dead()
            self.sprite_sheet = pygame.image.load("bin/Swordsman/Walk.png")


soldier = Soldier()
