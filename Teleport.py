from Consts import *
import random
from Soldier import soldier
class TP:
    def __init__(self):
        self.w = TP_WIDTH
        self.h = TP_HEIGHT
        self.img = pygame.transform.scale(pygame.image.load(TP_IMG), (self.w * CELL_SIZE[0], self.h * CELL_SIZE[1]))
        while True:
            self.y1 = random.randint(TP_START_ROW,TP_END_ROW)
            self.x1 = random.randint(0, GRID_COLS-1)
            if (self.x1 < SOLDIER_WIDTH and self.y1 < SOLDIER_HEIGHT) or (self.x1 >= GRID_COLS - FLAG_WIDTH - BOMB_LEN and self.y1 >= GRID_ROWS - FLAG_HEIGHT):
                continue
            break
        while True:
            self.y2 = random.randint(TP_START_ROW, TP_END_ROW)
            self.x2 = random.randint(0, GRID_COLS - 1)
            if (self.x2 < SOLDIER_WIDTH and self.y2 < SOLDIER_HEIGHT) or (self.x2 >= GRID_COLS - FLAG_WIDTH - BOMB_LEN and self.y2 >= GRID_ROWS - FLAG_HEIGHT):
                continue
            break


    def check_tp(self):
        start_x = int(soldier.x / CELL_SIZE[0])
        start_y = int(soldier.y / CELL_SIZE[1])
        for i in range(int(SOLDIER_SIZE[0] / CELL_SIZE[0])):
            for j in range(int(SOLDIER_SIZE[1] / CELL_SIZE[0])):
                if 1 <= i <= SOLDIER_WIDTH-2 and j == int(SOLDIER_SIZE[1] / CELL_SIZE[0]) - 1:
                    if int(start_y + j) == self.y1 and int(start_x + i) == self.x1:
                        soldier.x = self.x2*CELL_SIZE[0]
                        soldier.y = self.y2*(CELL_SIZE[1] -SOLDIER_HEIGHT -1)

        for i in range(int(SOLDIER_SIZE[0] / CELL_SIZE[0])):
            for j in range(int(SOLDIER_SIZE[1] / CELL_SIZE[0])):
                if 1 <= i <= SOLDIER_WIDTH - 2 and j == int(SOLDIER_SIZE[1] / CELL_SIZE[0]) - 1:
                    if int(start_y + j) == self.y2 and int(start_x + i) == self.x2:
                        soldier.x = self.x1 * CELL_SIZE[0]
                        soldier.y = self.y1 * (CELL_SIZE[1] -SOLDIER_HEIGHT -1)

tps = []
for i in range(TP_AMOUNT):
    tps.append(TP())

