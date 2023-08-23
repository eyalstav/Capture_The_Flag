from Consts import *
import random
class Guard:
    def __init__(self):
        self.h = SOLDIER_HEIGHT/2
        self.w = SOLDIER_WIDTH/2-1
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