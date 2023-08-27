from Consts import *
import random
from Soldier import soldier
class TP:
    def __init__(self, tp1=[], tp2 =[]):

        def random_location():
            '''
            this method looks for random location for the mine
            :return: location
            '''
            loc = []
            while True:
                loc.append(random.randint(0, GRID_COLS-1))
                loc.append(random.randint(TP_START_ROW,TP_END_ROW))
                if (loc[0] < SOLDIER_WIDTH and loc[1] < SOLDIER_HEIGHT) or (loc[0] >= GRID_COLS - FLAG_WIDTH - BOMB_LEN and loc[1] >= GRID_ROWS - FLAG_HEIGHT):
                    continue
                break
            return loc
        #init:
        self.w = TP_WIDTH
        self.h = TP_HEIGHT
        self.img = pygame.transform.scale(pygame.image.load(TP_IMG), (self.w * CELL_SIZE[0], self.h * CELL_SIZE[1]))
        if len(tp1) == 0 or len(tp2) == 0:
            self.x1, self.y1 = tuple(random_location())
            self.x2, self.y2 = tuple(random_location())
        else:
            self.x1, self.y1 = tuple(tp1)
            self.x2, self.y2 = tuple(tp1)


    def check_tp(self):
        def check_and_tp(source, dest, start):
            '''
            this method checks if should tp and teleports if needed
            :param source: first teleport platform location [x,y]
            :param dest: second teleport platform location [x,y]
            :return: None
            '''
            start_x, start_y = start
            for i in range(int(SOLDIER_SIZE[0] / CELL_SIZE[0])):
                for j in range(int(SOLDIER_SIZE[1] / CELL_SIZE[0])):
                    if 1 <= i <= SOLDIER_WIDTH - 2 and j == int(SOLDIER_SIZE[1] / CELL_SIZE[0]) - 1:
                        if int(start_y + j) == source[1] and int(start_x + i) == source[0]:
                            soldier.x = dest[0] * CELL_SIZE[0]
                            soldier.y = dest[1] * (CELL_SIZE[1] - SOLDIER_HEIGHT - 1)


        start_x = int(soldier.x / CELL_SIZE[0])
        start_y = int(soldier.y / CELL_SIZE[1])
        check_and_tp([self.x1, self.y1], [self.x2, self.y2], (start_x, start_y))

tps = []
for i in range(TP_AMOUNT):
    tps.append(TP())